import streamlit as st
from streamlit_option_menu import option_menu
import home, login, sales_dash, employ_dash, forecast, profile_page, contact

hide_st_style = """
                <style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                </style>
                """


st.set_page_config(
    page_title="Datainsider Profit Mangemesnt Tool",
    page_icon="📊",
)

st.markdown(hide_st_style, unsafe_allow_html=True)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            selected_option = option_menu(
                menu_title='Operation Monitor',
                options=['Home', 'Login', 'Sales_Monitor', 'Employee_Monitor', 'Forecast','Profile', 'Contact Us'],
                icons=['house-door-fill','box-arrow-in-right','graph-up','people', 'magic','person-fill', 'wechat'],
                menu_icon='robot',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": " #6FC276"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if selected_option == "Home":
            home.app()
        elif selected_option == 'Login':
            login.app()
        elif 'useremail' not in st.session_state or st.session_state['useremail'] == '':
            st.warning('Please log in to access other sections')
        elif selected_option == 'Sales_Monitor':
            if 'useremail' not in st.session_state or st.session_state['useremail'] == '':
                st.warning('Please log in to access other sections')
            elif 'data' not in st.session_state:
                st.warning('Please upload a file to access this section')
            else:
                sales_dash.app()
        elif selected_option == "Employee_Monitor":
            if 'useremail' not in st.session_state or st.session_state['useremail'] == '':
                st.warning('Please log in to access other sections')
            elif 'data' not in st.session_state:
                st.warning('Please upload a file to access this section')
            else:
                employ_dash.app()
        elif selected_option == "Forecast":
            if 'useremail' not in st.session_state or st.session_state['useremail'] == '':
                st.warning('Please log in to access other sections')
            elif 'data' not in st.session_state:
                st.warning('Please upload a file to access this section')
            else:
                forecast.app()
        elif selected_option == 'Profile':
            if 'useremail' not in st.session_state or st.session_state['useremail'] == '':
                st.warning('Please log in to access other sections')
            else:
                profile_page.app()
        elif selected_option == 'Contact Us':
            contact.app()


if __name__ == "__main__":
    app = MultiApp()
    app.run()