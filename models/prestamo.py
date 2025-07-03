from odoo import models, fields, api
from datetime import date

class Prestamo(models.Model):
    _name = 'gestion.prestamo'
    _description = 'Préstec de Dispositius'
    _rec_name = 'display_name'

    equipo_id = fields.Many2one('gestion.equipo', string="Equip", required=True)
    empleado_id = fields.Many2one('gestion.empleado', string="Empleat", required=True)
    fecha_inicio = fields.Date(string="Data d'Inici", required=True, default=fields.Date.today)
    fecha_fin = fields.Date(string="Data de Retorn")
    estado = fields.Selection([
        ('activo', 'Actiu'),
        ('devuelto', 'Retornat'),
        ('retrasado', 'Endarrerit')
    ], string="Estat", default='activo')
    observacions = fields.Text(string="Observacions")
    display_name = fields.Char(string="Nom visual", compute="_compute_display_name", store=True)
    signature = fields.Binary(string="Signatura")

    @api.depends('equipo_id', 'empleado_id', 'fecha_inicio')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.equipo_id.name or ''} → {record.empleado_id.name or ''}"

    @api.onchange('fecha_fin')
    def check_estado(self):
        for record in self:
            if record.fecha_fin:
                if record.fecha_fin < fields.Date.today():
                    record.estado = 'retrasado'
                else:
                    record.estado = 'devuelto'

    def action_send_report_email(self):
        return {
            'name': 'Enviar Informe per Correu',
            'type': 'ir.actions.act_window',
            'res_model': 'gestion.prestamo.mail.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_email_to': self.empleado_id.email if self.empleado_id and self.empleado_id.email else '',
                'default_prestamo_id': self.id,
            }
        }

    def action_print_report(self):
        """Acció que imprimeix l'informe en PDF"""
        return self.env.ref('gestio_equips_empleats.action_report_prestec').report_action(self)


