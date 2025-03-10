import streamlit as st

def run():
    st.title("Percentage Calculator")

    # Initialize session state variables
    for key in ["percent_x", "percent_y", "percent_result",
                "what_percent_x", "what_percent_y", "what_percent_result",
                "increase_x", "increase_y", "increase_result"]:
        if key not in st.session_state:
            st.session_state[key] = ""

    # Function to calculate: "What is X% of Y?"
    def calculate_percent_of():
        try:
            x = float(st.session_state["percent_x"])
            y = float(st.session_state["percent_y"])
            st.session_state["percent_result"] = f"{(x / 100) * y:.2f}"
        except ValueError:
            st.session_state["percent_result"] = "Invalid Input"

    # Function to calculate: "X is what percent of Y?"
    def calculate_what_percent():
        try:
            x = float(st.session_state["what_percent_x"])
            y = float(st.session_state["what_percent_y"])
            st.session_state["what_percent_result"] = f"{(x / y) * 100:.2f}"
        except ValueError:
            st.session_state["what_percent_result"] = "Invalid Input"

    # Function to calculate: "What is the percentage increase/decrease from X to Y?"
    def calculate_percentage_change():
        try:
            x = float(st.session_state["increase_x"])
            y = float(st.session_state["increase_y"])
            percent_change = ((y - x) / abs(x)) * 100
            st.session_state["increase_result"] = f"{percent_change:.2f}"
        except ValueError:
            st.session_state["increase_result"] = "Invalid Input"

    # Styling
    st.markdown("""
        <style>
            .calculator-box {
                background-color: #F5F5F5;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
            }
            .input-box {
                width: 100px !important;
                text-align: center;
                font-size: 16px;
                padding: 5px;
            }
            .calculate-button {
                background-color: #2E71B8;
                color: white;
                font-weight: bold;
                padding: 5px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .result-box {
                width: 80px;
                text-align: center;
                font-size: 16px;
                font-weight: bold;
                color: black;
                background-color: white;
                border: none;
                padding: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # 1️⃣ What is X% of Y?
    st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([2, 1, 2, 2, 1])
    with col1:
        percent_x = st.text_input("", key="percent_x", placeholder="X%", label_visibility="collapsed")
    with col2:
        st.markdown("<p style='font-size:18px; text-align:center;'>%</p>", unsafe_allow_html=True)
    with col3:
        percent_y = st.text_input("", key="percent_y", placeholder="Y", label_visibility="collapsed")
    with col4:
        st.button("CALCULATE", on_click=calculate_percent_of, use_container_width=True)
    with col5:
        st.text_input("", st.session_state["percent_result"], key="percent_result_display", label_visibility="collapsed", disabled=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 2️⃣ X is what percent of Y?
    st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([2, 3, 2, 2, 1])
    with col1:
        what_percent_x = st.text_input("", key="what_percent_x", placeholder="X", label_visibility="collapsed")
    with col2:
        st.markdown("<p style='font-size:18px; text-align:center;'>is what percent of</p>", unsafe_allow_html=True)
    with col3:
        what_percent_y = st.text_input("", key="what_percent_y", placeholder="Y", label_visibility="collapsed")
    with col4:
        st.button("CALCULATE", on_click=calculate_what_percent, use_container_width=True)
    with col5:
        st.text_input("", st.session_state["what_percent_result"], key="what_percent_result_display", label_visibility="collapsed", disabled=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 3️⃣ What is the percentage increase/decrease from X to Y?
    st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 1, 2, 1])
    with col1:
        st.markdown("<p style='font-size:18px; text-align:right;'>from</p>", unsafe_allow_html=True)
    with col2:
        increase_x = st.text_input("", key="increase_x", placeholder="X", label_visibility="collapsed")
    with col3:
        st.markdown("<p style='font-size:18px; text-align:right;'>to</p>", unsafe_allow_html=True)
    with col4:
        increase_y = st.text_input("", key="increase_y", placeholder="Y", label_visibility="collapsed")
    with col5:
        st.button("CALCULATE", on_click=calculate_percentage_change, use_container_width=True)
    with col6:
        st.text_input("", st.session_state["increase_result"], key="increase_result_display", label_visibility="collapsed", disabled=True)

    st.markdown('</div>', unsafe_allow_html=True)
