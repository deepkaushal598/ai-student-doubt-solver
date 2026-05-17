from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='.', static_folder='.')

# ===============================
# API CONFIG
# ===============================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# ===============================
# FAKE AGENTS (ALL USE SAME MODEL)
# ===============================

models = [
    {
        "id": "llama",
        "name": "Llama 3.1",
        "type": "Fast AI"
    },
    {
        "id": "gemini",
        "name": "Gemini Pro",
        "type": "Study Helper"
    },
    {
        "id": "gpt4",
        "name": "GPT-4 Turbo",
        "type": "Smart Reasoning"
    },
    {
        "id": "claude",
        "name": "Claude AI",
        "type": "Long Answers"
    },
    {
        "id": "physics",
        "name": "Physics Mentor",
        "type": "Science Expert"
    },
    {
        "id": "coder",
        "name": "Code Assistant",
        "type": "Programming AI"
    }
]

# ===============================
# ROUTES
# ===============================

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/api/models')
def get_models():
    return jsonify(models)


@app.route('/api/chat', methods=['POST'])
def chat():

    try:

        data = request.json

        user_message = data.get("message", "")
        selected_model = data.get("model", "llama")

        # All fake agents use same REAL model
        model_map = {
            "llama": "llama-3.1-8b-instant",
            "gemini": "llama-3.1-8b-instant",
            "gpt4": "llama-3.1-8b-instant",
            "claude": "llama-3.1-8b-instant",
            "physics": "llama-3.1-8b-instant",
            "coder": "llama-3.1-8b-instant"
        }

        real_model = model_map.get(
            selected_model,
            "llama-3.1-8b-instant"
        )

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": real_model,
            "messages": [
                {
                    "role": "system",
                    "content": """
                    You are a smart and friendly AI teacher.
                    Explain everything in simple student-friendly language.
                    Give clean formatting and points.
                    """
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        response = requests.post(
            GROQ_URL,
            headers=headers,
            json=payload
        )

        result = response.json()

        print(result)

        # Handle API errors
        if "choices" not in result:

            error_message = "Something went wrong"

            if "error" in result:
                error_message = result["error"].get(
                    "message",
                    "API Error"
                )

            return jsonify({
                "success": False,
                "error": error_message
            })

        ai_response = result["choices"][0]["message"]["content"]

        return jsonify({
            "success": True,
            "response": ai_response,
            "model_used": real_model
        })

    except Exception as e:

        print("SERVER ERROR:", str(e))

        return jsonify({
            "success": False,
            "error": str(e)
        })


# ===============================
# RUN APP
# ===============================

if __name__ == "__main__":
    app.run(debug=True, threaded=True)