from core.database import db_client

class AuthService:
    @staticmethod
    def login(email, password):
        try:
            # Supabase'e giriş isteği gönder
            res = db_client.auth.sign_in_with_password({"email": email, "password": password})
            # Başarılı ise kullanıcı objesini ve başarı mesajını dön
            return {"success": True, "user": res.user, "message": "Giriş başarılı!"}
        except Exception as e:
            # Hata varsa (örn: yanlış şifre), güvenli bir mesaj dön
            return {"success": False, "message": "Giriş başarısız. Bilgileri kontrol edin."}

    @staticmethod
    def register(email, password):
        try:
            # Supabase'e kayıt isteği gönder
            res = db_client.auth.sign_up({"email": email, "password": password})
            # Otomatik giriş yapmış sayılır, ancak biz mesaj dönelim
            return {"success": True, "message": "Kayıt başarılı! Şimdi giriş yapabilirsiniz."}
        except Exception as e:
            return {"success": False, "message": f"Kayıt hatası: {str(e)}"}

    @staticmethod
    def logout():
        db_client.auth.sign_out()