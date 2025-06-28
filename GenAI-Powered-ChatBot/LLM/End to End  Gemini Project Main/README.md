# 💬 TinyLLaMA Chatbot – Final Year Project

This project is a **locally running GenAI-powered chatbot** built using **LangChain**, **Ollama**, and **Streamlit**, powered by the lightweight `tinyllama` model for efficient offline conversational AI.

Developed by **Vineet Sharma (LNMIIT)** (May 2025 – June 2025).  
Email: vneetsharma01@gmail.com

---

## 🚀 Features

- 🔁 Memory-enabled conversation
- 💾 Chat download option
- 🎨 Stylish chat interface
- 🧠 Powered by TinyLLaMA (local LLM)
- 🗑️ Clear chat history
- 📍 Offline and open-source

---

## 🛠️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/Vineet012004/tinyllama_chatbot.git
```

### 2. Navigate into the project folder

```bash
cd tinyllama_chatbot
```

### 3. Install required Python dependencies

```bash
pip install -r requirements.txt
```

> Make sure you have Python ≥ 3.8 installed and activated in your environment.

### 4. Pull the TinyLLaMA model using Ollama

```bash
ollama pull tinyllama
```

---

## 💡 Usage

Start the chatbot using:

```bash
streamlit run app.py
```

- The chatbot will open in your default browser at:  
  `http://localhost:8501`

- Type your message in the input box.

- You can clear the conversation or download it as `.txt`.

---

## 🧠 Requirements

Make sure you have these installed:

- `ollama`
- `Python 3.8+`
- `Streamlit`
- `LangChain`
- `tinyllama` model (automatically downloaded via `ollama pull`)

---

## 📂 Folder Structure

```
tinyllama_chatbot/
├── app.py                 # Main Streamlit chatbot script
├── requirements.txt       # Required Python libraries
└── README.md              # This file
```

---

## 📢 Creator Info

👨‍💻 Created by: **Vineet Sharma (LNMIIT)**  
📧 Email: vneetsharma01@gmail.com  
📅 Duration: May 2025 – June 2025
