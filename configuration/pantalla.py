from libqtile.config import Screen
from libqtile import bar, widget
from theme.colors import Colores

class Pantalla:
    
    screen = []
    colors = []
    
    def __init__(self):
        self.screen = []
        self.colors = Colores()
        
    def Config(self):
        self.screen.append(
            Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayout(),
                        widget.GroupBox(),
                        widget.WindowName(),
                        widget.Clock(format="%a / %d-%m-%Y / %H:%M:%S"),
                        widget.QuickExit(), #Mirem de pusar el icno de shutdown
                    ],
                    30,
                    background = self.colors.Gris()
                    #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    #border_color=["ff00ff", "ff0000", "ff00ff", "ff0000"]  # Borders are magenta
                ),
            )
        )
        return self.screen

        
    