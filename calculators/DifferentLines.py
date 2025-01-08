import streamlit as st
from DifferentLines import DifferentLinesCalculator

def main():
    st.title("Different Lines Calculator")
    
    # Initialize calculator
    calculator = DifferentLinesCalculator()
    
    # Create input fields in columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Kaizen Data")
        kaizen_line = st.number_input("Kaizen Line", value=0.0, step=0.5)
        kaizen_odds = st.number_input("Kaizen Odds", value=1.0, min_value=1.0, step=0.01)
        
    with col2:
        st.subheader("Competition Data")
        comp_line = st.number_input("Competition Line", value=0.0, step=0.5)
        comp_odds = st.number_input("Competition Odds", value=1.0, min_value=1.0, step=0.01)
    
    # Add calculate button
    if st.button("Calculate"):
        try:
            # Calculate results
            result = calculator.calculate(
                kaizen_line=kaizen_line,
                kaizen_odds=kaizen_odds,
                comp_line=comp_line,
                comp_odds=comp_odds
            )
            
            # Display results in a nice format
            st.divider()
            st.subheader("Results")
            
            # Display main results
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Our Line", f"{result.kaizen_line}")
                st.metric("Our Odds", f"{result.kaizen_odds}")
            
            with col2:
                st.metric("Competition at Our Line", f"{result.comp_at_kaizen_line:.3f}")
                st.metric("Difference", f"{result.difference_percentage:.2f}%")
            
            # Display status with appropriate color
            status_colors = {
                "OK": "green",
                "Off 2": "orange",
                "Off 1": "red"
            }
            
            st.markdown(
                f"""
                <div style='padding: 10px; border-radius: 5px; background-color: {status_colors.get(result.status, "gray")}; color: white;'>
                    <h3 style='text-align: center; margin: 0;'>Status: {result.status}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Display disclaimer
            st.caption("Disclaimer: This is an approximated calculator. Real odds may have a small difference.")
            
        except ValueError as e:
            st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
