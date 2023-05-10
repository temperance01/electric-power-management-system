#HOME PAGE
"""
todo list
1. add widgets
2. connect to other modules 
3. other functions
4. maybe add separate pages for other fucntions?
"""
from flet import *
class Home(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page

  def build(self):
    return Column(
      controls=[
        Container(
          height=530,width=270,
          border_radius=35,
          bgcolor='red',
          content=Column(
            controls=[
              Text('Welcome to the homepage'),
              Container(
                on_click= lambda _: self.page.go('/login') ,
                content=Text('Goto Login',size=25,color='black')
              )
            ]
          )
          )
        ]
    )