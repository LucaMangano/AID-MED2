class Platform():
    def __init__(self, image, n, pos):
        self.position = pos
        self.number = n
        self.image = image
        self.visible = True

    def disappear(self):
        image = self.image.convert()
        image.set_alpha(0)
        self.visible = False
        return image

    
