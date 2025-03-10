import streamlit as st

def calculate_percentage_of():
    col1, col2 = st.columns([0.15, 0.85])  # 15% for inputs, 85% for other content
    with col1:
        x = st.number_input("Enter percentage (X):", min_value=0.0)
        y = st.number_input("Enter number (Y):", min_value=0.0)
    if st.button("Calculate X% of Y"):
        result = (x / 100) * y
        st.markdown(f"""
            <div style="
                border-bottom: 4px solid #4CAF50;
                border-bottom-width: 12.5%;
                background-color: rgba(211, 211, 211, 0.3);
                padding: 10px;
                border-radius: 5px;
                font-size: 24px;
            ">
                {x}% of {y} is <strong>{result}</strong>
            </div>
        """, unsafe_allow_html=True)

def calculate_what_percent():
    col1, col2 = st.columns([0.15, 0.85])  # 15% for inputs, 85% for other content
    with col1:
        x = st.number_input("Enter number (X):", min_value=0.0)
        y = st.number_input("Enter number (Y):", min_value=0.0)
    if st.button("Calculate X is what percent of Y"):
        result = (x / y) * 100
        st.markdown(f"""
            <div style="
                border-bottom: 4px solid #4CAF50;
                border-bottom-width: 12.5%;
                background-color: rgba(211, 211, 211, 0.3);
                padding: 10px;
                border-radius: 5px;
                font-size: 24px;
            ">
                {x} is <strong>{result}%</strong> of {y}
            </div>
        """, unsafe_allow_html=True)

def calculate_percentage_change():
    col1, col2 = st.columns([0.15, 0.85])  # 15% for inputs, 85% for other content
    with col1:
        x = st.number_input("Enter initial number (X):", min_value=0.0)
        y = st.number_input("Enter final number (Y):", min_value=0.0)
    if st.button("Calculate percentage change from X to Y"):
        result = ((y - x) / x) * 100
        st.markdown(f"""
            <div style="
                border-bottom: 4px solid #4CAF50;
                border-bottom-width: 12.5%;
                background-color: rgba(211, 211, 211, 0.3);
                padding: 10px;
                border-radius: 5px;
                font-size: 24px;
            ">
                The percentage change from {x} to {y} is <strong>{result}%</strong>
            </div>
        """, unsafe_allow_html=True)

def calculate_x_is_what_percent_of_y():
    col1, col2 = st.columns([0.15, 0.85])  # 15% for inputs, 85% for other content
    with col1:
        x = st.number_input("Enter number (X):", min_value=0.0, key="x_percent")
        y = st.number_input("Enter number (Y):", min_value=0.0, key="y_percent")
    if st.button("Calculate X is what % of Y"):
        result = (x / y) * 100
        st.markdown(f"""
            <div style="
                border-bottom: 4px solid #4CAF50;
                border-bottom-width: 12.5%;
                background-color: rgba(211, 211, 211, 0.3);
                padding: 10px;
                border-radius: 5px;
                font-size: 24px;
            ">
                {x} is <strong>{result}%</strong> of {y}
            </div>
        """, unsafe_allow_html=True)

def run():
    st.title("Percentage (%) Calculations")
    
    # Use columns to constrain the dropdown width to 15%
    col1, col2 = st.columns([0.15, 0.85])
    with col1:
        option = st.selectbox(
            "Choose a calculation:",
            (
                "What is X% of Y?",
                "X is what percent of Y?",
                "X is what % of Y?",
                "Percentage increase/decrease from X to Y"
            )
        )
    
    if option == "What is X% of Y?":
        calculate_percentage_of()
    elif option == "X is what percent of Y?":
        calculate_what_percent()
    elif option == "X is what % of Y?":
        calculate_x_is_what_percent_of_y()
    elif option == "Percentage increase/decrease from X to Y":
        calculate_percentage_change()

if __name__ == "__main__":
    run()
