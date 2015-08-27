import pygame
from shooter_player import Player
from shooter_token import Token
from shooter_shooter import Shooter
from shooter_bullets import Bullet
import math

class Shooter():
    def __init__(self, screen):
        pygame.init()

        self.screen = screen
        
        self.background = pygame.image.load('images/shooter/background.png')

        self.energy_img = pygame.image.load('images/shooter/energy.png')

        players_pos = [ (250 + 160, 250 + 40), (250 + 500, 250 + 150),
                        (250 + 370, 250 + 450), (250 + 40, 250 + 350) ]
        self.players = []
        self.player_0_rect = None
        self.bullet_0_rect = None
        self.player_1_rect = None
        self.bullet_1_rect = None
        self.player_2_rect = None
        self.bullet_2_rect = None
        self.player_3_rect = None
        self.bullet_3_rect = None
        for n in range(4):
            x, y = players_pos[n]
            player = Player(x, y, self.background, n)
            if n == 0: self.player_0_rect = pygame.Rect(player.x, player.y, 40, 40)
            elif n == 1: self.player_1_rect = pygame.Rect(player.x, player.y, 40, 40)
            elif n == 2: self.player_2_rect = pygame.Rect(player.x, player.y, 40, 40)
            elif n == 3: self.player_3_rect = pygame.Rect(player.x, player.y, 40, 40)
            self.players.append(player)

        self.dead_order = []
        self.points_ended = [ 0, 0, 0, 0 ]

        self.clock = pygame.time.Clock()

        self.rotation_left_1 = False
        self.rotation_left_4 = False
        self.rotation_right_1 = False
        self.rotation_right_4 = False
              
        self.running()

    def running(self):
        running = True
        while running:
            
            time = self.clock.tick(60)
            time_seconds = time / 1000.

            self.screen.blit(self.background, (250, 250))

            for n in range(len(self.players)):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.quit()  
                    if event.type == pygame.MOUSEMOTION:
                        self.rotation_right_1 = True
                        pos = pygame.mouse.get_pos()
                        if pos[1] <= 10:
                            pygame.mouse.set_pos(500, 500)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        elif event.key == pygame.K_f:
                            player = self.players[0]
                            player.bullet.check_shot()
                        elif event.key == pygame.K_1:
                            player = self.players[1]
                            player.bullet.check_shot()
                        elif event.key == pygame.K_2:
                            player = self.players[2]
                            player.bullet.check_shot()
                        elif event.key == pygame.K_g:
                            player = self.players[3]
                            player.bullet.check_shot()

                if pygame.mouse.get_pressed()[0]:
                    self.rotation_left_1 = True
                if pygame.mouse.get_pressed()[2]:
                    self.rotation_left_4 = True 

                key = pygame.key.get_pressed()
                if n  == 0:
                    player = self.players[0]
                    try:
                        if key[pygame.K_s]:     
                            player.moves_up(time_seconds)
                            player.index = 0
                        if key[pygame.K_w]:
                            player.moves_down(time_seconds)
                            player.index = 1
                        if key[pygame.K_d]:
                            player.moves_left(time_seconds)
                            player.index = 2
                        if key[pygame.K_a]:
                            player.moves_right(time_seconds)
                            player.index = 3
                        self.player_0_rect = pygame.Rect(player.x, player.y, 40, 40)
                    except IndexError:
                        pass
                elif n == 1:
                    player = self.players[1]
                    try:
                        if key[pygame.K_e]:     
                            player.moves_up(time_seconds)
                            player.index = 0
                        if key[pygame.K_r]:
                            player.moves_down(time_seconds)
                            player.index = 1
                        if key[pygame.K_t]:
                            player.moves_left(time_seconds)
                            player.index = 2
                        if key[pygame.K_y]:
                            player.moves_right(time_seconds)
                            player.index = 3
                        self.player_1_rect = pygame.Rect(player.x, player.y, 40, 40)
                    except IndexError:
                        pass
                elif n == 2:
                    player = self.players[2]
                    try:
                        if key[pygame.K_u]:     
                            player.moves_up(time_seconds)
                            player.index = 0
                        if key[pygame.K_i]:
                            player.moves_down(time_seconds)
                            player.index = 1
                        if key[pygame.K_o]:
                            player.moves_left(time_seconds)
                            player.index = 2
                        if key[pygame.K_p]:
                            player.moves_right(time_seconds)
                            player.index = 3
                        self.player_2_rect = pygame.Rect(player.x, player.y, 40, 40)
                    except IndexError:
                        pass
                elif n == 3:
                    player = self.players[3]
                    try:
                        if key[pygame.K_LEFT]:     
                            player.moves_up(time_seconds)
                            player.index = 0
                        if key[pygame.K_RIGHT]:
                            player.moves_down(time_seconds)
                            player.index = 1
                        if key[pygame.K_DOWN]:
                            player.moves_left(time_seconds)
                            player.index = 2
                        if key[pygame.K_UP]:
                            player.moves_right(time_seconds)
                            player.index = 3
                        self.player_3_rect = pygame.Rect(player.x, player.y, 40, 40)
                    except IndexError:
                        pass
                

                if player.energy <= 0:
                    self.dead_order.append(player)
                    del self.players[n]
                    self.players.insert(n, Token())
                    
                self.screen.blit(player.images[player.index], (player.x, player.y))
                try: self.bullet_0_rect = pygame.Rect(self.players[0].bullet.x, self.players[0].bullet.y, 4, 10)
                except IndexError: pass
                try: self.bullet_1_rect = pygame.Rect(self.players[1].bullet.x, self.players[1].bullet.y, 4, 10)
                except IndexError: pass
                try: self.bullet_2_rect = pygame.Rect(self.players[2].bullet.x, self.players[2].bullet.y, 4, 10)
                except IndexError: pass
                try: self.bullet_3_rect = pygame.Rect(self.players[3].bullet.x, self.players[3].bullet.y, 4, 10)
                except IndexError: pass

                try: player.bullet.moves(player.shooter.x, player.shooter.y)
                except: player.reset_bullet()
                    
                if player.bullet.rotate:
                    player.bullet.rotation_direction = 0
                    player.shooter.rotation_direction = 0
                    if (n == 1 and key[pygame.K_z]) or \
                       (n == 2 and key[pygame.K_x]) or \
                       (n == 3 and self.rotation_left_4) or \
                       (n == 0 and self.rotation_left_1):
                        player.bullet.rotation_direction = +1
                        player.shooter.rotation_direction = +1
                        if self.rotation_left_1:
                            self.rotation_left_1 = False
                        if self.rotation_left_4:
                            self.rotation_left_4 = False
                    if (n == 0 and self.rotation_right_1) or \
                       (n == 1 and key[pygame.K_n]) or \
                       (n == 2 and key[pygame.K_m]) or \
                       (n == 3 and key[pygame.K_SPACE]):
                        player.bullet.rotation_direction = -1
                        player.shooter.rotation_direction = -1
                        if self.rotation_right_1:
                            self.rotation_right_1 = False
                        if self.rotation_right_4:
                            self.rotation_right_4 = False
                    player.bullet.rotates(time_seconds)       
                    self.screen.blit(player.bullet.rotated_image,
                                     player.bullet.image_draw_pos)
                    
                if player.bullet.shot:
                    try:
                        self.screen.blit(player.bullet.rotated_image,
                                     (player.bullet.x, player.bullet.y))
                        player.bullet.hits_borders(self.background)
                        if n == 0:
                            try:
                                if self.bullet_0_rect.colliderect(self.player_1_rect):
                                    self.players[1].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_0_rect.colliderect(self.player_2_rect):
                                    self.players[2].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_0_rect.colliderect(self.player_3_rect):
                                    self.players[3].energy -= 10
                                    player.reset_bullet()
                            except IndexError: # dead
                                pass
                        if n == 1:
                            try:
                                if self.bullet_1_rect.colliderect(self.player_0_rect):
                                    self.players[0].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_1_rect.colliderect(self.player_2_rect):
                                    self.players[2].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_1_rect.colliderect(self.player_3_rect):
                                    self.players[3].energy -= 10
                                    player.reset_bullet()
                            except IndexError: # dead
                                pass
                        elif n == 2:
                            try:
                                if self.bullet_2_rect.colliderect(self.player_1_rect):
                                    self.players[1].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_2_rect.colliderect(self.player_0_rect):
                                    self.players[0].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_2_rect.colliderect(self.player_3_rect):
                                    self.players[3].energy -= 10
                                    player.reset_bullet()
                            except IndexError: # dead
                                pass
                        elif n == 3:
                            try:
                                if self.bullet_3_rect.colliderect(self.player_1_rect):
                                    self.players[1].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_3_rect.colliderect(self.player_2_rect):
                                    self.players[2].energy -= 10
                                    player.reset_bullet()
                                elif self.bullet_3_rect.colliderect(self.player_0_rect):
                                    self.players[0].energy -= 10
                                    player.reset_bullet()
                            except IndexError: # dead
                                pass
                    except:
                        player.reset_bullet()
                            
                if player.bullet.hits_bg:
                    player.reset_bullet()

                player.shooter.moves(player.x, player.y, player.d)
                player.shooter.rotates(time_seconds)
                self.screen.blit(player.shooter.rotated_image, player.shooter.image_draw_pos)

            for player in self.players:
                tot = player.energy / 10
                if player == self.players[0] and not player.token:                    
                    x = 230
                    for n in range(tot):
                        self.screen.blit(self.energy_img, (250 + x, 250 + 5))
                        x += 10
                elif player == self.players[1] and not player.token:
                    img = pygame.transform.rotate(self.energy_img, 90)
                    y = 230
                    for n in range(tot):
                        self.screen.blit(img, (250 + 575, 250 + y))
                        y += 10
                elif player == self.players[2] and not player.token:                    
                    x = 370
                    for n in range(tot):
                        self.screen.blit(self.energy_img, (250 + x, 250 + 575))
                        x -= 10
                elif player == self.players[3] and not player.token:
                    img = pygame.transform.rotate(self.energy_img, 90)
                    y = 370
                    for n in range(tot):
                        self.screen.blit(img, (250 + 5, 250 + y))
                        y -= 10

            counter = 0
            for player in self.players:
                if player.token:
                    counter += 1
                if counter == 3:
                    for player in self.players:
                        if not player.token:
                            self.dead_order.append(player)
                    self.end()
                    running = False
                
            pygame.display.update(250, 250, 600, 600)

            

    def end(self):
        for n in range(4):
            player = self.dead_order[n]
            m = player.number
            if n == 0:
                self.points_ended[m] = 100
            elif n == 1:
                self.points_ended[m] = 200
            elif n == 2:
                self.points_ended[m] = 300
            elif n == 3:
                self.points_ended[m] = 500
                
##Shooter(pygame.display.set_mode((1080, 1050), 0, 32))
