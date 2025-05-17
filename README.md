# 📦 Mòdul Odoo: Gestió d'Equips i Empleats

## 🔍 Descripció

Aquest mòdul permet gestionar el préstec d'equips a empleats dins d'una organització. Està pensat per escoles, empreses, ajuntaments o qualsevol entitat que cedeixi dispositius als seus treballadors.

### Funcionalitats Principals

- ✅ Gestió d’equips informàtics amb historial de préstecs  
- ✅ Registre complet d'empleats amb departament i foto  
- ✅ Assignació de préstecs entre equips i empleats  
- ✅ Impressió d'informes PDF amb estil modern i **signatura digital**  
- ✅ Enviament automàtic de l'informe per correu electrònic (amb configuració SMTP)
- ✅ QR pels equips
- ✅ **Integració amb OpenAI** per assistència intel·ligent via IA  
- ✅ Traducció disponible (ex: català, anglès)  
- ✅ Dades de demostració  
- ✅ Control d’accés per grups (Administrador / Consultor)

---

## 📁 Estructura del mòdul

- `models/`: Definició de models (`equipo`, `empleado`, `prestamo`, `busqueda_ia`)
- `views/`: Vistes XML (formularis, llistes, menús)
- `wizard/`: Assistent per enviar correu amb l’informe adjunt
- `report/`: Plantilla QWeb de l'informe PDF
- `i18n/`: Arxius `.po` de traducció
- `security/`: Permisos i grups d'accés
- `data/demo.xml`: Dades de demostració

---

## 🛠️ Requisits

- Odoo 14.0+ fins a 18.0 (provat en 18.0 Community)
- Connexió a Internet per la funcionalitat d’IA
- Clau d’API d’OpenAI
- Servidor SMTP configurat (ex: GMail amb contrasenya d'aplicació)

---

## 🚀 Instal·lació

1. Copia la carpeta `gestio_equips_empleats/` dins `addons/`
2. Reinicia el servidor Odoo
3. Activa el mòdul des de la interfície
4. (Opcional) Carrega les dades de demostració per veure el funcionament

---

## 💬 Autor

**Ariadna Pascual**  
Data de publicació: 15/04/2025  
Contacte: *ari.palau20@gmail.com*

---

## 📄 Llicència

Aquest mòdul es distribueix sota la llicència **Odoo Proprietary License v1.0 (OPL-1)**.  
No està permès copiar, redistribuir ni modificar aquest codi sense autorització expressa de l’autora.

(c) Ariadna Pascual Palau

---

**Amb aquest mòdul, digitalitzar la gestió de préstecs mai havia estat tan fàcil.**

🎯 Compatible amb la majoria d’instal·lacions d’Odoo i preparat per créixer 🚀
