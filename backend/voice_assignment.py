import tempfile
import os

_whisper_model = None


def _load_whisper_model():
    global _whisper_model
    if _whisper_model is None:
        try:
            import whisper
        except ImportError as exc:
            raise ImportError(
                "The openai-whisper package is required for backend.voice_assignment. "
                "Install it with pip install -U openai-whisper"
            ) from exc

        _whisper_model = whisper.load_model("base")

    return _whisper_model


def speech_to_text(audio_bytes):
    """
    Convert recorded audio into text using Whisper.
    """

    if not audio_bytes:
        return ""

    temp_path = None

    try:
        # Save recorded audio temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio_bytes)
            temp_path = temp_audio.name

        model = _load_whisper_model()

        # Convert Speech → Text
        result = model.transcribe(
            temp_path,
            fp16=False
        )

        return result.get("text", "").strip()

    except Exception as e:

        return f"Error: {str(e)}"

    finally:

        # Delete temporary file
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)