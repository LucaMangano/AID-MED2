import pygame
from shooter_bullets import Bullet
from shooter_shooter import Shooter

class Token(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.d = 0
        self.speed = 0
        img = pygame.image.load("images/shooter/token.png") 
        self.images = [ img, img, img, img ]
        self.index = 0
        self.shooter = Shooter(img, self.x, self.y, self.d)
        self.bullet = Bullet(img, self.shooter.x, self.shooter.y,
                             self.shooter.image_rotation)
        self.energy = 100
        self.token = True
    def moves_up(self, time):
        pass
    def moves_down(self, time):
        pass
    def moves_left(self, time):
        pass      
    def moves_right(self, time):
        pass
    def reset_bullet(self):
        pass


        
        
        
