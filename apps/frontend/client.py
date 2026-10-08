import json
import os
import socket
import time
from datetime import datetime, timezone

import requests


BACKEND_SERVICE = os.getenv("BACKEND_SERVICE")
REQUEST_INTERVAL = int(os.getenv("REQUEST_INTERVAL", "5"))
NODE_NAME = os.getenv("NODE_NAME", "unknown")
API_TOKEN = os.getenv("BACKEND_API_TOKEN")


while True:
    timestamp = datetime.now(timezone.utc).isoformat()
    pod_name = socket.gethostname()

    try:
        response = requests.get(
            f"http://{BACKEND_SERVICE}",
	    headers={
                "Authorization": f"Bearer {API_TOKEN}",
            },
            timeout=3,
        )

        print(
	    f"timestamp={timestamp} "
            f"pod={pod_name} "
            f"node={NODE_NAME} "
	    f"target=http://{BACKEND_SERVICE} "
	    f"status={response.status_code} "
            f"response={json.dumps(response.text)}",
            flush=True,
        )

    except requests.RequestException as e:
        print(
	    f"timestamp={timestamp} "
            f"pod={pod_name} "
            f"node={NODE_NAME} "
            f"target=http://{BACKEND_SERVICE} "
            f'error="connection refused"',
            flush=True,
        )

    time.sleep(REQUEST_INTERVAL)
