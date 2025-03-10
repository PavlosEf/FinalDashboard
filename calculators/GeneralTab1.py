import streamlit as st

def run():
    st.title("Percentage Calculator")
    st.markdown("### Step 1: What is X% of Y?")

    # Initialize session state for inputs
    if "percentage" not in st.session_state:
        st.session_state["percentage"] = ""
    if "total_value" not in st.session_state:
        st.session_state["total_value"] = ""
    if "result" not in st.session_state:
        st.session_state["result"] = ""

    # Function to calculate percentage
    def calculate_percentage():
        try:
            percent = float(st.session_state["percentage"])
            total = float(st.session_state["total_value"])
            result = (percent / 100) * total
            st.session_state["result"] = f"{percent}% of {total} = <b style='color:#FFD700'>{result}</b>"
        except ValueError:
            st.session_state["result"] = "Invalid Input"

    # Function to clear input fields
    def clear_inputs():
        st.session_state["percentage"] = ""
        st.session_state["total_value"] = ""
        st.session_state["result"] = ""

    # Custom CSS for Styling
    st.markdown("""
        <style>
            .percentage-container {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 5px;
                background-color: #F1F1F1;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #D1D1D1;
                width: 450px;
                margin: auto;
            }
            .input-box {
                width: 60px;
                height: 30px;
                text-align: center;
                font-size: 16px;
                border: 1px solid #A0A0A0;
                border-radius: 5px;
            }
            .result-box {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                margin-top: 10px;
            }
            .calc-button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            .clear-button {
                background-color: #A0A0A0;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML Structure for Input Fields
    st.markdown(
        f"""
        <div class="percentage-container">
            <input type="text" class="input-box" id="percentage" value="{st.session_state['percentage']}" 
            oninput="setPercentage(this.value)">
            <span>% of</span>
            <input type="text" class="input-box" id="total_value" value="{st.session_state['total_value']}" 
            oninput="setTotalValue(this.value)">
            <span>=</span>
            <input type="text" class="input-box" id="result" value="{st.session_state['result']}" disabled>
        </div>

        <script>
            function setPercentage(value) {{
                fetch("/_stcore_update?key=percentage&value=" + value, {{ method: "POST" }});
            }}
            function setTotalValue(value) {{
                fetch("/_stcore_update?key=total_value&value=" + value, {{ method: "POST" }});
            }}
        </script>
        """,
        unsafe_allow_html=True
    )

    # Buttons for Calculation & Clearing
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Calculate", on_click=calculate_percentage):
            pass
    with col2:
        if st.button("Clear", on_click=clear_inputs):
            pass

    # Styled Result Box
    st.markdown(
        f"""
        <div class="result-box">
            Result: {st.session_state["result"]}
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    run()
