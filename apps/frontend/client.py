import os
import socket
import time

import requests


BACKEND_SERVICE = os.getenv("BACKEND_SERVICE")
REQUEST_INTERVAL = int(os.getenv("REQUEST_INTERVAL", "5"))
NODE_NAME = os.getenv("NODE_NAME", "unknown")


while True:
    pod_name = socket.gethostname()

    try:
        response = requests.get(
            f"http://{BACKEND_SERVICE}",
            timeout=3,
        )

        print(
            f"[frontend] pod={pod_name} node={NODE_NAME} "
            f"-> {BACKEND_SERVICE}: {response.text}",
            flush=True,
        )

    except requests.RequestException as e:
        print(
            f"[frontend] pod={pod_name} node={NODE_NAME} "
            f"-> {BACKEND_SERVICE}: ERROR {e}",
            flush=True,
        )

    time.sleep(REQUEST_INTERVAL)
