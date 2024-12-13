import streamlit as st
import streamlit.components.v1 as components
import streamlit_authenticator as stauth

# Setup user authentication
passwords = ["ggi2025"]

# Create a hashed passwords list
hashed_passwords = stauth.Hasher(passwords).generate()

# Create dummy names and usernames to fit required parameters
authenticator = stauth.Authenticate(["user"], ["username"], hashed_passwords, "some_cookie_name", "some_signature_key", cookie_expiry_days=1)

# Simplify login by not showing username field
name, authentication_status, _ = authenticator.login("Login", "main", username_placeholder="", password_placeholder="Enter Password", hide_usernames=True)

if authentication_status:
    st.subheader("Dashboard from Looker Studio")
    looker_studio_url = "https://lookerstudio.google.com/embed/reporting/7b165fb5-3c3e-4429-b162-a4dbe6438e28/page/xFVvD"
    components.iframe(looker_studio_url, width=800, height=600)

    if st.button("Sign Out"):
        authenticator.logout("Sign Out", "main")
        st.experimental_rerun()
elif authentication_status == False:
    st.error("Password is incorrect")
else:
    st.warning("Please enter your password")
