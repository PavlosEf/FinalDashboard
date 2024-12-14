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
                padding: 5px !important;
                margin: 0 !important;
                width: 3000px !important; /* Fixed width for input fields */
                box-sizing: border-box;
            }}
            /* Styling for Results Box */
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
                color: #FFFFFF !important; /* Force white for header */
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
            /* Profit and Loss Colors */
            .profit-positive {{
                color: green !important; /* Green for positive values */
            }}
            .profit-negative {{
                color: red !important; /* Red for negative values */
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Lay Bet Calculator")
    st.markdown("Calculate lay stakes, liabilities, and profits for betting scenarios on Top Price Market prices.")

    # Function for calculation
    def calculate_back_lay_bet(back_stake, back_odds, lay_odds):
        lay_stake = (back_stake * back_odds) / lay_odds
        liability = lay_stake * (lay_odds - 1)

        # Back Bet Outcomes
        back_bet_profit_win = back_stake * (back_odds - 1)  # Profit when back bet wins
        back_bet_profit_lose = -back_stake  # Loss when back bet loses

        # Lay Bet Outcomes
        lay_bet_profit_win = -liability  # Loss when lay bet loses
        lay_bet_profit_lose = lay_stake  # Profit when lay bet wins

        # Market Profit (combined outcomes)
        market_profit_win = back_bet_profit_win + lay_bet_profit_win
        market_profit_lose = back_bet_profit_lose + lay_bet_profit_lose

        return {
            "Lay Stake": round(lay_stake, 2),
            "Liability": round(liability, 2),
            "Back Bet Profit Win": round(back_bet_profit_win, 2),
            "Back Bet Profit Lose": round(back_bet_profit_lose, 2),
            "Lay Bet Profit Win": round(lay_bet_profit_win, 2),
            "Lay Bet Profit Lose": round(lay_bet_profit_lose, 2),
            "Market Profit Win": round(market_profit_win, 2),
            "Market Profit Lose": round(market_profit_lose, 2),
        }

    # Input Fields
    st.markdown("### Input Parameters")
    col1, col2, col3, col_fake = st.columns([1, 1, 1, 2])  # Fake column for layout adjustment
    with col1:
        back_odds = st.number_input("Back Odds", min_value=1.01, value=2.5, step=0.01)
    with col2:
        lay_odds = st.number_input("Lay Odds", min_value=1.01, value=2.4, step=0.01)
    with col3:
        back_stake = st.number_input("Back Stake (€)", min_value=0.0, value=100.0, step=1.0)
    with col_fake:
        st.markdown("")  # Empty column for spacing

    # Calculation Button
    if st.button("Calculate"):
        results = calculate_back_lay_bet(back_stake, back_odds, lay_odds)

        # Display Results
        st.markdown(
            f"""
            <div class="result-box">
                <h4>Calculation Results</h4>
                <ul>
                    <li>Lay Stake: <span>{results['Lay Stake']}€</span></li>
                    <li>Liability: <span>{results['Liability']}€</span></li>
                    <h4>If Back Wins:</h4>
                    <li>Back Bet Profit: 
                        <span class="{'profit-positive' if results['Back Bet Profit Win'] >= 0 else 'profit-negative'}">
                            {results['Back Bet Profit Win']}€
                        </span>
                    </li>
                    <li>Lay Bet Profit: 
                        <span class="{'profit-positive' if results['Lay Bet Profit Win'] >= 0 else 'profit-negative'}">
                            {results['Lay Bet Profit Win']}€
                        </span>
                    </li>
                    <li>Market Profit: 
                        <span class="{'profit-positive' if results['Market Profit Win'] >= 0 else 'profit-negative'}">
                            {results['Market Profit Win']}€
                        </span>
                    </li>
                    <h4>If Back Loses:</h4>
                    <li>Back Bet Profit: 
                        <span class="{'profit-positive' if results['Back Bet Profit Lose'] >= 0 else 'profit-negative'}">
                            {results['Back Bet Profit Lose']}€
                        </span>
                    </li>
                    <li>Lay Bet Profit: 
                        <span class="{'profit-positive' if results['Lay Bet Profit Lose'] >= 0 else 'profit-negative'}">
                            {results['Lay Bet Profit Lose']}€
                        </span>
                    </li>
                    <li>Market Profit: 
                        <span class="{'profit-positive' if results['Market Profit Lose'] >= 0 else 'profit-negative'}">
                            {results['Market Profit Lose']}€
                        </span>
                    </li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Footer
    st.markdown("---")
