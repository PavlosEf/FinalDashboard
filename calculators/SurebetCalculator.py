import streamlit as st

def run():
    # Global Styles
    BACKGROUND_COLOR = "#3E4E56"  # Grey background for the main app
    TEXT_COLOR = "#FFFFFF"  # White text for all elements

    st.markdown(
        f"""
        <style>
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
                padding: 5px !important;
                margin: 0 !important;
                width: 100% !important;
                max-width: 120px !important;
                box-sizing: border-box;
            }}
            div[data-testid="stBlock"] {{
                gap: 5px !important;
            }}
            .css-18e3th9 {{
                padding: 0px !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Surebet Calculator")
    st.markdown("Calculate stakes and profits for arbitrage betting scenarios dynamically.")

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

    # Input Form
    with st.form(key="surebet_form"):
        st.markdown("### Input Values")

        # Row 1: Odds Inputs
        col1, col2 = st.columns([1, 1])
        with col1:
            w1_odds = st.number_input("Kaizen Odds", min_value=1.01, value=2.5, step=0.01, key="w1_odds")
        with col2:
            w2_odds = st.number_input("Competition Odds", min_value=1.01, value=2.0, step=0.01, key="w2_odds")

        # Row 2: Stake Inputs
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            w1_stake = st.number_input("Kaizen Stakes (€)", min_value=0.0, value=100.0, step=0.01, key="w1_stake")
        with col2:
            w2_stake = st.number_input("Competition Stakes (€)", min_value=0.0, value=0.0, step=0.01, key="w2_stake")
        with col3:
            total_stake = st.number_input("Total Stake (€)", min_value=0.0, value=0.0, step=0.01, key="total_stake")

        # Submit Button
        submitted = st.form_submit_button(label="Calculate")

    # Perform Calculation after Form Submission
    if submitted:
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

            st.markdown(
                f"""
                <div style="background-color:#FFD700; padding: 15px; border-radius: 5px; border: 1px solid #000;">
                    <h4>Calculation Results:</h4>
                    <ul>
                        <li>Kaizen Stakes: {results['W1 Stake']}€</li>
                        <li>Competition Stakes: {results['W2 Stake']}€</li>
                        <li>Total Stake: {results['Total Stake']}€</li>
                        <li>Profit Kaizen: <span style="color:{profit_w1_color}">{results['Profit W1']}€</span></li>
                        <li>Profit Competition: <span style="color:{profit_w2_color}">{results['Profit W2']}€</span></li>
                        <li>Arbitrage: <span style="color:{arbitrage_color}">{results['Arbitrage %']}%</span></li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("Please ensure all required fields are filled with valid values.")
