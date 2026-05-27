import socket
import json

log = {
    "service": "python-app",
    "level": "INFO",
    "message": "ELK stack log monitoring working successfully"
}

s = socket.socket()
s.connect(("localhost", 5000))

s.send(json.dumps(log).encode())

s.close()

print("Log sent successfully")