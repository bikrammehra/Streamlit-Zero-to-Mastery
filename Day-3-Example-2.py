import streamlit as st
import pandas as pd
import altair as alt

st.title("Climate Trends Dashboard")
st.write("Visualizing average temperature changes over time.")

#Sample data (You can replace this with real world data in your usecase)
data = {
    "Year": list(range(2000, 2025)),
    "Average_Temp": [14.5, 14.7, 14.8, 15.0, 15.2, 15.3, 15.5, 15.7, 15.9, 16.0,
              16.2, 16.4, 16.5, 16.7, 16.8, 17.0, 17.2, 17.3, 17.5, 17.7, 17.8, 18.0,
              18.2, 18.4, 18.5]
}

df = pd.DataFrame(data)

chart = alt.Chart(df).mark_line(point=True).encode(
    x="Year:O",
    y="Average_Temp:Q",
    tooltip=["Year", "Average_Temp"]
).properties(
    title="Average Temperature Over Years"
)

st.altair_chart(chart, use_container_width=True)