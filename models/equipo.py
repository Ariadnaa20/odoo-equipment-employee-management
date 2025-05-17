from odoo import models, fields, api, exceptions

class Equipo(models.Model):
    _name = 'gestion.equipo'
    _description = 'Equip informàtic'
    _rec_name = 'display_name'

    name = fields.Char(string="Nom de l'Equip", required=True)
    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Model", required=True)

    # ✅ Aquest és el camp que et faltava
    numero_serie = fields.Char(string="Núm. de Sèrie", required=True, unique=True)

    tipo = fields.Selection([
        ('portatil', 'Portàtil'),
        ('monitor', 'Monitor'),
        ('raton', 'Ratolí'),
        ('teclado', 'Teclat'),
        ('auriculars', 'Auriculars'),
        ('projector', 'Projector'),
        ('altre', 'Altres')
    ], string="Tipus d'Equip", default='altre', required=True)

    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('prestado', 'En Préstec'),
        ('mantenimiento', 'En Manteniment'),
        ('baixa', 'Donat de Baixa')
    ], string="Estat", default='disponible', required=True)

    fecha_alta = fields.Date(string="Data d'Alta", default=fields.Date.today, required=True)
    descripcion = fields.Text(string="Descripció")
    imagen = fields.Binary(string="Imatge")

    prestamo_ids = fields.One2many('gestion.prestamo', 'equipo_id', string="Historial de Préstecs")

    display_name = fields.Char(string="Nom Visual", compute="_compute_display_name", store=True)

    @api.depends('name', 'marca', 'modelo')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.marca or ''} {record.modelo or ''})"

    @api.onchange('prestamo_ids')
    def _onchange_estado(self):
        for record in self:
            if any(p.estado == 'activo' for p in record.prestamo_ids):
                record.estado = 'prestado'
            elif record.estado == 'prestado':
                record.estado = 'disponible'

    @api.constrains('marca', 'modelo', 'numero_serie', 'tipo', 'estado', 'fecha_alta')
    def _check_required_fields(self):
        for record in self:
            missing_fields = []
            if not record.marca:
                missing_fields.append("Marca")
            if not record.modelo:
                missing_fields.append("Model")
            if not record.numero_serie:
                missing_fields.append("Núm. de Sèrie")
            if not record.tipo:
                missing_fields.append("Tipus d'Equip")
            if not record.estado:
                missing_fields.append("Estat")
            if not record.fecha_alta:
                missing_fields.append("Data d'Alta")
            if missing_fields:
                raise exceptions.ValidationError(f"Falten camps obligatoris: {', '.join(missing_fields)}")
