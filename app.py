import streamlit as st
import streamlit.components.v1 as components
from auth import check_password, sign_out

# Check password
if not check_password():
    st.stop()

# Display the dashboard
st.subheader("Dashboard from Looker Studio")
looker_studio_url = "your_looker_embeded_URL"
components.iframe(looker_studio_url, width=800, height=600)

# Add Sign Out button below the dashboard
if st.button("Sign Out"):
    sign_out()
    st.experimental_rerun()
