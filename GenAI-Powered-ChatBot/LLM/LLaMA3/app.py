import streamlit as st
import time
from langchain_community.llms import Ollama

# --- Enhanced Retro-Style UI ---
st.markdown(
    """
    <style>
        /* Background gradient with motion */
        body {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            background-size: 600% 600%;
            animation: gradientMove 20s ease infinite;
            color: #f5f5f5;
        }

        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Texture overlay */
        body::after {
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            background: url("https://www.transparenttextures.com/patterns/asfalt-dark.png");
            opacity: 0.08;
            z-index: 0;
        }

        /* Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');
        html, body {
            font-family: 'Orbitron', sans-serif;
        }

        /* Main container */
        .main {
            background-color: rgba(0, 0, 0, 0.3) !important;
        }

        .block-container {
            padding-top: 2rem;
            position: relative;
            z-index: 1;
        }

        /* Chat Bubbles */
        .chat-bubble-user {
            background-color:#00ffc3;
            padding:10px;
            border-radius:10px;
            margin-bottom:10px;
            text-align:right;
            color: #000;
            box-shadow: 0 0 10px #00ffc3;
        }
        .chat-bubble-assistant {
            background-color:#ff2fe6;
            padding:10px;
            border-radius:10px;
            margin-bottom:10px;
            text-align:left;
            color: #000;
            box-shadow: 0 0 10px #ff2fe6;
        }

        /* Typing animation */
        .typing-dots {
            font-weight: bold;
            color: #fff;
            font-size: 16px;
            margin-top: 5px;
        }
        .dot-1, .dot-2, .dot-3 {
            animation: blink 1.5s infinite;
        }
        .dot-2 { animation-delay: 0.2s; }
        .dot-3 { animation-delay: 0.4s; }

        @keyframes blink {
            0%   { opacity: 0.2; }
            20%  { opacity: 1; }
            100% { opacity: 0.2; }
        }

        /* Creator tag */
        .creator-credit {
            position: fixed;
            bottom: 10px;
            right: 20px;
            font-size: 14px;
            color: #ccc;
            z-index: 9999;
        }

        /* Headings */
        .custom-heading {
            font-size: 28px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 8px #ff00ff;
        }
        .element-container h1, .element-container h2, .element-container h3, .element-container h4 {
            font-size: 16px !important;
            color: #ddd;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='creator-credit'>👨‍💻 Created by Vineet Sharma (LNMIIT) | 📧 vneetsharma01@gmail.com</div>",
    unsafe_allow_html=True,
)

# --- TITLE & TAGLINE ---
st.title("💬 Chat with LLaMA 3 🤖")
st.markdown(
    "<div class='custom-heading'>Smart AI. Simple Talk. 🚀</div>",
    unsafe_allow_html=True,
)

# Reduced subheader size visually via CSS
st.subheader("🧠 Memory Enabled | 💾 Save Chat | 🎨 Stylish UI")

# --- Load LLaMA 3 ---
ollama = Ollama(model="llama3")

# --- Chat History ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

# --- Clear Chat Button ---
if st.button("🗑️ Clear Chat"):
    st.session_state.clear()
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]
    st.rerun()


# --- Chat Bubble Renderer ---
def chat_bubble(message, is_user=True):
    bubble_class = "chat-bubble-user" if is_user else "chat-bubble-assistant"
    st.markdown(f"<div class='{bubble_class}'>{message}</div>", unsafe_allow_html=True)


# --- Render Past Messages ---
for msg in st.session_state["messages"]:
    chat_bubble(msg["content"], is_user=(msg["role"] == "user"))


# --- Response Generator ---
def generate_response(prompt):
    messages = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state["messages"]
    ]
    response = ollama.stream(input=prompt, messages=messages)
    full_response = ""
    for token in response:
        full_response += token
        yield token
    st.session_state["full_message"] = full_response


# --- Chat Input Box ---
if prompt := st.chat_input("Ask me anything..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    chat_bubble(prompt, is_user=True)

    with st.spinner("🤖 Thinking..."):
        st.markdown(
            '<div class="typing-dots">🤖 is typing<span class="dot-1">.</span><span class="dot-2">.</span><span class="dot-3">.</span></div>',
            unsafe_allow_html=True,
        )
        time.sleep(1.5)

        full_response = ""
        for token in generate_response(prompt):
            full_response += token
        chat_bubble(full_response, is_user=False)

    st.session_state["messages"].append({"role": "assistant", "content": full_response})

# --- Export Chat Button ---
if st.button("📥 Download Chat"):
    chat_log = "\n\n".join(
        [
            f"{msg['role'].upper()}: {msg['content']}"
            for msg in st.session_state["messages"]
        ]
    )
    st.download_button("Download as .txt", chat_log, "chat_history.txt", "text/plain")
