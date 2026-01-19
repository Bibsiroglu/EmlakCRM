import flet as ft
# Henüz oluşturmadığımız view'leri import edeceğiz, şimdilik hata verirse aldırma
# View dosyalarını birazdan oluşturacağız.

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        # body: Tüm sayfaların içine yükleneceği ana kutu
        self.body = ft.Container(expand=True)

    def go(self, route_name):
        # Önce mevcut sahneyi temizle
        self.body.content = None
        
        # Importları fonksiyon içine yazıyoruz ki "Döngüsel Import" hatası olmasın
        from views.login_view import LoginView
        from views.dashboard_view import DashboardView

        if route_name == "login":
            # LoginView'e diyoruz ki: "Giriş başarılı olursa router'ın 'dashboard' rotasına git"
            self.body.content = LoginView(self.page, on_success=lambda: self.go("dashboard"))
            
        elif route_name == "dashboard":
            # Dashboard'a diyoruz ki: "Çıkış yapılırsa router'ın 'login' rotasına git"
            self.body.content = DashboardView(self.page, on_logout=lambda: self.go("login"))

        self.body.update()

    def get_content(self):
        return self.body