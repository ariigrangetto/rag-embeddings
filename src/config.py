import os
from dotenv import load_dotenv

load_dotenv();


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Faltan las credenciales de Supabase en el archivo .env")

if not GEMINI_API_KEY:
    raise ValueError("Faltan GEMINI_API_KEY en el archivo .env")
