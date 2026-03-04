# 🔐 Zero Trust IAM System using Keycloak + Flask
## 📌 Project Overview

This project demonstrates a real-world Zero Trust Identity & Access Management (IAM) implementation using:
Keycloak as Identity Provider (IdP)
Flask as Client Application
PostgreSQL as backend database
OpenID Connect (OIDC) for authentication
JWT for token-based authorization
Role-Based Access Control (RBAC)
Multi-Factor Authentication (MFA - TOTP)
Audit Logging & Event Monitoring
This project simulates an enterprise-grade IAM architecture.

## 🏗 Architecture
User
 ↓
Flask App (Client)
 ↓ OIDC
Keycloak (Identity Provider)
 ↓
PostgreSQL (Database)

## Security Layers Implemented

OIDC Single Sign-On (SSO)
JWT Token Validation
Role-Based Access Control (RBAC)
Multi-Factor Authentication (TOTP)
Audit Event Logging
Admin Event Monitoring

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|----------|
| Identity & Access Management | Keycloak | Authentication, Authorization, SSO |
| Database | PostgreSQL | Persistent storage for Keycloak |
| Application Layer | Flask (Python) | OIDC Client Application |
| Auth Protocol | OpenID Connect (OIDC) | Secure authentication flow |
| Token Standard | JWT | Stateless token-based security |
| MFA | TOTP | Time-based One-Time Password verification |
| Container Platform | Docker | Service isolation & deployment |

## 🚀 Features

🔑 1. Single Sign-On (SSO)
Secure login redirect to Keycloak
OIDC authorization code flow
Token exchange & session handling

🛡 2. Role-Based Access Control (RBAC)
Admin role
Viewer role
Route protection inside Flask app
Access denied for unauthorized users

🔐 3. Multi-Factor Authentication (MFA)
OTP setup via QR Code
Enforced TOTP during login
Browser authentication flow modification

🧾 4. JWT Token Decoding
Token parsing
Role extraction
Claim validation

📊 5. Audit Logging
Login events
Logout events
Token events
Admin configuration events

## 🖥 How to Run the Project
1️⃣ Start Keycloak (Docker)
docker run -d ^
-p 8080:8080  ^
-e KEYCLOAK_ADMIN=admin ^
-e KEYCLOAK_ADMIN_PASSWORD=admin123 ^
--name keycloak ^
quay.io/keycloak/keycloak:latest start-dev

2️⃣ Setup PostgreSQL (Docker)
docker run -d ^
--name postgres ^
-e POSTGRES_DB=keycloak ^
-e POSTGRES_USER=keycloak ^
-e POSTGRES_PASSWORD=keycloak ^
-p 5432:5432 ^
postgres

3️⃣ Configure Keycloak

Create Realm
Create Client (flask-app)
Configure Redirect URI: http://localhost:5000/callback
Create Roles (Admin, Viewer)
Create Users
Map Roles to Users
Enable MFA (Configure OTP)
Enable Event Logging

4️⃣ Run Flask App

Install dependencies: pip install -r requirements.txt
Run: python app.py

Open browser: http://localhost:5000

## 🧪 Test Scenarios
✔ Admin User

* Login
* Access /admin route
* Should display: "Welcome Admin"

✔ Viewer User

* Login
* Access /admin route
* Should display: "Access Denied"

✔ MFA Flow

* Password
* OTP verification
* Successful login

✔ Audit Logs

* View login events in Keycloak
* Verify admin actions logging

📂 Project Structure
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── login.png
│   ├── otp.png
│   ├── admin_access.png
│   ├── logs.png
└── architecture_diagram.png

## 🔎 Security Concepts Demonstrated

Zero Trust Architecture
Centralized Identity Management
Secure Token-Based Authentication
Access Control Enforcement
Multi-Factor Authentication
Identity Audit & Monitoring

## 🎯 Learning Outcome

This project demonstrates practical understanding of:

IAM Architecture
Identity Federation
Secure Authentication Flows
Role Mapping & Authorization
Production-ready Security Controls

## 🚀 Future Enhancements

Docker Compose full stack
HTTPS (TLS) configuration
Reverse proxy (NGINX)
Deployment on cloud (AWS / Azure)
SIEM integration for logs
OAuth2 token introspection endpoint validation

👨‍💻 Author

Baji Shaik
Cybersecurity & IAM Enthusiast
