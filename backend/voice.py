import tempfile
import os


def text_to_speech(text):
    if text is None or text.strip() == "":
        return None

    try:
        from gtts import gTTS
    except ImportError as exc:
        raise ImportError(
            "The gTTS package is required for backend.voice. "
            "Install it with pip install gtts"
        ) from exc

    tts = gTTS(
        text=text,
        lang="en"
    )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts.save(temp_file.name)

    return temp_file.name
