import streamlit as st

def run():
    # Apply background image using CSS
    st.markdown(
        """
        <style>
            .stApp {
                background-image: url("https://png.pngtree.com/png-vector/20241009/ourlarge/pngtree-coming-soon-under-construction-vector-png-image_14018490.png");  /* Replace with your image URL */
                background-size: 75%;  /* Ensures the image covers the entire background */
                background-position: center;  /* Centers the image */
                background-repeat: no-repeat;  /* Prevents the image from repeating */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display content
    st.title("General Tab 1")
    st.write("This section is under construction.")

