import streamlit as st
from typing import List, Dict
from dataclasses import dataclass

def find_closest_pattern(odds: float, patterns: List[List[float]]) -> List[float]:
    """
    Finds the closest pattern of odds to match the input odds based on proximity.
    """
    closest_pattern = min(patterns, key=lambda p: min(abs(o - odds) for o in p))
    return closest_pattern

@dataclass
class OddsResult:
    """
    Stores the calculation results for odds comparison across different lines.
    """
    kaizen_line: float
    kaizen_odds: float
    comp_at_kaizen_line: float
    difference_percentage: float
    status: str

class DifferentLinesCalculator:
    """
    Calculator for analyzing odds differences between Kaizen and competition
    when they have different lines using pattern matching.
    """

    def __init__(self):
        # Odds progression patterns
        self.patterns: List[List[float]] = [
            [1.39, 1.43, 1.5, 1.54, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.65, 2.75],  # Example 1
            [1.4, 1.43, 1.5, 1.55, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.6, 2.7],  # Example 2
            [1.38, 1.43, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.65, 2.85],  # Example 3
            [1.36, 1.41, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.7, 2.85]  # Example 4
        ]

    def _find_nearest_in_pattern(self, value: float, pattern: List[float]) -> float:
        """Find the nearest value in the selected pattern."""
        return min(pattern, key=lambda x: abs(x - value))

    def _step_odds(self, odds: float, step_up: bool, pattern: List[float]) -> float:
        """Steps odds up or down using the selected pattern."""
        if odds not in pattern:
            odds = self._find_nearest_in_pattern(odds, pattern)

        index = pattern.index(odds)

        if step_up and index < len(pattern) - 1:
            return pattern[index + 1]
        elif not step_up and index > 0:
            return pattern[index - 1]
        return odds  # Return the same odds if at boundary

    def calculate_competition_odds(self, kaizen_line: float, kaizen_odds: float,
                                   comp_line: float, comp_odds: float) -> float:
        """Calculates the competition's odds adjusted to the Kaizen line."""
        line_diff = int(kaizen_line - comp_line)
        step_up = line_diff > 0

        # Find the closest pattern to comp_odds
        closest_pattern = find_closest_pattern(comp_odds, self.patterns)

        current_odds = comp_odds

        # Adjust odds based on line difference using the closest pattern
        for _ in range(abs(line_diff)):
            current_odds = self._step_odds(current_odds, step_up, closest_pattern)

        return current_odds

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

    def calculate(self, kaizen_line: float, kaizen_odds: float,
                   comp_line: float, comp_odds: float) -> OddsResult:
        """Performs the complete calculation and returns a result object."""
        comp_at_kaizen = self.calculate_competition_odds(
            kaizen_line, kaizen_odds, comp_line, comp_odds)
        difference = self.calculate_difference(kaizen_odds, comp_at_kaizen)
        status = self.get_status(difference)

        return OddsResult(
            kaizen_line=kaizen_line,
            kaizen_odds=kaizen_odds,
            comp_at_kaizen_line=comp_at_kaizen,
            difference_percentage=difference,
            status=status
        )

# Streamlit interface
st.set_page_config(page_title="Different Lines Calculator", layout="wide")

def main():
    st.title("Different Lines Calculator")

    # Initialize calculator
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

    # Add calculate button
    if st.button("Calculate", type="primary"):
        try:
            # Calculate results
            result = calculator.calculate(
                kaizen_line=kaizen_line,
                kaizen_odds=kaizen_odds,
                comp_line=comp_line,
                comp_odds=comp_odds
            )

            # Display results in a nice format
            st.divider()
            st.subheader("Results")

            # Display main results
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Our Line", f"{result.kaizen_line}")
                st.metric("Our Odds", f"{result.kaizen_odds}")

            with col2:
                st.metric("Competition at Our Line", f"{result.comp_at_kaizen_line:.3f}")
                st.metric("Difference", f"{result.difference_percentage:.2f}%")

            # Display status with appropriate color
            status_colors = {
                "OK": "green",
                "Off 2": "orange",
                "Off 1": "red"
            }

            st.markdown(
                f"""
                <div style='padding: 10px; border-radius: 5px; background-color: {status_colors.get(result.status, "gray")}; color: white;'>
                    <h3 style='text-align: center; margin: 0;'>Status: {result.status}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Display disclaimer
            st.caption("Disclaimer: This is an approximated calculator. Real odds may have a small difference.")

        except ValueError as e:
            st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
