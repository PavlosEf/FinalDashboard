import streamlit as st
from datetime import datetime
import pytz
from PIL import Image
import os


# Path to the flags folder
FLAGS_FOLDER = "Flags"

# Country to timezone and flag mapping
COUNTRY_TO_TIMEZONE = {
    "Greece": {"timezone": "Europe/Athens", "flag": "GR.png"},
    "Colombia": {"timezone": "America/Bogota", "flag": "CO.png"},
    "Brazil": {"timezone": "America/Sao_Paulo", "flag": "BR.png"},
    "Romania": {"timezone": "Europe/Bucharest", "flag": "RO.png"},
    "Czech Republic": {"timezone": "Europe/Prague", "flag": "CZ.png"},
    "Argentina": {"timezone": "America/Argentina/Buenos_Aires", "flag": "AR.png"},
    "Bulgaria": {"timezone": "Europe/Sofia", "flag": "BG.png"},
    "Canada": {"timezone": "America/Toronto", "flag": "CA.png"},
    "Chile": {"timezone": "America/Santiago", "flag": "CL.png"},
    "Denmark": {"timezone": "Europe/Copenhagen", "flag": "DK.png"},
    "Ecuador": {"timezone": "America/Guayaquil", "flag": "EC.png"},
    "Mexico": {"timezone": "America/Mexico_City", "flag": "MX.png"},
    "Nigeria": {"timezone": "Africa/Lagos", "flag": "Nigeria.png"},
    "Peru": {"timezone": "America/Lima", "flag": "PE.png"},
}

# Function to get current time in a specific timezone
def get_current_time(timezone):
    tz = pytz.timezone(timezone)
    return datetime.now(tz).strftime("%H:%M:%S")

# Function to display flag image
def display_flag(flag_file):
    flag_path = os.path.join(FLAGS_FOLDER, flag_file)
    if os.path.exists(flag_path):
        return Image.open(flag_path)
    else:
        return None  # Skip flag if missing

def run():
    st.title("🌍 World Clock")

    # ✅ Fix: Automatically refresh every 5 seconds
    st_autorefresh(interval=5000, key="clock_refresh")

    # Display live clock for each country
    for country, data in COUNTRY_TO_TIMEZONE.items():
        timezone = data["timezone"]
        flag_file = data["flag"]

        # Create columns for flag, country name, and time
        col1, col2, col3 = st.columns([1, 3, 2])
        with col1:
            flag = display_flag(flag_file)
            if flag:
                st.image(flag, width=30)
        with col2:
            st.write(f"**{country}**")
        with col3:
            st.write(f"`{get_current_time(timezone)}`")

if __name__ == "__main__":
    run()

