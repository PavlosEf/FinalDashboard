import streamlit as st

# Function to calculate stakes and arbitrage
def calculate_surebet(w1_odds, w2_odds, w1_stake=None, w2_stake=None, total_stake=None):
    if total_stake:
        # Split total stake for equal profit
        w1_stake = total_stake / (1 + w1_odds / w2_odds)
        w2_stake = total_stake - w1_stake
    elif w1_stake:
        # Calculate w2 stake for equal profit
        w2_stake = (w1_stake * w1_odds) / w2_odds
        total_stake = w1_stake + w2_stake
    elif w2_stake:
        # Calculate w1 stake for equal profit
        w1_stake = (w2_stake * w2_odds) / w1_odds
        total_stake = w1_stake + w2_stake

    # Calculate profits
    profit_w1 = (w1_odds * w1_stake) - total_stake
    profit_w2 = (w2_odds * w2_stake) - total_stake

    # Calculate arbitrage percentage
    arbitrage_percentage = max(profit_w1, profit_w2) / total_stake * 100

    return {
        "W1 Stake": round(w1_stake, 2),
        "W2 Stake": round(w2_stake, 2),
        "Total Stake": round(total_stake, 2),
        "Profit W1": round(profit_w1, 2),
        "Profit W2": round(profit_w2, 2),
        "Arbitrage %": round(arbitrage_percentage, 2)
    }

# Layout
st.title("Surebet Calculator")
st.markdown("Calculate stakes and profits for arbitrage betting scenarios dynamically.")

# Input Fields
st.markdown("### Input Parameters")
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        w1_odds = st.number_input("Kaizen Odds", min_value=1.01, value=2.5, step=0.01)
    with col2:
        w2_odds = st.number_input("Competition Odds", min_value=1.01, value=2.0, step=0.01)

# Dynamic Input for W1, W2, and Total stakes
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    w1_stake = st.number_input("Kaizen Stakes (€)", min_value=0.0, step=0.01, value=0.0)
with col2:
    w2_stake = st.number_input("Competition Stakes (€)", min_value=0.0, step=0.01, value=0.0)
with col3:
    total_stake = st.number_input("Total Stake (€)", min_value=0.0, step=0.01, value=0.0)

# Dynamic Calculation
if total_stake > 0:
    # Scenario 3: Total Stake provided
    results = calculate_surebet(w1_odds, w2_odds, total_stake=total_stake)
elif w1_stake > 0 and w2_stake == 0:
    # Scenario 1: W1 Stake provided
    results = calculate_surebet(w1_odds, w2_odds, w1_stake=w1_stake)
elif w2_stake > 0 and w1_stake == 0:
    # Scenario 2: W2 Stake provided
    results = calculate_surebet(w1_odds, w2_odds, w2_stake=w2_stake)
elif w1_stake > 0 and w2_stake > 0:
    # Scenario 4: Both W1 and W2 stakes provided
    results = calculate_surebet(w1_odds, w2_odds, w1_stake=w1_stake, w2_stake=w2_stake)
else:
    results = None

# Display Results
if results:
    st.markdown("### Results")

    # Styling for Arbitrage and Profits
    arbitrage_color = "green" if results["Arbitrage %"] > 0 else "red"
    profit_w1_color = "green" if results["Profit W1"] > 0 else "red"
    profit_w2_color = "green" if results["Profit W2"] > 0 else "red"

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
        .arbitrage {{
            color: {arbitrage_color};
            font-weight: bold;
        }}
        .profit-w1 {{
            color: {profit_w1_color};
            font-weight: bold;
        }}
        .profit-w2 {{
            color: {profit_w2_color};
            font-weight: bold;
        }}
        </style>
        <div class="result-box">
            <h4>Calculation Results:</h4>
            <ul>
                <li>Kaizen Stakes: {results['W1 Stake']}€</li>
                <li>Competition Stakes: {results['W2 Stake']}€</li>
                <li>Total Stake: {results['Total Stake']}€</li>
                <li>Profit Kaizen: <span class="profit-w1">{results['Profit W1']}€</span></li>
                <li>Profit Competition: <span class="profit-w2">{results['Profit W2']}€</span></li>
                <li>Arbitrage: <span class="arbitrage">{results['Arbitrage %']}%</span></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
