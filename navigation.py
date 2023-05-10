#navigation 
"""
this is where navigation happens :o
"""

from flet import *
from home import Home
from login import Login

def interface(page):
  return {
    '/home':View(
        route='/home',
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