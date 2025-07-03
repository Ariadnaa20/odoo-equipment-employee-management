from odoo import models, fields, api
from odoo.exceptions import UserError
import base64

class PrestamoMailWizard(models.TransientModel):
    _name = 'gestion.prestamo.mail.wizard'
    _description = 'Assistent per Enviar Informe de Préstec per Correu'

    email_to = fields.Char(string="Correu Destinatari", required=True)
    message_body = fields.Text(string="Missatge", default="Adjunto l'informe del préstec sol·licitat.")
    prestamo_id = fields.Many2one('gestion.prestamo', string='Préstec', required=True)

    def send_mail_with_report(self):
        if not self.prestamo_id:
            raise UserError("No s'ha trobat cap préstec associat.")

        report = self.env.ref('gestio_equips_empleats.action_report_prestec')
        pdf_content, _ = report._render_qweb_pdf(report.id, res_ids=[self.prestamo_id.id])

        attachment = self.env['ir.attachment'].create({
            'name': f"Informe_Prestec_{self.prestamo_id.display_name}.pdf",
            'type': 'binary',
            'datas': base64.b64encode(pdf_content),
            'res_model': 'gestion.prestamo',
            'res_id': self.prestamo_id.id,
            'mimetype': 'application/pdf',
        })

        mail_values = {
            'subject': f"Informe de Préstec - {self.prestamo_id.display_name}",
            'body_html': f"<p>{self.message_body}</p>",
            'email_to': self.email_to,
            'email_from': self.env.user.email or 'no-reply@example.com',
            'attachment_ids': [(6, 0, [attachment.id])],
        }

        mail = self.env['mail.mail'].create(mail_values)
        mail.send()

        # ✨ Mostrar notificación de éxito
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Èxit',
                'message': 'El correu s\'ha enviat correctament!',
                'type': 'success',
                'sticky': False,
            }
        }
