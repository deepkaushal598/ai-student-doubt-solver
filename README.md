# 🎓 AI Student Doubt Solver

A modern, fast chatbot interface for students to ask academic questions and get instant AI-powered answers using OpenRouter API.

## ✨ Features

- **Multiple AI Agents**: Switch between 5 different AI models/agents (all using the same OpenRouter API key)
- **Beautiful UI**: Modern dark-gradient design with smooth animations
- **Real-time Chat**: Instant responses from selected AI model
- **Responsive Design**: Works on desktop and mobile devices
- **Easy Setup**: One-click installation and configuration

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenRouter API Key (get it at https://openrouter.io)

### Installation

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Configure API Key**
   - Open `Main.py`
   - Find this line: `OPENROUTER_API_KEY = "your-openrouter-api-key-here"`
   - Replace with your actual OpenRouter API key

3. **Run the Application**
```bash
python Main.py
```

4. **Open in Browser**
   - Visit `http://localhost:5000`
   - Select an AI agent from the sidebar
   - Start asking your doubts!

## 🤖 Available AI Agents

1. **GPT-4 Turbo** - Advanced Reasoning (Best for complex problems)
2. **Claude 3 Opus** - General Purpose (Balanced & accurate)
3. **GPT-3.5 Turbo** - Fast Response (Quick answers)
4. **Mistral Large** - Code Expert (Programming help)
5. **Llama 2 70B** - Math Specialist (Math & science)

## 📝 How to Use

1. Open the application in your browser
2. Click on an AI agent in the left sidebar to select it
3. Type your question in the input box at the bottom
4. Press Enter or click "Send"
5. Wait for the AI response
6. Switch agents anytime to get different perspectives

## 🔧 Architecture

- **Backend**: Flask (Python) with OpenRouter API integration
- **Frontend**: Vanilla HTML, CSS, and JavaScript
- **API**: RESTful endpoints for model listing and chat

## 📁 Project Structure

```
AI student doubt solver/
├── Main.py              # Python Flask backend
├── index.html           # Frontend UI (HTML + CSS + JS)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## ⚙️ API Endpoints

- `GET /` - Load the web interface
- `GET /api/models` - Get list of available AI agents
- `POST /api/chat` - Send message and get response
- `GET /api/config` - Check if API key is configured

## 🔐 Security Notes

- Keep your OpenRouter API key private
- Don't commit your API key to version control
- Consider using environment variables for production

## 🐛 Troubleshooting

**"API Error" when sending messages?**
- Check if your OpenRouter API key is correct
- Verify you have sufficient credits on OpenRouter
- Check internet connection

**Port 5000 already in use?**
- Modify `app.run(debug=True, port=5000)` in Main.py to a different port

**Models not loading?**
- Ensure Flask server is running
- Check browser console for errors (F12)

## 📦 Dependencies

- Flask: Web framework
- Requests: HTTP library for API calls

## 🎨 Customization

You can easily customize:
- Chat colors: Modify the CSS gradients in index.html
- Available models: Edit `MODELS` list in Main.py
- System prompt: Change the "You are an expert educational assistant..." message
- UI styling: Edit the `<style>` section in index.html

## 📄 License

Free to use and modify for educational purposes.

## 🚀 Performance

- Lightning-fast UI rendering
- Minimal frontend dependencies (no frameworks needed)
- Streaming response support ready
- Handles multiple concurrent chats

---

**Happy Learning! 📚✨**
