from flask import Flask
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "WebRTC Signaling Server Running 🚀"

@socketio.on("offer")
def handle_offer(offer):
    emit("offer", offer, broadcast=True, include_self=False)

@socketio.on("answer")
def handle_answer( answer):
    emit("answer", answer, broadcast=True, include_self=False)

@socketio.on("ice-candidate")
def handle_ice(candidate):
    emit("ice-candidate", candidate, broadcast=True, include_self=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
