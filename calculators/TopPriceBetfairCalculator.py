import streamlit as st

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

# Layout
st.title("Lay Bet Calculator")
st.markdown("Calculate lay stakes, liabilities, and profits for betting scenarios on Top Price Market prices.")

# Input Fields
st.markdown("### Input Parameters")
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        back_odds = st.number_input("Back Odds", min_value=1.01, value=2.5, step=0.01)
    with col2:
        lay_odds = st.number_input("Lay Odds", min_value=1.01, value=2.4, step=0.01)
    with col3:
        back_stake = st.number_input("Back Stake (€)", min_value=0.0, value=100.0, step=1.0)

# Calculate Lay Stake on Input
calculated_lay_stake = (back_stake * back_odds) / lay_odds
calculated_total_stake = back_stake + calculated_lay_stake

# Dynamic Input Boxes for Lay Stake and Total Stake
col1, col2 = st.columns([1, 1])
with col1:
    lay_stake = st.number_input(
        "Lay Stake (€)", min_value=0.0, value=round(calculated_lay_stake, 2), step=0.01
    )
with col2:
    total_stake = st.number_input(
        "Total Stake (€)", min_value=0.0, value=round(calculated_total_stake, 2), step=0.01
    )

# Adjust Lay Stake and Total Stake Dynamically
if lay_stake != round(calculated_lay_stake, 2):
    total_stake = back_stake + lay_stake
elif total_stake != round(calculated_total_stake, 2):
    lay_stake = total_stake - back_stake

# Calculation Button
if st.button("Calculate"):
    results = calculate_back_lay_bet(back_stake, back_odds, lay_odds)

    # Display Results
    st.markdown("### Results Breakdown")

    # Simplified Display
    st.markdown(
        f"""
        <style>
        .result-box {{
            background-color: #3E4E56;
            border: 1px solid #DEE2E6;
            border-radius: 8px;
            padding: 15px;
            margin: 10px;
            color: #FFFFFF;
        }}
        .result-box h4 {{
            margin-bottom: 10px;
            text-decoration: underline;
        }}
        .result-box ul {{
            list-style-type: none;
            padding: 0;
        }}
        .result-box ul li {{
            margin-bottom: 5px;
        }}
        .warning {{
            color: red;
            font-weight: bold;
        }}
        </style>
        <div class="result-box">
            <h4>If Back Win:</h4>
            <ul>
                <li>Back Bet Profit: €{results['Back Bet Profit Win']}</li>
                <li>Lay Bet Profit: €{results['Lay Bet Profit Win']}</li>
                <li>Market Profit: €{results['Market Profit Win']}</li>
            </ul>
            <h4>If Back Lose:</h4>
            <ul>
                <li>Back Bet Profit: €{results['Back Bet Profit Lose']}</li>
                <li>Lay Bet Profit: €{results['Lay Bet Profit Lose']}</li>
                <li>Market Profit: €{results['Market Profit Lose']}</li>
            </ul>
        </div>
        <p class="warning">In case the outcome confirms in Exchange it will be applied a Commission (%) on the NET winnings. Most exchanges are on 2%.</p>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown("---")
