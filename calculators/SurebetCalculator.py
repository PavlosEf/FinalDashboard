import streamlit as st

def run():
    # Global Styles
    BACKGROUND_COLOR = "#3E4E56"  # Grey background for the main app
    TEXT_COLOR = "#FFFFFF"  # White text for all elements
    BUTTON_COLOR = "#DEE2E6"  # Button color for + and -

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
                padding: 5px !important;
                margin: 0 !important;
                width: 120px !important; /* Fixed width for input fields */
                box-sizing: border-box;
            }}
            /* Styling for + and - buttons */
            input[type="number"]::-webkit-inner-spin-button, 
            input[type="number"]::-webkit-outer-spin-button {{
                background-color: {BUTTON_COLOR} !important; /* Set button background color */
                color: {BACKGROUND_COLOR} !important; /* Set button text color */
                border: 1px solid #FFFFFF !important; /* Button border */
            }}
            input[type="number"]::-webkit-inner-spin-button:hover, 
            input[type="number"]::-webkit-outer-spin-button:hover {{
                background-color: #FFFFFF !important; /* Highlight button on hover */
                color: #000000 !important; /* Text color on hover */
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

    # Input Fields with Fake Column After Total Stake (€)
    for i in range(1):  # Adjusted to match layout from OffPricesCalculator.py
        # Row 1: Odds Inputs
        col1, col2, col_fake = st.columns([1, 1, 5])  # Fake column added after Competition Odds
        with col1:
            w1_odds = st.number_input("Kaizen Odds", min_value=1.01, value=2.5, step=0.01, key="w1_odds")
        with col2:
            w2_odds = st.number_input("Competition Odds", min_value=1.01, value=2.0, step=0.01, key="w2_odds")
        with col_fake:
            st.markdown("")  # Empty fake column for spacing

        # Row 2: Stake Inputs with Fake Column at the End
        col1, col2, col3, col_fake = st.columns([0.5, 0.5, 0.5, 2])  # Fake column added at the end
        with col1:
            w1_stake = st.number_input("Kaizen Stakes (€)", min_value=0.0, value=100.0, step=0.01, key="w1_stake")
        with col2:
            w2_stake = st.number_input("Competition Stakes (€)", min_value=0.0, value=0.0, step=0.01, key="w2_stake")
        with col3:
            total_stake = st.number_input("Total Stake (€)", min_value=0.0, value=0.0, step=0.01, key="total_stake")
        with col_fake:
            st.markdown("")  # Fake column for additional spacing at the end

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
        # Define dynamic colors for profits and arbitrage
        arbitrage_color = "green" if results["Arbitrage %"] > 0 else "red"
        profit_w1_color = "green" if results["Profit W1"] > 0 else "red"
        profit_w2_color = "green" if results["Profit W2"] > 0 else "red"

        # Render Stylish Results Box
        st.markdown(
            f"""
            <style>
                .result-box {{
                    background-color: #2B3A42; /* Darker background */
                    border: 1px solid #DEE2E6;
                    border-radius: 8px;
                    padding: 15px;
                    margin: 15px 0;
                    color: {TEXT_COLOR};
                    font-family: Arial, sans-serif;
                }}
                .result-box h4 {{
                    margin-bottom: 10px;
                    color: #FFFFFF; /* White color for headers */
                    font-size: 18px;
                    text-align: center;
                    text-decoration: underline;
                }}
                .result-box ul {{
                    list-style-type: none;
                    padding: 0;
                    margin: 0;
                }}
                .result-box ul li {{
                    margin-bottom: 10px;
                    font-size: 16px;
                }}
                .result-box ul li span {{
                    font-weight: bold;
                }}
            </style>
            <div class="result-box">
                <h4>Calculation Results</h4>
                <ul>
                    <li>Kaizen Stakes: <span>{results['W1 Stake']}€</span></li>
                    <li>Competition Stakes: <span>{results['W2 Stake']}€</span></li>
                    <li>Total Stake: <span>{results['Total Stake']}€</span></li>
                    <li>Profit Kaizen: 
                        <span style="color:{profit_w1_color};">{results['Profit W1']}€</span>
                    </li>
                    <li>Profit Competition: 
                        <span style="color:{profit_w2_color};">{results['Profit W2']}€</span>
                    </li>
                    <li>Arbitrage: 
                        <span style="color:{arbitrage_color};">{results['Arbitrage %']}%</span>
                    </li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
