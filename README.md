# 🧠 Mental Health Support Bot

Welcome to the **Mental Health Support Bot**—your AI-powered, compassionate companion designed to offer understanding, empathy, and practical wellness advice. Built with cutting-edge AI frameworks and a friendly interface, this project aims to make mental health support more accessible and personalized for everyone.

---

## ✨ Features

- **Emotion Understanding:** The bot listens to your words and gently senses your mood, providing support that truly resonates.
- **Empathetic Responses:** Receive kind, comforting messages tailored to your emotions, ensuring every conversation feels personal.
- **Personalized Self-Care Suggestions:** Get practical self-care ideas based on your preferences and needs, helping you build better wellness habits.
- **AI Teamwork:** Powered by CrewAI and LangChain, the bot leverages multiple specialized agents for smart, seamless interactions.
- **User-Friendly Interface:** An intuitive Streamlit UI makes connecting with your support bot easy and enjoyable.
- **Privacy-Focused:** Your conversations are handled securely, and environment variables are managed safely with Dotenv.

---

## 🛠️ Tech Stack

- **Python**
- **[CrewAI](https://github.com/joaomdmoura/crewAI)** (multi-agent framework)
- **[LangChain](https://github.com/langchain-ai/langchain)**
- **[OpenAI GPT](https://platform.openai.com/docs/api-reference/introduction)**
- **[Streamlit](https://streamlit.io/)** (for the UI)
- **[Dotenv](https://pypi.org/project/python-dotenv/)** (secure env variables)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ZJK-15/Mental_Health_Support_Bot.git
cd Mental_Health_Support_Bot
```

### 2. Install Dependencies

We recommend using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key
# Add other environment variables as needed
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open in your browser. Chat with the bot and receive support!

---

## 🤝 Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit and push (`git commit -am 'Add new feature' && git push origin feature/your-feature`)
5. Open a pull request

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Disclaimer

This bot is intended for general mental wellness support and is **not a substitute for professional medical advice, diagnosis, or treatment**. If you are experiencing a mental health crisis, please reach out to a qualified healthcare provider or call your local emergency number.


---

**With kindness and support,  
The Mental Health Support Bot Team**
