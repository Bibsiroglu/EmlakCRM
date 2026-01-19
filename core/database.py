import os
from supabase import create_client, Client
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")

if not url or not key:
    print("⚠️ HATA: .env dosyasında Supabase bilgileri eksik!")

# Bağlantıyı oluştur ve dışarıya aç
db_client: Client = create_client(url, key)