#main page
"""
note to self: wag na mag procrastinate pls 

diary: |||

day 1: okay naman medyo gets ko kaso nalilito lang ako ng konti sa ibang syntax
day 2: pano mag center huhuhuh
day 3:
"""


import flet as ft
from flet import *
from navigation import interface

#main application
def main(page: ft.Page):
    #initialize primary properties
    page.title = "EPM System"
    page.vertical_alignment = "CENTER"
    page.window_height = 600
    page.window_width = 300

    #navigation login to homepage
    def route_change(route):
      print(page.route)
      page.views.clear()
      page.views.append(
         interface(page)[page.route]   
      )

    #goto login first
    page.on_route_change = route_change
    page.go('/home')

    page.update()

# just change to (target=main, view=ft.WEB_BROWSER) to open it to browser :)
ft.app(target=main)


