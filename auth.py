import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == "ggi2025":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Remove the password from session state
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # Enter the password
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Incorrect password.")
        return False
    else:
        return True
