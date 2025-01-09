import streamlit as st

def run():
    # Global Styles
    BACKGROUND_COLOR = "#FFFFFF"  # Background color for the app
    TEXT_COLOR = "#000000"  # Text color for all elements

    # Inject global CSS for styling
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {BACKGROUND_COLOR} !important;
                color: {TEXT_COLOR} !important;
            }}
            .small-result-box {{
                background-color: #e9f2f7;
                border: 1px solid #DEE2E6;
                border-radius: 8px;
                padding: 15px;
                margin: 15px 0;
                color: {TEXT_COLOR};
                font-family: Arial, sans-serif;
            }}
            .small-result-box h4 {{
                margin-bottom: 10px;
                color: #000000 !important;
                font-size: 16px;
                text-decoration: underline;
                text-align: center;
            }}
            .small-result-box ul {{
                list-style-type: none;
                padding: 0;
                margin: 0;
            }}
            .small-result-box ul li {{
                margin-bottom: 10px;
                font-size: 14px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Page title
    st.title("Surebet Calculator")
    st.markdown("Calculate stakes and profits dynamically for 2-way, 3-way, or 4-way betting scenarios.")

    # Market selection
    market_type = st.radio("Market Type", ["2-Way Market", "3-Way Market", "4-Way Market"], horizontal=True)

    # Stake option
    stake_option = st.radio("Calculation Based On:", ["Kaizen Stakes", "Total Stake"], horizontal=True)

    # Odds inputs
    odds = []
    if market_type == "2-Way Market":
        col1, col2 = st.columns(2)
        with col1:
            odd1 = st.number_input("Kaizen Odds", min_value=1.01, value=2.0, step=0.01)
        with col2:
            odd2 = st.number_input("Competition Odds", min_value=1.01, value=2.5, step=0.01)
        odds = [odd1, odd2]
    elif market_type == "3-Way Market":
        col1, col2, col3 = st.columns(3)
        with col1:
            odd1 = st.number_input("Kaizen Odds", min_value=1.01, value=2.0, step=0.01)
        with col2:
            odd2 = st.number_input("Competition 1 Odds", min_value=1.01, value=2.5, step=0.01)
        with col3:
            odd3 = st.number_input("Competition 2 Odds", min_value=1.01, value=3.0, step=0.01)
        odds = [odd1, odd2, odd3]
    elif market_type == "4-Way Market":
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            odd1 = st.number_input("Kaizen Odds", min_value=1.01, value=2.0, step=0.01)
        with col2:
            odd2 = st.number_input("Competition 1 Odds", min_value=1.01, value=2.5, step=0.01)
        with col3:
            odd3 = st.number_input("Competition 2 Odds", min_value=1.01, value=3.0, step=0.01)
        with col4:
            odd4 = st.number_input("Competition 3 Odds", min_value=1.01, value=4.0, step=0.01)
        odds = [odd1, odd2, odd3, odd4]

    # Stake input
    if stake_option == "Kaizen Stakes":
        kaizen_stake = st.number_input("Kaizen Stake (€)", min_value=0.0, value=100.0, step=0.01)
    else:
        total_stake = st.number_input("Total Stake (€)", min_value=0.0, value=100.0, step=0.01)

    # Calculation function
    def calculate_surebet(odds, kaizen_stake=None, total_stake=None):
        probabilities = [1 / odd for odd in odds]
        total_probability = sum(probabilities)

        if kaizen_stake is not None:
            stakes = [kaizen_stake * (prob / probabilities[0]) for prob in probabilities]
            total_stake = sum(stakes)
        else:
            stakes = [total_stake * (prob / total_probability) for prob in probabilities]

        profits = [round((odds[i] * stakes[i]) - total_stake, 2) for i in range(len(odds))]
        arbitrage_percentage = (1 - total_probability) * 100

        return {
            "Stakes": [round(stake, 2) for stake in stakes],
            "Profits": profits,
            "Total Stake": round(total_stake, 2),
            "Arbitrage %": round(arbitrage_percentage, 2)
        }

    # Calculate results
    if st.button("Calculate Surebet"):
        if stake_option == "Kaizen Stakes":
            results = calculate_surebet(odds, kaizen_stake=kaizen_stake)
        else:
            results = calculate_surebet(odds, total_stake=total_stake)

        # Display results
        st.markdown("### Results")
        st.markdown(
            f"""
            <div class="small-result-box">
                <h4>Calculation Results</h4>
                <ul>
                    {"".join([f"<li>Stake {i+1}: <span>{results['Stakes'][i]}€</span></li>" for i in range(len(odds))])}
                    {"".join([f"<li>Profit {i+1}: <span>{results['Profits'][i]}€</span></li>" for i in range(len(odds))])}
                    <li>Total Stake: <span>{results['Total Stake']}€</span></li>
                    <li>Arbitrage: <span>{results['Arbitrage %']}%</span></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    run()
