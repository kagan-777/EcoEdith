import os

OPENROUTER_API_KEY_ENV = "OPENROUTER_API_KEY"

if os.path.exists(".env"):
    try:
        from dotenv import load_dotenv
    except ImportError:
        load_dotenv = None
    if load_dotenv:
        load_dotenv()


def get_api_key():
    api_key = os.getenv(OPENROUTER_API_KEY_ENV)
    if not api_key:
        raise EnvironmentError(
            f"{OPENROUTER_API_KEY_ENV} environment variable is required. "
            "Set it in .env or the system environment."
        )
    return api_key


def get_openai_client():
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ImportError(
            "The openai package is required for backend.gemini. "
            "Install it with pip install openai"
        ) from exc

    return OpenAI(
        api_key=get_api_key(),
        base_url="https://openrouter.ai/api/v1"
    )


def ask_gemini(prompt):

    try:

        client = get_openai_client()

        response = client.chat.completions.create(

            model="google/gemini-2.5-flash",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,
            max_tokens=4096

        )

        answer = response.choices[0].message.content

        if answer is None:
            return ""

        return answer.strip()

    except Exception as e:

        return f"Error: {e}"