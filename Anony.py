import streamlit as st
import time

# Define a dictionary of responses
responses = {
    "hello": {"response": "Hi there! I'm an anonymous bot here to assist you.", "index": 1},
    "how are you": {"response": "I'm just a computer program, but I'm here and ready to help you.", "index": 2},
    "what all features an anonymous bot can provide": {"response": "I can assist you with various tasks as an  anonymous bot i can provide secure, encrypted messaging while ensuring user privacy and offering support features like reporting, guidance, and community engagement, fostering a safe environment for anonymous communication.","index": 3},
   "what is anonymous message": {"response": "An anonymous message is a communication sent without disclosing the sender's identity, often used for sharing information or opinions discreetly. It allows individuals to communicate freely while maintaining privacy, but can also be misused for malicious purposes like harassment or spreading false information.","index": 4},
    "what is local  message" : {"response":"A local message is a communication exchanged within a limited area or network, facilitating quick transmission without relying on external connections, often used for peer-to-peer sharing or local file transfers. ","index":6},
    "bye": {"response": "Goodbye! Have a nice day!", "index": 8},
}

# Streamed response emulator
def response_generator(prompt):
    if prompt.lower() in responses:
        response = responses[prompt.lower()]["response"]
    else:
        response = "I'm not sure how to respond to that. Please try again."
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Anony"" Bot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What can I help you with?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Feedback functionality
    if st.button("Provide Feedback"):
        feedback = st.text_area("Share your feedback:")
        if feedback:
            st.write("Thank you for your feedback! We appreciate your input.")
            # You can store the feedback in a database or file for further analysis