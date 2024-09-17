import streamlit as st
def app():
    st.title("Contact Page")
    st.write("Any requests, please feel free to contact us")
    st.write("We are happy to help you")
    st.snow()
    st.balloons()
    container = st.container(border=True)
    with container:
        cols1, cols2 = st.columns([7,2])
        cols1.subheader(':green[Chat with Us]')
        cols1.markdown('Contact via: [E-mail](lovewenwenbb@gmail.com)')