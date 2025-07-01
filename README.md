# 🧮 Smart Calculator

A full-stack calculator web app built using **FastAPI** (Python) for backend and **HTML + Tailwind CSS** for frontend. It supports basic arithmetic operations and shows results in real-time.

---

## 🔧 Features

- FastAPI-powered REST API (`/calculate`)
- Interactive and clean UI with Tailwind CSS
- Real-time result display without page reload
- Frontend served directly by backend using static files

---

## 📁 Project Structure

calcu/
├── main.py # FastAPI backend logic
├── static/
│ └── index.html # Frontend HTML page



---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/smart-calculator.git
cd smart-calculator


pip install fastapi uvicorn

uvicorn main:app --reload

Visit: http://127.0.0.1:8000



