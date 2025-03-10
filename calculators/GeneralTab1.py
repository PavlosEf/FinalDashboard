import streamlit as st

def run():
    st.title("Percentage Calculator")
    st.markdown("Enter values and calculate percentages using different formulas.")

    # Define session state to track inputs
    for key in ["perc1", "perc2", "perc3", "perc4", "perc5", "perc6", "perc7", "perc8"]:
        if key not in st.session_state:
            st.session_state[key] = ""

    # Function to clear input fields
    def clear_input(key):
        st.session_state[key] = ""
        st.rerun()  # Updated from st.experimental_rerun() to st.rerun()

    # 🔹 **Basic Percentage Calculator**
    st.subheader("Basic Percentage Calculator")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        perc1 = st.text_input("Percent", value=st.session_state.perc1, key="perc1")
        st.button("Clear", on_click=clear_input, args=("perc1",), key="clear_perc1")
    with col2:
        perc2 = st.text_input("Value", value=st.session_state.perc2, key="perc2")
        st.button("Clear", on_click=clear_input, args=("perc2",), key="clear_perc2")
    with col3:
        result1 = st.text_input("Result", value="", disabled=True, key="result1")
        if st.button("Calculate Basic %", key="calc1"):
            try:
                result1 = str((float(perc1) / 100) * float(perc2))
            except:
                result1 = "Invalid Input"
            st.rerun()

    # 🔹 **Percentage Calculator in Common Phrases**
    st.subheader("Percentage Calculator in Common Phrases")

    # **"What is X% of Y?"**
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        perc3 = st.text_input("What is", value=st.session_state.perc3, key="perc3")
        st.button("Clear", on_click=clear_input, args=("perc3",), key="clear_perc3")
    with col2:
        perc4 = st.text_input("% of", value=st.session_state.perc4, key="perc4")
        st.button("Clear", on_click=clear_input, args=("perc4",), key="clear_perc4")
    with col3:
        result2 = st.text_input("Result", value="", disabled=True, key="result2")
        if st.button("Calculate Phrase 1", key="calc2"):
            try:
                result2 = str((float(perc3) / 100) * float(perc4))
            except:
                result2 = "Invalid Input"
            st.rerun()

    # **"X is what percent of Y?"**
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        perc5 = st.text_input("X", value=st.session_state.perc5, key="perc5")
        st.button("Clear", on_click=clear_input, args=("perc5",), key="clear_perc5")
    with col2:
        perc6 = st.text_input("Y", value=st.session_state.perc6, key="perc6")
        st.button("Clear", on_click=clear_input, args=("perc6",), key="clear_perc6")
    with col3:
        result3 = st.text_input("Result (%)", value="", disabled=True, key="result3")
        if st.button("Calculate Phrase 2", key="calc3"):
            try:
                result3 = str((float(perc5) / float(perc6)) * 100) + " %"
            except:
                result3 = "Invalid Input"
            st.rerun()

    # 🔹 **Percentage Difference Calculator**
    st.subheader("Percentage Difference Calculator")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        perc7 = st.text_input("Value 1", value=st.session_state.perc7, key="perc7")
        st.button("Clear", on_click=clear_input, args=("perc7",), key="clear_perc7")
    with col2:
        perc8 = st.text_input("Value 2", value=st.session_state.perc8, key="perc8")
        st.button("Clear", on_click=clear_input, args=("perc8",), key="clear_perc8")
    with col3:
        result4 = st.text_input("Result (%)", value="", disabled=True, key="result4")
        if st.button("Calculate Difference", key="calc4"):
            try:
                result4 = str(abs((float(perc7) - float(perc8)) / ((float(perc7) + float(perc8)) / 2) * 100)) + " %"
            except:
                result4 = "Invalid Input"
            st.rerun()

if __name__ == "__main__":
    run()
