import flet as ft

class DashboardView(ft.Container):
    def __init__(self, page: ft.Page, on_logout):
        super().__init__()
        self.on_logout = on_logout
        self.expand = True
        self.alignment = ft.Alignment(0, 0)
        
        # Kullanıcı ID'sini görmek için alalım
        user_id = page.session.get("user_id")

        self.content = ft.Column(
            [
                ft.Icon(ft.icons.VERIFIED_USER, size=60, color="green"),
                ft.Text("Hoşgeldiniz!", size=30, weight="bold"),
                ft.Text(f"Kullanıcı ID: {user_id}", size=12, color="grey"),
                ft.Container(height=20),
                ft.ElevatedButton("Çıkış Yap", on_click=self.cikis_yap, bgcolor="red", color="white")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def cikis_yap(self, e):
        # Servisten çıkış yap (Authentication açısından)
        from services.auth_service import AuthService
        AuthService.logout()
        
        # Router'ın verdiği on_logout fonksiyonunu çalıştır (Bizi Login'e atar)
        self.on_logout()