<!-- HERO SECTION -->
<div align="center">
  <img src="https://avatars.githubusercontent.com/u/98168252?v=4" alt="Gemini Telegram Bot" width="200" height="200" style="border-radius: 100%; object-fit: cover;"/>

  <h1>
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=35&duration=3000&pause=1000&color=8B5CF6&center=true&vCenter=true&width=600&lines=%F0%9F%94%A5+Gemini+Telegram+AI+Bot;Your+Personal+AI+Assistant;Powered+by+Google+Gemini+API" alt="Typing SVG" />
  </h1>

  <p align="center">
    <img src="https://img.shields.io/badge/AI_Gemini-Google-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
    <img src="https://img.shields.io/badge/Telegram-Bot-10B981?style=for-the-badge&logo=telegram&logoColor=white"/>
    <img src="https://img.shields.io/badge/Open_Source-Contributions_Welcome-F59E0B?style=for-the-badge"/>
  </p>

  <p align="center">
    <a href="https://x.com/emeediong_peter">
      <img src="https://img.shields.io/badge/𝕏-Follow_My_Journey-1DA1F2?style=for-the-badge&logo=x&logoColor=white"/>
    </a>
    <a href="https://www.linkedin.com/in/emediong-peter-81b46a330">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
    </a>
    <a href="https://github.com/EmediongPeter">
      <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/>
    </a>
  </p>

  <blockquote>
    <p><em>"Building Jarvis for everyday life: a multi-agentic assistant that can talk to other agents, execute tasks, and help you beyond simple Q&A."</em></p>
  </blockquote>
</div>

---

## 🗺️ Navigation

<div align="center">

| [🎯 **About**](#-project-overview) | [🧠 **Gemini API**](#-using-google-gemini-api) | [🛠️ **Tech Stack**](#️-arsenal) | [🚀 **Quick Start**](#-deployment-guide) | [🌟 **Improvements**](#-future-improvements) |
|:--:|:--:|:--:|:--:|:--:|

</div>

---

## 🎯 Project Overview

> **Meet Emediong Peter** - *AI Agentic Workflow Enthusiast & Telegram Bot Builder*

This repository is a creative journey into building a Telegram bot powered by **Google Gemini API**. The bot acts as a personal assistant, answering questions, executing tasks, and paving the way for multi-agentic workflows. The code is open-source and designed for extensibility—anyone can contribute and improve upon it!

---

## 🧠 Using Google Gemini API

### Why Gemini Instead of OpenAI?

- **Google Gemini API** offers powerful generative capabilities, similar to OpenAI, but with unique models and integration features.
- The bot uses Gemini’s `generate_content` endpoint to process user queries and return concise, accurate answers.

### How It Works

```python
try:
    response = client.models.generate_content(
        model=GEMINI_MODEL_NAME,
        contents=[
            genai_types.Content(role="user", parts=[
                genai_types.Part.from_text(text=user_msg)
            ]),
            # ...add previous history here if needed...
        ],
        config=genai_types.GenerateContentConfig(
            system_instruction="You are a helpful telegram bot assistant...",
            max_output_tokens=256,
        )
    )
    if response.text is not None:
        await message.answer(response.text.strip())
except Exception as e:
    logging.error("Error when calling Gemini API: %s", e)
    await message.answer("⚠️ Sorry, I couldn’t process that right now.")
```

- **All Gemini API calls are wrapped in try/except blocks** to ensure errors are caught and the user always receives a response.
- The bot listens for messages on Telegram, sends them to Gemini, and replies with the AI’s answer.

---

## 🛠️ Arsenal

| **Tool** | **Purpose** |
|:--|:--|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Bot & API integration |
| ![Aiogram](https://img.shields.io/badge/Aiogram-Telegram_Bot-0088CC?style=flat&logo=telegram&logoColor=white) | Telegram bot framework |
| ![Google Gemini](https://img.shields.io/badge/Gemini-API-4285F4?style=flat&logo=google&logoColor=white) | Generative AI |
| ![dotenv](https://img.shields.io/badge/dotenv-Env_Management-10B981?style=flat) | Secrets management |

---

## 🚀 Deployment Guide

### ⚡ Quick Start

```bash
# Clone the project
git clone https://github.com/EmediongPeter/ai-agents-learning
cd ai-agents-learning/telegram-bot

# Install dependencies
pip install -r requirements.txt

# Set up your .env file
cp .env.example .env
# Add your TELEGRAM_BOT_TOKEN and GEMINI_API_KEY

# Run the bot
python app.py
```

---

## 🌟 Future Improvements

> This project is open-source—**anyone can contribute and improve upon it!**

### Ideas for Next-Level Features

- **User-Specific Memory:**  
  Store chat history in a vector database or relational DB, tied to each Telegram user for personalized context.

- **Agentic Loop & Multi-Agent Workflows:**  
  Integrate with [n8n](https://n8n.io/) or build out with [LangChain](https://langchain.com/) to enable the bot to:
  - Communicate with other agents
  - Execute complex tasks (e.g., generate images, post to LinkedIn/X, reminders)
  - Become a true "Jarvis" for everyday life

- **Task Execution:**  
  Move beyond Q&A—let the bot perform actions based on user instructions.

---

## 🗂️ Repository Architecture

```
ai-agents-learning/
┣━━ telegram-bot/
┃   ┣━━ app.py                # Main bot logic
┃   ┣━━ requirements.txt      # Python dependencies
┃   ┗━━ .env.example          # Environment variable template
┣━━ README.md                 # This documentation
```

---

## 🤝 Join the Creative Community

<div align="center">

<img src="https://img.shields.io/github/followers/EmediongPeter?style=social" alt="GitHub followers" />
<img src="https://img.shields.io/github/stars/EmediongPeter?style=social" alt="GitHub stars" />

### 🔗 Connect & Collaborate

<a href="https://x.com/emeediong_peter">
  <img src="https://img.shields.io/badge/𝕏-Growth_Updates-1DA1F2?style=for-the-badge&logo=x&logoColor=white" alt="X (Twitter)"/>
</a>
<a href="https://www.linkedin.com/in/emediong-peter-81b46a330">
  <img src="https://img.shields.io/badge/LinkedIn-Professional_Network-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
<a href="https://github.com/EmediongPeter">
  <img src="https://img.shields.io/badge/GitHub-Code_Journey-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>

</div>

> **🚀 Ready to build the future of AI assistants together?**  
> *Open to collaborations, learning opportunities, and building the next generation of agentic bots.*

---

## 📝 License & Usage

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
📜 MIT License
├── ✅ Commercial use allowed
├── ✅ Modification allowed  
├── ✅ Distribution allowed
├── ✅ Private use allowed
└── ⚠️  Limitation of liability
```

---

<div align="center">

### 🤖 **"AI assistants are the new creative frontier—let's build Jarvis for everyone."**

<p><em>Built with ❤️ by Emediong Peter | Powered by Google Gemini | Open for contributions</em></p>

<a href="#-navigation">
  <img src="https://img.shields.io/badge/⬆️-Back_to_Top-8B5CF6?style=for-the-badge" alt="Back to top"/>
</a>

</div>

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=100&section=footer" width="100%"/>
</div>
