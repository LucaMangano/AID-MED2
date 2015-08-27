class Enemy():
    def __init__(self, image, pos, number, w):
        self.image = image
        self.x, self.y = pos
        self.w = w
        self.number = number

        if self.number == 1 or self.number == 2:
            self.speed = 75.
        elif self.number == 3 or self.number == 4:
            self.speed = 100.
        elif self.number == 5:
            self.speed = 200.
        elif self.number == 6:
            self.speed = 100.
        elif self.number == 7: 
            self.speed = 100.
        elif self.number == 8:
            self.speed = 150.
        elif self.number == 9:
            self.speed = 150.

        self.append_enemy_1 = False
        self.append_enemy_2 = False
        self.append_enemy_3 = False
        self.append_enemy_4 = False
        self.append_enemy_5 = False
        self.append_enemy_6 = False
        self.append_enemy_7 = False
        self.append_enemy_8 = False
        self.append_enemy_9 = False

    def move_left(self, time):
        self.x -= self.speed*time
        if ((self.number == 1 or self.number == 3) and self.x <= 250 - 50) or\
             (self.number == 5 and self.x <= 250 - 150) or \
             (self.number == 7 and self.x <= 250 - 250) or \
             (self.number == 9 and self.x <= 250 - 250):
            self.x = 250 + 600

    def move_right(self, time):
        self.x += self.speed*time
        if self.x >= 250 + 600:
            if self.number == 2:
                self.x = 250 - 50
            elif self.number == 4:
                self.x = 250 - 100
            elif self.number == 6:
                self.x = 250 - 150
            elif self.number == 6:
                self.x = 250 - 150
            elif self.number == 8:
                self.x = 250 - 100

        
            
        
