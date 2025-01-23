import streamlit as st
from typing import List
from dataclasses import dataclass

def find_closest_pattern(odds: float, patterns: List[List[float]]) -> List[float]:
    """ Finds the closest pattern of odds to match the input odds based on proximity. """
    closest_pattern = min(patterns, key=lambda p: min(abs(o - odds) for o in p))
    return closest_pattern

@dataclass
class OddsResult:
    """ Stores the calculation results for odds comparison across different lines. """
    kaizen_line: float
    kaizen_odds: float
    comp_at_kaizen_line: float
    difference_percentage: float
    status: str

class DifferentLinesCalculator:
    """ Calculator for analyzing odds differences between kaizen and competition using pattern matching. """

    def __init__(self):
        self.patterns = [
            [1.39, 1.43, 1.5, 1.54, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.65, 2.75],
            [1.4, 1.43, 1.5, 1.55, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.6, 2.7],
            [1.38, 1.43, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.65, 2.85],
            [1.36, 1.41, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.7, 2.85]
        ]

    def calculate(self, kaizen_line: float, kaizen_odds: float, comp_line: float, comp_odds: float, direction: str) -> OddsResult:
        """ Perform the complete calculation and return a result object. """
        comp_at_kaizen = self.calculate_competition_odds(kaizen_line, kaizen_odds, comp_line, comp_odds, direction)
        difference = self.calculate_difference(kaizen_odds, comp_at_kaizen)
        status = self.get_status(difference)
        return OddsResult(kaizen_line=kaizen_line, kaizen_odds=kaizen_odds, comp_at_kaizen_line=comp_at_kaizen, difference_percentage=difference, status=status)

    # Include other methods as defined previously...

# Streamlit interface
st.set_page_config(page_title="Different Lines Calculator", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #fafafa; 
    }
    .header {
        color: #FF4B4B;
        text-align: center;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin: 10px;
    }
    .status-ok {
        color: green;
    }
    .status-off2 {
        color: orange;
    }
    .status-off1 {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def run():
    st.title("Different Lines Calculator", anchor="header")

    calculator = DifferentLinesCalculator()

    # Create input fields in columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Kaizen Data")
        kaizen_line = st.number_input("Kaizen Line", value=0.0, step=0.5)
        kaizen_odds = st.number_input("Kaizen Odds", value=1.0, min_value=1.0, step=0.01)

    with col2:
        st.subheader("Competition Data")
        comp_line = st.number_input("Competition Line", value=0.0, step=0.5)
        comp_odds = st.number_input("Competition Odds", value=1.0, min_value=1.0, step=0.01)

    # Add direction selector
    direction = st.radio("Select Adjustment Direction", ("over", "under"))

    # Add calculate button
    if st.button("Calculate"):
        try:
            result = calculator.calculate(kaizen_line, kaizen_odds, comp_line, comp_odds, direction)

            # Display results
            st.markdown("<hr>", unsafe_allow_html=True)
            st.subheader("Results")

            results_box = f"""
            <div class='result-box'>
                <h3>Our Line: {result.kaizen_line}</h3>
                <h3>Our Odds: {result.kaizen_odds}</h3>
                <h3>Competition at Our Line: {result.comp_at_kaizen_line:.3f}</h3>
                <h3>Difference: {result.difference_percentage:.2f}%</h3>
                <h3 class="{('status-' + result.status).lower()}">Status: {result.status}</h3>
            </div>
            """
            st.markdown(results_box, unsafe_allow_html=True)
            st.caption("Disclaimer: This is an approximated calculator. Real odds may differ.")

        except ValueError as e:
            st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    run()
