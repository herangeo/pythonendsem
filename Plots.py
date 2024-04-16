
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state='expanded')


st.sidebar.header('Dashboard')


st.sidebar.subheader('Bar chart parameter')
bar_data_options = ['Positive Feedback Count', 'Rating']
bar_value = st.sidebar.selectbox('Select data', bar_data_options)


data = pd.read_csv("WomensClothingE-CommerceReviews.csv")


st.markdown('### Metrics')
col1, col2 = st.columns(2)
col1.metric("Average Age", data['Age'].mean(), "years")
col2.metric("Average Positive Feedback Count", data['Positive Feedback Count'].mean(), "")


st.markdown('### 3D Scatter plot: Age vs Rating vs Positive Feedback Count')
scatter_3d_fig = px.scatter_3d(data, x='Age', y='Rating', z='Positive Feedback Count', color='Department Name',
                                title='Age vs Rating vs Positive Feedback Count', hover_data=data.columns)
st.plotly_chart(scatter_3d_fig, use_container_width=True)


st.markdown('### Bar chart')
bar_chart_fig = px.bar(data, x='Department Name', y=bar_value, color='Department Name',
                        title='Department-wise ' + bar_value)
st.plotly_chart(bar_chart_fig, use_container_width=True)



st.markdown('### 2D Scatter plot: Age vs Positive Feedback Count')
scatter_2d_fig = px.scatter(data, x='Age', y='Positive Feedback Count', color='Rating',
                            title='Age vs Positive Feedback Count', hover_data=data.columns)
st.plotly_chart(scatter_2d_fig, use_container_width=True)





