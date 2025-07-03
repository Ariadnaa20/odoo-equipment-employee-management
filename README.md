# 📦 Módulo Odoo: Gestión de Equipos y Empleados

## 🔍 Descripción

Este módulo permite gestionar el préstamo de equipos a empleados dentro de una organización. Está pensado para escuelas, empresas, ayuntamientos o cualquier entidad que ceda dispositivos a sus trabajadores.

### Funcionalidades Principales

- ✅ Gestión de equipos informáticos con historial de préstamos  
- ✅ Registro completo de empleados con departamento y foto  
- ✅ Asignación de préstamos entre equipos y empleados  
- ✅ Impresión de informes PDF con estilo moderno y **firma digital**  
- ✅ Envío automático del informe por correo electrónico (con configuración SMTP)  
- ✅ Código QR para los equipos  
- ✅ **Integración con OpenAI** para asistencia inteligente vía IA  
- ✅ Traducción disponible (ej: catalán, inglés)  
- ✅ Datos de demostración incluidos  
- ✅ Control de acceso por grupos (Administrador / Consultor)

---

## 📁 Estructura del módulo

- `models/`: Definición de modelos (`equipo`, `empleado`, `prestamo`, `busqueda_ia`)
- `views/`: Vistas XML (formularios, listas, menús)
- `wizard/`: Asistente para enviar el informe por correo
- `report/`: Plantilla QWeb del informe PDF
- `i18n/`: Archivos `.po` de traducción
- `security/`: Permisos y grupos de acceso
- `data/demo.xml`: Datos de demostración

---

## 🛠️ Requisitos

- Odoo 14.0+ hasta 18.0 (probado en 18.0 Community)
- Conexión a Internet para la funcionalidad de IA
- Clave de API de OpenAI
- Servidor SMTP configurado (ej: Gmail con contraseña de aplicación)

---

## 🚀 Instalación

1. Copia la carpeta `gestio_equips_empleats/` dentro de `addons/`
2. Reinicia el servidor de Odoo
3. Activa el módulo desde la interfaz
4. (Opcional) Carga los datos de demostración para ver cómo funciona

---

## 💬 Autor

**Ariadna Pascual**  
📅 Fecha de publicación: 15/04/2025  
📧 Contacto: *ari.palau20@gmail.com*

---

**Con este módulo, digitalizar la gestión de préstamos nunca había sido tan fácil.**  
🎯 Compatible con la mayoría de instalaciones de Odoo y preparado para crecer 🚀
