import streamlit as st

def run():
    st.title("Surebet Calculator")

    # Function to validate numeric input
    def validate_input(value, field_name):
        try:
            return float(value)
        except ValueError:
            st.error(f"Please enter a valid number for {field_name}.")
            return None

    # Odds Inputs
    st.markdown("### Odds Input")
    col1, col2 = st.columns(2)
    with col1:
        w1_odds = st.text_input("Kaizen Odds", "2.5", key="w1_odds")
        w1_odds = validate_input(w1_odds, "Kaizen Odds")

    with col2:
        w2_odds = st.text_input("Competition Odds", "2.0", key="w2_odds")
        w2_odds = validate_input(w2_odds, "Competition Odds")

    # Stakes Inputs
    st.markdown("### Stakes Input")
    col3, col4, col5 = st.columns(3)
    with col3:
        w1_stake = st.text_input("Kaizen Stakes (€)", "100", key="w1_stake")
        w1_stake = validate_input(w1_stake, "Kaizen Stakes (€)")

    with col4:
        w2_stake = st.text_input("Competition Stakes (€)", "0", key="w2_stake")
        w2_stake = validate_input(w2_stake, "Competition Stakes (€)")

    with col5:
        total_stake = st.text_input("Total Stake (€)", "0", key="total_stake")
        total_stake = validate_input(total_stake, "Total Stake (€)")

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

    # Perform Calculation if all inputs are valid
    if all(value is not None for value in [w1_odds, w2_odds]) and any(
        value is not None for value in [w1_stake, w2_stake, total_stake]
    ):
        results = calculate_surebet(w1_odds, w2_odds, w1_stake, w2_stake, total_stake)

        # Display Results
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
        st.warning("Please ensure all required fields are filled with valid numbers.")

