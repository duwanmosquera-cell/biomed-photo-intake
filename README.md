# 📸 Biomed Photo Intake / Recepción de fotos biomédicas  
**Python FastAPI + n8n + Docker**

---

## 🧠 Intelligent Management of Biomedical Equipment
### 🌟 Project Vision
This system digitizes the registration, traceability, and maintenance of biomedical equipment in hospitals, clinics, and laboratories.  
Each device is registered through a photo of its label, automatically generates a digital life record, and is assigned a maintenance schedule based on its technical classification.

---

## 📱 Key Features
- 📸 Equipment registration with OCR (optical character recognition from labels).  
- 🗂️ Dynamic inventory with an updatable database.  
- 📄 Digital life record per device (model, serial number, batch, location, history).  
- 📅 Automated maintenance scheduling (quarterly, semiannual, annual).  
- 🔗 Unique QR code generation per device for direct access to its life record.  
- ⚙️ Workflow automation with **n8n** (alerts, GitHub issues, notifications).  

---

## ⚙️ Technical Architecture
- **Frontend:** Mobile/web app for data capture and QR scanning.  
- **Backend:** FastAPI with RESTful endpoints and Swagger documentation.  
- **OCR:** pytesseract or cloud services for label reading.  
- **Database:** PostgreSQL with tables:  
  - `equipos` → technical data of the device.  
  - `hojas_de_vida` → history and associated events.  
  - `mantenimientos` → schedule and records per device.  
- **Visualization:** Dashboards via Power BI or web interface.  
- **Automation:** n8n workflows deployed via Docker.  

---

## 🧩 Registration Flow
1. A biomedical device is identified.  
2. A photo of its label is taken and data is extracted via OCR.  
3. The device is registered in the database and its life record is generated.  
4. A unique QR code is created and linked to the device.  
5. A maintenance schedule is automatically assigned based on its classification.  
6. Alerts and GitHub issues are triggered via n8n when `estado = "fallo crítico"`.  

---

## 🚀 Deployment (Docker + n8n)
Run n8n locally with Docker:
```bash
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
