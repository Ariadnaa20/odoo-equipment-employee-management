from odoo import models, fields, api, exceptions

class Empleado(models.Model):
    _name = 'gestion.empleado'
    _description = 'Empleat'
    _rec_name = 'name'

    name = fields.Char(string="Nom", required=True)
    cognoms = fields.Char(string="Cognoms", required=True)
    email = fields.Char(string="Email", required=True)
    telefon = fields.Char(string="Telèfon", required=True)
    departament = fields.Selection([
        ('it', 'IT'),
        ('rrhh', 'Human Resources'),
        ('finances', 'Finance'),
        ('logistica', 'Logistics'),
        ('altres', 'Others')
    ], string="Departament", default='altres', required=True)
    foto = fields.Image(string="Foto")
    prestamo_ids = fields.One2many('gestion.prestamo', 'empleado_id', string="Préstecs")

    @api.constrains('name', 'cognoms', 'email', 'telefon', 'departament', 'foto')
    def _check_required_fields(self):
        for record in self:
            missing = []
            if not record.name:
                missing.append("Name")
            if not record.surname:
                missing.append("Surname")
            if not record.email:
                missing.append("Email")
            if not record.phone:
                missing.append("Phone")
            if not record.department:
                missing.append("Department")
            if not record.photo:
                missing.append("Photo")
            if missing:
                raise exceptions.ValidationError(
                    f"Missing required fields: {', '.join(missing)}"
                )