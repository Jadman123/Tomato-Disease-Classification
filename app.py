import streamlit as st
import pandas as pd


# Configure Streamlit page
st.set_page_config(page_title="Tomato Disease Classification", layout="centered")


# Users data for the login
users = {
    "admin": {"password": "admin", "role": "Admin"},
    "farmer1": {"password": "farmerpass", "role": "Farmer"},
}

# Initialize session state for login
if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False
    st.session_state["role"] = None

# Login logic
if not st.session_state["is_logged_in"]:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)  # Open login box

    st.title("Welcome Farmers")
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", placeholder="Enter your password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state["is_logged_in"] = True
            st.session_state["role"] = users[username]["role"]
            st.success(f"Welcome, {username}! Redirecting to your dashboard...")
            st.rerun()  # This will refresh the page after a successful login
        else:
            st.error("Invalid username or password.")

    st.markdown('</div>', unsafe_allow_html=True)  # Close login box

# Admin Page
if st.session_state["is_logged_in"] and st.session_state["role"] == "Admin":
    st.title("Admin Dashboard")

    # Logout button at the top-right corner
    if st.button("Logout", key="logout", help="Click to log out", use_container_width=False):
        # Clear session state to log out
        st.session_state["is_logged_in"] = False
        st.session_state["role"] = None
        st.success("You have logged out. Redirecting to the login page...")
        st.rerun()

    # Tabs for the admin dashboard
    tab1, tab2, tab3 = st.tabs(["Predicted Table", "History Table", "Add Farmer"])

    # Predicted Table
    with tab1:
        st.header("Predicted Table")
        predicted_data = pd.DataFrame(
            {
                "ID": [1, 2, 3],
                "Farmer Name": ["John Doe", "Jane Smith", "Alex Brown"],
                "Prediction": ["Healthy", "Diseased", "Diseased"],
                "Confidence (%)": [95, 80, 87],
            }
        )
        st.dataframe(predicted_data, use_container_width=True)

    # History Table
    with tab2:
        st.header("History Table")
        history_data = pd.DataFrame(
            {
                "Date": ["2024-11-27", "2024-11-26", "2024-11-25"],
                "Farmer Name": ["John Doe", "Jane Smith", "Alex Brown"],
                "Action": ["Submitted a sample", "Reviewed prediction", "Added a new crop"],
            }
        )
        st.dataframe(history_data, use_container_width=True)

    # Add Farmer
    with tab3:
        st.header("Add Farmer")
        with st.form("add_farmer_form"):
            farmer_name = st.text_input("Farmer Name", placeholder="Enter the farmer's name")
            farmer_username = st.text_input("Username", placeholder="Enter a unique username")
            farmer_password = st.text_input("Password", placeholder="Enter a secure password", type="password")

            submitted = st.form_submit_button("Add Farmer")
            if submitted:
                if farmer_name and farmer_username and farmer_password:
                    st.success(f"Farmer '{farmer_name}' added successfully!")
                else:
                    st.error("All fields are required!") 
