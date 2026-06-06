from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    container_ip = socket.gethostbyname(socket.gethostname())
    return f"<h1>Hello Class! Served by Fargate Container IP: {container_ip}</h1>"

if __name__ == "__main__":
    # The application opens its door on Port 3000
    app.run(host="0.0.0.0", port=3000)
