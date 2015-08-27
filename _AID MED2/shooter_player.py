import pygame
from shooter_bullets import Bullet
from shooter_shooter import Shooter

class Player(object):

    def __init__(self, x, y, background, number):
        self.x = x #w/2 - 20
        self.y = y #h/2 - 20
        self.d = 40
        self.background = background
        self.speed = 100.
        self.number = number
        if number == 0:
            self.images = [ pygame.image.load("images/shooter/tank_up_0.png"),
                            pygame.image.load("images/shooter/tank_down_0.png"),
                            pygame.image.load("images/shooter/tank_left_0.png"),
                            pygame.image.load("images/shooter/tank_right_0.png") ]
        elif number == 1:
            self.images = [ pygame.image.load("images/shooter/tank_up_1.png"),
                            pygame.image.load("images/shooter/tank_down_1.png"),
                            pygame.image.load("images/shooter/tank_left_1.png"),
                            pygame.image.load("images/shooter/tank_right_1.png") ]
        elif number == 2:
            self.images = [ pygame.image.load("images/shooter/tank_up_2.png"),
                            pygame.image.load("images/shooter/tank_down_2.png"),
                            pygame.image.load("images/shooter/tank_left_2.png"),
                            pygame.image.load("images/shooter/tank_right_2.png") ]
        elif number == 3:
            self.images = [ pygame.image.load("images/shooter/tank_up_3.png"),
                            pygame.image.load("images/shooter/tank_down_3.png"),
                            pygame.image.load("images/shooter/tank_left_3.png"),
                            pygame.image.load("images/shooter/tank_right_3.png") ]
        self.index = 0

        self.bullet_img = pygame.image.load("images/shooter/bullet.png")
        shooter_img = pygame.image.load("images/shooter/cannon.png")

        self.shooter = Shooter(shooter_img, self.x, self.y, self.d)
        self.bullet = Bullet(self.bullet_img, self.shooter.x, self.shooter.y,
                             self.shooter.image_rotation)
        self.energy = 100

        self.token = False

    def moves_up(self, time):
        ## manages movement upwards checking for collision with walls
        d_speed = self.speed * time
        if self.background.get_at((int(self.x) - 250, int(self.y) - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d/2 - 250, int(self.y) - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d - 250, int(self.y) - 250)) != (0, 0, 0):
            self.y -= d_speed
        elif ( self.background.get_at((int(self.x) - 250, int(self.y) - 250)) == (0, 0, 0) and \
               self.background.get_at((int(self.x) + self.d/2 - 250, int(self.y) - 250)) == (0, 0, 0) ) or \
               ( self.background.get_at((int(self.x) + self.d/2 - 250, int(self.y) - 250)) == (0, 0, 0) or \
                 self.background.get_at((int(self.x) + self.d - 250, int(self.y) - 250)) == (0, 0, 0) ):
            d_speed = 0
    
    def moves_down(self, time):
        ## manages movement downwards checking for collision with walls
        d_speed = self.speed * time
        if self.background.get_at((int(self.x) - 250, int(self.y) + self.d - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d/2 - 250, int(self.y) + self.d - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d - 250, int(self.y) + self.d - 250)) != (0, 0, 0):
            self.y += d_speed
        elif ( self.background.get_at((int(self.x) - 250, int(self.y) + self.d - 250)) == (0, 0, 0) and \
               self.background.get_at((int(self.x) + self.d/2 - 250, int(self.y) + self.d - 250)) == (0, 0, 0) ) or \
               ( self.background.get_at((int(self.x) + self.d/2 - 250, int(self.y) + self.d - 250)) == (0, 0, 0) and \
                 self.background.get_at((int(self.x) + self.d - 250, int(self.y) + self.d - 250)) == (0, 0, 0)) :
            d_speed = 0

    def moves_left(self, time):
        ## manages movement leftwards checking for collsion with walls
        d_speed = self.speed * time
        if self.background.get_at((int(self.x) - 250, int(self.y) - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) - 250, int(self.y) + self.d/2 - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) - 250, int(self.y) + self.d - 250)) != (0, 0, 0):
            self.x -= d_speed
        elif ( self.background.get_at((int(self.x) - 250, int(self.y) - 250)) == (0, 0, 0) and \
               self.background.get_at((int(self.x) - 250, int(self.y) + self.d/2 - 250)) == (0, 0, 0) )  or \
               ( self.background.get_at((int(self.x) - 250, int(self.y) + self.d/2 - 250)) == (0, 0, 0) and \
                 self.background.get_at((int(self.x) - 250, int(self.y) + self.d - 250)) == (0, 0, 0) ):
            d_speed = 0
            
    def moves_right(self, time):
        ## manages movement rightwards checking for collision with walls
        d_speed = self.speed * time
        if self.background.get_at((int(self.x) + self.d - 250, int(self.y) - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d - 250, int(self.y) + self.d/2 - 250)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d - 250, int(self.y) + self.d - 250)) != (0, 0, 0):
            self.x += d_speed
        elif ( self.background.get_at((int(self.x) + self.d - 250, int(self.y) - 250)) == (0, 0, 0) and \
               self.background.get_at((int(self.x) + self.d - 250, int(self.y) + self.d/2 - 250)) == (0, 0, 0) ) or \
               ( self.background.get_at((int(self.x) + self.d - 250, int(self.y) + self.d/2 - 250)) == (0, 0, 0) and \
                 self.background.get_at((int(self.x) + self.d - 250, int(self.y) + self.d - 250)) == (0, 0, 0) ):
            d_speed = 0

    def reset_bullet(self):
        self.bullet = Bullet(self.bullet_img, self.shooter.x, self.shooter.y, self.shooter.image_rotation)


        
        
        
