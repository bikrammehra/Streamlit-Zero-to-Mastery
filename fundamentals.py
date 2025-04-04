import streamlit as st
import pandas as pd


st.title("Welcome to my Streamlit App!")

st.header("Sales Overview")

st.subheader("Monthly Breakdown")

st.text("This is a plain text, useful for instructions or code samples")

st.markdown("**Bold Text** or _Italic Text_ can be easily formatted")

var = 12345

st.write(f"This is dynamic text output, You can even show variables :{var}")


data = pd.DataFrame({"Product":['Product A', 'Product B', 'Product C'],
                     "Sales":[100, 200, 300],
                     "Profit":[30, 50, 70]})

st.dataframe(data)


st.table(data)


st.button("Click Me!")

if st.checkbox("Show Details"):
    st.write("Here are the additional details...")

fruit = st.selectbox("Choose a fruit", ["Apple", "Banana", "Cherry"])
st.write(f"You have selected: {fruit}")

age = st.slider("select your age", min_value=0, max_value=100, value=25, step=5)


name = st.text_input("what is your name?")
if name:
    st.write(f"Hello {name}, welcome to AI Incarnation!")

quantity = st.number_input("enter the quantity", min_value=0, max_value=100, value=30, step=20)
if quantity:
    st.write(f"You have selected Quantity: {quantity}")

feedback = st.text_area("Your feedback is important to us. Leave your comments here:")
if feedback:
    st.write(f"Feedback received: {feedback}")

import datetime

date_selected = st.date_input("Pick a date", datetime.date.today())
if date_selected:
    st.write(f"You selected: {date_selected}")

uploaded_file = st.file_uploader("Upload any file")

if uploaded_file:
    st.write(f"Uploaded file is : {uploaded_file.name}")


message = st.chat_input("Send a message")
if message:
    st.write(f"You said: {message}")


st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page",['Home', 'About Us', 'Contact Us'])
if page:
    st.sidebar.write(f"You have slected: {page}")



col1, col2 = st.columns(2)

with col1:
    st.header("Left Panel")
    st.write("This might show a chart or key metrics")
with col2:
    st.header("Right Panel")
    st.write("This column can show controls or additional data")

with st.expander("See more details"):
    st.write("Here are some additional details that were hidden before.")
    st.write("You can add your content here, like charts, tables etc.")


with st.form(key="contact_form"):
    st.write("Contact Us")
    user_name = st.text_input("Name")
    user_email = st.text_input("Email")
    message = st.text_area("your message here...")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.write(f"Thank you {user_name}, we will get back to you at {user_email} soon!")
        st.write(f"Your message: {message}")