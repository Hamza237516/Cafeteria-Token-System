<div align="center">

# 🍽️ Cafeteria Token System

**A secure, cryptographic full-stack application to streamline cafeteria operations and eliminate resource abuse.**

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

---

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Key Features & Security](#-key-features--security)
- [Local Installation](#-local-installation)
- [Application Flow](#-application-flow)
- [Future Enhancements](#-future-enhancements)

---

## 🎯 Project Overview

The **Cafeteria Token System** is a full-stack web application designed to solve a real-world logistics problem: preventing duplicate meal claims and ensuring a frictionless dining experience.

Students log in to generate secure, one-time-use cryptographic QR codes for their daily meals. Cafeteria administrators use a built-in, hardware-integrated webcam scanner to instantly verify and consume the tokens in real time — no duplicate claims, no manual bookkeeping.

---

## 🧠 System Architecture

This project strictly adheres to the separation of concerns, decoupling the frontend user interface from the backend data API.

```text
CLIENT (Browser)                 SERVER (Localhost)
┌────────────────────┐           ┌────────────────────┐
│   React + Vite     │           │  FastAPI (Python)  │
│                    │ ◄───────► │                    │
│ - Hardware Scanner │   JSON    │ - CORS Middleware  │
│ - Axios API Client │   HTTP    │ - Double-book Logic│
│ - QR Generation    │           │ - UUID Generation  │
└────────────────────┘           └─────────┬──────────┘
                                           │
                                 ┌─────────▼──────────┐
                                 │  SQLite Database   │
                                 │  (SQLAlchemy ORM)  │
                                 └────────────────────┘
```

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React + Vite | Fast, component-driven UI |
| API Client | Axios | Handles HTTP requests to the backend |
| Backend | FastAPI (Python) | High-performance REST API |
| Database | SQLite + SQLAlchemy ORM | Lightweight, file-based persistence |
| Token Security | UUID4 | Cryptographically unique, one-time-use meal tokens |

---

## 🛡️ Key Features & Security

- **Frictionless Authentication** — A streamlined onboarding flow that securely registers new students or verifies returning users instantly.
- **Cryptographic Tokens** — Leverages UUID4 generation to create mathematically unique, unguessable meal tokens.
- **Double-Booking Defense** — Backend middleware enforces a strict database constraint, automatically rejecting duplicate token generation requests.
- **Anti-Screenshot Verification** — Once an admin scans a token, the database permanently updates its state. If a student screenshots and shares a QR code, the admin scanner immediately flags it as "already used."
- **Optical Fallback System** — The admin dashboard includes a manual-override input so operations continue even under poor lighting conditions.

---

## 🛠️ Local Installation

Because this is a decoupled full-stack application, the frontend and backend must be run simultaneously in two separate terminal windows.

### Prerequisites
- Node.js (v18+)
- Python (3.10+)

### 1. Start the Backend API

Open your first terminal window and navigate to the project root:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows users: venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

The API is now live and listening at: `http://127.0.0.1:8000`

### 2. Start the Frontend Application

Leave the backend running, open a new terminal window, and navigate to the project root:

```bash
cd frontend
npm install
npm run dev
```

The web interface is now live at: `http://localhost:5173`

---

## 📱 Application Flow

1. **Student Portal** (`/login`) — Enter a unique Roll Number to access the dashboard.
2. **Token Generation** (`/student`) — Request today's allocation. A scannable, margin-optimized QR code is rendered directly on screen.
3. **Admin Verification** (`/admin`) — On a separate device or tab, open the Admin dashboard. Point the camera at a student's QR code to securely read the UUID and instantly mark the meal as consumed in the database.

---

## 🚀 Future Enhancements

- [ ] **Role-Based Access Control (RBAC)** — Implement JWT tokens to explicitly separate Admin accounts from Student accounts.
- [ ] **Cloud Deployment** — Host the backend on Render and the frontend on Vercel for public access.
- [ ] **Data Analytics** — Build a dashboard for admins to visualize peak cafeteria hours and total meals served per week.

---

<div align="center">

**🍽️ Built to make cafeteria lines faster, fairer, and fraud-free.**

</div>
