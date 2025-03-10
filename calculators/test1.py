import streamlit as st
import requests
from PIL import Image
import os

# Path to the flags folder
FLAGS_FOLDER = "Flags"

# Currency to country mapping
CURRENCY_TO_COUNTRY = {
    "EUR": {"name": "Euro", "flag": "EUR.png"},
    "ARS": {"name": "Argentina", "flag": "AR.png"},
    "BGN": {"name": "Bulgaria", "flag": "BG.png"},
    "BRL": {"name": "Brazil", "flag": "BR.png"},
    "CAD": {"name": "Canada", "flag": "CA.png"},
    "CLP": {"name": "Chile", "flag": "CL.png"},
    "COP": {"name": "Colombia", "flag": "CO.png"},
    "CZK": {"name": "Czech Republic", "flag": "CZ.png"},
    "DKK": {"name": "Denmark", "flag": "DK.png"},
    "USD": {"name": "Ecuador", "flag": "EC.png"},  # Ecuador uses USD
    "MXN": {"name": "Mexico", "flag": "MX.png"},
    "NGN": {"name": "Nigeria", "flag": "Nigeria.png"},
    "PEN": {"name": "Peru", "flag": "PE.png"},
    "RON": {"name": "Romania", "flag": "RO.png"},
}

# Fetch today's exchange rates
def fetch_exchange_rates(base_currency):
    API_KEY = "f155bbe573194b9c9eb48462"  # Replace with your API key 
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["conversion_rates"]
    else:
        st.error("Failed to fetch exchange rates. Please try again later.")
        return None

# Currency converter function
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount
    if from_currency not in rates or to_currency not in rates:
        st.error("Invalid currency selection.")
        return None
    return amount * rates[to_currency] / rates[from_currency]

# Function to display flag image
def display_flag(currency_code):
    flag_path = os.path.join(FLAGS_FOLDER, CURRENCY_TO_COUNTRY[currency_code]["flag"])
    if os.path.exists(flag_path):
        return Image.open(flag_path)
    else:
        st.warning(f"Flag for {currency_code} not found.")
        return None

def run():
    st.title("Currency Converter")

    # Fetch exchange rates (base: EUR)
    rates = fetch_exchange_rates("EUR")
    if not rates:
        return

    # Input fields
    col1, col2 = st.columns([0.15, 0.85])
    with col1:
        amount = st.number_input("Amount", min_value=0.0, value=100.0)
        
        # From currency dropdown with flag
        from_currency = st.selectbox(
            "From",
            options=list(CURRENCY_TO_COUNTRY.keys()),
            index=0,  # Default to Euro (EUR)
            format_func=lambda x: f"{CURRENCY_TO_COUNTRY[x]['name']} ({x})",
        )
        from_flag = display_flag(from_currency)
        if from_flag:
            st.image(from_flag, width=30)  # Display flag image

        # To currency dropdown with flag
        to_currency = st.selectbox(
            "To",
            options=list(CURRENCY_TO_COUNTRY.keys()),
            index=0,  # Default to Euro (EUR)
            format_func=lambda x: f"{CURRENCY_TO_COUNTRY[x]['name']} ({x})",
        )
        to_flag = display_flag(to_currency)
        if to_flag:
            st.image(to_flag, width=30)  # Display flag image

    # Convert currency
    if st.button("Convert"):
        result = convert_currency(amount, from_currency, to_currency, rates)
        if result is not None:
            st.markdown(f"""
                <div style="
                    border-bottom: 4px solid #4CAF50;
                    border-bottom-width: 12.5%;
                    background-color: rgba(211, 211, 211, 0.3);
                    padding: 10px;
                    border-radius: 5px;
                    font-size: 24px;
                ">
                    {amount} {from_currency} = <strong>{result:.6f} {to_currency}</strong>
                </div>
            """, unsafe_allow_html=True)

            # Display exchange rates
            st.write(f"1 {from_currency} = {rates[to_currency] / rates[from_currency]:.6f} {to_currency}")
            st.write(f"1 {to_currency} = {rates[from_currency] / rates[to_currency]:.6f} {from_currency}")

if __name__ == "__main__":
    run()
