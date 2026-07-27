# 🍽️ Cafeteria Token System

A full-stack web application designed to streamline cafeteria operations and prevent resource abuse. This system allows students to generate secure, cryptographic QR code tokens for their daily meals, which cafeteria administrators can instantly verify and consume using a built-in webcam scanner.

## 🚀 Tech Stack

* **Frontend:** React, Vite, React Router, Axios
* **Backend:** Python, FastAPI, Uvicorn
* **Database:** SQLite, SQLAlchemy (ORM)
* **Hardware Integration:** `@yudiel/react-qr-scanner` for webcam barcode parsing

## ✨ Key Features

* **Frictionless Authentication:** Simplified login flow that automatically registers new users or logs in returning students via database verification.
* **Cryptographic Tokens:** Generates secure UUID-based QR codes that are nearly impossible to forge.
* **Double-Booking Defense:** Backend middleware enforces a strict "one meal per student" rule, instantly rejecting duplicate token requests.
* **Screenshot Prevention:** Once an admin scans a token, the database permanently marks it as `scanned`. If a student attempts to screenshot and share their QR code, the admin scanner will immediately flag it as "already used."
* **Cross-Origin Resource Sharing (CORS):** Fully configured middleware allowing seamless, secure communication between the Vite development server and the Python API.

---

## 🛠️ Local Installation & Setup

Because this is a full-stack application, the frontend and backend must be run simultaneously in two separate terminal windows.

### 1. Backend Setup (FastAPI)
Open your first terminal window and navigate to the project root.

cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload

The backend will be available at http://127.0.0.1:8000

### 2. Frontend Setup (React/Vite)
Open a new terminal window and navigate to the project root.

cd frontend
npm install
npm run dev

The frontend will be available at http://localhost:5173

---

## 📱 Application Flow

1. Student Portal (/login): Enter a Roll Number. The system will route you to your dashboard.
2. Token Generation (/student): Click "Generate Meal Token" to request today's allocation. A QR code is rendered on screen.
3. Admin Scanner (/admin): On a separate device or tab, open the Admin dashboard. Point the camera at the student's QR code. The system will securely read the UUID, verify it against the database, and mark the meal as consumed.
