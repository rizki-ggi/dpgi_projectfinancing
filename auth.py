import streamlit as st

# Function to check the password
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    with st.form("login_form"):
        st.text_input("Password", type="password", key="password")
        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            if st.session_state["password"] == "ggi2025":
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # Remove password from session state
            else:
                st.error("Incorrect password.")

    return st.session_state["password_correct"]

# Function to sign out
def sign_out():
    st.session_state["password_correct"] = False