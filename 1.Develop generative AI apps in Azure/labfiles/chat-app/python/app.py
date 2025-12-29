from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import os

from chat import get_openai_client, get_completion

# Load env and simple config
load_dotenv()
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "change-me-secret")

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json() or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Message is empty"}), 400

    # Initialize client
    try:
        openai_client, model_deployment = get_openai_client()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Initialize conversation in session
    if "prompt" not in session:
        session["prompt"] = [{"role": "system", "content": "You are a helpful AI assistant that answers questions."}]

    prompt = session["prompt"]
    prompt.append({"role": "user", "content": message})

    try:
        reply = get_completion(openai_client, model_deployment, prompt)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    prompt.append({"role": "assistant", "content": reply})
    session["prompt"] = prompt

    return jsonify({"reply": reply, "messages": prompt})


@app.route("/api/reset", methods=["POST"])
def api_reset():
    session.pop("prompt", None)
    return jsonify({"status": "reset"})


if __name__ == "__main__":
    # Listen on localhost:5000 by default
    app.run(host="127.0.0.1", port=5000, debug=True)
