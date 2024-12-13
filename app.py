import streamlit as st
import streamlit.components.v1 as components
from auth import check_password

if check_password():
    st.subheader("Dashboard from Looker Studio")
    looker_studio_url = "https://lookerstudio.google.com/embed/reporting/7b165fb5-3c3e-4429-b162-a4dbe6438e28/page/xFVvD"
    components.iframe(looker_studio_url, width=800, height=600)
