import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu # Import the new component

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Income Inequality",
    page_icon="🌍",
    layout="wide"
)

# --- CUSTOM STYLES ---
custom_css = """
    <style>
        /* Main page background */
        .stApp {
            background-color: #f0f2f6;
            color: #333333;
        }

        /* Title and header colors */
        h1, h2, h3 {
            color: #005A9C; /* A professional blue color */
        }
        
        /* Reduce top padding for the main content */
        .block-container {
            padding-top: 2rem;
        }

        /* Hides default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- TOP NAVIGATION BAR ---
# Replaces the st.sidebar.radio from the previous version
selected_page = option_menu(
    menu_title=None,  # Don't show a title
    options=["Home", "About", "Dashboard"],
    icons=["house-fill", "person-badge-fill", "bar-chart-line-fill"],  # Bootstrap icons
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FFFFFF", "border-bottom": "2px solid #E0E0E0"},
        "icon": {"color": "#005A9C", "font-size": "20px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#F0F2F6"
        },
        "nav-link-selected": {"background-color": "#005A9C", "color": "#FFFFFF"},
    }
)

# --- PAGE DISPLAY LOGIC ---

# ------------------------------------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------------------------------------
if selected_page == "Home":
    
    st.title("Global Income Inequality Dashboard 🌏")
    st.markdown("### An Interactive Tool to Explore Economic Disparities")
    st.write(
        "Welcome! This dashboard provides an in-depth look at income inequality across the globe. "
        "Use the navigation at the top of the page to view the interactive dashboard or learn more about the author."
    )
    st.image(
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0", 
        caption="Data-driven Insights"
    )

# ------------------------------------------------------------------------------------------
# ABOUT PAGE (Previously Candidate Profile)
# ------------------------------------------------------------------------------------------
elif selected_page == "About":
    
    st.header("About the Author")
    st.divider()

    col1, col2 = st.columns([1, 2]) 

    with col1:
        # Replace this URL with a link to your professional photo.
        st.image("https://via.placeholder.com/250", width=250)

    with col2:
        st.markdown("### Subhomoy Halder")
        st.markdown("##### Part of the Infosys Springboard Data Visualization Internship")
        st.write(
            "Passionate about leveraging data to uncover insights and tell compelling stories. "
            "This project is a demonstration of data visualization skills using Power BI for analysis "
            "and Streamlit for creating an interactive web application."
        )
        # Replace the '#' with your actual profile links.
        st.write("🔗 [LinkedIn](#) | 🔗 [GitHub](#)")

# ------------------------------------------------------------------------------------------
# DASHBOARD PAGE
# ------------------------------------------------------------------------------------------
elif selected_page == "Dashboard":
    
    st.header("Interactive Power BI Dashboard")
    st.write("Interact with the visuals below to explore the data. Use the filters within the dashboard for a granular analysis.")

    power_bi_iframe = """
        <iframe title="Dashboard 3" width="100%" height="755" src="https://app.powerbi.com/view?r=eyJrIjoiYTc1NWU0MTItMGRhZS00YjY5LWJjNWMtMjc0OWQyOTdiNWJjIiwidCI6ImNlYjVhMDZjLTY2ZjEtNGE3NC1iZDExLTVmZDEwNTQwYTVlYSJ9&pageName=8650f3g3bcc395c7c66c" frameborder="0" allowFullScreen="true"></iframe>
    """
    
    components.html(power_bi_iframe, height=750, scrolling=True)
