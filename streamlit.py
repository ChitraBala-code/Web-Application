import streamlit as st

st.set_page_config(page_title="Data manager", page_icon=":material/edit:", layout="wide",
                   initial_sidebar_state="auto",
                   )
# --- PAGE SETUP ---
about_page =st.Page(
    "https://github.com/ChitraBala-code/Web-Application/blob/main/deploy/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "https://github.com/ChitraBala-code/Web-Application/blob/main/deploy/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "https://github.com/ChitraBala-code/Web-Application/blob/main/deploy/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("C:/Users/Elcot/PycharmProject/pythonProject/Web-Application/assets/logo1.png")
st.sidebar.markdown("Made with 😊 by [Chitra](https://youtube.com/@codingisfun)")

pg.run()

