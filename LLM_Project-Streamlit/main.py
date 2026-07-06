# Importing necessary libraries
from ollama import Client
import streamlit as st

# Setting up the Streamlit page configuration
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Chatbot")

# Initializing the OpenAI client using the API key from Streamlit's secrets
client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {st.secrets['API_KEY']}"
    }
)

# Setting up the OpenAI model in session state if it is not already defined
if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = "gpt-oss:120b"

# Initializing the 'messages' list 
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful tool that speaks like a pirate"}]


# Looping through the 'messages' list to display each message except system messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
# It helps running the chatbot in repeat mode
# Input field for the user to send a new message
prompt = st.chat_input("Your answer.")
if prompt:
    # Appending the user's input to the 'messages' list in session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display the user's message in a chat bubble
    with st.chat_message("user"):
        st.markdown(prompt)
   
    # Assistant's response
    with st.chat_message("assistant"):
        stream = client.chat(
            model=st.session_state["ollama_model"],
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(
            chunk["message"]["content"] for chunk in stream
        )
        # Display the assistant's response as it streams
     # Append the assistant's full response to the 'messages' list
    st.session_state.messages.append({"role": "assistant", "content": response})