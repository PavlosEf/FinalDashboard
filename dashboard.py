import streamlit as st
import calculators.OffPricesCalculator as OffPricesCalculator
import calculators.SurebetCalculator as SurebetCalculator
import calculators.TopPriceBetfairCalculator as TopPriceBetfairCalculator
import calculators.MarginsRemoval as MarginsRemoval
import calculators.AlternativeLinesConverter as AlternativeLinesConverter
import calculators.PercentageCalculations as PercentageCalculations
import calculators.CurrencyConverter as CurrencyConverter 
import calculators.GeneralTab2 as GeneralTab2
import calculators.TimeCalculator as TimeCalculator

# Set page configuration
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar styles
SIDEBAR_BACKGROUND = "#FFFFFF"  # Darker grey for the sidebar
TEXT_COLOR = "#0a0a0a"  # White text for all elements

# Apply locked global CSS for sidebar only
st.markdown(f"""
    <style>
        /* Locked sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: {SIDEBAR_BACKGROUND} !important;
            color: "#FFFFFF" !important;
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
            "Percentage (%) Calculations",
            "Currency Converter",
            "Current Time Calculator",
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

elif selected_tool == "Percentage (%) Calculations":
    PercentageCalculations.run()
    
elif selected_tool == "Currency Converter":  # New option
    CurrencyConverter.run()    

elif selected_tool == "Current Time Calculator":  # New option
    TimeCalculator.run()   
    
elif selected_tool == "General Tab 2":
    GeneralTab2.run() 
