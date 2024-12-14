import streamlit as st

def run():
    st.title("Off Prices Calculator")
    st.markdown("Enter prices below to calculate the percentage difference Kaizen odds are 1st!")

    # Add custom CSS for styling
    st.markdown(
        """
        <style>
            input[type="text"] {
               width: 100% !important;
               max-width: 200px !important;
               background-color: #EAEAEA !important;
               color: #000000 !important;
               caret-color: #000000 !important;
               padding: 5px !important;
               border-radius: 5px;
            }
            .result-box {
                border: 2px solid #FFFFFF;
                padding: 5px;
                margin: 5px 10px;
                text-align: center;
                border-radius: 5px;
                width: 70px;
                display: inline-block;
                position: relative;
                top: 20px;
            }
            .result-container {
                display: flex;
                align-items: center;
                justify-content: flex-start;
                gap: 2px;
                margin-top: 5px;
            }
            .ok {
                color: #FFFFFF;
                background-color: #00FF00;
                border: 2px solid #00FF00;
            }
            .off2 {
                color: #FFFFFF;
                background-color: #800080;
                border: 2px solid #800080;
            }
            .off1 {
                color: #FFFFFF;
                background-color: #FF0000;
                border: 2px solid #FF0000;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Helper functions
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
