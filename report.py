import pandas as pd
import streamlit as st
import plotly.express as px

def group_plot(df, target, time):
    """
    Generate a grouped plot based on the given DataFrame, target column, and time period.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    target (str): The column name of the target variable to be plotted.
    time (str): The time period for grouping the data. Possible values are 'Day', 'Week', 'Month', and 'Year'.

    Returns:
    plotly.graph_objects.Figure: The generated plotly line plot.

    """
    df['Date'] = pd.to_datetime(df['Date'])
    if target == 'Amount before tax':
        df['Amount before tax'] = abs(df['Amount before tax'])
    if target == 'Item number':
        df['Item number'] = 1

    if time == 'Date':
        daily_df = df.groupby(by='Date')[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target)
    if time == 'Week':
    # Group by week
        daily_df = df.resample('W', on='Date')[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target)
    if time == 'Weekday':
    # Group by weekday
        daily_df = df.groupby(by='Weekday')[target].sum().reset_index()
        fig = px.line(daily_df, x="Weekday", y=target)
    if time == 'Month':
    # Group by month
        daily_df = df.groupby(pd.Grouper(key='Date', freq='M'))[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target)
    if time == 'Year':
    # Group by year
        daily_df = df.groupby(pd.Grouper(key='Date', freq='Y'))[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target)
    if time == 'Datetime':
        daily_df = df.groupby(pd.Grouper(key='Date', freq='h'))[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target)
    return fig


def employee_plot(df, target, time):
    """
    Generate a grouped plot based on the given DataFrame, target column, and time period.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    target (str): The column name of the target variable to be plotted.
    time (str): The time period for grouping the data. Possible values are 'Day', 'Week', 'Month', and 'Year'.

    Returns:
    plotly.graph_objects.Figure: The generated plotly line plot.

    """
    df['Date'] = pd.to_datetime(df['Date'])

    if time == 'Date':
        daily_df = df.groupby(by=['Date','Operator ID'])[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target, color='Operator ID')
    # if time == 'Week':
    # # Group by week
    #     daily_df = df.resample('W', on='Date')[target].sum().reset_index()
    #     fig = px.line(daily_df, x="Date", y=target, color='Operator ID')
    if time == 'Weekday':
    # Group by weekday
        daily_df = df.groupby(by=['Weekday','Operator ID'])[target].sum().reset_index()
        fig = px.line(daily_df, x="Weekday", y=target, color='Operator ID')
    if time == 'Month':
    # Group by month
        daily_df = df.groupby([pd.Grouper(key='Date', freq='ME'),'Operator ID'])[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target, color='Operator ID')
    if time == 'Year':
    # Group by year
        daily_df = df.groupby([pd.Grouper(key='Date', freq='Y'),'Operator ID'])[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target, color='Operator ID')
    if time == 'Datetime':
        daily_df = df.groupby([pd.Grouper(key='Date', freq='h',,'Operator ID'))[target].sum().reset_index()
        fig = px.line(daily_df, x="Date", y=target, color='Operator ID')
    return fig