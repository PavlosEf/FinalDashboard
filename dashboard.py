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

# Locked global background styling
BACKGROUND_COLOR = "#3E4E56"  # Grey background for the entire app
st.markdown(f"""
    <style>
        /* Locked background styling */
        .stApp {{
            background-color: {BACKGROUND_COLOR} !important;
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
