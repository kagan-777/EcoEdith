import json
import os

USER_DATA_DIR = "user_data"


def _get_user_dir(username):
    """Get the directory path for a user."""
    return os.path.join(USER_DATA_DIR, username.lower())


def _ensure_user_dir(username):
    """Create user directory if it doesn't exist."""
    user_dir = _get_user_dir(username)
    os.makedirs(user_dir, exist_ok=True)
    return user_dir


def _get_file_path(username, filename):
    """Get full path to user's file."""
    user_dir = _ensure_user_dir(username)
    return os.path.join(user_dir, filename)


def get_user_stats(username):
    """Get user's statistics."""
    file_path = _get_file_path(username, "stats.json")
    
    if not os.path.exists(file_path):
        default_stats = {
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
        with open(file_path, "w") as f:
            json.dump(default_stats, f, indent=4)
        return default_stats
    
    with open(file_path, "r") as f:
        return json.load(f)


def save_user_stats(username, stats):
    """Save user's statistics."""
    file_path = _get_file_path(username, "stats.json")
    with open(file_path, "w") as f:
        json.dump(stats, f, indent=4)


def get_user_history(username):
    """Get user's chat history."""
    file_path = _get_file_path(username, "history.json")
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f, indent=4)
        return []
    
    with open(file_path, "r") as f:
        return json.load(f)


def save_user_history(username, history):
    """Save user's chat history."""
    file_path = _get_file_path(username, "history.json")
    with open(file_path, "w") as f:
        json.dump(history, f, indent=4)


def add_to_history(username, question, answer):
    """Add to user's chat history."""
    from datetime import datetime
    history = get_user_history(username)
    history.insert(0, {
        "time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "question": question,
        "answer": answer
    })
    save_user_history(username, history)


def clear_user_history(username):
    """Clear user's chat history."""
    save_user_history(username, [])


def get_user_full_text(username):
    """Get user's full text file."""
    file_path = _get_file_path(username, "full_text.txt")
    
    if not os.path.exists(file_path):
        return ""
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def save_user_full_text(username, content):
    """Save user's full text file."""
    file_path = _get_file_path(username, "full_text.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def get_user_chroma_path(username):
    """Get user's ChromaDB path."""
    user_dir = _ensure_user_dir(username)
    chroma_path = os.path.join(user_dir, "chroma_db")
    os.makedirs(chroma_path, exist_ok=True)
    return chroma_path
