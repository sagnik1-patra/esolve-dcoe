🏦 Esolve DCOE (Debt Collection Orchestration Engine)

A full-stack backend & frontend system for managing debt collection workflows across multiple banks — built with FastAPI, PostgreSQL, and React (Vite + Tailwind).

🚀 Overview

The Debt Collection Orchestration Engine (DCOE) automates the lifecycle of debt cases:

📥 Receives debt data (CSV/JSON) from banks

🔄 Normalizes & stores it in PostgreSQL

🧠 Assigns cases dynamically to Call Center, Field, or Legal teams

🔐 Secures APIs with JWT and role-based access

📊 Generates analytics summaries for Admins

🧩 Tech Stack
Layer	Technology
Frontend	React + Vite + TailwindCSS + Axios + Recharts
Backend	FastAPI + SQLAlchemy + PostgreSQL
Authentication	JWT (via python-jose)
Containerization	Docker + Docker Compose
Docs	Swagger/OpenAPI (/docs)
Deployment	Railway (Backend) + Netlify (Frontend)
🧠 Architecture Diagram
               ┌────────────────────────────┐
               │         Frontend (React)    │
               │  - Upload Cases             │
               │  - Case Table UI            │
               │  - Analytics Dashboard      │
               └────────────┬────────────────┘
                            │
                            ▼
               ┌────────────────────────────┐
               │      FastAPI Backend       │
               │  /cases, /auth, /analytics │
               │  JWT Auth + Rule Engine    │
               └────────────┬────────────────┘
                            │
                            ▼
               ┌────────────────────────────┐
               │      PostgreSQL Database    │
               │  - Users, Cases, AuditTrail │
               └────────────────────────────┘

⚙️ Functional Modules
Module	Key Features
Case Ingestion	Upload debt cases (CSV/JSON) via /cases/upload. Data validation + normalization before storage.
Assignment Engine	Auto-assigns cases using rules.json — based on days_past_due.
Status Management	Update & track case progress (Pending, In Progress, etc.).
Analytics	/analytics/summary provides case distribution, team load, and recovery stats.
Authentication	/auth/login issues JWT tokens for Admins, Leads, and Agents.
Security	Role-based access, password hashing, and audit logging.
🛠️ Local Setup (Development)
1️⃣ Clone the Repo
git clone https://github.com/annan-sadr/esolve-dcoe.git
cd esolve-dcoe

2️⃣ Run Backend
cd backend
docker-compose up --build


Backend will start at: http://localhost:8000

📘 Swagger Docs → http://localhost:8000/docs

3️⃣ Run Frontend

Open another terminal:

cd frontend
npm install
npm run dev


Frontend runs at: http://localhost:5173

To connect the frontend with your backend, create a file .env inside /frontend:

VITE_API_URL=http://localhost:8000

🧩 Folder Structure
esolve-dcoe/
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── cases/
│   │   ├── analytics/
│   │   ├── utils/
│   │   └── main.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── README.md
└── DESIGN_SUMMARY.md

🔑 API Endpoints Summary
Method	Endpoint	Description
POST	/auth/login	Authenticate user (JWT)
POST	/cases/upload	Upload debt cases (CSV or JSON)
GET	/cases	Fetch all cases
PATCH	/cases/{case_id}/update-status	Update case status
GET	/analytics/summary	Analytics overview
🔐 Roles
Role	Capabilities
Admin	Full access: upload, assign, analytics
Team Lead	View & manage team cases
Agent	View + update assigned cases
🧮 Example Assignment Rules (rules.json)
{
  "rules": [
    {"min": 0, "max": 30, "team": "Call Center"},
    {"min": 31, "max": 90, "team": "Field Agent"},
    {"min": 91, "max": 9999, "team": "Legal Team"}
  ]
}

🧪 Testing

To run FastAPI tests:

pytest


To test API manually, use:

Swagger UI → /docs

Postman Collection (included in repo)

☁️ Deployment Guide
🚀 Backend (Railway)

Go to https://railway.app

Create a New Project → Deploy from GitHub

Select this repo (esolve-dcoe)

Add environment variables:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=dcoe_db
POSTGRES_HOST=db


Railway auto-deploys Docker and exposes your API
✅ Copy your backend URL (e.g. https://dcoe-api.up.railway.app)
