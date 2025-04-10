import streamlit as st
import pandas as pd

#Create a simple Dataframe
df = pd.DataFrame([
    {"Command": "st.selectbox", "rating": 4, "is_widget":True},
    {"Command": "st.balloons", "rating": 5, "is_widget":False},
    {"Command": "st.time_input","rating":3, "is_widget":True}
])

#Render an editable DataFrame
edited_df = st.data_editor(df, hide_index=True, use_container_width=True)

#Display a message based on the user's edit
favourite_command = edited_df.loc[edited_df["rating"].idxmax()]['Command']
st.success(f"Your favourite command is {favourite_command}")