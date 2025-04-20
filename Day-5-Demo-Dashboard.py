import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV sales data
try:
    data = pd.read_csv("Data/Sales_Data_AI_Incarnation.csv")
except FileNotFoundError:
    st.error("Error: Sales_Data_AI_Incarnation.csv not found.  Make sure the file is in the 'Data' folder.")
    st.stop()  # Stop execution if the file is missing

# Convert 'sales_date' to datetime
data['sales_date'] = pd.to_datetime(data['sales_date'])

st.title("🚀 Sales & Profit Dashboard: Unleashing Dynamic Analytics 🔍💡")

# Sidebar Navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a view", ["Overview", "Data Table", "Charts", "Filters"])

# Recalculate metrics based on filtered data
total_sales = data['sales_amount'].sum()
average_profit = data["profit"].mean()

# --- Filters ---
if option == "Filters":
    st.title("Data Filters")  # Page Title

    # Date Range Filter
    min_date = data['sales_date'].min()
    max_date = data['sales_date'].max()
    start_date, end_date = st.date_input(
        "Select Date Range:",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    # Product Category Filter
    product_categories = sorted(data['category'].unique())
    selected_categories = st.multiselect("Select Product Categories:", product_categories, default=product_categories)

    # Apply Filters
    filtered_data = data[
        (data['sales_date'] >= pd.to_datetime(start_date)) &
        (data['sales_date'] <= pd.to_datetime(end_date)) &
        (data['category'].isin(selected_categories))
    ]

    # Display Filtered Data Table
    st.header("Filtered Data Table")
    st.dataframe(filtered_data, use_container_width=True)

    # Recalculate metrics based on filtered data
    total_sales = filtered_data['sales_amount'].sum()
    average_profit = filtered_data["profit"].mean()

    # Display Filtered Charts
    st.header("Filtered Charts")
    fig_sales = px.bar(filtered_data, x="sales_date", y="sales_amount",
                       title="Daily Sales (Filtered)",
                       labels={"sales_date": "Date", "sales_amount": "Sales Amount"},
                       color="category",
                       template="plotly_white")
    st.plotly_chart(fig_sales, use_container_width=True)

    fig_profit = px.line(filtered_data.sort_values(by="sales_date"), x="sales_date", y="profit",
                        title="Daily Profit (Filtered)",
                        labels={"sales_date": "Date", "profit": "Profit"},
                        color="category",
                        template="plotly_white")
    st.plotly_chart(fig_profit, use_container_width=True)


# --- Overview ---
elif option == "Overview":
    st.title("Dashboard Overview")  # Page Title

    st.write("Here you can see the key metrics and interactive charts.")

    # Key Metrics with Borders, Box Shadow, and Title Inside
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); background-color: #fff;">
                <h3 style="text-align: center;"><b>Total Sales</b></h3>
                <p style="text-align: center; font-size: 24px;">${total_sales:,.2f}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); background-color: #fff;">
                <h3 style="text-align: center;"><b>Average Profit</b></h3>
                <p style="text-align: center; font-size: 24px;">${average_profit:,.2f}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Data Table ---
elif option == "Data Table":
    st.title("Full Data Table")  # Page Title
    st.dataframe(data, use_container_width=True)

# --- Charts ---
elif option == "Charts":
    st.title("Sales and Profit Charts")  # Page Title

    # Sales Chart
    fig_sales = px.bar(data, x="sales_date", y="sales_amount",
                       title="Daily Sales",
                       labels={"sales_date": "Date", "sales_amount": "Sales Amount"},
                       color="category",
                       template="plotly_white")
    st.plotly_chart(fig_sales, use_container_width=True)

    # Profit Chart
    fig_profit = px.line(data.sort_values(by="sales_date"), x="sales_date", y="profit",
                        title="Daily Profit",
                        labels={"sales_date": "Date", "profit": "Profit"},
                        color="category",
                        template="plotly_white")
    st.plotly_chart(fig_profit, use_container_width=True)