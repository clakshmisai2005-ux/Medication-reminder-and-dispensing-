import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="MedRemind IoT — ESP32 Smart Medication Dispenser",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default chrome (menu, footer, header padding) so the
# dashboard's own sidebar/topbar look native inside the page.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "dashboard.html"
html_content = html_path.read_text(encoding="utf-8")

# Render the full self-contained HTML/CSS/JS dashboard inside an iframe.
# height is generous so the dashboard's internal scroll areas behave well;
# scrolling=True lets the iframe itself scroll if content exceeds it.
components.html(html_content, height=1000, scrolling=True)
