import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from random import random

""""
class Board(BoxLayout):
    
    def float x,y
    
    def __init__(self,**kwargs):
        x
"""      

class TestBoardApp(App):

    def build(self):
        widget = Widget()
        
        widget.canvas.add(Color(random(),1,1))
        widget.canvas.add(Rectangle(pos=(10, 10),size=(50,20)))
        widget.canvas.add(Color(random(),1,0))
        widget.canvas.add(Rectangle(pos=(10.5, 10.5),size=(50,20)))
        """widget.canvas.add(Color(random(),0,1))
        widget.canvas.add(Rectangle(pos=(11, 11),size=(50,20)))
        """
        
        layout = BoxLayout()
        layout.add_widget(widget)
        
        return layout

if __name__ == '__main__':
    TestBoardApp().run()