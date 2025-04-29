# FastAPI To-Do Auth Demo 🚀

A professional FastAPI-based To-Do API with JWT Authentication.

## Features
- ✅ Secure Login (Get Bearer Token)
- ✅ Create Tasks
- ✅ View All Tasks
- ✅ View Single Task
- ✅ Update Tasks
- ✅ Delete Tasks
- ✅ Protected Endpoints (JWT Required)

## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

# 1. Login
# POST /login

# json
# Copy
# Edit
# {
#     "username": "admin",
#     "password": "password"
# }
# Response:

# json
# Copy
# Edit
# {
#     "access_token": "JWT_TOKEN",
#     "token_type": "bearer"
# }
# 2. Use Token
# Add Authorization header in every request:

# bash
# Copy
# Edit
# Authorization: Bearer YOUR_JWT_TOKEN
# 3. API Docs
# Swagger UI available at: http://127.0.0.1:8000/docs

# Folder Structure
# bash
# Copy
# Edit
# app/
# ├── __init__.py
# ├── main.py
# ├── models.py
# ├── schemas.py
# ├── auth.py
# requirements.txt
# README.md