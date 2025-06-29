-> This is a lightweight AI-powered customer support chatbot built using LangChain, Streamlit, and LLama3 via Ollama. -> The chatbot understands natural language queries and responds with helpful answers in real-time through an interactive and user-friendly web interface.



-> FEATURES

Memory-enabled conversation
Chat download option
Stylish chat interface
Powered by TinyLLaMA (local LLM)
Clear chat history
Offline and open-source



🛠 INSTALLATION

Clone this repository bash Copy Edit git clone https://github.com/Vineet012004/GenAI-Chatbot.git Replace yourusername with your GitHub username if you're uploading the project there.

Navigate into the project folder bash Copy Edit cd tinyllama_chatbot

Install required Python dependencies bash Copy Edit pip install -r requirements.txt Make sure you have Python ≥ 3.8 installed and activated in your environment.

Pull the TinyLLaMA model using Ollama bash Copy Edit ollama pull tinyllama.




💡 USAGE
Start the chatbot using:

- bash
- Copy
- Edit
- streamlit run app.py
- The chatbot will open in your default browser at:
- http://localhost:8501
Type your message in the input box. You can clear the conversation or download it as .txt.



🧠 REQUIREMENTS

Make sure you have these installed:

ollama
Python 3.8+
Streamlit
LangChain
llama3 model (automatically downloaded via ollama pull)




📂 Folder Structure

main.py: The main Streamlit application script.
langchain_helper.py: This has all the langchain code
requirements.txt: A list of required Python packages for the project.


📢 Creator Info Created by: Vineet Sharma (LNMIIT) Email: vneetsharma01@gmail.com 
    Duration: May 2025 – June 2025
