# 📸 Biomed Photo Intake / Recepción de fotos biomédicas

## 🎯 Goal / Objetivo

Register biomedical devices from photos and auto-assign preventive maintenance plans.  
Registrar dispositivos biomédicos desde fotos y asignar automáticamente planes de mantenimiento preventivo.

## 📦 Scope V0 (2 weeks) / Alcance V0 (2 semanas)

- Device intake with photos (mobile-first form).  
  Alta de equipo con fotos (formulario móvil).
- PM templates by class/risk and next PM date.  
  Plantillas PM por clase/riesgo y fecha próxima.
- QR generator linked to device page.  
  Generador de QR vinculado a la ficha del equipo.
- Basic dashboard (traffic lights) and CSV export.  
  Dashboard básico (semáforo) y exportación CSV.

## 🚀 Quick start / Inicio rápido

- **Frontend**: HTML/CSS/JS (responsive).
- **Backend**: FastAPI with SQLite.
- **Docs**: GitHub Pages for guides and templates.

## 🗺️ Roadmap / Ruta técnica

- V0: manual intake + photos + PM template + QR
- V1: OCR for plate (brand/model/serial)
- V2: assisted class suggestion from image
- V3: corrective maintenance workflow from QR

## 🧬 Data model / Modelo de datos

```python
Device(id, class, service, location, brand, model, serial, status, risk, next_pm, photos[])
PMTemplate(class, frequency, checklist)
Document(type, date, device_id, technician, attachments[], notes)
```
