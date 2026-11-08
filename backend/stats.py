import streamlit as st
from backend.user_db import (
    get_user_stats, save_user_stats, get_user_history, 
    save_user_history, add_to_history, clear_user_history
)


def get_current_user():
    """Get current logged-in user."""
    if "username" not in st.session_state or not st.session_state.logged_in:
        return None
    return st.session_state.username


def add_question():
    """Add question to user's stats."""
    username = get_current_user()
    if not username:
        return
    
    stats = get_user_stats(username)
    stats["questions"] += 1
    save_user_stats(username, stats)
    print("Question Added:", stats)


def add_quiz(score):
    """Add quiz to user's stats."""
    username = get_current_user()
    if not username:
        return
    
    stats = get_user_stats(username)
    stats["quizzes"] += 1
    score = round(score)
    
    if score > stats["best_score"]:
        stats["best_score"] = score
    
    save_user_stats(username, stats)
    print("Quiz Added:", stats)


def add_flashcards():
    """Add flashcards to user's stats."""
    username = get_current_user()
    if not username:
        return
    
    stats = get_user_stats(username)
    stats["flashcards"] += 1
    save_user_stats(username, stats)
    print("Flashcards Added:", stats)


def add_notes():
    """Add notes to user's stats."""
    username = get_current_user()
    if not username:
        return
    
    stats = get_user_stats(username)
    stats["notes"] += 1
    save_user_stats(username, stats)
    print("Notes Added:", stats)


def add_study_plan():
    """Add study plan to user's stats."""
    username = get_current_user()
    if not username:
        return
    
    stats = get_user_stats(username)
    stats["study_plans"] += 1
    save_user_stats(username, stats)
    print("Study Plan Added:", stats)


def add_summary():
    """Add summary to user's stats."""
    username = get_current_user()
    if not username:
        return
    
    stats = get_user_stats(username)
    stats["summaries"] += 1
    save_user_stats(username, stats)
    print("Summary Added:", stats)


def add_voice_assignment(score=0):
    """Add voice assignment to user's stats."""
    username = get_current_user()
    if not username:
        return
    
    stats = get_user_stats(username)
    stats["voice_assignments"] += 1
    score = round(score)
    
    if score > stats["best_voice_score"]:
        stats["best_voice_score"] = score
    
    stats["voice_total_score"] += score
    save_user_stats(username, stats)
    print("Voice Assignment Added:", stats)


def get_stats():
    """Get user's statistics."""
    username = get_current_user()
    if not username:
        return {
            "questions": 0,
            "quizzes": 0,
            "flashcards": 0,
            "notes": 0,
            "study_plans": 0,
            "voice_assignments": 0,
            "summaries": 0,
            "best_score": 0,
            "best_voice_score": 0,
            "voice_total_score": 0
        }
    
    return get_user_stats(username)


def add_history(question, answer):
    """Add to user's chat history."""
    username = get_current_user()
    if not username:
        return
    
    add_to_history(username, question, answer)


def get_history():
    """Get user's chat history."""
    username = get_current_user()
    if not username:
        return []
    
    return get_user_history(username)


def clear_history():
    """Clear user's chat history."""
    username = get_current_user()
    if not username:
        return
    
    clear_user_history(username)
