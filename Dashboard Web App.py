import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dashboard Streamlit",
    page_icon="📊",
    layout="wide"
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def set_page(page_name):
    st.session_state.page = page_name

if st.session_state.page == 'home':
    st.title("Global Income Inequality Dashboard")
    st.markdown("### Navigate using the buttons below")

    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "Candidate Profile",
            on_click=set_page,
            args=('profile',),
            use_container_width=True
        )

    with col2:
        st.button(
            "View Dashboard",
            on_click=set_page,
            args=('dashboard',),
            use_container_width=True
        )

elif st.session_state.page == 'profile':
    st.header("Global Income Inequality Dashboard")
    
    st.markdown("#### by **Subhomoy Halder**") 
    
    st.markdown("##### Part of the Infosys Springboard Data Visualization Internship")

    st.divider()

    st.button(
        "View Dashboard",
        on_click=set_page,
        args=('dashboard',),
        use_container_width=True
    )

elif st.session_state.page == 'dashboard':
    
    power_bi_iframe = """
        <iframe title="Dashboard 3" width="100%" height="755" src="https://app.powerbi.com/view?r=eyJrIjoiYTc1NWU0MTItMGRhZS00YjY5LWJjNWMtMjc0OWQyOTdiNWJjIiwidCI6ImNlYjVhMDZjLTY2ZjEtNGE3NC1iZDExLTVmZDEwNTQwYTVlYSJ9&pageName=8650f3g3bcc395c7c66c" frameborder="0" allowFullScreen="true"></iframe>
    """
    
    components.html(power_bi_iframe, height=700)

    st.button(
        "Go To Home Page",
        on_click=set_page,
        args=('home',),
        use_container_width=True
    )