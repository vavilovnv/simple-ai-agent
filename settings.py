import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    LLM_NAME: str = os.getenv("LLM_NAME", "unknown LLM")
    LANGUAGE: str = os.getenv("ANSWER_LANGUAGE", "English")

settings = Settings()
