# 📧 AI Email Responder using LangChain + Groq

An intelligent email automation system that reads incoming emails, detects user intent, and generates context-aware replies using **LangChain**, **Groq LLM**, and **LangSmith**.

---

## 🚀 Overview

This project is an AI-powered email assistant that automates responses by understanding the intent behind emails and generating human-like replies.

It is designed for use cases like:

* Customer support automation
* Email triaging
* Quick reply generation

---

## ✨ Features

* 📥 Fetch and process emails
* 🧠 Intent detection using LLM chains
* ✉️ AI-generated contextual responses
* ⚡ Fast inference using Groq API
* 📊 Monitoring with LangSmith
* 🔐 Secure API key handling using `.env`
* 🧩 Modular chain-based architecture

---

## 🛠️ Tech Stack

* Python
* LangChain (Core + Community)
* Groq API (LLM)
* LangSmith (Tracing & Monitoring)
* IMAPClient & Pyzmail (Email Parsing)

---

## 📂 Project Structure

```
EMAIL-RESPONDER-LANGCHAIN/
│── chains/
│   ├── intent_chain.py        # Detects user intent
│   ├── response_chain.py      # Generates response
│
│── prompts/
│   ├── intent_prompt.py       # Prompt for intent classification
│   ├── response_prompt.py     # Prompt for response generation
│
│── utils/
│   ├── llm_config.py          # LLM configuration (Groq setup)
│
│── main.py                    # Entry point
│── requirements.txt           # Dependencies
│── .env                       # API keys (not pushed to GitHub)
│── command.txt                # Commands / notes
│── README.md
│── venv/                      # Virtual environment (ignored)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/email-responder-langchain.git
cd email-responder-langchain
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```
langchain
langchain-core
langchain-community
langchain-groq
langsmith
python-dotenv
pydantic
tiktoken
faiss-cpu
chromadb
imapclient
pyzmail36
email-validator
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=email-responder
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 Working Flow

1. Email content is received or provided as input
2. `intent_chain.py` → Classifies the intent (complaint, query, etc.)
3. `response_chain.py` → Generates a response using LLM
4. Prompts from `prompts/` guide the LLM behavior
5. `llm_config.py` connects Groq API with LangChain

---

## 📌 Example

### Input:

```
I have not received my order yet. Please help.
```

### Output:

```
We’re sorry for the inconvenience. Kindly share your order ID so we can check the status for you.
```

---

## 📊 LangSmith Integration

* Tracks LLM execution
* Helps debug chains
* Monitors performance

---

## 🔮 Future Scope

* 📤 Auto-send emails using SMTP
* 🌐 Web UI using Streamlit
* 📚 Add RAG for better context
* 🌍 Multi-language support
* 🤖 Fine-tuned response generation

---

## 🙏 Acknowledgment

This project was developed as part of an internship, focusing on practical implementation of **LLMs, LangChain, and AI automation systems**.

---

## 📬 Author:

Shreya Sutar

Agentic AI
