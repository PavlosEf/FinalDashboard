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
                width: 120px !important; /* Fixed width for input fields */
                box-sizing: border-box;
            }}
            /* Styling for Smaller Results Box */
            .small-result-box {{
                background-color: #2B3A42;
                border: 1px solid #DEE2E6;
                border-radius: 8px;
                padding: 15px;
                margin: 15px 0;
                width: 50%; /* Smaller width */
                color: {TEXT_COLOR};
                font-family: Arial, sans-serif;
                display: inline-block;
                vertical-align: top;
            }}
            .small-result-box h4 {{
                margin-bottom: 10px;
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

    st.title("Odds Margin Calculator")
    st.markdown("Calculate the margin, implied probabilities, and fair odds for 2-way or 3-way betting markets.")

    # Function to calculate probabilities, margin, and fair odds
    def calculate_margins(odds):
        probabilities = [100 / odd for odd in odds]
        margin = sum(probabilities) - 100
        pseudo_probabilities = [prob / (1 + margin / 100) for prob in probabilities]
        fair_odds = [100 / pseudo_prob for pseudo_prob in pseudo_probabilities]

        return {
            "Margin %": round(margin, 2),
            "Probabilities with Margin": [round(prob, 2) for prob in probabilities],
            "Pseudo-Probabilities": [round(pseudo_prob, 2) for pseudo_prob in pseudo_probabilities],
            "Fair Odds": [round(fair_odd, 2) for fair_odd in fair_odds],
        }

    # Input Type Selection
    st.markdown("### Select Market Type")
    market_type = st.radio("Market Type", ["2-Way Market", "3-Way Market"], horizontal=True)

    # Inputs for Odds
    odds = []
    if market_type == "2-Way Market":
        st.markdown("### Enter Odds for 2-Way Market")
        col1, col2, col_fake = st.columns([0.5, 0.5, 2])  # Adjust layout
        with col1:
            odd1 = st.number_input("Odd 1", min_value=1.01, value=2.0, step=0.01)
        with col2:
            odd2 = st.number_input("Odd 2", min_value=1.01, value=2.0, step=0.01)
        odds = [odd1, odd2]

    elif market_type == "3-Way Market":
        st.markdown("### Enter Odds for 3-Way Market")
        col1, col2, col3, col_fake = st.columns([0.5, 0.5, 0.5, 2])  # Adjust layout
        with col1:
            odd1 = st.number_input("Odd 1", min_value=1.01, value=3.0, step=0.01)
        with col2:
            odd2 = st.number_input("Odd 2", min_value=1.01, value=3.5, step=0.01)
        with col3:
            odd3 = st.number_input("Odd 3", min_value=1.01, value=4.0, step=0.01)
        odds = [odd1, odd2, odd3]

    # Calculate Results
    if st.button("Calculate Margin"):
        results = calculate_margins(odds)

        # Display Results in Smaller Box
        st.markdown("### Results")
        st.markdown(
            f"""
            <div class="small-result-box">
                <h4>Calculation Results</h4>
                <ul>
                    <li>Margin: <span>{results['Margin %']}%</span></li>
                    <h4>Probabilities with Margin:</h4>
                    {"".join([f"<li>Odd {i+1}: <span>{results['Probabilities with Margin'][i]}%</span></li>" for i in range(len(odds))])}
                    <h4>Pseudo-Probabilities:</h4>
                    {"".join([f"<li>Odd {i+1}: <span>{results['Pseudo-Probabilities'][i]}%</span></li>" for i in range(len(odds))])}
                    <h4>Fair Odds:</h4>
                    {"".join([f"<li>Odd {i+1}: <span>{results['Fair Odds'][i]}</span></li>" for i in range(len(odds))])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Footer
    st.markdown("---")
