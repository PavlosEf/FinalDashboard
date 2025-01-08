import streamlit as st
from typing import Dict, Optional
from dataclasses import dataclass

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
    when they have different lines.
    """
    
    def __init__(self):
        # Standard odds increment ladder
        self.INCREMENTS: Dict[float, float] = {
            1.38: 1.40, 1.40: 1.43, 1.43: 1.45, 1.45: 1.47, 1.47: 1.50,
            1.50: 1.52, 1.52: 1.55, 1.55: 1.57, 1.57: 1.62, 1.62: 1.66,
            1.66: 1.71, 1.71: 1.76, 1.76: 1.90, 1.90: 2.00, 2.00: 2.10,
            2.10: 2.20, 2.20: 2.30, 2.30: 2.40, 2.40: 2.50, 2.50: 2.60,
            2.60: 2.70, 2.70: 2.85
        }
        self.REVERSE_INCREMENTS = {v: k for k, v in self.INCREMENTS.items()}

    def _validate_input(self, value: float, name: str) -> None:
        """Validates input values for the calculator."""
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        if name.endswith('odds') and value < 1:
            raise ValueError(f"{name} must be greater than or equal to 1")

    def _find_nearest_odds(self, odds: float, lookup_dict: Dict[float, float]) -> Optional[float]:
        """Finds the nearest valid odds value in the lookup dictionary."""
        if odds in lookup_dict:
            return odds
        
        keys = sorted(lookup_dict.keys())
        for i in range(len(keys) - 1):
            if keys[i] <= odds <= keys[i + 1]:
                return keys[i] if abs(odds - keys[i]) < abs(odds - keys[i + 1]) else keys[i + 1]
        return None

    def _step_odds(self, odds: float, step_up: bool = True) -> float:
        """Steps odds up or down according to the increment ladder."""
        if step_up:
            nearest = self._find_nearest_odds(odds, self.INCREMENTS)
            return self.INCREMENTS.get(nearest, odds + 0.05)
        else:
            nearest = self._find_nearest_odds(odds, self.REVERSE_INCREMENTS)
            return self.REVERSE_INCREMENTS.get(nearest, odds - 0.05)

    def calculate_competition_odds(self, kaizen_line: float, kaizen_odds: float,
                                comp_line: float, comp_odds: float) -> float:
        """Calculates the competition's odds adjusted to the Kaizen line."""
        # Validate all inputs
        for name, value in [
            ("Kaizen line", kaizen_line),
            ("Kaizen odds", kaizen_odds),
            ("Competition line", comp_line),
            ("Competition odds", comp_odds)
        ]:
            self._validate_input(value, name)

        line_diff = int(kaizen_line - comp_line)
        current_odds = comp_odds

        # Adjust odds based on line difference
        for _ in range(abs(line_diff)):
            current_odds = self._step_odds(current_odds, line_diff > 0)
            
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
