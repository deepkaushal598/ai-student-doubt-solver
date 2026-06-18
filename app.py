from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os

from crewai import Agent, Task, Crew, LLM
from langchain_groq import ChatGroq

load_dotenv()

app = Flask(__name__)
#my name is yashh
# =========================
# GROQ LLM
# =========================


groq_key = os.getenv("GROQ_API_KEY")

langchain_llm = ChatGroq(
    groq_api_key=groq_key,
    model_name="llama-3.1-8b-instant"
)

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=groq_key
)
# =========================
# AGENTS
# =========================

physics_agent = Agent(
    role="Physics Expert",
    goal="Solve physics doubts in easy student language",
    backstory="You are an expert physics teacher helping students learn concepts simply.",
    llm=llm,
    verbose=False
)

chemistry_agent = Agent(
    role="Chemistry Expert",
    goal="Explain chemistry concepts clearly",
    backstory="You simplify chemistry for beginners.",
    llm=llm,
    verbose=False
)

math_agent = Agent(
    role="Math Expert",
    goal="Solve mathematical problems step by step",
    backstory="You are a professional math tutor.",
    llm=llm,
    verbose=False
)

notes_agent = Agent(
    role="Notes Generator",
    goal="Generate concise study notes",
    backstory="You create beautiful short notes for students.",
    llm=llm,
    verbose=False
)

quiz_agent = Agent(
    role="Quiz Generator",
    goal="Generate MCQs and quizzes",
    backstory="You create quizzes for learning revision.",
    llm=llm,
    verbose=False
)

# =========================
# FRONTEND
# =========================

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# =========================
# MODELS / AGENTS LIST
# =========================

@app.route("/api/models")
def models():
    return jsonify([
        {
            "id": "physics",
            "name": "Physics AI",
            "type": "Concept Expert"
        },
        {
            "id": "chemistry",
            "name": "Chemistry AI",
            "type": "Reaction Expert"
        },
        {
            "id": "math",
            "name": "Math AI",
            "type": "Problem Solver"
        },
        {
            "id": "notes",
            "name": "Notes AI",
            "type": "Study Notes"
        },
        {
            "id": "quiz",
            "name": "Quiz AI",
            "type": "MCQ Generator"
        }
    ])

# =========================
# CHAT API
# =========================

@app.route("/api/chat", methods=["POST"])
def chat():

    try:
        data = request.json

        user_message = data.get("message", "")
        selected_model = data.get("model", "physics")

        # SELECT AGENT

        selected_agent = physics_agent

        if selected_model == "chemistry":
            selected_agent = chemistry_agent

        elif selected_model == "math":
            selected_agent = math_agent

        elif selected_model == "notes":
            selected_agent = notes_agent

        elif selected_model == "quiz":
            selected_agent = quiz_agent

        # TASK

        task = Task(
            description=user_message,
            expected_output="Helpful educational response for the student.",
            agent=selected_agent
        )

        # CREW

        crew = Crew(
            agents=[selected_agent],
            tasks=[task],
            verbose=False
        )

        result = crew.kickoff()

        return jsonify({
            "success": True,
            "response": str(result),
            "model_used": selected_model
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })

# =========================

if __name__ == "__main__":
    app.run(debug=True)