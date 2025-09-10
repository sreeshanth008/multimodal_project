import streamlit as st

from agents import MasterAgent






# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        if (prompt) :
            try:
                weather_api_key="bDSwa5u31no621tcFnhyQvMWLnUDGVKQ"
                master=MasterAgent(weather_api_key)

                assistant_response = master.perform_task(prompt)
            except Exception as e:
                assistant_response = f"Error: {str(e)}" 
        else:
            assistant_response = "Please enter your Huggingface API key in the sidebar to get a response."
        # Simulate stream of response with milliseconds delay
       
        message_placeholder.markdown(assistant_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
