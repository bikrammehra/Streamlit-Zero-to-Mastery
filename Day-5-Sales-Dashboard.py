import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv("Data/Sales_Data_AI_Incarnation.csv")

st.title("Dashboard App: Sales and Profit Analytics")

#Calaculate Metrics
total_sales = data['sales_amount'].sum()
average_profit = data['profit'].mean()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales}")
col2.metric("Average Profit", f"${average_profit:,.2f}")


data['sales_date'] = pd.to_datetime(data['sales_date'])
data.sort_values(by='sales_date', inplace=True)

#Bar Chart : Daily Sales
fig_sales = px.bar(data, x="sales_date", y="sales_amount", color="category")

#Line Chart : Profit over time
fig_profit = px.line(data, x="sales_date", y="profit", color="category")

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a view:", ["Overview", "Data Table", "Charts"])

if option == "Overview":
    st.write("Here you can see the key Metrics and Interactive Charts")
    st.plotly_chart(fig_sales, use_container_width=True)
    st.plotly_chart(fig_profit, use_container_width=True)
elif option == "Data Table":
    st.write("Data Table is as below")
    st.dataframe(data)
elif option == "Charts":
    st.write("Interactive Charts")
    st.plotly_chart(fig_sales, use_container_width=True)
    st.plotly_chart(fig_profit, use_container_width=True)