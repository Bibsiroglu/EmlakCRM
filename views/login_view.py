import flet as ft
from services.auth_service import AuthService

class LoginView(ft.Container):
    def __init__(self, page: ft.Page, on_success):
        super().__init__()
        self.page = page
        self.on_success = on_success # Başarı durumunda çalışacak fonksiyon (Router'dan gelir)
        self.expand = True
        self.alignment = ft.alignment.center
        self.bgcolor = ft.colors.BLUE_GREY_50

        # Form Elemanları
        self.email_input = ft.TextField(label="E-posta", width=300, border_radius=10)
        self.pass_input = ft.TextField(label="Şifre", password=True, can_reveal_password=True, width=300, border_radius=10)

        self.content = ft.Column(
            [
                ft.Icon(ft.icons.SECURITY, size=80, color="blue"),
                ft.Text("Emlak CRM", size=30, weight="bold"),
                ft.Text("Yönetici Girişi", color="grey"),
                ft.Container(height=20),
                self.email_input,
                self.pass_input,
                ft.Container(height=10),
                ft.ElevatedButton("Giriş Yap", on_click=self.handle_login, width=300, height=45),
                ft.OutlinedButton("Kayıt Ol", on_click=self.handle_register, width=300)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def handle_login(self, e):
        # Servise emir ver
        result = AuthService.login(self.email_input.value, self.pass_input.value)
        
        if result["success"]:
            # Başarılıysa ID'yi oturuma kaydet
            self.page.session.set("user_id", result["user"].id)
            self.show_snack(result["message"], "green")
            # Router'ın verdiği on_success fonksiyonunu çalıştır (Bizi Dashboard'a atar)
            self.on_success()
        else:
            self.show_snack(result["message"], "red")

    def handle_register(self, e):
        result = AuthService.register(self.email_input.value, self.pass_input.value)
        color = "green" if result["success"] else "red"
        self.show_snack(result["message"], color)

    def show_snack(self, msg, color):
        self.page.snack_bar = ft.SnackBar(ft.Text(msg), bgcolor=color)
        self.page.snack_bar.open = True
        self.page.update()