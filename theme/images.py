class Imagenes:
    
    images = []
    
    def __init__(self):
        images = []
        images.append({ 'assets/wallpaper.jpg' })
        images.append({ 'assets/bola.png' })
        images.append({ 'assets/shutdown.png' })

    def GetWallpaper(self):
        #return images[0].wallpaper
        return '/home/z4dk1el/.config/qtile/assets/wallpaper.jpg'
    
    def GetBolaSelected(self):
        #return images[0].bolaselected
        return '/home/z4dk1el/.config/qtile/assets/bola.png'
    
    def GetShutdonw(self):
        #return images[0].shutdown
        return '/home/z4dk1el/.config/qtile/assets/shutdown.png'
