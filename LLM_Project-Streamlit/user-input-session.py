import streamlit as st
from ollama import Client

# Setting up the Streamlit page configuration
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Chatbot")

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

def complete_setup():
    st.session_state.setup_complete = True

if not st.session_state.setup_complete:
    st.subheader('Personal information', divider='rainbow')

    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    # Input fields for collecting user's personal information
    name = st.text_input(label = "Name", max_chars = None, placeholder = "Enter your name")
    experience = st.text_area(label = "Expirience", value = "", height = None, max_chars = None, placeholder = "Describe your experience")
    skills = st.text_area(label = "Skills", value = "", height = None, max_chars = None, placeholder = "List your skills")

    st.write(f"**Your Name**: {name}")
    st.write(f"**Your Experience**: {experience}")
    st.write(f"**Your Skills**: {skills}")

    if "level" not in st.session_state:
        st.session_state["level"] = "Junior"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "company" not in st.session_state:
        st.session_state["company"] = "Amazon"

    st.subheader('Company and Position', divider = 'rainbow')
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state["level"] = st.radio(
        "Choose level",
        key="visibility",
        options=["Junior", "Mid-level", "Senior"],
        )

    with col2:
        st.session_state["position"] = st.selectbox(
        "Choose a position",
        ("Data Scientist", "Data engineer", "ML Engineer", "BI Analyst", "Financial Analyst"))

    st.session_state["company"] = st.selectbox(
        "Choose a Company",
        ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify")
    )
    
    st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")

    if st.button("Start Interview", on_click=complete_setup):
        st.write("Setup complete. Starting interview...")


if st.session_state.setup_complete:
    # Display a welcome message and prompt the user to introduce themselves
    st.info(
        """
        Start by introducing yourself.
        """,
        icon = "👋"
    )

    client = Client(
        host="https://ollama.com",
        headers={
            "Authorization": f"Bearer {st.secrets['API_KEY']}"
        }
    )

    if "ollama_model" not in st.session_state:
        st.session_state["ollama_model"] = "gpt-oss:120b"

    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "system",
            "content": (f"You are an HR executive that interviews an interviewee called {st.session_state['name']} "
                        f"with experience {st.session_state['experience']} and skills {st.session_state['skills']}. "
                        f"You should interview him for the position {st.session_state['level']} {st.session_state['position']} "
                        f"at the company {st.session_state['company']}")
        }]

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
                options={
                    "num_predict": 200,   # Max output tokens
                }
            )
            response = st.write_stream(
                chunk["message"]["content"] for chunk in stream
            )
            # Display the assistant's response as it streams
        # Append the assistant's full response to the 'messages' list
        st.session_state.messages.append({"role": "assistant", "content": response})