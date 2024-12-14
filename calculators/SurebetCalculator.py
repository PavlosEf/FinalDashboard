import streamlit as st

def run():
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

    # Settings Panel
    st.sidebar.title("Style Settings")
    input_bg_color = st.sidebar.color_picker("Input Field Background", "#3E4E56")
    input_text_color = st.sidebar.color_picker("Input Field Text Color", "#FFFFFF")
    result_bg_color = st.sidebar.color_picker("Result Box Background", "#FFD700")
    result_text_color = st.sidebar.color_picker("Result Box Text Color", "#000000")
    border_radius = st.sidebar.slider("Border Radius (px)", 0, 20, 8)
    padding_size = st.sidebar.slider("Horizontal Padding (px)", 0, 20, 10)
    input_height = st.sidebar.slider("Input Height (px)", 30, 60, 40)
    input_width = st.sidebar.slider("Input Width (px)", 200, 400, 300)

    # Inject updated CSS
    st.markdown(f"""
        <style>
            /* Remove default margin and padding for input containers */
            div[data-baseweb="input"] {{
                padding: 0 !important;
                margin: 0 !important;
                width: auto !important; /* Ensure the width adjusts properly */
            }}

            /* Input field styling */
            input[type="number"] {{
                background-color: {input_bg_color} !important; /* Dynamic background color */
                color: {input_text_color} !important; /* Dynamic text color */
                border: 1px solid #DEE2E6 !important; /* Border color */
                border-radius: {border_radius}px !important; /* Dynamic border radius */
                padding: 0px {padding_size}px !important; /* Remove vertical padding */
                height: {input_height}px !important; /* Dynamic height */
                width: {input_width}px !important; /* Dynamic width */
                box-shadow: none !important; /* Remove shadow effect */
            }}

            /* Remove margin from column layout (Streamlit container) */
            [data-testid="stVerticalBlock"] {{
                gap: 0px !important; /* Remove extra spacing between columns */
            }}

            /* Result box styling */
            .result-box {{
                background-color: {result_bg_color} !important; /* Dynamic background color */
                color: {result_text_color} !important; /* Dynamic text color */
                border-radius: {border_radius}px !important; /* Dynamic border radius */
                padding: {padding_size}px !important; /* Padding inside the box */
                margin: 10px !important; /* Margin outside the box */
                border: 1px solid #000000 !important; /* Box border color */
            }}

            /* General styling for the app */
            .stApp * {{
                color: #FFFFFF !important; /* Force white text for all content */
            }}
        </style>
    """, unsafe_allow_html=True)

    # Layout
    st.title("Surebet Calculator")
    st.markdown("Calculate stakes and profits for arbitrage betting scenarios dynamically.")

    # Input Fields
    col1, col2 = st.columns([1, 1])
    with col1:
        w1_odds = st.number_input("Kaizen Odds", min_value=1.01, value=2.5, step=0.01)
    with col2:
        w2_odds = st.number_input("Competition Odds", min_value=1.01, value=2.0, step=0.01)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        w1_stake = st.number_input("Kaizen Stakes (€)", min_value=0.0, value=0.0, step=0.01)
    with col2:
        w2_stake = st.number_input("Competition Stakes (€)", min_value=0.0, value=0.0, step=0.01)
    with col3:
        total_stake = st.number_input("Total Stake (€)", min_value=0.0, value=0.0, step=0.01)

    # Display Results (example result box to test styling)
    st.markdown('<div class="result-box">Example Result Box</div>', unsafe_allow_html=True)
