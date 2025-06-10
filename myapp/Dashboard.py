import streamlit as st

def dashboard_page():
    st.title("📋 Visited Places Dashboard")

    visited = st.session_state.get("visited_places", [])
    if not visited:
        st.info("No places visited yet.")
        return

    st.write("### ✅ Visited Places:")
    for place in visited:
        st.markdown(f"- {place}")

    st.write("### 📍 Total Places Visited: ", len(visited))
