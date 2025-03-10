import streamlit as st
import requests

# Country flags (Unicode emojis)
COUNTRY_FLAGS = {
    "EUR": "🇪🇺",  # Euro
    "RON": "🇷🇴",  # Romania
    "BRL": "🇧🇷",  # Brazil
    "BGN": "🇧🇬",  # Bulgaria
    "CZK": "🇨🇿",  # Czech Republic
    "CLP": "🇨🇱",  # Chile
    "PEN": "🇵🇪",  # Peru
    "USD": "🇺🇸",  # Ecuador (uses USD)
    "NGN": "🇳🇬",  # Nigeria
    "CAD": "🇨🇦",  # Canada
    "COP": "🇨🇴",  # Colombia
    "MXN": "🇲🇽",  # Mexico
    "ARS": "🇦🇷",  # Argentina
    "DKK": "🇩🇰",  # Denmark
}

# Fetch today's exchange rates
def fetch_exchange_rates(base_currency):
    API_KEY = "YOUR_API_KEY"  # Replace with your API key
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
        from_currency = st.selectbox(
            "From",
            options=list(COUNTRY_FLAGS.keys()),
            format_func=lambda x: f"{COUNTRY_FLAGS[x]} {x}",
        )
        to_currency = st.selectbox(
            "To",
            options=list(COUNTRY_FLAGS.keys()),
            format_func=lambda x: f"{COUNTRY_FLAGS[x]} {x}",
        )

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
