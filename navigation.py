from flet import *
from home import Home
from login import Login

def interface(page):
  return {
    '/':View(
        route='/',
        controls=[
          Home(page)
        ]
      ),
    '/login':View(
        route='/login',
        controls=[
          Login(page)
        ]
      ),
  }