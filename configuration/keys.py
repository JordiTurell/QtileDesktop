from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import layout

class Teclado:

    keys = []
    mod = ""
    terminal = ""

    def __init__(self):
        self.keys = []
        self.mod = "mod4"
        self.terminal = "kitty"
    
    def createkeys(self):
        self.keys.append(Key([self.mod], "h", lazy.layout.left(), desc="Move focus to left"))
        self.keys.append(Key([self.mod], "l", lazy.layout.right(), desc="Move focus to right"))
        self.keys.append(Key([self.mod], "j", lazy.layout.down(), desc="Move focus down"))
        self.keys.append(Key([self.mod], "k", lazy.layout.up(), desc="Move focus up"))
        self.keys.append(Key([self.mod], "space", lazy.layout.next(), desc="Move window focus to other window"))
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        self.keys.append(Key([self.mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"))
        self.keys.append(Key([self.mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"))
        self.keys.append(Key([self.mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"))
        self.keys.append(Key([self.mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"))
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        self.keys.append(Key([self.mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"))
        self.keys.append(Key([self.mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"))
        self.keys.append(Key([self.mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"))
        self.keys.append(Key([self.mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"))
        self.keys.append(Key([self.mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"))
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        self.keys.append(Key(
            [self.mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ))
        self.keys.append(Key([self.mod], "Return", lazy.spawn(self.terminal), desc="Launch terminal"))
        # Toggle between different layouts as defined below
        self.keys.append(Key([self.mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"))
        self.keys.append(Key([self.mod], "w", lazy.window.kill(), desc="Kill focused window"))
        self.keys.append(Key([self.mod, "control"], "r", lazy.reload_config(), desc="Reload the config"))
        self.keys.append(Key([self.mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"))
        self.keys.append(Key([self.mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"))

        #Lanzar menu
        self.keys.append(Key([self.mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"))
        return self.keys
    
t = Teclado()