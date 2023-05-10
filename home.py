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
          bgcolor='red',
          border_radius=35,
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