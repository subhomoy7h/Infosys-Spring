import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Income Inequality",
    page_icon="🌍",
    layout="wide"
)

# --- CUSTOM STYLES ---
# This CSS hides the default Streamlit menu, header, and footer, and adds a custom theme.
# You can generate new color schemes using tools like coolors.co
custom_css = """
    <style>
        /* Main page background */
        .stApp {
            background-color: #f0f2f6; /* A light grey background */
            color: #333333;
        }

        /* Sidebar style */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 2px solid #e0e0e0;
        }
        
        /* Title and header colors */
        h1, h2, h3 {
            color: #005A9C; /* A professional blue color */
        }

        /* Hides default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- NAVIGATION SIDEBAR ---
# Using the sidebar for navigation is a common and effective pattern for dashboards.
st.sidebar.title("Navigation")
# --- EDITABLE CONTENT ---
# You can change the page names and the emojis here
page = st.sidebar.radio("Go to", ("🏠 Home", "👤 Candidate Profile", "📊 Dashboard"))


# --- PAGE DISPLAY LOGIC ---

# ------------------------------------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------------------------------------
if page == "🏠 Home":
    
    # --- EDITABLE CONTENT ---
    st.title("Global Income Inequality Dashboard 🌏")
    st.markdown("### An Interactive Tool to Explore Economic Disparities")
    st.write(
        "Welcome! This dashboard provides an in-depth look at income inequality across the globe. "
        "Use the navigation on the left to view the interactive dashboard or learn more about the author."
    )
    
    # --- EDITABLE CONTENT ---
    # Find a good image online (e.g., from Unsplash, Pexels) and replace the URL.
    st.image(
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0", 
        caption="Data-driven Insights" # You can change the caption text
    )

# ------------------------------------------------------------------------------------------
# CANDIDATE PROFILE PAGE
# ------------------------------------------------------------------------------------------
elif page == "👤 Candidate Profile":
    
    # --- EDITABLE CONTENT ---
    st.header("Candidate Profile")
    st.divider()

    # Using columns for a cleaner layout
    col1, col2 = st.columns([1, 2]) 

    with col1:
        # --- PERSONALIZATION ---
        # Replace this URL with a link to your professional photo.
        # You can upload a photo to a site like Imgur or a public GitHub repo to get a link.
        st.image("https://via.placeholder.com/250", width=250)

    with col2:
        # --- EDITABLE CONTENT ---
        st.markdown("### Subhomoy Halder")
        st.markdown("##### Part of the Infosys Springboard Data Visualization Internship")
        st.write(
            "Passionate about leveraging data to uncover insights and tell compelling stories. "
            "This project is a demonstration of data visualization skills using Power BI for analysis "
            "and Streamlit for creating an interactive web application."
        )
        
        # --- PERSONALIZATION ---
        # Replace the '#' with your actual profile links.
        st.write("🔗 [LinkedIn](#) | 🔗 [GitHub](#)")

# ------------------------------------------------------------------------------------------
# DASHBOARD PAGE
# ------------------------------------------------------------------------------------------
elif page == "📊 Dashboard":
    
    # --- EDITABLE CONTENT ---
    st.header("Interactive Power BI Dashboard")
    st.write("Interact with the visuals below to explore the data. Use the filters within the dashboard for a granular analysis.")

    # --- POWER BI EMBED ---
    # This is your Power BI iframe code. Ensure the link is correct.
    power_bi_iframe = """
        <iframe title="Dashboard 3" width="100%" height="755" src="https://app.powerbi.com/view?r=eyJrIjoiYTc1NWU0MTItMGRhZS00YjY5LWJjNWMtMjc0OWQyOTdiNWJjIiwidCI6ImNlYjVhMDZjLTY2ZjEtNGE3NC1iZDExLTVmZDEwNTQwYTVlYSJ9&pageName=8650f3g3bcc395c7c66c" frameborder="0" allowFullScreen="true"></iframe>
    """
    
    # The `components.html` function is used to render the iframe.
    # The height can be adjusted to best fit your dashboard's aspect ratio.
    components.html(power_bi_iframe, height=750, scrolling=True)
