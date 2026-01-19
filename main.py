import flet as ft

from core.navigation import Router

def main(page: ft.Page):
    page.title = 'Emlak CRM v1.0'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    app_router = Router(page)
    page.add(app_router.get_content())
    app_router.go('login')

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)