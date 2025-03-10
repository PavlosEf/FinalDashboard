import streamlit as st

def run():
    st.title("Percentage Calculator")

    # ✅ Ensure session state is initialized to avoid KeyErrors
    default_values = {
        "percent_find_x": "",
        "percent_find_y": "",
        "percent_result": "",
        "percent_of_x": "",
        "percent_of_y": "",
        "percent_of_result": "",
        "increase_x": "",
        "increase_z": "",
        "increase_result": "",
        "is_percent_x": "",
        "is_percent_z": "",
        "is_percent_result": "",
    }
    
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

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

if __name__ == "__main__":
    run()
