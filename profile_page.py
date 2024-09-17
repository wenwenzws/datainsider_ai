import streamlit as st
import stripe
from stripe import StripeClient

def app():
    st.title("Profile Page")
    st.write("This is the profile page")
    st.write("You can view and edit your profile here")
    st.snow()
    st.balloons()
