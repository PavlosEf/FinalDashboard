import streamlit as st
from datetime import datetime
import pytz
import time

# Country to timezone mapping
COUNTRY_TO_TIMEZONE = {
    "Greece": "Europe/Athens",
    "Colombia": "America/Bogota",
    "Brazil": "America/Sao_Paulo",
    "Romania": "Europe/Bucharest",
    "Czech Republic": "Europe/Prague",
    "Argentina": "America/Argentina/Buenos_Aires",
    "Bulgaria": "Europe/Sofia",
    "Canada": "America/Toronto",
    "Chile": "America/Santiago",
    "Denmark": "Europe/Copenhagen",
    "Ecuador": "America/Guayaquil",
    "Mexico": "America/Mexico_City",
    "Nigeria": "Africa/Lagos",
    "Peru": "America/Lima",
}

# Function to get current time in a specific timezone
def get_current_time(timezone):
    tz = pytz.timezone(timezone)
    return datetime.now(tz).strftime("%H:%M:%S")

def run():
    st.title("World Clock 🌍")

    # Placeholder for updating clocks dynamically
    clock_placeholder = st.empty()

    while True:
        # Store the latest time results
        clock_data = ""

        for country, timezone in COUNTRY_TO_TIMEZONE.items():
            time_now = get_current_time(timezone)
            clock_data += f"**{country}**: `{time_now}`  \n"

        # Update the displayed clocks
        clock_placeholder.markdown(clock_data)

        # Wait 1 second before refreshing
        time.sleep(1)

if __name__ == "__main__":
    run()
