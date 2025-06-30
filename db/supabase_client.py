from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("Supabase_Url")
SUPABASE_KEY = os.getenv("Supabase_Key")

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
