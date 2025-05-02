import streamlit as st
import pandas as pd

# Initialize session-state variables
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Name', 'Age'])

if 'show_add_dialog' not in st.session_state:
    st.session_state.show_add_dialog = False

if 'previous_action' not in st.session_state:
    st.session_state.previous_action = None

# Segmented control for Add/Delete
action = st.segmented_control(
    label="Action",
    options=["➕ Add", "🗑️ Delete"],
    key="action_control"
)

# Update show_add_dialog based on action change
current_action = action
if st.session_state.previous_action != current_action:
    st.session_state.show_add_dialog = (current_action == "➕ Add")
    st.session_state.previous_action = current_action

# Handle Add mode
if action == "➕ Add":
    @st.dialog("Add New Entry")
    def add_entry_dialog():
        with st.form("entry_form"):
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0, max_value=120, step=1)
            submitted = st.form_submit_button("Submit")
            if submitted:
                new_row = pd.DataFrame({'Name': [name], 'Age': [age]})
                st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
                st.session_state.show_add_dialog = False
                st.rerun()

    if st.session_state.show_add_dialog:
        add_entry_dialog()

# Handle Delete mode
elif action == "🗑️ Delete":
    st.markdown("### Select rows to delete:")
    df = st.session_state.df.copy()
    if df.empty:
        st.info("No entries to delete.")
    else:
        selected = []
        # Header row
        cols = st.columns([1, 3, 2])
        cols[1].write("Name")
        cols[2].write("Age")
        # Data rows with checkboxes
        for i, row in df.iterrows():
            c0, c1, c2 = st.columns([1, 3, 2])
            # Updated checkbox with accessible label
            if c0.checkbox("Select row", 
                          key=f"sel_{i}", 
                          label_visibility="collapsed"):
                selected.append(i)
            c1.write(row["Name"])
            c2.write(row["Age"])
        # Delete selected rows
        if st.button("🗑️ Delete Selected") and selected:
            st.session_state.df = df.drop(index=selected).reset_index(drop=True)
            st.rerun()

# Display current entries
st.markdown("### Current Entries")
st.dataframe(st.session_state.df)