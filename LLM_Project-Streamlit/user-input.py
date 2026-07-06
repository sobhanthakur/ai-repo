import streamlit as st
from ollama import Client

# Setting up the Streamlit page configuration
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Chatbot")

# Personal Information Section
st.subheader('Personal information', divider='rainbow')

# Input fields for collecting user's personal information
name = st.text_input(label = "Name", max_chars = None, placeholder = "Enter your name")
experience = st.text_area(label = "Expirience", value = "", height = None, max_chars = None, placeholder = "Describe your experience")
skills = st.text_area(label = "Skills", value = "", height = None, max_chars = None, placeholder = "List your skills")

st.write(f"**Your Name**: {name}")
st.write(f"**Your Experience**: {experience}")
st.write(f"**Your Skills**: {skills}")

st.subheader('Company and Position', divider = 'rainbow')
col1, col2 = st.columns(2)
with col1:
    level = st.radio(
    "Choose level",
    key="visibility",
    options=["Junior", "Mid-level", "Senior"],
    )

with col2:
    position = st.selectbox(
    "Choose a position",
    ("Data Scientist", "Data engineer", "ML Engineer", "BI Analyst", "Financial Analyst"))

company = st.selectbox(
    "Choose a Company",
    ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify")
)

st.write(f"**Your information**: {level} {position} at {company}")

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {st.secrets['API_KEY']}"
    }
)

if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = "gpt-oss:120b"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system", "content": f"You are an HR executive that interviews an interviewee called {name} with expirience {experience} and skills {skills}. You should interview him for the position {level} {position} at the company {company}"}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

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