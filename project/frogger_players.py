class Player():
    def __init__ (self, images, pos, number):
        self.images = images
        self.x, self.y = pos
        self.image_index = 0
        self.number = number
        self.appended = False

    def moves_up(self):
        self.y -= 50
        if self.y <= 250:
            self.y = 250
        self.image_index = 0

    def moves_down(self):
        self.y += 50
        if self.y >= 250 + 600 - 50:
            self.y = 250 + 600 - 50
        self.image_index = 2
        
    def moves_right(self):
        self.x += 25
        if self.x >= 250 + 600 - 50:
            self.x = 250 + 600 - 50
        self.image_index = 1
        
    def moves_left(self):
        self.x -= 25
        if self.x <= 250:
            self.x = 250
        self.image_index = 3
        
