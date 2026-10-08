import hmac
import os
import socket

from flask import Flask, request


app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "unknown")
BACKEND_API_TOKEN = os.getenv("BACKEND_API_TOKEN", "")

@app.get("/health")
def health():
    return "OK", 200


@app.get("/ready")
def ready():
    return "READY", 200


@app.get("/")
def index():
    authorization = request.headers.get("Authorization", "")

    expected = f"Bearer {BACKEND_API_TOKEN}"

    if not hmac.compare_digest(authorization, expected):
        return "Unauthorized", 401

    pod_name = socket.gethostname()
    node_name = os.getenv("NODE_NAME", "unknown")

    return(
	"Hello from backend "
	f"pod={pod_name} "
	f"node={node_name} "
	f"version={APP_VERSION}"
    )

app.run(
    host="0.0.0.0",
    port=8080,
)
