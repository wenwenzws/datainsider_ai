import pandas as pd
import streamlit as st
import plotly.express as px
from report import group_plot

st.title("Analyzer for Smart Operations")

email_address = st.sidebar.text_input('Email address')
questionarie = st.sidebar.text_area('Questions you would like to know from your business')
uploaded_file = st.sidebar.file_uploader('Upload a excel file', type='xlsx')


if uploaded_file is None:
    st.sidebar.write('Please upload a file')
    st.title('Please upload a file')
else:
    df = st.session_state['data']
    st.write(df)
    list_of_columns = df.columns.tolist()   
    df['Date'] = pd.to_datetime(df['Date'])

    # Add a column for the weekday name
    df['Weekday'] = df['Date'].dt.day_name()
    df['Sales dollars before tax'] = abs(df['Amount before tax'])
    df['Items_count'] = 1

    sales_columns = ['Sales dollars before tax', 'Items_count']
    target = st.selectbox('Select the column for daily sales', sales_columns)
    time = st.selectbox('Select the column for daily sales', ['Year', 'Month', 'Week','Weekday', 'Date','Datetime'])

    fig = group_plot(df, target, time)
    event = st.plotly_chart(fig)
