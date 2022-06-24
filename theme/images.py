class Imagenes:
    
    images = []
    
    def __init__(self):
        images = []
        images.append({ 'wallpaper':'assets/wallpaper.jpg' })
        images.append({ 'bolaselected':'assets/bola.png' })
        images.append({ 'shutdown':'assets/shutdown.png' })

    def GetWallpaper(self):
        return images[0].wallpaper
    
    def GetBolaSelected(self):
        return images[0].bolaselected
    
    def GetShutdonw(self):
        return images[0].shutdown
