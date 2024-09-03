import re
import streamlit as st
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

@st.dialog("Contact me")
def show_contact_form():
    with st.form("Contact form"):
        name = st.text_input("First name")
        email = st.text_input("Email Address")
        Message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
     if not WEBHOOK_URL:
        st.error("Email service is not setup. Please try again later.", icon="✉")
        st.stop()

    if not name:
        st.error(
            "Please provide your name.", icon="🤔"
        )
        st.stop()

    if not email:
        st.error(
            "Please provide your email.", icon="🤔"
        )
        st.stop()

    if not is_valid_email(email):
        st.error(
            "Please provide a valid email address.", icon="🤔"
        )
        st.stop()

    if not Message:
        st.error(
            "Please provide a message.", icon="🤔"
        )
        st.stop()

    data = {"email": email, "name": name, "Message": Message}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 200:
        st.success("Your message has been sent successfully! 🎉 ", icon="👍")
    else:
        st.error("There was an error sending your message")

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("C:/Users/ELCOT/PycharmProject/pythonProject/Web-Application/assets/Chitra.jpg", width=200)

with col2:
    st.title("Chitra Bala", anchor=False)
    st.write("I am a Business Analyst and a web developer, assisting enterprise driven web applications")
    if st.button("✉ Contact Me"):
        show_contact_form()

st.write("\n")
st.subheader("Experience and skills", anchor="False")
st.write(
    """
    Data Analyst\n
    Software developer\n
    Good with excel\n
    """
)

# ***skills***
st.write("\n")
st.subheader("Hard Skills", anchor="False")
st.write(
    """
    Programming Language python (scikit learn, tensor flow)\n
    Machine learning Algorithms\n
    Deep learning Algorithms\n
    """
)
