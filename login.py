import flet as ft
import subprocess

def main(page: ft.Page):
    page.title = "Syntax Sisters"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_login(event):
        subprocess.run(["python", "calendarPage.py"])
        page.close()

    #:O login!!!! yayyyy 
    login_box = ft.Container(
        content=ft.Column(
            [
                ft.Text("Syntax Sisters", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.TextField(label="Username", autofocus=True),
                ft.TextField(label="Password", password=True),
                ft.ElevatedButton("Login", on_click=handle_login, bgcolor="#6200EE", color="white"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )

    #background cause we like stuff pretty <3
    background_container = ft.Container(
        content=ft.Column(
            [login_box], 
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        ),
        image_src="backgroundtemp.png",
        image_fit=ft.ImageFit.FILL,
        expand=True,
    )

    # add
    page.add(background_container)
    page.update()

ft.app(target=main)
