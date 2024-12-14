import streamlit as st

def run():
    # Global Styles
    BACKGROUND_COLOR = "#3E4E56"  # Grey background for the main app
    TEXT_COLOR = "#FFFFFF"  # White text for all elements

    st.markdown(
        f"""
        <style>
            /* Global background and text styling */
            .stApp {{
                background-color: {BACKGROUND_COLOR} !important;
                color: {TEXT_COLOR} !important;
            }}
            input[type="text"], input[type="number"] {{
                background-color: {BACKGROUND_COLOR} !important;
                color: {TEXT_COLOR} !important;
                caret-color: {TEXT_COLOR} !important;
                border: 1px solid #DEE2E6 !important;
                border-radius: 5px !important;
                padding: 8px !important;
                margin: 0px !important;
                width: 100px !important; /* Fixed width for input fields */
                text-align: center; /* Center-align the text */
            }}
            .result-box {{
                border: 2px solid #FFFFFF;
                padding: 5px;
                margin: 5px 10px;
                text-align: center;
                border-radius: 5px;
                width: 70px;
                display: inline-block;
                position: relative;
                top: 20px;
            }}
            .result-container {{
                display: flex;
                align-items: center;
                justify-content: flex-start;
                gap: 10px;
                margin-top: 10px;
            }}
            div[data-testid="stBlock"] {{
                gap: 0px !important; /* Remove extra gaps between Streamlit blocks */
            }}
            .css-18e3th9 {{
                padding: 0px !important; /* Remove padding around input fields */
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Surebet Calculator")
    st.markdown("Calculate stakes and profits for arbitrage betting scenarios dynamically.")

    # Helper Function for Parsing Inputs
    def parse_number(number_str):
        try:
            return float(number_str.replace(",", "."))
        except ValueError:
            return None

    # Function to calculate stakes and arbitrage
    def calculate_surebet(w1_odds, w2_odds, w1_stake=None, w2_stake=None, total_stake=None):
        if total_stake:
            w1_stake = total_stake / (1 + w1_odds / w2_odds)
            w2_stake = total_stake - w1_stake
        elif w1_stake:
            w2_stake = (w1_stake * w1_odds) / w2_odds
            total_stake = w1_stake + w2_stake
        elif w2_stake:
            w1_stake = (w2_stake * w2_odds) / w1_odds
            total_stake = w1_stake + w2_stake

        profit_w1 = (w1_odds * w1_stake) - total_stake
        profit_w2 = (w2_odds * w2_stake) - total_stake
        arbitrage_percentage = max(profit_w1, profit_w2) / total_stake * 100

        return {
            "W1 Stake": round(w1_stake, 2),
            "W2 Stake": round(w2_stake, 2),
            "Total Stake": round(total_stake, 2),
            "Profit W1": round(profit_w1, 2),
            "Profit W2": round(profit_w2, 2),
            "Arbitrage %": round(arbitrage_percentage, 2)
        }

    # Input Fields
    for i in range(1):  # Adjusted to match layout from OffPricesCalculator.py
        # Row 1: Odds Inputs
        col1, col2 = st.columns([2, 5])  # Adjusted column widths for better alignment
        with col1:
            w1_odds = st.text_input("Kaizen Odds 1:", "2.5", key=f"w1_odds_{i}")
            w1_odds = parse_number(w1_odds) or 0

        with col2:
            w2_odds = st.text_input("Competition Odds 1:", "2.0", key=f"w2_odds_{i}")
            w2_odds = parse_number(w2_odds) or 0

        # Row 2: Stake Inputs
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            w1_stake = st.text_input("Kaizen Stakes (€):", "100", key=f"w1_stake_{i}")
            w1_stake = parse_number(w1_stake) or 0

        with col2:
            w2_stake = st.text_input("Competition Stakes (€):", "0", key=f"w2_stake_{i}")
            w2_stake = parse_number(w2_stake) or 0

        with col3:
            total_stake = st.text_input("Total Stake (€):", "0", key=f"total_stake_{i}")
            total_stake = parse_number(total_stake) or 0

    # Perform Calculation
    if total_stake > 0:
        results = calculate_surebet(w1_odds, w2_odds, total_stake=total_stake)
    elif w1_stake > 0 and w2_stake == 0:
        results = calculate_surebet(w1_odds, w2_odds, w1_stake=w1_stake)
    elif w2_stake > 0 and w1_stake == 0:
        results = calculate_surebet(w1_odds, w2_odds, w2_stake=w2_stake)
    elif w1_stake > 0 and w2_stake > 0:
        results = calculate_surebet(w1_odds, w2_odds, w1_stake=w1_stake, w2_stake=w2_stake)
    else:
        results = None

    # Display Results
    if results:
        arbitrage_color = "green" if results["Arbitrage %"] > 0 else "red"
        profit_w1_color = "green" if results["Profit W1"] > 0 else "red"
        profit_w2_color = "green" if results["Profit W2"] > 0 else "red"

        # Render Result Box
        st.markdown(
            f"""
            <div class="result-container">
                <div class="result-box">
                    <strong>Kaizen Profit:</strong> {results['Profit W1']}€
                </div>
                <div class="result-box">
                    <strong>Competition Profit:</strong> {results['Profit W2']}€
                </div>
                <div class="result-box">
                    <strong>Arbitrage:</strong> {results['Arbitrage %']}%
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
