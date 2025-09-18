import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Income Inequality Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- DASHBOARD UI STYLES ---
# This CSS is crucial for creating the card-based, dashboard-like look.
custom_css = """
    <style>
        /* Base app styling */
        .stApp {
            background-color: #0f172a; /* Dark slate blue background */
            color: #e2e8f0;
            font-family: 'sans-serif';
        }

        /* Titles and headers */
        h1, h2, h3 {
            color: #67e8f9; /* Bright Cyan accent */
        }

        /* Main content container styling */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            background-color: #1e293b; /* Darker slate for cards */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px; /* Space between cards */
            height: 100%; /* Make cards in a row have the same height */
        }

        /* Metric card specific styling */
        .metric-card {
            text-align: center;
        }
        .metric-value {
            font-size: 2.5em;
            font-weight: bold;
            color: #67e8f9;
        }
        .metric-label {
            font-size: 1.1em;
            color: #94a3b8; /* Muted text color */
        }

        /* Table styling inside cards */
        .stMarkdown table {
            width: 100%;
            border-collapse: collapse;
        }
        .stMarkdown th {
            background-color: #334155;
            color: #cbd5e1;
            font-weight: bold;
            text-align: left;
            padding: 12px;
        }
        .stMarkdown td {
            color: #e2e8f0;
            padding: 12px;
            border-top: 1px solid #334155;
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
    icons=["speedometer2", "person-workspace", "graph-up"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0f172a", "border-bottom": "1px solid #334155"},
        "icon": {"color": "#e2e8f0", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#1e293b"},
        "nav-link-selected": {"background-color": "#67e8f9", "color": "#0f172a", "font-weight": "bold"},
    }
)

# --- PAGE DISPLAY LOGIC ---

# ------------------------------------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------------------------------------
if selected_page == "Home":
    
    st.title("Global Income Inequality Dashboard")
    st.markdown("An overview of key concepts and metrics for analyzing economic disparities.")
    st.divider()

    # --- METRIC CARDS ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="card metric-card">
                <div class="metric-value">7+</div>
                <div class="metric-label">Key Metrics</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card metric-card">
                <div class="metric-value">150+</div>
                <div class="metric-label">Countries Analyzed</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="card metric-card">
                <div class="metric-value">Global</div>
                <div class="metric-label">Perspective</div>
            </div>
        """, unsafe_allow_html=True)

    # --- GLOSSARY CARD ---
    st.markdown("""
        <div class="card">
            <h3>Glossary of Inequality Measures</h3>
            <table>
                <tr><th>Measure</th><th>Explanation</th></tr>
                <tr><td><strong>Gini Coefficient</strong></td><td>The most common metric, ranging from 0 (perfect equality) to 1 (perfect inequality). It measures the dispersion of income distribution.</td></tr>
                <tr><td><strong>Decile Ratios</strong></td><td>Compares the income of the richest 10% of the population to the poorest 10%. A high ratio indicates significant disparity.</td></tr>
                <tr><td><strong>Headcount Ratio</strong></td><td>The percentage of a country's population living below the established Poverty Line. It measures the prevalence of poverty.</td></tr>
                <tr><td><strong>Poverty Gap Index</strong></td><td>Measures the intensity of poverty by calculating the average distance of the poor's income from the poverty line.</td></tr>
                <tr><td><strong>PPP (Purchasing Power Parity)</strong></td><td>An economic theory used to adjust income figures across countries, accounting for differences in the cost of living for accurate comparison.</td></tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------
# ABOUT PAGE
# ------------------------------------------------------------------------------------------
elif selected_page == "About":
    
    st.header("About This Project")
    st.divider()

    st.markdown("""
        <div class="card">
            <h3>Subhomoy Halder</h3>
            <h5>Part of the Infosys Springboard Data Visualization Internship</h5>
            <p>This dashboard is a demonstration of data visualization and web application development skills. It leverages <strong>Power BI</strong> for in-depth data analysis and <strong>Streamlit</strong> to create a fully interactive and user-friendly web interface.</p>
            <p>The goal of this project is to make complex data on global income inequality accessible and understandable to a broader audience.</p>
            <p>🔗 <strong>Connect with me:</strong> <a href="#">LinkedIn</a> | <a href="#">GitHub</a></p>
        </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------
# DASHBOARD PAGE
# ------------------------------------------------------------------------------------------
elif selected_page == "Dashboard":
    
    st.markdown("""
        <div class="card">
            <h3>Interactive Power BI Report</h3>
            <p>Interact with the visuals below to explore the data. Use the filters within the dashboard for a granular analysis. Full-screen mode is recommended for the best experience.</p>
        </div>
    """, unsafe_allow_html=True)

    power_bi_iframe = """
        <iframe title="Dashboard 3" width="100%" height="700" src="https://app.powerbi.com/view?r=eyJrIjoiYTc1NWU0MTItMGRhZS00YjY5LWJjNWMtMjc0OWQyOTdiNWJjIiwidCI6ImNlYjVhMDZjLTY2ZjEtNGE3NC1iZDExLTVmZDEwNTQwYTVlYSJ9&pageName=8650f3g3bcc395c7c66c" frameborder="0" allowFullScreen="true" style="border-radius: 10px; margin-top: 10px;"></iframe>
    """
    
    components.html(power_bi_iframe, height=720)
