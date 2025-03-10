import streamlit as st

def run():
    st.title("Percentage Calculator in Common Phrases")

    # Initialize session state for all calculators
    if "percent_of" not in st.session_state:
        st.session_state["percent_of"] = ""
    if "total_of" not in st.session_state:
        st.session_state["total_of"] = ""
    if "percent_result" not in st.session_state:
        st.session_state["percent_result"] = ""

    if "percent_find_x" not in st.session_state:
        st.session_state["percent_find_x"] = ""
    if "percent_find_y" not in st.session_state:
        st.session_state["percent_find_y"] = ""
    if "percent_find_result" not in st.session_state:
        st.session_state["percent_find_result"] = ""

    if "increase_x" not in st.session_state:
        st.session_state["increase_x"] = ""
    if "increase_z" not in st.session_state:
        st.session_state["increase_z"] = ""
    if "increase_result" not in st.session_state:
        st.session_state["increase_result"] = ""

    if "is_percent_x" not in st.session_state:
        st.session_state["is_percent_x"] = ""
    if "is_percent_z" not in st.session_state:
        st.session_state["is_percent_z"] = ""
    if "is_percent_result" not in st.session_state:
        st.session_state["is_percent_result"] = ""

    # Function to calculate "X is what percent of Y?"
    def calculate_percent():
        try:
            x = float(st.session_state["percent_find_x"])
            y = float(st.session_state["percent_find_y"])
            result = (x / y) * 100
            st.session_state["percent_find_result"] = f"{result:.2f}%"
        except ValueError:
            st.session_state["percent_find_result"] = "Invalid Input"

    # Function to calculate percentage increase/decrease
    def calculate_increase():
        try:
            x = float(st.session_state["increase_x"])
            z = float(st.session_state["increase_z"])
            result = ((z - x) / x) * 100
            st.session_state["increase_result"] = f"{result:.2f}%"
        except ValueError:
            st.session_state["increase_result"] = "Invalid Input"

    # Function to calculate "X is Z% of what?"
    def calculate_is_percent():
        try:
            x = float(st.session_state["is_percent_x"])
            z = float(st.session_state["is_percent_z"])
            result = (x / (z / 100))
            st.session_state["is_percent_result"] = f"{result:.2f}"
        except ValueError:
            st.session_state["is_percent_result"] = "Invalid Input"

    # Function to clear inputs
    def clear_inputs(key_list):
        for key in key_list:
            st.session_state[key] = ""

    # Custom CSS for styling
    st.markdown("""
        <style>
            .calc-container {
                background-color: #F1F1F1;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #D1D1D1;
                width: 500px;
                margin: auto;
                text-align: center;
            }
            .input-box {
                width: 80px;
                height: 35px;
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
                width: 80px; /* 1/7 of input field */
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

    # ------------------ 1st Calculation: "X is what percent of Y?" -------------------
    st.markdown("### 1️⃣ X is what percent of Y?")
    col1, col2, col3, col4, col5 = st.columns([1.2, 1, 1.2, 0.8, 1])
    with col1:
        st.session_state["percent_find_x"] = st.text_input(" ", st.session_state["percent_find_x"], key="find_x")
    with col2:
        st.markdown("<p style='text-align:center; font-size:20px;'>is what % of</p>", unsafe_allow_html=True)
    with col3:
        st.session_state["percent_find_y"] = st.text_input(" ", st.session_state["percent_find_y"], key="find_y")
    with col4:
        st.button("Calculate", on_click=calculate_percent)
    with col5:
        st.button("Clear", on_click=lambda: clear_inputs(["percent_find_x", "percent_find_y", "percent_find_result"]))

    st.markdown(f"<div class='result-box'>{st.session_state['percent_find_result']}</div>", unsafe_allow_html=True)

    # ------------------ 2nd Calculation: "Percentage Increase/Decrease" -------------------
    st.markdown("### 2️⃣ Percentage Increase/Decrease from X to Z?")
    col1, col2, col3, col4, col5 = st.columns([1.2, 1, 1.2, 0.8, 1])
    with col1:
        st.session_state["increase_x"] = st.text_input(" ", st.session_state["increase_x"], key="increase_x")
    with col2:
        st.markdown("<p style='text-align:center; font-size:20px;'>to</p>", unsafe_allow_html=True)
    with col3:
        st.session_state["increase_z"] = st.text_input(" ", st.session_state["increase_z"], key="increase_z")
    with col4:
        st.button("Calculate", on_click=calculate_increase)
    with col5:
        st.button("Clear", on_click=lambda: clear_inputs(["increase_x", "increase_z", "increase_result"]))

    st.markdown(f"<div class='result-box'>{st.session_state['increase_result']}</div>", unsafe_allow_html=True)

    # ------------------ 3rd Calculation: "X is Z% of what?" -------------------
    st.markdown("### 3️⃣ X is Z% of what?")
    col1, col2, col3, col4, col5 = st.columns([1.2, 1, 1.2, 0.8, 1])
    with col1:
        st.session_state["is_percent_x"] = st.text_input(" ", st.session_state["is_percent_x"], key="is_percent_x")
    with col2:
        st.markdown("<p style='text-align:center; font-size:20px;'>is</p>", unsafe_allow_html=True)
    with col3:
        st.session_state["is_percent_z"] = st.text_input(" ", st.session_state["is_percent_z"], key="is_percent_z")
    with col4:
        st.button("Calculate", on_click=calculate_is_percent)
    with col5:
        st.button("Clear", on_click=lambda: clear_inputs(["is_percent_x", "is_percent_z", "is_percent_result"]))

    st.markdown(f"<div class='result-box'>{st.session_state['is_percent_result']}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    run()
