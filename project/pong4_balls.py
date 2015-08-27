import pygame
import random

class Ball():

    def __init__(self, number, img, pos):
        self.number = number
        self.img = img
        self.x, self.y = pos
        self.dead = False
        self.pos = None
        self.rect_x = [ pygame.Rect(self.x, self.y + 1, 2, 28),
                        pygame.Rect(self.x + 29, self.y + 1, 2, 28) ]
        self.rect_y = [ pygame.Rect(self.x + 1, self.y, 28, 2),
                        pygame.Rect(self.x + 1, self.y + 29, 28, 2) ]

    def generate_speed(self):
        s_x = [ -187., -153., -94., 29., 76., 167. ]
        s_y = [ -198., -87., -53., 177., 129., 176. ]
        self.speed_x = random.choice(s_x)
        self.speed_y = random.choice(s_y)
        
    def moves(self, time):
        dx = self.speed_x * time
        dy = self.speed_y * time
        self.x += dx
        self.y += dy
        self.rect_x = [ pygame.Rect(self.x, self.y + 1, 2, 28),
                        pygame.Rect(self.x + 29, self.y + 1, 2, 28) ]
        self.rect_y = [ pygame.Rect(self.x + 1, self.y, 28, 2),
                        pygame.Rect(self.x + 1, self.y + 29, 28, 2) ]
                        
        
    def check_bounces_players(self, player_x, player_y, number, token,
                              speed_1, speed_2, speed_3, speed_4):
        if number == 0:
            if not token:
                if self.y <= 250 + 50 and self.y >= 250 + 0:
                    if self.x + 30 >= player_x and self.x <= player_x + 100:
                        self.y = 250 + 50
                        self.reverse_y()
                        if speed_1:
                            self.speed_x *= 2
                            self.speed_y *= 2
                        speed_1 = False
                elif self.y <= 250 + 0:
                    self.dead = True
                    self.pos = 0
            else:
                if self.y <= 250 + 50:
                    self.reverse_y()

        elif number == 1:
            if not token:
                if self.x >= 250 + 550 - 30 and self.x <= 250 + 600 - 30:
                    if self.y + 30 >= player_y and self.y <= player_y + 100:
                        self.x = 250 + 550 - 30
                        self.reverse_x()
                        if speed_2:
                            self.speed_x *= 2
                            self.speed_y *= 2
                            speed_2 = False
                elif self.x >= 250 + 600 - 30:
                    self.dead = True
                    self.pos = 1
            else:
                if self.x >= 250 + 550 - 30:
                    self.reverse_x()
                    
                
        elif number == 2:
            if not token:
                if self.y >= 250 + 550 - 30 and self.y <= 250 + 600 - 30:
                    if self.x + 30 >= player_x and self.x <= player_x + 100:
                        self.y = 250 + 550 - 30
                        self.reverse_y()
                        if speed_3:
                            self.speed_x *= 2
                            self.speed_y *= 2
                            speed_3 = False
                elif self.y >= 250 + 600 - 30:
                    self.dead = True
                    self.pos = 2
            else:
                if self.y >= 250 + 550 - 30:
                    self.reverse_y()
                    

        elif number == 3:
            if not token:
                if self.x <= 250 + 50 and self.x >= 250 + 0:
                    if self.y + 30 >= player_y and self.y <= player_y + 100:
                        self.x <= 250 + 50
                        self.reverse_x()
                        if speed_4:
                            self.speed_x *= 2
                            self.speed_y *= 2
                            speed_4 = False
                elif self.x <= 250  + 0:
                    self.dead = True
                    self.pos = 3
            else:
                if self.x <= 250 + 50:
                    self.reverse_x()
                    

    def reverse_x(self):
        self.speed_x = -self.speed_x

    def reverse_y(self):
        self.speed_y = -self.speed_y
