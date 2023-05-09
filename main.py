import flet as ft
from flet import *

def login_page(page: ft.Page):
    page.title = "EPM System"
    page.vertical_alignment = "center"
    page.window_height = 600
    page.window_width = 300
    
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)

    page.update()
    

ft.app(target=login_page)

