import streamlit as st
import pandas as pd

st.title("Advanced Handling of Inserts and Deletes in st.data_editor")


def process_changes():
    editor_state = st.session_state.get("dynamic_editor",{})

    edited = editor_state.get("edited_rows",{})

    added = editor_state.get("added_rows",[])

    deleted = editor_state.get("deleted_rows",[])


    # Display the captured change information on the app
    st.write("### Processed Changes:")
    st.write("Edited Rows:", edited)
    st.write("Added Rows:", added)
    st.write("Deleted Row Indices:", deleted)

# Create a sample DataFrame to be edited
df = pd.DataFrame([
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
])

# Render an editable DataFrame with dynamic row features
edited_df = st.data_editor(
    df,
    key="dynamic_editor",         # Unique key for session state tracking
    hide_index=True,              # Hide the default DataFrame index
    use_container_width=True,     # Stretch editor to the container width
    num_rows="dynamic",           # Allow adding or deleting rows dynamically
    on_change=process_changes     # Callback function when changes occur
)

#display the edited DataFrame
st.markdown("### Edited DataFrame:")
st.write(edited_df)

editor_state = st.session_state.get("dynamic_editor",{})
added_rows = editor_state.get("added_rows",[])
deleted_rows = editor_state.get("deleted_rows",[])

st.write("### Added Rows:")
st.write(added_rows)
st.write("### Deleted Rows:")
st.write(deleted_rows)