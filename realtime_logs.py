import socket
import json
import time
import random

messages = [
    "User login success",
    "Payment completed",
    "Database connected",
    "API request received",
    "File uploaded",
    "Server running normally",
    "Invalid login attempt",
    "Memory usage high"
]

levels = ["INFO", "WARNING", "ERROR"]

while True:

    log = {
        "service": "python-app",
        "level": random.choice(levels),
        "message": random.choice(messages)
    }

    s = socket.socket()
    s.connect(("localhost", 5000))

    s.send(json.dumps(log).encode())

    s.close()

    print(log)

    time.sleep(3)