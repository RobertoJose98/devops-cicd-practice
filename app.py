from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "DevOps CI/CD Practice running successfully",
        "status": "OK",
        "technology": "GitHub Actions + DockerHub",
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)