import streamlit as st
import numpy as np
import pandas as pd

def calculate_total_bets(outcomes_per_selection):
    return np.prod(outcomes_per_selection)

def calculate_profit(win_odds, stake, total_stakes):
    return (win_odds * stake) - total_stakes

def run():
    st.title("Bonus Abuse Betting Calculator")
    
    # Number of selections
    selections = st.slider("Number of Selections", min_value=3, max_value=20, value=3)
    
    # Define outcomes per selection
    st.write("Enter the number of outcomes per selection (comma-separated):")
    outcomes_input = st.text_input("", value="2,2,2")
    outcomes_per_selection = list(map(int, outcomes_input.split(',')))
    
    if len(outcomes_per_selection) != selections:
        st.error("Number of selections and outcomes per selection mismatch! Check your input.")
        return
    
    # Calculate total bets needed
    total_bets = calculate_total_bets(outcomes_per_selection)
    st.write(f"Total Bets Needed: {total_bets}")
    
    # Input odds
    st.write("Enter 6 example odds:")
    odds = [st.number_input(f"Odds {i+1}", min_value=1.01, value=2.0) for i in range(6)]
    
    # Average Stake Input
    avg_stake = st.number_input("Enter the average stake per bet", min_value=1.0, value=10.0)
    
    # Total Stakes Calculation
    total_stakes = avg_stake * total_bets
    st.write(f"Total Stakes Invested: {total_stakes}")
    
    # Profit Calculation
    min_profit = calculate_profit(min(odds), avg_stake, total_stakes)
    max_profit = calculate_profit(max(odds), avg_stake, total_stakes)
    avg_profit = calculate_profit(sum(odds) / len(odds), avg_stake, total_stakes)
    
    # Extra Profit Calculation (50% Bonus Boost)
    min_extra_profit = min_profit + (0.5 * min_profit)
    max_extra_profit = max_profit + (0.5 * max_profit)
    avg_extra_profit = avg_profit + (0.5 * avg_profit)
    
    # Display Profit Calculations
    st.subheader("Profit Calculations")
    st.write(f"Profit for Lowest Odds: {min_profit:.2f} | Extra Profit: {min_extra_profit:.2f}")
    st.write(f"Profit for Highest Odds: {max_profit:.2f} | Extra Profit: {max_extra_profit:.2f}")
    st.write(f"Profit for Average Odds: {avg_profit:.2f} | Extra Profit: {avg_extra_profit:.2f}")
    
if __name__ == "__main__":
    main()
