import streamlit as st
from calculators import surebet_calc, top_price_calc, margins_removal, alternative_lines_converter

# Set page configuration
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling the dark theme
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            background-color: #2B3A42;
            color: #FFFFFF;
        }
        section[data-testid="stSidebar"] * {
            color: #FFFFFF;
        }
        .stApp {
            background-color: #3E4E56;
            color: #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("Tools Menu")
    selected_tool = st.radio(
        "Select a Tool:",
        [
            "Surebet Calculator",
            "Top Price / Betfair Calculator",
            "Margins Removal",
            "Alternative Lines Converter",
        ]
    )

# Render the selected tool by calling the respective module
if selected_tool == "Surebet Calculator":
    surebet_calc.run()
elif selected_tool == "Top Price / Betfair Calculator":
    top_price_calc.run()
elif selected_tool == "Margins Removal":
    margins_removal.run()
elif selected_tool == "Alternative Lines Converter":
    alternative_lines_converter.run()
