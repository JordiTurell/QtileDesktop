from theme.colors import Colores
from theme.images import Imagenes

class ConfigTheme:
    colors = []
    imagenes = []
    
    def __init__(self):
        self.colors = Colores()
        self.imagenes = Imagenes()
        
    def GetColors(self):
        return self.colors
    
    def GetImagenes(self):
        return self.imagenes
        