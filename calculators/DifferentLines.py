import streamlit as st
from typing import List
from dataclasses import dataclass

def find_closest_pattern(odds: float, patterns: List[List[float]]) -> List[float]:
    """Finds the closest pattern of odds to match the input odds based on proximity."""
    return min(patterns, key=lambda p: min(abs(o - odds) for o in p))

@dataclass
class OddsResult:
    """Stores the calculation results for odds comparison across different lines."""
    kaizen_line: float
    kaizen_odds: float
    comp_at_kaizen_line: float
    difference_percentage: float
    status: str

class DifferentLinesCalculator:
    """Calculator for analyzing odds differences between Kaizen and competition."""
    def __init__(self):
        self.patterns: List[List[float]] = [
            [1.39, 1.43, 1.5, 1.54, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.65, 2.75],
            [1.4, 1.43, 1.5, 1.55, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.6, 2.7],
            [1.38, 1.43, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.65, 2.85],
            [1.36, 1.41, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.7, 2.85]
        ]

    def calculate_competition_odds(self, kaizen_line: float, kaizen_odds: float, comp_line: float, comp_odds: float) -> float:
        """Calculates the competition's odds adjusted to the Kaizen line."""
        return comp_odds  # Placeholder logic (adjust as needed)

    def calculate_difference(self, kaizen_odds: float, comp_odds: float) -> float:
        """Calculates the percentage difference between Kaizen and competition odds."""
        return ((1 / kaizen_odds) - (1 / comp_odds)) * 100

    def get_status(self, difference: float) -> str:
        """Determines the status based on the calculated difference percentage."""
        if difference > -2:
            return "OK"
        elif -3 <= difference <= -2:
            return "Off 2"
        else:
            return "Off 1"

    def calculate(self, kaizen_line: float, kaizen_odds: float, comp_line: float, comp_odds: float) -> OddsResult:
        """Performs the complete calculation and returns a result object."""
        comp_at_kaizen = self.calculate_competition_odds(kaizen_line, kaizen_odds, comp_line, comp_odds)
        difference = self.calculate_difference(kaizen_odds, comp_at_kaizen)
        status = self.get_status(difference)

        return OddsResult(
            kaizen_line=kaizen_line,
            kaizen_odds=kaizen_odds,
            comp_at_kaizen_line=comp_at_kaizen,
            difference_percentage=difference,
            status=status
        )

# Streamlit Interface
st.set_page_config(page_title="Different Lines Calculator", layout="wide")

def run():
    st.title("Different Lines Calculator")

    # Styling Fixes
    st.markdown("""
        <style>
            /* Input Field Styling */
            input[type="number"] {
                width: 100% !important;
                max-width: 200px !important;
                background-color: #EAEAEA !important;
                color: #000000 !important;
                caret-color: #000000 !important;
                padding: 5px !important;
                border-radius: 5px;
                border: 1px solid #CCCCCC !important;
            }

            /* Result Box Styling */
            .result-box {
                background-color: #FFD700 !important;
                color: #000000 !important;
                padding: 12px;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
                border: 1px solid #000000;
                margin-top: 15px;
            }

            /* Status Box Styling */
            .status-box {
                font-size: 18px;
                padding: 12px;
                text-align: center;
                border-radius: 8px;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize Calculator
    calculator = DifferentLinesCalculator()

    # Input Fields
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Kaizen Data")
        kaizen_line = st.number_input("Kaizen Line", value=0.0, step=0.5)
        kaizen_odds = st.number_input("Kaizen Odds", value=1.0, min_value=1.0, step=0.01)

    with col2:
        st.subheader("Competition Data")
        comp_line = st.number_input("Competition Line", value=0.0, step=0.5)
        comp_odds = st.number_input("Competition Odds", value=1.0, min_value=1.0, step=0.01)

    if st.button("Calculate", type="primary"):
        try:
            result = calculator.calculate(kaizen_line, kaizen_odds, comp_line, comp_odds)

            st.subheader("Results")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Our Line:** {result.kaizen_line}")
                st.write(f"**Our Odds:** {result.kaizen_odds}")

            with col2:
                st.write(f"**Competition at Our Line:** {result.comp_at_kaizen_line:.3f}")
                st.write(f"**Difference:** {result.difference_percentage:.2f}%")

            # Status Box Color
            status_colors = {"OK": "#008000", "Off 2": "#FFA500", "Off 1": "#FF0000"}
            status_color = status_colors.get(result.status, "gray")

            # Display Status Box
            st.markdown(
                f"""
                <div class="status-box" style="background-color: {status_color};">
                    Status: {result.status}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Disclaimer
            st.caption("Disclaimer: This is an approximated calculator. Real odds may have small variations.")

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    run()
