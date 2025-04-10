import streamlit as st
import pandas as pd

def process_changes():
    #Access the change in dictionary from the session state using the widget key
    changes = st.session_state["data_editor_key"].get("edited_rows",{})
    st.write("Processed changes: ", changes)


#Create a Dataframe
df = pd.DataFrame([
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
])


#render this dataframe in the data editor and on_change callback
edited_df = st.data_editor(
    df,
    key="data_editor_key",
    hide_index=True,
    use_container_width=True,
    on_change=process_changes
)


st.markdown("### Edited DataFrame")
st.write(edited_df)