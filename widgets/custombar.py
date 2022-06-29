from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen

class CustomBar:
    color = ''
    def __init__(self):
        color = '#393939'
        
    def init_topbar(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(padding=3),
                widget.GroupBox(
                    highlight_method="line",
                    disable_drag=True,
                    hide_unused=True,
                    active=foreground,
                    inactive=black0,
                    block_highlight_text_color=foreground,
                    this_screen_border=purple,
                    this_current_screen_border=purple,
                    other_screen_border=black0,
                    other_current_screen_border=foreground,
                    highlight_color=[black0],
                    padding=6,
                    spacing=0,
                    margin_x=0,
                ),
                widget.WindowName(for_current_screen=True, padding=6),
                mpd,
                widget.TextBox(
                    padding=0,
                    text=separator,
                    foreground=soft,
                    fontsize=28,
                    font="UbuntuNerdFont",
                ),
                widget.TextBox(text="vol:", background=soft),
                volume,
                widget.TextBox(
                    padding=0,
                    text=separator,
                    background=soft,
                    foreground=background,
                    fontsize=28,
                    font="UbuntuNerdFont",
                ),
                widget.TextBox(text="bat:"),
                battery,
                widget.TextBox(
                    padding=0,
                    text=separator,
                    foreground=soft,
                    fontsize=28,
                    font="UbuntuNerdFont",
                ),
                widget.Clock(format="%I:%M%P %m/%d/%Y", background=soft, padding=0),
                widget.TextBox(
                    padding=0,
                    text=separator,
                    background=soft,
                    foreground=background,
                    fontsize=28,
                    font="UbuntuNerdFont",
                ),
                caffeine,
                widget.Systray(padding=2),
                powermenu,
            ],
        )