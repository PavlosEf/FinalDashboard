
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

# Locked global styles (for sidebar and main background, and text color)
BACKGROUND_COLOR = "#3E4E56"  # Grey background for the main app
SIDEBAR_BACKGROUND = "#2B3A42"  # Darker grey for the sidebar
TEXT_COLOR = "#FFFFFF"  # White text for all elements

# Apply locked global CSS
st.markdown(f"""
    <style>
        /* Sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: {SIDEBAR_BACKGROUND} !important;
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] h1, h2, h3, h4, h5, h6 {{
            color: {TEXT_COLOR} !important; /* Ensure sidebar headings are white */
        }}
        section[data-testid="stSidebar"] label {{
            color: {TEXT_COLOR} !important; /* Ensure sidebar labels are white */
        }}
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {{
            background-color: transparent !important;
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"]:hover {{
            background-color: #1F2A32 !important; /* Darker background on hover */
        }}
        section[data-testid="stSidebar"] {{
            padding: 20px;
        }}

        /* Main content styling */
        .stApp {{
            background-color: {BACKGROUND_COLOR} !important;
        }}

        /* Input titles and labels */
        label {{
            color: {TEXT_COLOR} !important; /* Ensure input titles are white */
            font-weight: bold !important; /* Optional: Make titles bold */
        }}

        /* Input field styling */
        input[type="text"], input[type="number"], textarea {{
            background-color: #3E4E56 !important;
            color: {TEXT_COLOR} !important;
            caret-color: {TEXT_COLOR} !important;
            border: 1px solid #DEE2E6 !important;
            border-radius: 5px !important;
            padding: 8px !important;
        }}

        /* Styling for + and - buttons */
        input[type="number"]::-webkit-inner-spin-button, 
        input[type="number"]::-webkit-outer-spin-button {{
            background-color: #FF0000 !important;
            color: #FFFFFF !important;
            border: none !important;
        }}
        input[type="number"]::-webkit-inner-spin-button:hover, 
        input[type="number"]::-webkit-outer-spin-button:hover {{
            background-color: #CC0000 !important;
        }}

        /* Streamlit button styling */
        button[kind="primary"] {{
            background-color: #FF0000 !important; /* Red background */
            color: #FFFFFF !important; /* White text */
            border: none !important;
            border-radius: 5px !important;
            font-weight: bold !important;
            font-size: 16px !important;
            padding: 10px 20px !important;
        }}
        button[kind="primary"]:hover {{
            background-color: #CC0000 !important; /* Darker red on hover */
        }}

        /* Fix for sidebar radio button text */
        [data-testid="stSidebar"] .stRadio {{
            color: {TEXT_COLOR} !important; /* White text for sidebar radio buttons */
        }}
        [data-testid="stSidebar"] .stRadio:hover {{
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
