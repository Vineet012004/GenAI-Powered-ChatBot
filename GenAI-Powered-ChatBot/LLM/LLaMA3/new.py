from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

import streamlit as st
import os

# 📘 Prompt Template with memory
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful, polite assistant skilled in data science. You answer clearly and with examples.",
        ),
        MessagesPlaceholder(variable_name="history"),  # for chat history
        ("user", "{question}"),
    ]
)

# 🧠 Memory to store chat
memory = ConversationBufferMemory(return_messages=True)

# 🤖 Load local LLM (like Llama3)
llm = Ollama(model="llama3")

# 🔗 Connect prompt → model → output
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# 🌐 Streamlit UI
st.title("🔍 GenAI Chatbot with Memory + File Upload")

# 📁 File Upload section
uploaded_file = st.file_uploader("Upload a text or CSV file", type=["txt", "csv"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("File Content", content, height=150)
    st.session_state["file_data"] = content

# 🗣️ Chat Input
input_text = st.text_input("Ask something below 👇")

# 🧠 Store memory in session
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# 💬 Chatbot logic
if input_text:
    # Add memory to inputs
    full_prompt = {"question": input_text, "history": st.session_state["chat_history"]}

    # 🔄 Get response
    response = chain.invoke(full_prompt)

    # Show response
    st.write("🤖 Bot:", response)

    # Save to history
    st.session_state["chat_history"].append(("user", input_text))
    st.session_state["chat_history"].append(("assistant", response))
