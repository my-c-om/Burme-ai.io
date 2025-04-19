# server/config/gemini_config.py
from google.generativeai import configure

def init_gemini(api_key: str):
    configure(api_key=api_key)
