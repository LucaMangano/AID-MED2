class Player():

    def __init__(self, number, img, pos):
        self.number = number
        self.x, self.y = pos
        self.img = img
        self.speed = 250.
        self.points = 20
        self.token = False
       
    def moves_up(self, time):
        dy = self.speed*time
        self.y -= dy
        if self.y <= 250 + 50:
            self.y = 250 + 50
        
    def moves_down(self, time):
        dy = self.speed*time
        self.y += dy
        if self.y >= 250 + 450:
            self.y = 250 + 450
            
    def moves_right(self, time):
        dx = self.speed*time
        self.x += dx
        if self.x >= 250 + 450:
            self.x = 250 + 450
        
    def moves_left(self, time):
        dx = self.speed*time
        self.x -= dx
        if self.x <= 250 + 50:
            self.x = 250 + 50

    def speed_up(self):
        self.speed = 500.
