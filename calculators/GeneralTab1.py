import streamlit as st

def run():
    # Apply background image using CSS
    st.markdown(
        """
        <style>
            .stApp {
                background-image: url("https://img.freepik.com/free-vector/construction-with-black-yellow-stripes_1017-30755.jpg?semt=ais_hybrid");  /* Replace with your image URL */
                background-size: 75%;  /* Ensures the image covers the entire background */
                background-position: center;  /* Centers the image */
                background-repeat: no-repeat;  /* Prevents the image from repeating */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

   
