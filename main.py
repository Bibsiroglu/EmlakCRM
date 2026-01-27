import flet as ft



def main(page: ft.Page):
    page.title = 'Emlak CRM v1.0'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)