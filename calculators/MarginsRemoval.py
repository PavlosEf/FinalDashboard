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
            /* Styling for Results Boxes */
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

    st.title("Margins Removal Calculator")
    st.markdown("Calculate margin, probabilities, pseudo-probabilities, and fair odds for 2-Way or 3-Way Odds.")

    # Function to calculate probabilities and fair odds
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

    # Input: Select Odds Type
    odds_type = st.radio("Select Odds Type:", ["2-Way Odds", "3-Way Odds"])

    # Input Fields
    if odds_type == "2-Way Odds":
        col1, col2, col_fake = st.columns([1, 1, 2])  # Fake column for layout adjustment
        with col1:
            odd1 = st.number_input("Odd 1", min_value=1.01, value=2.0, step=0.01, key="odd1_2way")
        with col2:
            odd2 = st.number_input("Odd 2", min_value=1.01, value=2.0, step=0.01, key="odd2_2way")
        with col_fake:
            st.markdown("")  # Empty column for spacing
        odds = [odd1, odd2]

    elif odds_type == "3-Way Odds":
        col1, col2, col3, col_fake = st.columns([1, 1, 1, 1])  # Fake column for layout adjustment
        with col1:
            odd1 = st.number_input("Odd 1", min_value=1.01, value=3.0, step=0.01, key="odd1_3way")
        with col2:
            odd2 = st.number_input("Odd 2", min_value=1.01, value=3.5, step=0.01, key="odd2_3way")
        with col3:
            odd3 = st.number_input("Odd 3", min_value=1.01, value=4.0, step=0.01, key="odd3_3way")
        with col_fake:
            st.markdown("")  # Empty column for spacing
        odds = [odd1, odd2, odd3]

    # Calculation Button
    if st.button("Calculate"):
        results = calculate_margins(odds)

        # Display Results
        st.markdown("### Results")
        st.markdown(
            f"""
            <div class="result-box">
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

