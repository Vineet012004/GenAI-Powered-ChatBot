import streamlit as st
import time
from langchain_community.llms import Ollama

# --- Style Enhancements ---
st.markdown(
    """
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .block-container {
            padding-top: 2rem;
        }
        .chat-bubble-user {
            background-color:#DCF8C6;
            padding:10px;
            border-radius:10px;
            margin-bottom:10px;
            text-align:right;
            color: #000;
        }
        .chat-bubble-assistant {
            background-color:#ECECEC;
            padding:10px;
            border-radius:10px;
            margin-bottom:10px;
            text-align:left;
            color: #000;
        }
        .typing-dots {
            font-weight: bold;
            color: #666;
            font-size: 16px;
            margin-top: 5px;
        }
        .dot-1, .dot-2, .dot-3 {
            animation: blink 1.5s infinite;
        }
        .dot-2 {
            animation-delay: 0.2s;
        }
        .dot-3 {
            animation-delay: 0.4s;
        }
        @keyframes blink {
            0%   { opacity: 0.2; }
            20%  { opacity: 1; }
            100% { opacity: 0.2; }
        }
        .creator-credit {
            position: fixed;
            bottom: 10px;
            right: 20px;
            font-size: 14px;
            color: #888;
            z-index: 9999;
        }
        .custom-heading {
            font-size: 28px;
            font-weight: bold;
            color: #333;
            margin-bottom: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='creator-credit'>👨‍💻 Created by Vineet Sharma (LNMIIT) | 📧 vneetsharma01@gmail.com</div>",
    unsafe_allow_html=True,
)

st.title("💬 Chat with LLaMA 3 🤖")
st.markdown(
    "<div class='custom-heading'>Smart AI. Simple Talk. 🚀</div>",
    unsafe_allow_html=True,
)
st.subheader("🧠 Memory Enabled | 📥 Save Chat | 🎨 Stylish UI")

# Initialize Ollama with a lighter model for faster response
ollama = Ollama(model="mistral")

# Store message history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

# Clear Chat Feature
if st.button("🗑 Clear Chat"):
    st.session_state.clear()
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]
    st.rerun()


# Custom Chat Bubbles
def chat_bubble(message, is_user=True):
    bubble_class = "chat-bubble-user" if is_user else "chat-bubble-assistant"
    st.markdown(f"<div class='{bubble_class}'>{message}</div>", unsafe_allow_html=True)


# Display past messages
for msg in st.session_state["messages"]:
    chat_bubble(msg["content"], is_user=(msg["role"] == "user"))


# Generator for response (non-streaming)
def generate_response(prompt):
    messages = st.session_state["messages"][-5:]  # Only keep last 5 for speed
    response = ollama.invoke(input=prompt, messages=messages)
    return response


# Chat input and handling
if prompt := st.chat_input("Ask me anything..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    chat_bubble(prompt, is_user=True)

    with st.spinner("🤖 Thinking..."):
        st.markdown(
            '<div class="typing-dots">🤖 is typing<span class="dot-1">.</span><span class="dot-2">.</span><span class="dot-3">.</span></div>',
            unsafe_allow_html=True,
        )

        full_response = generate_response(prompt)
        chat_bubble(full_response, is_user=False)

    st.session_state["messages"].append({"role": "assistant", "content": full_response})

# Export Chat History
if st.button("🗓️ Download Chat"):
    chat_log = "\n\n".join(
        [
            f"{msg['role'].upper()}: {msg['content']}"
            for msg in st.session_state["messages"]
        ]
    )
    st.download_button("Download as .txt", chat_log, "chat_history.txt", "text/plain")
