
import streamlit as st
import requests



st.title("CONFIDANT - A COMPANION TO TALK TO") #Page title
query = st.text_input("Start a chat...") # Taking the message

if st.button("Send"):
    reply_ready = False
    typing_placeholder = st.empty()
    typing_placeholder.write("Typing....")
    try:
        response = requests.post("http://localhost:5000/query",json={"query":query})
    except:
        ConnectionError()
        st.write("Error occured!!")

    if response.status_code == 200:
        typing_placeholder.empty()
        st.write(response.text)
    else:
        st.write("Error occured while fetching the result")
    


