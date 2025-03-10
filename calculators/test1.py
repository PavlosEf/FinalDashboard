import streamlit as st

def calculate_percentage_of():
    x = st.number_input("Enter percentage (X):", min_value=0.0)
    y = st.number_input("Enter number (Y):", min_value=0.0)
    if st.button("Calculate X% of Y"):
        result = (x / 100) * y
        st.write(f"{x}% of {y} is {result}")

def calculate_what_percent():
    x = st.number_input("Enter number (X):", min_value=0.0)
    y = st.number_input("Enter number (Y):", min_value=0.0)
    if st.button("Calculate X is what percent of Y"):
        result = (x / y) * 100
        st.write(f"{x} is {result}% of {y}")

def calculate_percentage_change():
    x = st.number_input("Enter initial number (X):", min_value=0.0)
    y = st.number_input("Enter final number (Y):", min_value=0.0)
    if st.button("Calculate percentage change from X to Y"):
        result = ((y - x) / x) * 100
        st.write(f"The percentage change from {x} to {y} is {result}%")

def run():
    st.title("Percentage Calculator")
    
    option = st.selectbox(
        "Choose a calculation:",
        ("What is X% of Y?", "X is what percent of Y?", "Percentage increase/decrease from X to Y")
    )
    
    if option == "What is X% of Y?":
        calculate_percentage_of()
    elif option == "X is what percent of Y?":
        calculate_what_percent()
    elif option == "Percentage increase/decrease from X to Y":
        calculate_percentage_change()

if __name__ == "__main__":
    run()
