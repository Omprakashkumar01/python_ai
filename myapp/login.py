import streamlit as st

def login_page():
    st.title("🔐 Login")

    if st.session_state.logged_in:
        st.success("Already logged in.")
        return

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "user" and password == "pass123":
            st.session_state.logged_in = True
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Invalid credentials.")
