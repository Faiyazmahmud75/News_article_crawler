from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.Supabae_Url
SUPABASE_KEY = os.Supabase_Key

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
