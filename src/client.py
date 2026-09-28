from supabase import create_client, Client
from google import genai
from src.config import SUPABASE_URL, SUPABASE_KEY, GEMINI_API_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
gemini_client = genai.Client(api_key=GEMINI_API_KEY);

