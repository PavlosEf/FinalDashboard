import streamlit as st
from typing import List
from dataclasses import dataclass

def find_closest_pattern(odds: float, patterns: List[List[float]]) -> List[float]:
    closest_pattern = min(patterns, key=lambda p: min(abs(o - odds) for o in p))
    return closest_pattern

@dataclass
class OddsResult:
    kaizen_line: float
    kaizen_odds: float
    comp_at_kaizen_line: float
    difference_percentage: float
    status: str

class DifferentLinesCalculator:
    def __init__(self):
        self.patterns: List[List[float]] = [
            [1.39, 1.43, 1.5, 1.54, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.65, 2.75],
            [1.4, 1.43, 1.5, 1.55, 1.62, 1.66, 1.74, 1.8, 1.95, 2.05, 2.15, 2.25, 2.35, 2.5, 2.6, 2.7],
            [1.38, 1.43, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.65, 2.85],
            [1.36, 1.41, 1.47, 1.52, 1.57, 1.64, 1.71, 1.76, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.55, 2.7, 2.85]
        ]

    def _find_nearest_in_pattern(self, value: float, pattern: List[float]) -> float:
        return min(pattern, key=lambda x: abs(x - value))

    def _step_odds(self, odds: float, step_up: bool, pattern: List[float]) -> float:
        if odds not in pattern:
            odds = self._find_nearest_in_pattern(odds, pattern)
        index = pattern.index(odds)
        if step_up and index < len(pattern) - 1:
            return pattern[index + 1]
        elif not step_up and index > 0:
            return pattern[index - 1]
        return odds

    def calculate_competition_odds(self, kaizen_line: float, kaizen_odds: float,
                                   comp_line: float, comp_odds: float, direction: str) -> float:
        line_diff = int(kaizen_line - comp_line)
        step_up = line_diff > 0 if direction == "over" else line_diff < 0
        closest_pattern = find_closest_pattern(comp_odds, self.patterns)
        current_odds = comp_odds
        for _ in range(abs(line_diff)):
            current_odds = self._step_odds(current_odds, step_up, closest_pattern)
        return current_odds

    def calculate_difference(self, kaizen_odds: float, comp_odds: float) -> float:
        return ((1 / kaizen_odds) - (1 / comp_odds)) * 100

    def get_status(self, difference: float) -> str:
        if difference > -2:
            return "OK"
        elif -3 <= difference <= -2:
            return "Off 2"
        else:
            return "Off 1"

    def calculate(self, kaizen_line: float, kaizen_odds: float,
                   comp_line: float, comp_odds: float, direction: str) -> OddsResult:
        comp_at_kaizen = self.calculate_competition_odds(
            kaizen_line, kaizen_odds, comp_line, comp_odds, direction)
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

    calculator = DifferentLinesCalculator()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Kaizen Data")
        kaizen_line = st.number_input("Kaizen Line", value=0.0, step=0.5)
        kaizen_odds = st.number_input("Kaizen Odds", value=1.0, min_value=1.0, step=0.01)

    with col2:
        st.subheader("Competition Data")
        comp_line = st.number_input("Competition Line", value=0.0, step=0.5)
        comp_odds = st.number_input("Competition Odds", value=1.0, min_value=1.0, step=0.01)

    direction = st.radio("Select Adjustment Direction", ("over", "under"))

    if st.button("Calculate", type="primary"):
        try:
            result = calculator.calculate(
                kaizen_line=kaizen_line,
                kaizen_odds=kaizen_odds,
                comp_line=comp_line,
                comp_odds=comp_odds,
                direction=direction
            )

            # Stylish Results Box
            st.markdown(
                """
                <style>
                    .result-box {
                        background-color: #e9f2f7;
                        border: 1px solid #DEE2E6;
                        border-radius: 8px;
                        padding: 20px;
                        margin-top: 20px;
                        color: #000000;
                        font-family: Arial, sans-serif;
                    }
                    .result-box h4 {
                        margin-bottom: 15px;
                        color: #000000;
                        font-size: 24px;
                        text-align: center;
                        font-weight: bold;
                        text-decoration: underline;
                    }
                    .result-box ul {
                        list-style-type: none;
                        padding: 0;
                        margin: 0;
                    }
                    .result-box ul li {
                        margin-bottom: 10px;
                        font-size: 18px;
                    }
                    .result-box ul li span {
                        font-weight: bold;
                        color: inherit !important;
                    }
                    .status-ok {
                        color: green;
                        font-weight: bold;
                    }
                    .status-off2 {
                        color: orange;
                        font-weight: bold;
                    }
                    .status-off1 {
                        color: red;
                        font-weight: bold;
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="result-box">
                    <h4>Calculation Results</h4>
                    <ul>
                        <li>Our Line: <span>{result.kaizen_line}</span></li>
                        <li>Our Odds: <span>{result.kaizen_odds}</span></li>
                        <li>Competition at Our Line: <span>{result.comp_at_kaizen_line:.3f}</span></li>
                        <li>Difference: <span>{result.difference_percentage:.2f}%</span></li>
                        <li>Status: 
                            <span class="{'status-ok' if result.status == 'OK' else 'status-off2' if result.status == 'Off 2' else 'status-off1'}">
                                {result.status}
                            </span>
                        </li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.caption("Disclaimer: This is an approximated calculator. Real odds may have a small difference.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    run()
