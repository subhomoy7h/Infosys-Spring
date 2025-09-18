import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Income Inequality",
    page_icon="✨", # A more modern, abstract icon
    layout="wide"
)

# --- PROFESSIONAL UI/UX STYLES ---
# This CSS creates the modern, dark aesthetic of an AI startup
custom_css = """
    <style>
        /* Base app styling */
        .stApp {
            background-color: #0f172a; /* Dark slate blue background */
            color: #e2e8f0; /* Light slate gray text */
            font-family: 'sans-serif';
        }

        /* Titles and headers */
        h1, h2, h3 {
            color: #38bdf8; /* Vibrant sky blue accent */
        }
        
        /* Custom styling for the option menu */
        .st-emotion-cache-13ln4jf { /* This targets the container of the option menu */
            border-bottom: 2px solid #334155;
        }

        /* Markdown tables */
        .stMarkdown table {
            width: 100%;
            border-collapse: collapse;
            border-radius: 8px;
            overflow: hidden; /* Ensures the border-radius is applied to corners */
        }
        .stMarkdown th {
            background-color: #1e293b; /* Darker slate for header */
            color: #94a3b8;
            font-weight: bold;
            text-align: left;
            padding: 12px;
        }
        .stMarkdown td {
            background-color: #334155; /* Lighter slate for cells */
            color: #e2e8f0;
            padding: 12px;
            border-top: 1px solid #1e293b;
        }

        /* Hides default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- TOP NAVIGATION BAR ---
selected_page = option_menu(
    menu_title=None,
    options=["Home", "About", "Dashboard"],
    icons=["house-door-fill", "person-fill", "clipboard-data-fill"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0f172a"},
        "icon": {"color": "#e2e8f0", "font-size": "20px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#1e293b"
        },
        "nav-link-selected": {"background-color": "#38bdf8", "color": "#0f172a", "font-weight": "bold"},
    }
)

# --- PAGE DISPLAY LOGIC ---

# ------------------------------------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------------------------------------
if selected_page == "Home":
    
    st.title("Understanding Income Inequality 💡")
    st.markdown(
        "Income inequality refers to the uneven distribution of income within a population. "
        "Below are some of the key metrics used globally to measure and understand these disparities."
    )
    st.divider()

    # --- EDITABLE CONTENT: TABLE OF METRICS ---
    # The table is created using Markdown for better styling and control.
    table_data = """
| Measure                 | Explanation                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gini Coefficient** | The most common metric, ranging from 0 (perfect equality) to 1 (perfect inequality). It measures the dispersion of income distribution.       |
| **Decile Ratios** | Compares the income of the richest 10% of the population to the poorest 10%. A high ratio indicates significant disparity.                      |
| **Poverty Line** | A minimum income threshold below which an individual or household is considered to be in poverty. This can be absolute or relative.            |
| **Headcount Ratio** | The percentage of a country's population living below the established Poverty Line. It measures the prevalence of poverty.                    |
| **Poverty Gap Index** | Measures the intensity of poverty by calculating the average distance of the poor's income from the poverty line.                               |
| **Watts Index** | A poverty measure that is sensitive to the distribution of income among the poor, giving more weight to the poorest individuals.              |
| **PPP (Purchasing Power Parity)** | An economic theory used to adjust income figures across countries. It accounts for differences in the cost of living to allow for a more accurate comparison. |
    """
    st.markdown(table_data, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------
# ABOUT PAGE
# ------------------------------------------------------------------------------------------
elif selected_page == "About":
    
    st.header("About This Project")
    st.divider()

    # --- EDITABLE CONTENT: ABOUT TEXT (IMAGE REMOVED) ---
    st.markdown(
        """
        ### Subhomoy Halder
        ##### *Part of the Infosys Springboard Data Visualization Internship*

        This dashboard is a demonstration of data visualization and web application development skills. 
        It leverages **Power BI** for in-depth data analysis and **Streamlit** to create a fully interactive and user-friendly web interface.

        The goal of this project is to make complex data on global income inequality accessible and understandable to a broader audience.

        🔗 **Connect with me:** [LinkedIn](#) | [GitHub](#)
        """,
        unsafe_allow_html=True # Allows rendering of links
    )

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
