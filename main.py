import flet as ft
from flet import *
from navigation import interface

#main application
def main(page: ft.Page):
    #initialize primary properties
    page.title = "EPM System"
    page.vertical_alignment = "center"
    page.window_height = 600
    page.window_width = 300

    #navigation login to homepage
    def route_change(route):
      print(page.route)
      page.views.clear()
      page.views.append(
         interface(page)[page.route]   
      )

    page.on_route_change = route_change
    page.go('/login')

    page.update()
   
ft.app(target=main)

