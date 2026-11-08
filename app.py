import streamlit as st
from backend.auth import login_user, register_user, get_user_info

st.set_page_config(
    page_title="EcoEdith",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None


def logout():
    """Handle logout."""
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()


def show_login_page():
    """Display login/register page."""
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("## 🔐 Login")
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submit = st.form_submit_button("🔓 Login")
            
            if submit:
                if username.strip() and password.strip():
                    success, message = login_user(username, password)
                    if success:
                        st.session_state.logged_in = True
                        st.session_state.username = username.lower()
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter username and password")
    
    with col2:
        st.markdown("## 📝 Register")
        with st.form("register_form"):
            new_username = st.text_input("Username", placeholder="Choose a username", key="reg_user")
            email = st.text_input("Email", placeholder="your@email.com", key="reg_email")
            new_password = st.text_input("Password", type="password", placeholder="At least 6 characters", key="reg_pass")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm password", key="reg_confirm")
            register_btn = st.form_submit_button("✅ Register")
            
            if register_btn:
                if not new_username.strip() or not email.strip() or not new_password.strip():
                    st.warning("Please fill all fields")
                elif new_password != confirm_password:
                    st.error("Passwords don't match")
                else:
                    success, message = register_user(new_username, new_password, email)
                    if success:
                        st.success(message)
                        st.info("Now you can login with your credentials!")
                    else:
                        st.error(message)


def show_main_page():
    """Display main app page."""
    # Sidebar with user info and logout
    with st.sidebar:
        st.markdown("---")
        user_info = get_user_info(st.session_state.username)
        
        st.markdown(f"### 👤 {user_info['username'].upper()}")
        st.caption(f"📧 {user_info['email']}")
        
        if st.button("🚪 Logout", key="logout_btn", use_container_width=True):
            logout()
        
        st.markdown("---")
    
    # Main content
    st.title("🎓 EcoEdith")
    st.caption("Your AI-Powered Multimodal Learning Assistant")
    
    st.divider()
    
    st.header("📚 Learn Smarter with AI")
    
    st.write("""
EcoEdith helps students understand concepts from their own study materials.

✅ Upload Notes

✅ Ask Questions

✅ Learn with AI

✅ Voice & Text Support

✅ Visual Learning
""")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💬 Chat with AI", use_container_width=True):
            st.switch_page("pages/chat.py")
    
    with col2:
        if st.button("📄 Upload Materials", use_container_width=True):
            st.switch_page("pages/upload.py")
    
    with col3:
        if st.button("📊 Analytics", use_container_width=True):
            st.switch_page("pages/analytics.py")


# Main logic
if st.session_state.logged_in:
    show_main_page()
else:
    show_login_page()
