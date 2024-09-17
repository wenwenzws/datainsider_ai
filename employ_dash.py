import pandas as pd
import streamlit as st
import plotly.express as px
from report import employee_plot


def app():
    df = pd.read_excel(st.session_state['data'])
    list_of_columns = df.columns.tolist()   
    df['Date'] = pd.to_datetime(df['Date'])

    # Add a column for the weekday name
    df['Weekday'] = df['Date'].dt.day_name()
    df['Sales dollars before tax'] = abs(df['Amount before tax'])
    df['Items_count'] = 1

    sales_columns = ['Sales dollars before tax', 'Items_count']
    target = st.selectbox('Select for daily sales per employee', sales_columns)
    time = st.selectbox('Select the frequency for daily sales', ['Month','Weekday', 'Date','Datetime'])

    fig = employee_plot(df, target, time)
    event = st.plotly_chart(fig)