from odoo import models, fields, api, exceptions
import qrcode
import base64
from io import BytesIO

class Equipo(models.Model):
    _name = 'gestion.equipo'
    _description = 'Equip informàtic'
    _rec_name = 'display_name'

    name = fields.Char(string="Nom de l'Equip", required=True)
    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Model", required=True)
    numero_serie = fields.Char(string="Núm. de Sèrie", required=True, unique=True)
    qr_image = fields.Binary("Codi QR")  # NO compute ni store

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
            missing = []
            if not record.marca: missing.append("Marca")
            if not record.modelo: missing.append("Model")
            if not record.numero_serie: missing.append("Núm. de Sèrie")
            if not record.tipo: missing.append("Tipus d'Equip")
            if not record.estado: missing.append("Estat")
            if not record.fecha_alta: missing.append("Data d'Alta")
            if missing:
                raise exceptions.ValidationError(f"Falten camps obligatoris: {', '.join(missing)}")

    def _generate_qr_code_from_vals(self, vals):
        """
        Genera el QR en base a vals dict (o al record) y devuelve la imagen en base64.
        """
        name = vals.get('name', False)
        marca = vals.get('marca', False)
        modelo = vals.get('modelo', False)
        numero_serie = vals.get('numero_serie', False)

        # Si no están en vals, intentamos coger del registro (para write)
        # Si self tiene un solo registro y alguno falta en vals, tomamos del registro actual
        if self and len(self) == 1:
            rec = self
            if not name:
                name = rec.name
            if not marca:
                marca = rec.marca
            if not modelo:
                modelo = rec.modelo
            if not numero_serie:
                numero_serie = rec.numero_serie

        info = (
            f"Nom: {name or ''}\n"
            f"Marca: {marca or ''}\n"
            f"Model: {modelo or ''}\n"
            f"Núm. de Sèrie: {numero_serie or ''}"
        )
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(info)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_b64 = base64.b64encode(temp.getvalue())
        return qr_b64

    @api.model_create_multi
    def create(self, vals_list):
        # Para cada vals en la lista generamos el QR y lo añadimos al dict antes de crear
        for vals in vals_list:
            vals['qr_image'] = self._generate_qr_code_from_vals(vals)
        return super().create(vals_list)

    def write(self, vals):
        # Solo generamos QR si alguno de los campos clave está en vals
        fields_for_qr = ['name', 'marca', 'modelo', 'numero_serie']
        if any(field in vals for field in fields_for_qr):
            # Generar el QR en base a vals + registro actual
            vals['qr_image'] = self._generate_qr_code_from_vals(vals)
        return super().write(vals)

    def action_print_etiqueta_qr(self):
        return self.env.ref('gestio_equips_empleats.action_etiqueta_equipo_qr').report_action(self)
