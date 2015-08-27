import pygame
from math import *
from vector2 import Vector2  

class Shooter(object):

    def __init__(self, img, player_x, player_y, player_d):
        ## sets coordinates, loads image, sets angle of rotation and sets speed of rotation
        pygame.init()
        self.x = player_x + (player_d/2)
        self.y = player_y + (player_d/2)
        self.image = img
        self.image_rotation = 0.   
        self.image_rotation_speed = 120.

    def moves(self, player_x, player_y, player_d):
        ## manages movement according to player
        self.x = player_x + (player_d/2)
        self.y = player_y + (player_d/2)

    def rotates(self, time):
        ## manages rotation according to input
            
        self.rotated_image = pygame.transform.rotate(self.image, self.image_rotation)
        x, y = self.rotated_image.get_size()
        self.image_draw_pos = Vector2(self.x-x/2, self.y-y/2)
        self.image_rotation += self.rotation_direction * self.image_rotation_speed * time

        
