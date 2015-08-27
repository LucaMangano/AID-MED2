import pygame

class Token():

    def __init__(self, number):
        self.number = number
        if number == 0:
            img = pygame.image.load('images/pong4/token_horiz.png')
            pos = (250 + 50, 250 + 30)
        elif number == 1:
            img = pygame.image.load('images/pong4/token_vert.png')
            pos = (250 + 550, 250 + 50)
        elif number == 2:
            img = pygame.image.load('images/pong4/token_horiz.png')
            pos = (250 + 50, 250 + 550)
        elif number == 3:
            img = pygame.image.load('images/pong4/token_vert.png')
            pos = (250 + 30, 250 + 50)
        self.x, self.y = pos
        self.img = img
        self.speed = 0.
        self.points = 1
        self.token = True
       
    def moves_up(self, time):
        pass
        
    def moves_down(self, time):
        pass
            
    def moves_right(self, time):
        pass
    
    def moves_left(self, time):
        pass

    def speed_up(self):
        pass
