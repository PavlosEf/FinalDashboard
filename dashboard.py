import streamlit as st
import calculators.OffPricesCalculator as OffPricesCalculator
import calculators.SurebetCalculator as SurebetCalculator
import calculators.TopPriceBetfairCalculator as TopPriceBetfairCalculator
import calculators.MarginsRemoval as MarginsRemoval
import calculators.AlternativeLinesConverter as AlternativeLinesConverter
import calculators.GeneralTab1 as GeneralTab1
import calculators.GeneralTab2 as GeneralTab2

# Set page configuration
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Display settings (customizable)
BACKGROUND_COLOR = "#3E4E56"  # Main background color
TEXT_COLOR = "#FFFFFF"       # Text color
SIDEBAR_BACKGROUND = "#2B3A42"  # Sidebar background color
SIDEBAR_TEXT_COLOR = "#FFFFFF"  # Sidebar text color
BOX_COLOR = "#3E4E56"        # Result box background color
HIGHLIGHT_COLOR = "#00FF00"  # Highlight color for active components

# Apply CSS for custom theme
st.markdown(f"""
    <style>
        /* Sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: {SIDEBAR_BACKGROUND}; /* Sidebar background */
            color: {SIDEBAR_TEXT_COLOR}; /* Sidebar text color */
        }}
        section[data-testid="stSidebar"] h1, h2, h3, h4, h5, h6 {{
            color: {SIDEBAR_TEXT_COLOR}; /* Ensure all headers in the sidebar are white */
        }}
        section[data-testid="stSidebar"] label {{
            color: {SIDEBAR_TEXT_COLOR}; /* Sidebar labels */
        }}
        section[data-testid="stSidebar"] {{
            padding: 20px;
        }}
        
        /* Main content styling */
        .stApp {{
            background-color: {BACKGROUND_COLOR}; /* Main background color */
            color: {TEXT_COLOR}; /* Main text color */
        }}

        /* Result box styling */
        .result-box {{
            background-color: {BOX_COLOR}; /* Box background */
            border-radius: 8px;
            padding: 15px;
            margin: 10px;
            border: 1px solid #DEE2E6;
            color: {TEXT_COLOR};
        }}
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("Tools Menu")
    selected_tool = st.radio(
        "Select a Tool:",
        [
            "Off Prices Calculator",
            "Surebet Calculator",
            "Top Price / Betfair Calculator",
            "Margins Removal",
            "Alternative Lines Converter",
            "General Tab 1",
            "General Tab 2"
        ]
    )

# Display content based on selected tool
if selected_tool == "Off Prices Calculator":
    st.title("Off Prices Calculator")
    OffPricesCalculator.run()  # Calls the `run` function from OffPricesCalculator.py

elif selected_tool == "Surebet Calculator":
    st.title("Surebet Calculator")
    SurebetCalculator.run()  # Calls the `run` function from SurebetCalculator.py

elif selected_tool == "Top Price / Betfair Calculator":
    st.title("Top Price / Betfair Calculator")
    TopPriceBetfairCalculator.run()  # Calls the `run` function from TopPriceBetfairCalculator.py

elif selected_tool == "Margins Removal":
    st.title("Margins Removal")
    MarginsRemoval.run()  # Calls the `run` function from MarginsRemoval.py

elif selected_tool == "Alternative Lines Converter":
    st.title("Alternative Lines Converter")
    AlternativeLinesConverter.run()  # Calls the `run` function from AlternativeLinesConverter.py

elif selected_tool == "General Tab 1":
    st.title("General Tab 1")
    GeneralTab1.run()  # Calls the `run` function from GeneralTab1.py

elif selected_tool == "General Tab 2":
    st.title("General Tab 2")
    GeneralTab2.run()  # Calls the `run` function from GeneralTab2.py
