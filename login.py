import streamlit as st
import pandas as pd
import utils

def app():
    st.title("Login Page")
    account = {
        "vera_1029@outlook.com": "1029",
        "oldhomeless@gmail.com": "0411",
    }

    username = st.text_input("Enter Email: ")
    password = st.text_input("Enter Password:")

    btn = st.button('Login here!')

    if btn:
        if username in account and password == account[username]:
            st.session_state['useremail'] = username
            st.success("Login and upload successfully!")
            uploaded_file = st.file_uploader('Upload an excel file from your data system', type='xlsx',key='_data', on_change=utils.store_value, args=['data'])
            if uploaded_file is None:
                st.success("Please upload a file")
            else:
                st.success("File uploaded successfully")
                df = pd.read_excel(uploaded_file)
                st.write(df)
            st.snow()
        else:
            st.error("Invalid username or password") # type: ignore
