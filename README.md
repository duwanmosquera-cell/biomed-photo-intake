# 📸 Biomed Photo Intake / Recepción de fotos biomédicas

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

# 🧠 Gestión Inteligente de Equipos Biomédicos

## 🌟 Visión del Proyecto
Este sistema busca digitalizar el registro, trazabilidad y mantenimiento de equipos biomédicos en hospitales, clínicas y laboratorios.  
Cada equipo se registra mediante foto de su placa, se genera automáticamente su hoja de vida digital y se programa su cronograma de mantenimiento según su clase técnica.

---

## 📱 Funcionalidades Clave
- 📸 Registro de equipos con OCR (reconocimiento de texto en placas).
- 🗂️ Inventario dinámico con base de datos actualizable.
- 📄 Hoja de vida digital por equipo (modelo, serie, lote, ubicación, historial).
- 📅 Cronograma automático de mantenimiento (trimestral, semestral, anual).
- 🔗 Generación de código QR único por equipo para acceso directo a su hoja de vida.

---

## ⚙️ Arquitectura Técnica
- **Frontend:** App móvil/web para captura de datos y escaneo de QR.
- **Backend:** FastAPI con endpoints RESTful y documentación Swagger.
- **OCR:** `pytesseract` o servicios cloud para lectura de placas.
- **Base de datos:** PostgreSQL con las siguientes tablas:
  - `equipos` → datos técnicos del equipo.
  - `hojas_de_vida` → historial y eventos asociados.
  - `mantenimientos` → cronograma y registros por equipo.
- **Visualización:** Dashboards en Power BI o interfaz web.

---

## 🧩 Flujo de Registro
1. Se detecta un equipo biomédico.
2. Se toma foto de su placa y se extraen datos con OCR.
3. Se registra en la base de datos y se genera su hoja de vida.
4. Se crea un QR único vinculado al equipo.
5. Se programa automáticamente su cronograma de mantenimiento.

---

## 🚀 Roadmap Técnico
- [x] Estructura inicial del backend en FastAPI.
- [x] Conexión con base de datos PostgreSQL.
- [ ] Módulo OCR para lectura de placas.
- [ ] Generación automática de QR por equipo.
- [ ] Hoja de vida digital con historial y mantenimientos.
- [ ] Cronograma inteligente según clase de equipo.
- [ ] Interfaz móvil/web para registro y escaneo.

---

## 📌 Gestión del Proyecto
Este repositorio se organiza con [GitHub Projects](https://github.com/users/duwanmosquare/projects), donde cada tarea está vinculada a su issue y Pull Request.  
Las tareas se agrupan en:
- **Todo:** funcionalidades pendientes.
- **In Progress:** módulos en desarrollo.
- **Done:** entregables completados y validados.

---

## 🤝 Cómo Contribuir
1. Haz fork del repositorio.
2. Crea una rama para tu funcionalidad:
   ```bash
   git checkout -b feature/nueva-funcionalidad
```
