
from custombar import CustomBar

class Widgets:
    
    bar = None
    
    def __init__(self):
        bar = CustomBar()
        
    def GetTopBar(self):
        return self.bar.init_topbar()