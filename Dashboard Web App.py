import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore
import streamlit.components.v1 as components
from contextlib import contextmanager
import base64 # We need this library to encode the image
import os # To check for file existence

# --- Firebase Initialization ---
# This should only run once. We use a try-except block to prevent re-initialization
# on every script rerun, which Streamlit does.
try:
    # IMPORTANT: Create a file named 'serviceAccountKey.json' in the same directory
    # with your Firebase service account credentials.
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
except ValueError:
    # If the app is already initialized, do nothing.
    pass

db = firestore.client()

# --- Helper Functions ---

def get_image_as_base64(file_path):
    """Reads an image file and returns its base64 encoded string."""
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_page_style():
    """Applies custom CSS for the enhanced dashboard UI with the new background."""
    
    # --- Background Image Setup ---
    # The image is now loaded from a local file and encoded.
    # IMPORTANT: You must download the image and save it as 'background.jpg' in the same folder.
    image_file = 'background.jpg'
    
    if os.path.exists(image_file):
        bg_image_base64 = get_image_as_base64(image_file)
        background_css = f"""
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(data:image/jpeg;base64,{bg_image_base64});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        """
    else:
        # Fallback to a solid color if the image file is not found
        background_css = "background-color: #0C0F16;"


    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

        /* --- Custom Variables (LA Palm Tree Theme) --- */
        :root {{
            --primary-color: #00A896; /* Deep Teal */
            --secondary-color: #FFC300; /* Warm Gold */
            --background-color-transparent: rgba(12, 15, 22, 0.9); /* Dark, semi-transparent */
            --text-color: #F0F2F6;
            --subtle-text-color: #B0B0B0;
            --border-color: rgba(40, 48, 61, 0.8);
        }}

        /* --- General Theme --- */
        body {{
            font-family: 'Montserrat', sans-serif;
        }}
        
        .stApp {{
            {background_css}
            color: var(--text-color);
        }}

        /* Reduce top padding of the main block container in Streamlit */
        .main > div.block-container {{
            padding-top: 2rem;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            color: var(--text-color);
            font-weight: 600;
        }}
        .stMarkdown {{
            color: var(--subtle-text-color);
        }}
        [data-testid="stExpander"] {{
            border-color: var(--border-color);
            background-color: var(--background-color-transparent);
            border-radius: 10px;
        }}

        /* --- Login Page --- */
        .login-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start; /* Aligns content to the top */
            padding-top: 5rem; /* Adds space from the top */
        }}
        .login-container .stForm {{
            background-color: var(--background-color-transparent);
            padding: 2.5rem;
            border-radius: 15px;
            width: 450px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border: 1px solid var(--border-color);
            backdrop-filter: blur(8px);
        }}
        .login-container .stButton>button {{
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 0;
            font-weight: 600;
        }}
        
        /* --- Main Content Area --- */
        .main-content-wrapper {{
            background-color: var(--background-color-transparent);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid var(--border-color);
            backdrop-filter: blur(8px);
        }}

        /* --- Sidebar --- */
        [data-testid="stSidebar"] {{
            background-color: var(--background-color-transparent);
            border-right: 1px solid var(--border-color);
            backdrop-filter: blur(10px);
        }}
        [data-testid="stSidebar"] .stButton>button {{
            width: 100%;
            border-radius: 8px;
            border: 1px solid var(--primary-color);
            background-color: transparent;
            color: var(--primary-color);
        }}
        [data-testid="stSidebar"] .stButton>button:hover {{
            background-color: var(--primary-color);
            color: white;
        }}

        /* --- Navigation Bar --- */
        div[data-testid="stHorizontalBlock"] {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1rem;
            padding: 0.5rem 0;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 1rem;
        }}

        /* Style for the buttons in the navbar */
        div[data-testid="stHorizontalBlock"] button {{
            background-color: transparent;
            border: none;
            color: var(--subtle-text-color);
            font-size: 1rem;
            font-weight: 400;
            padding: 10px 15px;
            margin: 0;
            border-radius: 8px;
            transition: all 0.2s ease-in-out;
        }}
        div[data-testid="stHorizontalBlock"] button:hover {{
            background-color: rgba(40, 48, 61, 0.7);
            color: var(--text-color);
        }}
        div[data-testid="stHorizontalBlock"] button:focus {{
            box-shadow: none !important;
            outline: none !important;
        }}

        /* Style for the active page text in the navbar */
        .nav-item-active {{
            text-align: center;
            font-size: 1rem;
            color: white;
            font-weight: 600;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            padding: 10px 15px;
            border-radius: 8px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

@contextmanager
def main_content_wrapper():
    """Context manager to wrap page content in a styled div for a card effect."""
    st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)
    try:
        yield
    finally:
        st.markdown('</div>', unsafe_allow_html=True)


def is_admin(uid):
    """Checks if a user has the 'admin' role in Firestore."""
    user_ref = db.collection('users').document(uid)
    user_doc = user_ref.get()
    if user_doc.exists:
        return user_doc.to_dict().get('role') == 'admin'
    return False

# --- Page Functions ---

def login_page():
    """Displays the login and sign-up forms with improved UI."""
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    if 'auth_form' not in st.session_state:
        st.session_state.auth_form = 'Login'
    
    # Display the selected form
    if st.session_state.auth_form == 'Login':
        st.title("Welcome Back")
        st.markdown("Sign in to access your dashboard.")
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="you@example.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("Sign In")
            if submit:
                try:
                    user = auth.get_user_by_email(email)
                    st.session_state['logged_in'] = True
                    st.session_state['user_info'] = {'uid': user.uid, 'email': user.email}
                    st.session_state['is_admin'] = is_admin(user.uid)
                    st.rerun()
                except Exception as e:
                    st.error(f"Login failed: Invalid credentials or user not found.")
        
        if st.button("Don't have an account? Sign Up", key="signup_switch"):
            st.session_state.auth_form = 'Signup'
            st.rerun()

    else: # Signup
        st.title("Create an Account")
        st.markdown("Get started by creating a new account.")
        with st.form("signup_form"):
            email = st.text_input("Email", placeholder="you@example.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("Create Account")
            if submit:
                try:
                    users_ref = db.collection('users')
                    docs = users_ref.stream()
                    is_first_user = not any(True for _ in docs)
                    new_user = auth.create_user(email=email, password=password)
                    user_data = {'email': new_user.email, 'role': 'admin' if is_first_user else 'user'}
                    db.collection('users').document(new_user.uid).set(user_data)
                    st.success("Account created successfully! Please sign in.")
                    st.session_state.auth_form = 'Login' # Switch back to login form
                    st.rerun()
                except Exception as e:
                    st.error(f"Could not create account: {e}")
        
        if st.button("Already have an account? Sign In", key="login_switch"):
            st.session_state.auth_form = 'Login'
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


def home_page():
    with main_content_wrapper():
        st.title("Inequality in Income Across the Globe")
        st.markdown("""
            ### Why This Matters
            Understanding global income inequality is crucial for fostering stable, prosperous, and just societies. 
            Extreme disparities can hinder economic growth, fuel social unrest, and limit opportunities for millions, 
            preventing them from reaching their full potential. By analyzing the distribution of wealth, we can identify 
            vulnerable populations, advocate for more equitable policies, and work towards a world where everyone has 
            a fair chance to succeed.
        """)
        st.markdown("---")
        st.header("Metrics Used")
        st.info("""
            This dashboard uses various metrics to provide a comprehensive view of income distribution, from poverty indicators like the Headcount and Poverty Gap to inequality measures such as the Gini Index.
        """)
        with st.expander("See all metrics"):
            st.markdown("""
            - **Headcount, Poverty Gap, Poverty Severity, Watts Index:** Measure different dimensions of poverty.
            - **Mean, Median:** Basic measures of central tendency for income.
            - **Mean Log Deviation, Gini Index, Polarization:** Advanced metrics for inequality.
            - **Decile 1-10:** Income shares held by different tenths of the population.
            - **CPI, PPP, PCE:** Economic indicators for price levels and consumption.
            - **Regional Poverty Line/Rate:** Poverty measures specific to a region.
            """)

def about_page():
    with main_content_wrapper():
        st.title("About This Project")
        st.markdown("""
            Hi, I'm **[Your Name]**. This dashboard is a key component of my project for the 
            Infosys Springboard Data Visualization Internship.

            The goal was to transform a complex dataset on global income inequality into an 
            interactive, accessible, and insightful visual story. Through this dashboard, I aimed to 
            hone my skills in data analysis, visualization with Power BI, and web application development.

            **Connect with me:**
            - **LinkedIn:** [Your LinkedIn Profile URL](https://www.linkedin.com/in/your-profile/)
        """)

def dashboard_page():
    with main_content_wrapper():
        st.title("Interactive Dashboard")
        st.markdown("Explore the data using the embedded Power BI dashboard below.")
        embed_code = """<iframe title="Dashboard 3" width="100%" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiYTc1NWU0MTItMGRhZS00YjY5LWJjNWMtMjc0OWQyOTdiNWJjIiwidCI6ImNlYjVhMDZjLTY2ZjEtNGE3NC1iZDExLTVmZDEwNTQwYTVlYSJ9" frameborder="0" allowFullScreen="true"></iframe>"""
        components.html(embed_code, height=612, scrolling=False)


def feedback_page():
    with main_content_wrapper():
        st.title("Feedback Form")
        st.markdown("Your feedback is valuable to us. Please share your thoughts.")
        
        with st.form("feedback_form", clear_on_submit=True):
            name = st.text_input("Name", max_chars=50)
            email = st.text_input("Email", value=st.session_state.get('user_info', {}).get('email', ''), disabled=True)
            feedback_text = st.text_area("Your Feedback", height=150)
            submitted = st.form_submit_button("Submit Feedback")
            
            if submitted:
                if not name or not feedback_text:
                    st.warning("Please fill out all fields.")
                else:
                    try:
                        feedback_data = {
                            'name': name, 'email': email, 'feedback': feedback_text,
                            'timestamp': firestore.SERVER_TIMESTAMP
                        }
                        db.collection('feedbacks').add(feedback_data)
                        st.success("Thank you for your feedback!")
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

def admin_page():
    with main_content_wrapper():
        st.title("Admin Panel: View Feedbacks")
        try:
            feedbacks_ref = db.collection('feedbacks').order_by('timestamp', direction=firestore.Query.DESCENDING).stream()
            feedbacks = []
            for feedback in feedbacks_ref:
                data = feedback.to_dict()
                feedbacks.append({
                    "Name": data.get("name"), "Email": data.get("email"), "Feedback": data.get("feedback"),
                    "Timestamp": data.get("timestamp").strftime('%Y-%m-%d %H:%M:%S') if data.get('timestamp') else 'N/A'
                })
            if feedbacks:
                st.dataframe(feedbacks, use_container_width=True)
            else:
                st.info("No feedbacks submitted yet.")
        except Exception as e:
            st.error(f"Failed to fetch feedbacks: {e}")

# --- Main App Logic ---

def main():
    st.set_page_config(layout="wide") # Use wide layout for a dashboard feel
    set_page_style()

    # Apply custom styling to the auth switch buttons after they are created
    st.markdown("""
        <style>
            [data-testid="stButton-secondary"] {
                background-color: transparent !important;
                color: var(--primary-color) !important;
                border: none !important;
                text-align: center;
                width: 100%;
                margin-top: 1rem;
            }
            [data-testid="stButton-secondary"]:hover {
                text-decoration: underline;
                border: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
    if 'is_admin' not in st.session_state: st.session_state['is_admin'] = False
    if 'page' not in st.session_state: st.session_state['page'] = "Home"

    # Show login page if not logged in
    if not st.session_state['logged_in']:
        login_page()
    else:
        # --- Sidebar for User Info and Logout ---
        user_email = st.session_state.get('user_info', {}).get('email', 'User')
        st.sidebar.header(f"Welcome,")
        st.sidebar.write(user_email)
        st.sidebar.divider()
        if st.sidebar.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['user_info'] = {}
            st.session_state['is_admin'] = False
            st.session_state['page'] = "Home"
            st.rerun()

        # --- Top Navigation Bar ---
        # Reordered pages as requested
        pages = {"Home": home_page, "About": about_page, "Dashboard": dashboard_page, "Feedback": feedback_page}
        if st.session_state.get('is_admin', False):
            pages["Admin Page"] = admin_page
        
        page_items = list(pages.keys())
        # Create enough columns for the pages
        cols = st.columns(len(page_items))

        for i, page_name in enumerate(page_items):
            with cols[i]:
                if page_name == st.session_state.page:
                    st.markdown(f'<p class="nav-item-active">{page_name}</p>', unsafe_allow_html=True)
                else:
                    if st.button(page_name, key=f"nav_{page_name}", use_container_width=True):
                        st.session_state.page = page_name
                        st.rerun()
        
        # Display the selected page
        pages[st.session_state.page]()

if __name__ == "__main__":
    main()

