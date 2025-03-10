import streamlit as st

def run():
    st.title("Percentage Calculator")

    # ✅ Initialize session state to avoid errors
    for key in ["percent_find_x", "percent_find_y", "percent_result",
                "percent_of_x", "percent_of_y", "percent_of_result",
                "increase_x", "increase_z", "increase_result",
                "is_percent_x", "is_percent_z", "is_percent_result"]:
        if key not in st.session_state:
            st.session_state[key] = ""

    # ✅ Function to reset a specific input
    def clear_input(input_key):
        st.session_state[input_key] = ""

    # ✅ Function to calculate: "X% of Y"
    def calculate_percent_of():
        try:
            x = float(st.session_state["percent_find_x"])
            y = float(st.session_state["percent_find_y"])
            st.session_state["percent_result"] = f"{(x / 100) * y:.2f}"
        except ValueError:
            st.session_state["percent_result"] = "Invalid Input"

    # ✅ Function to calculate: "X is what percent of Y?"
    def calculate_what_percent():
        try:
            x = float(st.session_state["percent_of_x"])
            y = float(st.session_state["percent_of_y"])
            st.session_state["percent_of_result"] = f"{(x / y) * 100:.2f}%"
        except ValueError:
            st.session_state["percent_of_result"] = "Invalid Input"

    # ✅ Function to calculate: "Percentage Increase/Decrease"
    def calculate_percentage_increase():
        try:
            x = float(st.session_state["increase_x"])
            z = float(st.session_state["increase_z"])
            percent_change = ((z - x) / abs(x)) * 100
            st.session_state["increase_result"] = f"{percent_change:.2f}%"
        except ValueError:
            st.session_state["increase_result"] = "Invalid Input"

    # ✅ Function to calculate: "X is Z% of what?"
    def calculate_is_percent_of():
        try:
            x = float(st.session_state["is_percent_x"])
            z = float(st.session_state["is_percent_z"])
            st.session_state["is_percent_result"] = f"{(x / (z / 100)):.2f}"
        except ValueError:
            st.session_state["is_percent_result"] = "Invalid Input"

    # ✅ Apply custom CSS for styling
    st.markdown("""
        <style>
            .result-box {
                background-color: #4CAF50; /* Green */
                color: white;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                margin-top: 10px;
            }
            .calc-box {
                background-color: #F0F0F0; 
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #CCC;
                margin-bottom: 15px;
            }
            .stButton button {
                background-color: #4CAF50 !important;
                color: white !important;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    # ✅ SECTION 1: "X% of Y"
    with st.container():
        st.subheader("What is X% of Y?")
        col1, col2, col3 = st.columns([1, 1, 0.5])
        with col1:
            st.text_input("X%", key="percent_find_x")
        with col2:
            st.text_input("of", key="percent_find_y")
        with col3:
            st.button("Calculate", on_click=calculate_percent_of)

        # Display result
        if st.session_state["percent_result"]:
            st.markdown(f"<div class='result-box'>Result: {st.session_state['percent_result']}</div>", unsafe_allow_html=True)

    # ✅ SECTION 2: "X is what percent of Y?"
    with st.container():
        st.subheader("X is what percent of Y?")
        col1, col2, col3 = st.columns([1, 1, 0.5])
        with col1:
            st.text_input("X", key="percent_of_x")
        with col2:
            st.text_input("is what % of", key="percent_of_y")
        with col3:
            st.button("Calculate", on_click=calculate_what_percent)

        # Display result
        if st.session_state["percent_of_result"]:
            st.markdown(f"<div class='result-box'>Result: {st.session_state['percent_of_result']}</div>", unsafe_allow_html=True)

    # ✅ SECTION 3: "Percentage Increase/Decrease"
    with st.container():
        st.subheader("Percentage Increase/Decrease")
        col1, col2, col3 = st.columns([1, 1, 0.5])
        with col1:
            st.text_input("From", key="increase_x")
        with col2:
            st.text_input("To", key="increase_z")
        with col3:
            st.button("Calculate", on_click=calculate_percentage_increase)

        # Display result
        if st.session_state["increase_result"]:
            st.markdown(f"<div class='result-box'>Result: {st.session_state['increase_result']}</div>", unsafe_allow_html=True)

    # ✅ SECTION 4: "X is Z% of what?"
    with st.container():
        st.subheader("X is Z% of what?")
        col1, col2, col3 = st.columns([1, 1, 0.5])
        with col1:
            st.text_input("X", key="is_percent_x")
        with col2:
            st.text_input("is Z% of", key="is_percent_z")
        with col3:
            st.button("Calculate", on_click=calculate_is_percent_of)

        # Display result
        if st.session_state["is_percent_result"]:
            st.markdown(f"<div class='result-box'>Result: {st.session_state['is_percent_result']}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    run()
