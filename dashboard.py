st.markdown(f"""
    <style>
        /* Locked sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: {SIDEBAR_BACKGROUND} !important;
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] h1, h2, h3, h4, h5, h6 {{
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] label {{
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {{
            background-color: transparent !important; /* Fix for sidebar selections */
            color: {TEXT_COLOR} !important;
        }}
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"]:hover {{
            background-color: #1F2A32 !important; /* Darker background on hover */
        }}
        section[data-testid="stSidebar"] {{
            padding: 20px;
        }}
        
        /* Locked main content styling */
        .stApp {{
            background-color: {BACKGROUND_COLOR} !important;
            color: {TEXT_COLOR} !important;
        }}

        /* Default input styling (make text white and background consistent) */
        input[type="text"], input[type="number"], textarea {{
            background-color: #3E4E56 !important; /* Same as app background */
            color: {TEXT_COLOR} !important; /* White text */
            caret-color: {TEXT_COLOR} !important; /* White caret */
            border: 1px solid #DEE2E6 !important;
            border-radius: 5px !important;
            padding: 8px !important;
        }}

        /* Fix for sidebar and primary buttons */
        button[kind="primary"] {{
            background-color: #FF0000 !important; /* Red background */
            color: #FFFFFF !important; /* White text */
            border: none !important;
            border-radius: 5px !important;
            font-weight: bold !important;
            font-size: 16px !important;
            padding: 10px 20px !important;
        }}
        button[kind="primary"]:hover {{
            background-color: #CC0000 !important; /* Darker red on hover */
        }}

        /* Styling for + and - buttons on number inputs */
        input[type="number"]::-webkit-inner-spin-button,
        input[type="number"]::-webkit-outer-spin-button {{
            background-color: #FF0000 !important; /* Red color */
            color: #FFFFFF !important; /* White text */
        }}
        input[type="number"]::-webkit-inner-spin-button:hover,
        input[type="number"]::-webkit-outer-spin-button:hover {{
            background-color: #CC0000 !important; /* Darker red on hover */
        }}

        /* Ensure all other elements are properly visible */
        .stApp * {{
            color: inherit !important;
        }}

        /* Specific fix for sidebar selections */
        [data-testid="stSidebar"] .stRadio {{
            color: {TEXT_COLOR} !important; /* White text */
            font-size: 14px !important;
        }}
        [data-testid="stSidebar"] .stRadio:hover {{
            color: {TEXT_COLOR} !important;
        }}
    </style>
""", unsafe_allow_html=True)
