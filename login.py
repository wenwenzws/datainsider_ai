import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import utils


def app():
    st.title("Login Page")
    # Create tabs
    tabs = st.tabs(["Login", "Subscribe", "Documentation"])
    with tabs[0]:
        login()
    with tabs[1]:
        sub()
    with tabs[2]:
        doc()


def login():
    account = {
        "vera_1029@outlook.com": "1029",
        "oldhomeless@gmail.com": "0411",
        "guest": "9999"
    }
    username = st.text_input("Enter Email: ")
    password = st.text_input("Enter Password:")

    btn = st.button("Login here!", key="login_txt")

    if btn:
        if username in account and password == account[username]:
            st.session_state["useremail"] = username
            st.success("Login and upload successfully!")
            uploaded_file = st.file_uploader(
                "Upload an excel file from your data system",
                type="xlsx",
                key="_data",
                on_change=utils.store_value,
                args=["data"],
            )
            if uploaded_file is None:
                st.success("Please upload a file")
            else:
                st.success("File uploaded successfully")
                df = pd.read_excel(uploaded_file)
                st.write(df)
            st.snow()
        else:
            st.error("Invalid username or password")


def sub():
    with st.container(border=True):
        checkbox_agree = st.checkbox(
            "I Understand and Agree with the Terms and Conditions"
        )
        cols = st.columns([1, 1])
        if checkbox_agree:
            with cols[0]:
                components.html(
                    """
                            <script async
                            src="https://js.stripe.com/v3/buy-button.js">
                            </script>

                            <stripe-buy-button
                            buy-button-id="buy_btn_1Q06ZqAjJDLK6lMMryOcPNRD"
                            publishable-key="pk_live_51PkaASAjJDLK6lMMTnTkwj1DAni6tEEFyiYjuCNK9BB7VhLf2tsDA1C09RyXdublK1AM5dtBSViR15iZXxnDb55x00sebdGJpf"
                            >
                            </stripe-buy-button>
                            """,
                    height=400,
                )
            with cols[1]:
                components.html(
                    """
                            <script async
                            src="https://js.stripe.com/v3/buy-button.js">
                            </script>

                            <stripe-buy-button
                            buy-button-id="buy_btn_1Q06eDAjJDLK6lMM8ux1g9FK"
                            publishable-key="pk_live_51PkaASAjJDLK6lMMTnTkwj1DAni6tEEFyiYjuCNK9BB7VhLf2tsDA1C09RyXdublK1AM5dtBSViR15iZXxnDb55x00sebdGJpf"
                            >
                            </stripe-buy-button>
                            """,
                    height=400,
                )
        else:
            st.warning(
                "Read, understand and agree with the terms and conditions first! "
                "Then check the checkbox to see the subscription plans."
            )


def doc():
    st.markdown(
        """ Please refer to stripe documentation and policies for more information. """
    )
