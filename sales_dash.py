import pandas as pd
import streamlit as st
import plotly.express as px
from report import group_plot


def app():
    df = pd.read_excel(st.session_state['data'])
    #list_of_columns = df.columns.tolist()   
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