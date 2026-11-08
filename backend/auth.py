import json
import os
import hashlib
from datetime import datetime

USERS_FILE = "users.json"


def _hash_password(password):
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def initialize_users():
    """Create users.json if it doesn't exist."""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f, indent=4)


def load_users():
    """Load all users from file."""
    initialize_users()
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    """Save users to file."""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def user_exists(username):
    """Check if user already exists."""
    users = load_users()
    return username.lower() in users


def register_user(username, password, email):
    """Register a new user."""
    username = username.lower().strip()
    
    if user_exists(username):
        return False, "User already exists"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    
    users = load_users()
    users[username] = {
        "password": _hash_password(password),
        "email": email,
        "created_at": datetime.now().isoformat(),
        "last_login": None
    }
    save_users(users)
    return True, "User registered successfully"


def login_user(username, password):
    """Authenticate user login."""
    username = username.lower().strip()
    users = load_users()
    
    if username not in users:
        return False, "Invalid username or password"
    
    user = users[username]
    if user["password"] != _hash_password(password):
        return False, "Invalid username or password"
    
    # Update last login
    user["last_login"] = datetime.now().isoformat()
    save_users(users)
    
    return True, "Login successful"


def get_user_info(username):
    """Get user information."""
    users = load_users()
    username = username.lower().strip()
    
    if username not in users:
        return None
    
    user = users[username]
    return {
        "username": username,
        "email": user.get("email", ""),
        "created_at": user.get("created_at", ""),
        "last_login": user.get("last_login", "")
    }
