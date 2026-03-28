# 🚀 RootLens

> Trace failures. Identify root causes. Understand your system.

---

## 📌 Overview

RootLens is an AI-assisted system for analyzing application logs, detecting failures, and identifying their root causes. It ingests structured logs, correlates events across services, reconstructs timelines, and generates actionable insights for debugging distributed systems.

---

## 🎯 Key Features

* Log ingestion via API
* Advanced log querying and filtering
* Event correlation across services
* Timeline reconstruction of failures
* Root cause analysis (rule-based + AI-assisted)
* Impact analysis (affected services, duration, severity)
* Incident summary dashboard

---

## 🧱 Architecture

```
Frontend (Next.js)
        ↓
Backend (FastAPI)
        ↓
PostgreSQL + Redis
```

---

## 🧰 Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy (async)
* asyncpg
* Pydantic

### Database

* PostgreSQL

### Async / Queue

* Redis
* Celery

### AI

* OpenAI API

### Frontend

* Next.js
* TypeScript
* Tailwind CSS
* Recharts

### Infrastructure

* Docker
* Docker Compose

---

## 📂 Project Structure

```
root-cause-analyzer/
│
├── backend/
├── frontend/
├── infra/
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone <your-repo-url>
cd root-cause-analyzer
```

### 2. Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend Setup

```
cd frontend
npm install
npm run dev
```

---

## 📡 Core APIs (MVP)

* `POST /ingest-log` → Ingest logs
* `GET /logs` → Query logs
* `GET /timeline` → Failure timeline
* `POST /analyze` → Root cause analysis
* `GET /incident-summary` → Final insights

---

## 🎯 MVP Goal

Given a set of logs, the system should:

* reconstruct a clear failure timeline
* identify the most probable root cause
* summarize impact across services

---

## ⚠️ Notes

* AI is used only for explanation, not core logic
* Rule-based analysis is implemented first
* System is designed to scale with async processing and advanced analytics

---

## 📌 Future Enhancements

* Anomaly detection
* Deployment correlation
* Alerting system
* Advanced visualizations

---

## 📜 License

MIT License (or choose your preferred license)
