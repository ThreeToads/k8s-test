import os
import socket

from flask import Flask


app = Flask(__name__)


@app.get("/")
def index():
    pod_name = socket.gethostname()
    node_name = os.getenv("NODE_NAME", "unknown")

    return f"Hello from server: pod={pod_name} node={node_name}"


app.run(host="0.0.0.0", port=8080)
