import streamlit as st

# Function to check the password
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        with st.form("login_form"):
            st.text_input("Password", type="password", key="password")
            submit_button = st.form_submit_button(label="Submit")

            if submit_button:
                if st.session_state["password"] == "ggi2025":
                    st.session_state["password_correct"] = True
                    st.experimental_rerun()  # Rerun to update session state
                else:
                    st.error("Incorrect password.")

    return st.session_state["password_correct"]

# Function to sign out
def sign_out():
    st.session_state["password_correct"] = False

    return st.session_state["password_correct"]

# Function to sign out
def sign_out():
    st.session_state["password_correct"] = False
