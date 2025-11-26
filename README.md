# 📸 Biomed Photo Intake / Recepción de fotos biomédicas

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)
# 🧠 Intelligent Management of Biomedical Equipment

## 🌟 Project Vision
This system aims to digitize the registration, traceability, and maintenance of biomedical equipment in hospitals, clinics, and laboratories.  
Each device is registered through a photo of its label, automatically generates a digital life record, and is assigned a maintenance schedule based on its technical classification.

---

## 📱 Key Features
- 📸 Equipment registration with OCR (optical character recognition from labels).
- 🗂️ Dynamic inventory with an updatable database.
- 📄 Digital life record per device (model, serial number, batch, location, history).
- 📅 Automated maintenance scheduling (quarterly, semiannual, annual).
- 🔗 Unique QR code generation per device for direct access to its life record.

---

## ⚙️ Technical Architecture
- **Frontend:** Mobile/web app for data capture and QR scanning.
- **Backend:** FastAPI with RESTful endpoints and Swagger documentation.
- **OCR:** `pytesseract` or cloud services for label reading.
- **Database:** PostgreSQL with the following tables:
  - `equipos` → technical data of the device.
  - `hojas_de_vida` → history and associated events.
  - `mantenimientos` → schedule and records per device.
- **Visualization:** Dashboards via Power BI or web interface.

---

## 🧩 Registration Flow
1. A biomedical device is identified.
2. A photo of its label is taken and data is extracted via OCR.
3. The device is registered in the database and its life record is generated.
4. A unique QR code is created and linked to the device.
5. A maintenance schedule is automatically assigned based on its classification.

---

## 🚀 Technical Roadmap
- [x] Initial backend structure in FastAPI.
- [x] PostgreSQL database connection.
- [ ] OCR module for label reading.
- [ ] Automatic QR generation per device.
- [ ] Digital life record with history and maintenance logs.
- [ ] Smart scheduling based on device class.
- [ ] Mobile/web interface for registration and scanning.

---

## 📌 Project Management
This repository is organized using [GitHub Projects](https://github.com/users/duwanmosquare/projects), where each task is linked to its issue and Pull Request.  
Tasks are grouped into:
- **Todo:** pending features.
- **In Progress:** modules under development.
- **Done:** completed and validated deliverables.

---

## 🤝 How to Contribute
1. Fork the repository.
2. Create a branch for your feature:
   ```bash
   git checkout -b feature/new-feature
