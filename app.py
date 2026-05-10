from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "DevOps CI/CD Pipeline updated automatically from GitHub Actions",
        "status": "OK",
        "version": "2.0",
        "technology": "GitHub Actions + DockerHub",
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "version": "2.0"
    }

@app.route("/info")
def info():
    return {
        "project": "DevOps CI/CD Practice",
        "repository": "GitHub",
        "container_registry": "DockerHub",
        "pipeline": "Automatic build and push using GitHub Actions",
        "version": "2.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)