from flask import Flask, redirect, request, session, jsonify
import requests
import jwt

app = Flask(__name__)
app.secret_key = "secret"

KEYCLOAK_URL = "http://localhost:8080"
REALM = "Infotact"
CLIENT_ID = "flask-app"
CLIENT_SECRET = "KEY HERE"
REDIRECT_URI = "http://localhost:5000/callback"

@app.route("/")
def home():
    return '<a href="/login">Login with Keycloak</a>'

@app.route("/login")
def login():
    auth_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/auth"
    return redirect(f"{auth_url}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}")

@app.route("/callback")
def callback():
    code = request.args.get("code")

    token_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    token_response = requests.post(token_url, data=data).json()
    access_token = token_response.get("access_token")

    session["access_token"] = access_token

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "access_token" not in session:
        return redirect("/")

    decoded = jwt.decode(session["access_token"], options={"verify_signature": False})

    username = decoded.get("preferred_username")
    roles = decoded.get("realm_access", {}).get("roles", [])

    return jsonify({
        "user": username,
        "roles": roles
    })

@app.route("/admin")
def admin():
    if "access_token" not in session:
        return redirect("/")

    decoded = jwt.decode(session["access_token"], options={"verify_signature": False})
    roles = decoded.get("realm_access", {}).get("roles", [])

    if "admin" in roles:
        return "Welcome Admin 🔐"
    else:
        return "Access Denied ❌"

app.run(port=5000)

