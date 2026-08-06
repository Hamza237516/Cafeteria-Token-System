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
- [Key Features & Security](#-key-features--security)
- [Local Installation](#-local-installation)
- [Application Flow](#-application-flow)
- [Future Enhancements](#-future-enhancements)

---

## 🎯 Project Overview

The **Cafeteria Token System** is a full-stack web application designed to solve a real-world logistics problem: preventing duplicate meal claims and ensuring a frictionless dining experience. 

Students can log in to generate secure, one-time-use cryptographic QR codes for their daily meals. Cafeteria administrators use a built-in, hardware-integrated webcam scanner to instantly verify and consume the tokens in real time. 

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
