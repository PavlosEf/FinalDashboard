 st.markdown(
    """
    <style>
        /* Input fields with black text */
        input[type="text"] {
           width: 100% !important; /* Ensure input area takes full width of the column */
           max-width: 200px !important; /* Limit the maximum size of the box */
           background-color: #EAEAEA !important; /* Light grey background */
           color: #000000 !important; /* Black text */
           caret-color: #000000 !important; /* Black caret for typing */
           padding: 5px !important; /* Adjust padding for a compact input */
           border-radius: 5px; /* Optional: keep rounded corners */
        }

        /* Result boxes for percentage */
       .result-box {
            border: 2px solid #FFFFFF; /* White border */
            padding: 5px;
            margin: 5px 10px; /* Adjust the spacing around the box */
            text-align: center;
            border-radius: 5px;
            width: 70px; /* Smaller width */
            display: inline-block;
            position: relative; /* Adjust position relative to normal flow */
            top: 20px; /* Moves the box slightly up */
        }
       
     .result-container {
            display: flex; /* Use flexbox for alignment */
            align-items: center; /* Vertically align items */
            justify-content: flex-start; /* Align items to the left */
            gap: 2px; /* Add spacing between the percentage and label boxes */
            margin-top: 5px; /* Optional: Add some space above the container */
        }


        /* Color-coded labels */
        .ok {
            color: #FFFFFF;
            background-color: #00FF00; /* Green for OK */
            border: 2px solid #00FF00;
        }

        .off2 {
            color: #FFFFFF;
            background-color: #800080; /* Purple for OFF 2 */
            border: 2px solid #800080;
        }

        .off1 {
            color: #FFFFFF;
            background-color: #FF0000; /* Red for OFF 1 */
            border: 2px solid #FF0000;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Define helper functions
    def parse_number(number_str):
        try:
            return float(number_str.replace(",", "."))
        except ValueError:
            return None

    def get_label(difference):
        if difference > -2:
            return '<div class="result-box ok">OK</div>' 
        elif -3 <= difference <= -2:
            return '<div class="result-box off2">OFF 2</div>'
        elif difference < -3:
            return '<div class="result-box off1">OFF 1</div>'
        else:
            return '<div class="result-box">None</div>'

    # Create input fields and calculate results
    for i in range(5):
        col1, col2, col3, col4 = st.columns([0.3, 0.3, 1, 1])  # Adjust column sizes
        
        with col1:
            price_a = st.text_input(f"Kaizen Odds {i + 1}:", key=f"price_a_{i}")
        with col2:
            price_b = st.text_input(f"Competition Odds {i + 1}:", key=f"price_b_{i}")
        
        if price_a and price_b:
            parsed_a = parse_number(price_a)
            parsed_b = parse_number(price_b)
       
            if parsed_a and parsed_b and parsed_a > 0 and parsed_b > 0:
                 # Calculate percentage difference
                 difference = ((1 / parsed_a) - (1 / parsed_b)) * 100

                    # Display percentage difference and label together in col3
                 with col3:
                     st.markdown(
                         f"""
                         <div class="result-container">
                             <div class="result-box">{difference:.2f}%</div>
                             {get_label(difference)}
                         </div>
                         """,
                         unsafe_allow_html=True,
                     )
elif selected_tool == "Surebet Calculator":
    st.title("Surebet Calculator")
    st.write("Placeholder for the Surebet Calculator.")
    # Add your Surebet Calculator logic here

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
