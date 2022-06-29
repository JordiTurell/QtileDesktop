from libqtile.config import Screen
from libqtile import bar, widget



class Pantalla:
    
    screen = []
    
    def __init__(self):
        self.screen = []
        
    def Config(self, theme, widgets):
        self.screen.append(
            Screen(
                #top = bar.Bar(
                #    [
                #        widget.CurrentLayout(),
                #        widget.GroupBox(),
                #        widget.WindowName(),
                #        widget.Clock(format="%a / %d-%m-%Y / %H:%M:%S"),
                #        widget.QuickExit(), #Mirem de pusar el icno de shutdown
                #    ],
                #    30,
                #    background = theme.GetColors().Gris(),
                #    margin = 10
                #    #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                #    #border_color=["ff00ff", "ff0000", "ff00ff", "ff0000"]  # Borders are magenta
                #),
                top = widgets.GetTopBar(),
                wallpaper='/home/z4dk1el/.config/qtile/assets/wallpaper.jpg',
                wallpaper_mode='stretch'
            )
        )
        return self.screen

        
    