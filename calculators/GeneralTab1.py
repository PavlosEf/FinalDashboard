import streamlit as st

def run():
    st.title("Percentage Calculator")
    st.markdown("### Step 1: What is X% of Y?")
    
    # Initialize session state for inputs if not already set
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
            st.session_state["result"] = f"The {percent}% of {total} is = {result}"
        except ValueError:
            st.session_state["result"] = "Invalid input. Please enter valid numbers."

    # Function to clear input fields
    def clear_inputs():
        st.session_state["percentage"] = ""
        st.session_state["total_value"] = ""
        st.session_state["result"] = ""

    # Layout for input fields
    col1, col2 = st.columns([1, 1])
    with col1:
        st.text_input("Enter Percentage (%)", key="percentage", on_change=calculate_percentage)
    with col2:
        st.text_input("Enter Total Value", key="total_value", on_change=calculate_percentage)

    # Result Box
    st.markdown("### Result:")
    st.markdown(
        f"""
        <div style='background-color:#3E4E56; color:white; padding:10px; border-radius:8px; text-align:center; font-size:16px; font-weight:bold;'>
            {st.session_state["result"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Clear Button
    st.button("Clear", on_click=clear_inputs)

if __name__ == "__main__":
    run()
