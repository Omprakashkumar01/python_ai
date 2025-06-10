import streamlit as st
from login import login_page
from Home import home_page
from Dashboard import dashboard_page

st.set_page_config(page_title="Jaipur Planner", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "visited_places" not in st.session_state:
    st.session_state.visited_places = []

# Sidebar
if st.session_state.logged_in:
    with st.sidebar:
        st.title("🧭 Navigation")
        if st.button("🛺 Route Planner"):
            st.session_state.page = "home"
        if st.button("📋 Dashboard"):
            st.session_state.page = "dashboard"
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()

# Routing
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "home":
    home_page()
elif st.session_state.page == "dashboard":
    dashboard_page()
