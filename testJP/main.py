from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty
  
XGRIDSIZE = 10
YGRIDSIZE = 15 

# Classe principale qui herite de kivy.app
class JrcApp(App):
    def build(self):
        return Board()

# Classe du board qui herite de kivy.uix.gridlayout
class Board(GridLayout):
    def __init__(self, *args, **kwargs):
        # Added here because .kv file not loaded
        self.cols = XGRIDSIZE
        self.rows = YGRIDSIZE
        
        super(Board, self).__init__(*args, **kwargs)
        for row in range(self.cols):
            for column in range(self.rows):
                grid_entry = GridEntry( 
                       coords=(row, column))
                grid_entry.bind(on_release=self.button_pressed)
                self.add_widget(grid_entry)

    def button_pressed(self, button):
        # Print output just to see what's going on
        print ('{} button clicked!'.format(button.coords))

# Classe des cases
class GridEntry(Button):
    coords = ListProperty([0, 0])


if __name__ == "__main__":
    JrcApp().run()