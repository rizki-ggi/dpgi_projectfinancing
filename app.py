import streamlit as st
import streamlit.components.v1 as components
from auth import check_password

if check_password():
    st.subheader("Dashboard from Looker Studio")
    looker_studio_url = "your_looker_embeded_URL"
    components.iframe(looker_studio_url, width=800, height=600)
