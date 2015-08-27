import pygame
from math import *
from vector2 import Vector2

class Bullet():
    
    def __init__(self, img, shooter_x, shooter_y, shooter_rotation):
        ## sets coordinates, loads image, sets dimensions of the image and sets rotation speed
        pygame.init()
        self.image = img
        self.x = shooter_x      
        self.y = shooter_y
        self.image_rotation = shooter_rotation     
        self.image_rotation_speed = 120.    
        self.rotate = True
        self.shot = False
        self.hits_bg = False

    def moves(self, shooter_x, shooter_y):
        ## moves and rotates together with the shooter
        if self.rotate == True:
            self.x = shooter_x
            self.y = shooter_y
        else:
            self.x += self.heading_x*18
            self.y += self.heading_y*18
            
    def rotates(self, time):
        self.rotated_image = pygame.transform.rotate(self.image, self.image_rotation)
        x, y = self.rotated_image.get_size()
        self.image_draw_pos = Vector2(self.x-x/2, self.y-y/2)
        self.image_rotation += self.rotation_direction * self.image_rotation_speed * time
        self.heading_x = -sin(self.image_rotation*pi/180.)
        self.heading_y = -cos(self.image_rotation*pi/180.)

    def check_shot(self):
        self.shot = True
        self.rotate = False

    def hits_borders(self, background):
        ## checks if the bullet hits the walls (coloured in black)
        if background.get_at((int(self.x) - 250, int(self.y) - 250)) == (0, 0, 0):
            self.hits_bg = True
        else:
            self.hits_bg = False
            


        
            
            
        
