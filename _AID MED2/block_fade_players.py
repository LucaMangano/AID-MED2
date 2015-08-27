import pygame

class Player():
    def __init__(self, image, x, y, number):
        self.image = image
        self.number = number
        self.x = x
        self.y = y
        self.speed = 200.
        self.slide_speed = 3
        self.slides_up = self.slides_down = self.slides_right = self.slides_left = False
        self.is_colliding = False
        self.dead = False
        self.update_rect()

    def update_rect(self):
        if self.number == 0 or self.number == 2:
            self.rect_up = pygame.Rect(self.x, self.y, 20, 6)
            self.rect_right = pygame.Rect(self.x + 17, self.y + 3, 6, 24)
            self.rect_down = pygame.Rect(self.x, self.y + 27, 20, 6)
            self.rect_left = pygame.Rect(self.x, self.y + 3, 6, 24)
        elif self.number == 1 or self.number == 3:
            self.rect_up = pygame.Rect(self.x, self.y, 30, 6)
            self.rect_right = pygame.Rect(self.x + 27, self.y + 3, 6, 14)
            self.rect_down = pygame.Rect(self.x, self.y + 17, 30, 6)
            self.rect_left = pygame.Rect(self.x, self.y + 3, 6, 14)

    def moves_up(self, time):
        dy = self.speed*time
        self.y -= dy

    def moves_down(self, time):
        dy = self.speed*time
        self.y += dy

    def moves_right(self, time):
        dx = self.speed*time
        self.x += dx

    def moves_left(self, time):
        dx = self.speed*time
        self.x -= dx

    def slides(self, time):
        if self.slides_up == True:
            self.slide_speed -= 0.07*2
            if self.slide_speed <= 0:
                self.slides_up = False
                self.slide_speed = 3
            else:
                self.y -= self.slide_speed
                
        if self.slides_down == True:
            self.slide_speed -= 0.07*2
            if self.slide_speed <= 0:
                self.slides_down = False
                self.slide_speed = 3
            else:
                self.y += self.slide_speed
                
        if self.slides_right == True:
            self.slide_speed -= 0.07*2
            if self.slide_speed <= 0:
                self.slides_right = False
                self.slide_speed = 3
            else:
                self.x += self.slide_speed
                
        if self.slides_left == True:
            self.slide_speed -= 0.07*2
            if self.slide_speed <= 0:
                self.slides_left = False
                self.slide_speed = 3
            else:
                self.x -= self.slide_speed
                
    def collides(self, others, self_rect):
        for other in others:
            if other!=self:
                if self_rect.colliderect(other):
                    self.is_colliding = True

    def Dead(self):
        self.dead = True

    def check_collision(self, players):
        for player in players:
            if player != self:
                if player.rect_down.colliderect(self.rect_up):
                    self.slides_down = True
                    player.slides_up = True
                if player.rect_up.colliderect(self.rect_down):
                    self.slides_up = True
                    player.slides_down = True
                if player.rect_left.colliderect(self.rect_right):
                    self.slides_left = True
                    player.slides_right = True
                if player.rect_right.colliderect(self.rect_left):
                    self.slides_right = True
                    player.slides_left = True
                    
        
        
        



















