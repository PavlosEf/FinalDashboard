import streamlit as st
import calculators.OffPricesCalculator as OffPricesCalculator
import calculators.SurebetCalculator as SurebetCalculator
import calculators.TopPriceBetfairCalculator as TopPriceBetfairCalculator
import calculators.MarginsRemoval as MarginsRemoval
import calculators.calculators/DifferentLines as AlternativeLinesConverter
import calculators.GeneralTab1 as GeneralTab1
import calculators.GeneralTab2 as GeneralTab2

# Set page configuration
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Locked global styles (for sidebar and main background, and text color)
BACKGROUND_COLOR = "#3E4E56"  # Grey background for the main app
SIDEBAR_BACKGROUND = "#2B3A42"  # Darker grey for the sidebar
TEXT_COLOR = "#FFFFFF"  # White text for all elements

# Apply locked global CSS
st.markdown(f"""
    <style>
        /* Locked sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: {SIDEBAR_BACKGROUND} !important;
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] h1, h2, h3, h4, h5, h6 {{
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] label {{
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] {{
            padding: 20px;
        }}
        
        /* Locked main content styling */
        .stApp {{
            background-color: {BACKGROUND_COLOR} !important;
            color: {TEXT_COLOR} !important;
        }}

    
        /* Make all text across the app white */
        .stApp * {{
            color: {TEXT_COLOR} !important;
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
    OffPricesCalculator.run()

elif selected_tool == "Surebet Calculator":
    SurebetCalculator.run()

elif selected_tool == "Top Price / Betfair Calculator":
    TopPriceBetfairCalculator.run()

elif selected_tool == "Margins Removal":
    MarginsRemoval.run()

elif selected_tool == "Alternative Lines Converter":
    AlternativeLinesConverter.run()

elif selected_tool == "General Tab 1":
    GeneralTab1.run()

elif selected_tool == "General Tab 2":
    GeneralTab2.run()
