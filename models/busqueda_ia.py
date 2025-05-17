import requests
from odoo import models, fields
import os
from dotenv import load_dotenv
load_dotenv()


class BusquedaIA(models.TransientModel):
    _name = 'gestion.busqueda.ia'
    _description = 'Buscar informació amb IA'

    pregunta = fields.Text(string="Pregunta")
    respuesta = fields.Text(string="Resposta", readonly=True)

    def buscar_con_ia(self):
        try:
            api_key = os.getenv("OPENAI_API_KEY")
            url = "https://api.openai.com/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }

            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "Ets un assistent útil."},
                    {"role": "user", "content": self.pregunta},
                ]
            }

            response = requests.post(url, headers=headers, json=data, timeout=20)

            if response.status_code == 200:
                result = response.json()
                self.respuesta = result['choices'][0]['message']['content']
            else:
                self.respuesta = f"Error {response.status_code}: {response.text}"

        except requests.exceptions.RequestException as e:
            self.respuesta = f"Error de connexió: {str(e)}"
        except Exception as e:
            self.respuesta = f"Error inesperat: {str(e)}"

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'gestion.busqueda.ia',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }
