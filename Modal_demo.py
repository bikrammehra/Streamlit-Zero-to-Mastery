import streamlit as st
import pandas as pd

#Initialize the session state dataframe
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Name', 'Age'])

#Track whether to show the dialog
if 'show_form' not in st.session_state:
    st.session_state.show_form = False

#Segmented control + button
if st.button("+ Add New Entry"):
    st.session_state.show_form = True

@st.dialog("Add New Entry")
def show_add_entry():
    with st.form("entry_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            new_row = pd.DataFrame([[name, age]], columns=['Name', 'Age'])
            st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
            st.session_state.show_form = False
            st.success("Entry added!")
            st.rerun()

if st.session_state.show_form:
    show_add_entry()

#display the updated dataframe
st.dataframe(st.session_state.df)
