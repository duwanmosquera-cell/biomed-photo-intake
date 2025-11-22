Why
Clinics struggle with accurate inventory and organized documentation. This project lets technicians create a device record from a photo, attach documents, and auto‑assign a PM plan.

V0 Scope (2 weeks)
Device creation with photos (mobile‑first form).

PM templates by class/risk and next PM date.

QR generator linking to the device page.

Basic dashboard (traffic lights) and CSV export.

Quick start
Frontend: HTML/CSS/JS (responsive).

Backend: FastAPI/Node with SQLite.

Docs: GitHub Pages for guides and templates.

Roadmap
V0: manual intake + photos + PM template + QR
V1: OCR for plate (brand/model/serial) with human confirmation
V2: assisted class suggestion from image
V3: corrective maintenance workflow from QR + parts usage

Data model
Device(id, class, service, location, brand, model, serial, status, risk, next_pm, photos[])

PMTemplate(class, frequency, checklist)

Document(type, date, device_id, technician, attachments[], notes)

Project plan
Deliverables: minimal web demo, README, 10 GitHub issues (Project board).

Timeline: Week 1 CRUD+photos+QR; Week 2 PM templates+dashboard+CSV.

Metrics: <2 min intake; 100% devices with next PM; CSV export OK.

Getting involved
Questions or ideas? duwanmosquera@gmail.com.]
code.

