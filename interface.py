#this contains the interface module of the program
import flet 
from flet import *

#login page
def login_page(page: flet.Page):
    page.title = "EPM System"
    page.vertical_alignment = "center"
    page.window_height = 600
    page.window_width = 300
    


    page.update()
    

flet.app(target=login_page)