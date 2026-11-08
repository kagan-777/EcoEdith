
import streamlit as st
from backend.user_db import (
    get_user_history,
    add_to_history,
    clear_user_history
)


def get_current_user():
    """Get current logged-in user."""
    if not st.session_state.get("logged_in", False):
        return None

    return st.session_state.get("username")


def add_to_chat_history(question, answer):
    """Add chat to the current user's history."""
    username = get_current_user()

    if not username:
        return

    add_to_history(username, question, answer)


def add_history(*args):
    """
    Compatibility function for existing project imports.

    Supports:
    add_history(question, answer)
    add_history(category, question, answer)
    """
    if len(args) == 2:
        question, answer = args

    elif len(args) == 3:
        category, question, answer = args

    else:
        raise TypeError(
            "add_history expects 2 or 3 arguments"
        )

    add_to_chat_history(question, answer)


def get_chat_history():
    """Get current user's chat history."""
    username = get_current_user()

    if not username:
        return []

    return get_user_history(username)


def clear_chat_history():
    """Clear current user's chat history."""
    username = get_current_user()

    if not username:
        return

    clear_user_history(username)
