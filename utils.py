import streamlit as st
import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image


def  store_value(key):
    st.session_state[key] = st.session_state["_"+key]

    
def  load_value(key):
    st.session_state["_"+key] = st.session_state[key]

def send_email(email_address):
    message = email_address #+'/'+name+'/'+transaction_id
    try:
        message = MIMEText(message)
        message['To'] = st.secrets['email_user']
        message['From'] = st.secrets['email_user']
        message['Subject'] = 'Datainsider Inquiry'

        context = ssl.create_default_context()
        server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
        server.starttls(context=context)
        server.login(st.secrets['email_user'], st.secrets['email_pass'])
        server.send_message(message, st.secrets['email_user'], st.secrets['email_user'])
        st.success('You have successfully been entered, please monitor your email to see if you won. \n Please note, regardless of the number of times you submit your email, you will recieve only 1 entry per donation. Feel free to scan the QR again to make a second donation!')
    except Exception as error:
        print(error)
        print('Unfortunately their was a submission error, please try again. If this error continues, please email "vera_1029@outlook.com" with the subject "Please help me I am Drowning') 