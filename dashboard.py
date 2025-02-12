import flet as ft

def dashboard(page: ft.Page):
    page.title = "Dashboard"
    page.add(ft.Text("Welcome to the Dashboard!", size=24, weight=ft.FontWeight.BOLD))
    page.update()

ft.app(target=dashboard)
