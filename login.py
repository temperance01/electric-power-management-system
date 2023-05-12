#LOGIN PAGE
"""
todo list
1. fix layout huhuhuh
2. add verification 
3. register user lool
4. send info to database
5. design
"""

from flet import *

#di ko to alam pang initialize ata? hahahaha
class Login(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
   
#magic wow
  def build(self):
    return Column(
      controls=[
        Container(
            #background
            gradient=LinearGradient(begin=alignment.top_center, end=alignment.bottom_center, colors=['green', '#93C572']),
            height=530,width=270,
            bgcolor='blue',
            border_radius=35,
            
          
            content=Column(
            
            controls=[
              #for spacing
            Container(
                Text(' '),
                alignment=alignment.center,
                padding=50
        
            ),
              
            Container(
                Text('Login Page', size=20, weight='BOLD', color='black'),
                alignment=alignment.center,
            ),
            #username
            Container(
                TextField(label="Username", width=170, height=60, border_radius=35, color='black'),
                alignment=alignment.center,
            ),
            #password
            Container(
                TextField(label="Password", width=170, height=60, border_radius=35, color='black' ,
                      password=True, can_reveal_password=True),
                alignment=alignment.center,
        
            ),

            #button to send the user to homepageee
            Container(
                alignment=alignment.center,
                on_click= lambda _: self.page.go('/home'), 
                content=ElevatedButton(text="LOGIN")
            )
            ]
        
          )
          )
        ]
    )