import pygame
from frogger_players import Player
from frogger_enemies import Enemy

class Frogger():
    def __init__(self, screen):
        pygame.init()
        
        self.screen = screen
        self.w = h = 600
                
        self.images_players = [ [ pygame.image.load('images/frogger/player_1.1.png'),
                             pygame.image.load('images/frogger/player_1.2.png'),
                             pygame.image.load('images/frogger/player_1.3.png'),
                             pygame.image.load('images/frogger/player_1.4.png') ],
                           [ pygame.image.load('images/frogger/player_2.1.png'),
                             pygame.image.load('images/frogger/player_2.2.png'),
                             pygame.image.load('images/frogger/player_2.3.png'),
                             pygame.image.load('images/frogger/player_2.4.png') ],
                           [ pygame.image.load('images/frogger/player_3.1.png'),
                             pygame.image.load('images/frogger/player_3.2.png'),
                             pygame.image.load('images/frogger/player_3.3.png'),
                             pygame.image.load('images/frogger/player_3.4.png') ],
                           [ pygame.image.load('images/frogger/player_4.1.png'),
                             pygame.image.load('images/frogger/player_4.2.png'),
                             pygame.image.load('images/frogger/player_4.3.png'),
                             pygame.image.load('images/frogger/player_4.4.png') ] ]

        self.players_pos = [ (250 + 100, 250 + h - 50),
                        (250 + 200, 250 + h - 50),
                        (250 + 350, 250 + h - 50),
                        (250 + 450, 250 + h - 50) ]

        self.players = []
        for n in range(0,4):
            player = Player(self.images_players[n], self.players_pos[n], n)
            self.players.append(player)

        self.players_ended = []

        self.points_ended = [ 0, 0, 0, 0 ]
                           

        self.images_enemies = [ pygame.image.load('images/frogger/enemy_1.png'),
                                pygame.image.load('images/frogger/enemy_1.1.png'),
                                pygame.image.load('images/frogger/enemy_2.png'),
                                pygame.image.load('images/frogger/enemy_3.png'),
                                pygame.image.load('images/frogger/enemy_3.1.png'),
                                pygame.image.load('images/frogger/enemy_4.png') ]

        self.enemies_pos= [ (250 + self.w, 250 + 500),
                       (250 - 50, 250 + 450),
                       (250 + self.w, 250 + 400),
                       (250 - 100, 250 + 350),
                       (250 + self.w, 250 + 250),
                       (250 - 150, 250 + 200),
                       (250 - 250, 250 + 150),
                       (250 + self.w, 250 + 100),
                       (250 - 150, 250 + 50) ]

        self.enemies_1 = []
        self.enemies_2 = []
        self.enemies_3 = []
        self.enemies_4 = []
        self.enemies_5 = []
        self.enemies_6 = []
        self.enemies_7 = []
        self.enemies_8 = []
        self.enemies_9 = []

        for n in range(0,9):
            pos = self.enemies_pos[n]
            if n == 0:
                enemy = Enemy(self.images_enemies[0], pos, 1, self.w)
                self.enemies_1.append(enemy)
            elif n == 1:
                enemy = Enemy(self.images_enemies[1], pos, 2, self.w)
                self.enemies_2.append(enemy)
            elif n == 2:
                enemy = Enemy(self.images_enemies[0], pos, 3, self.w)
                self.enemies_3.append(enemy)
            elif n == 3:
                enemy = Enemy(self.images_enemies[2], pos, 4, self.w)
                self.enemies_4.append(enemy)
            elif n == 4:
                enemy = Enemy(self.images_enemies[3], pos, 5, self.w)
                self.enemies_5.append(enemy)
            elif n == 5:
                enemy = Enemy(self.images_enemies[4], pos, 6, self.w)
                self.enemies_6.append(enemy)
            elif n == 6:
                enemy = Enemy(self.images_enemies[5], pos, 7, self.w)
                self.enemies_7.append(enemy)
            elif n == 7:
                enemy = Enemy(self.images_enemies[2], pos, 8, self.w)
                self.enemies_8.append(enemy)
            elif n == 8:
                enemy = Enemy(self.images_enemies[5], pos, 9, self.w)
                self.enemies_9.append(enemy)

        self.countdown = [ pygame.image.load('images/pong4/10.png'),
                           pygame.image.load('images/pong4/9.png'),
                           pygame.image.load('images/pong4/8.png'),
                           pygame.image.load('images/pong4/7.png'),
                           pygame.image.load('images/pong4/6.png'),
                           pygame.image.load('images/pong4/5.png'),
                           pygame.image.load('images/pong4/4.png'),
                           pygame.image.load('images/pong4/3.png'),
                           pygame.image.load('images/pong4/2.png'),
                           pygame.image.load('images/pong4/1.png'),
                           pygame.image.load('images/pong4/end.png') ]
        
        self.background = pygame.image.load('images/frogger/background.png')

        self.clock = pygame.time.Clock()
        self.timer = 0
        
        self.main()

    def main(self):
        running = True
        while running:
            
            time = self.clock.tick(60)
            time_seconds = time/1000.
            self.timer += self.clock.get_rawtime()/1000.
                
            players_rects = []
            enemies_rects = []
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    player = self.players[0]
                    if not player.y == 250:
                        if event.key == pygame.K_s:
                            player.moves_up()
                        if event.key == pygame.K_w:
                            player.moves_down()
                        if event.key == pygame.K_a:
                            player.moves_right()
                        if event.key == pygame.K_d:
                            player.moves_left()
                        
                    player = self.players[1]
                    if not player.y == 250:
                        if event.key == pygame.K_e:
                            player.moves_up()
                        if event.key == pygame.K_r:
                            player.moves_down()
                        if event.key == pygame.K_y:
                            player.moves_right()
                        if event.key == pygame.K_t:
                            player.moves_left()
                        
                    player = self.players[2]
                    if not player.y == 250:
                        if event.key == pygame.K_u:
                            player.moves_up()
                        if event.key == pygame.K_i:
                            player.moves_down()
                        if event.key == pygame.K_p:
                            player.moves_right()
                        if event.key == pygame.K_o:
                            player.moves_left()
                        
                    player = self.players[3]
                    if not player.y == 250:
                        if event.key == pygame.K_LEFT:
                            player.moves_up()
                        if event.key == pygame.K_RIGHT:
                            player.moves_down()
                        if event.key == pygame.K_UP:
                            player.moves_right()
                        if event.key == pygame.K_DOWN:
                            player.moves_left()

            for player in self.players:
                rect = pygame.Rect(player.x, player.y, 50, 50)
                players_rects.append(rect)
                
            for enemy in self.enemies_1:
                enemy.move_left(time_seconds)
                if enemy.x <= 250 + 2*600/3 and enemy.append_enemy_1 == False and len(self.enemies_1) <= 2:
                    self.enemies_1.append( Enemy(self.images_enemies[0], self.enemies_pos[0], 1, self.w) )
                    enemy.append_enemy_1 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_3:
                enemy.move_left(time_seconds)
                if enemy.x <= 250 + 2*600/3 and enemy.append_enemy_3 == False and len(self.enemies_3) <= 2:
                    self.enemies_3.append( Enemy(self.images_enemies[0], self.enemies_pos[2], 3, self.w) )
                    enemy.append_enemy_3 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_5:
                enemy.move_left(time_seconds)
                if enemy.x <= 250 + 600/2 and enemy.append_enemy_5 == False and len(self.enemies_5) <= 1:
                    self.enemies_5.append( Enemy(self.images_enemies[3], self.enemies_pos[4], 5, self.w) )
                    enemy.append_enemy_5 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 150, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_7:
                enemy.move_left(time_seconds)
                if enemy.x <= 250 + 2*600/3 and enemy.append_enemy_7 == False and len(self.enemies_7) <= 2:
                    self.enemies_7.append( Enemy(self.images_enemies[5], self.enemies_pos[6], 7, self.w) )
                    enemy.append_enemy_7 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 250, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_9:
                enemy.move_left(time_seconds)
                if enemy.x <= 250 + 600/3 and enemy.append_enemy_9 == False and len(self.enemies_9) <= 2:
                    self.enemies_7.append( Enemy(self.images_enemies[5], self.enemies_pos[8], 9, self.w) )
                    enemy.append_enemy_9 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 250, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_2:
                enemy.move_right(time_seconds)
                if enemy.x >= 250 + 600/3 - 50 and enemy.append_enemy_2 == False and len(self.enemies_2) <= 2:
                    self.enemies_2.append( Enemy(self.images_enemies[1], self.enemies_pos[1], 2, self.w) )
                    enemy.append_enemy_2 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_4:
                enemy.move_right(time_seconds)
                if enemy.x >= 250 + 600/3 - 100 and enemy.append_enemy_4 == False and len(self.enemies_4) <= 2:
                    self.enemies_4.append( Enemy(self.images_enemies[2], self.enemies_pos[3], 4, self.w) )
                    enemy.append_enemy_4 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 100, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_6:
                enemy.move_right(time_seconds)
                if enemy.x >= 250 + 600/3 + 150 and enemy.append_enemy_6 == False and len(self.enemies_6) <= 2:
                    self.enemies_6.append( Enemy(self.images_enemies[4], self.enemies_pos[5], 6, self.w) )
                    enemy.append_enemy_6 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 150, 50)
                enemies_rects.append(enemy_rect)

            for enemy in self.enemies_8:
                enemy.move_right(time_seconds)
                if enemy.x >= 250 + 600/3 - 100 and enemy.append_enemy_8 == False and len(self.enemies_8) <= 2:
                    self.enemies_8.append( Enemy(self.images_enemies[2], self.enemies_pos[7], 8, self.w) )
                    enemy.append_enemy_8 = True
                enemy_rect = pygame.Rect(enemy.x, enemy.y, 100, 50)
                enemies_rects.append(enemy_rect)

                for player in self.players:
                    for rect_player in players_rects:
                        for rect_enemy in enemies_rects:
                            if rect_player.colliderect(rect_enemy):
                                if rect_player == players_rects[0]:
                                    n = 0
                                elif rect_player == players_rects[1]:
                                    n = 1
                                elif rect_player == players_rects[2]:
                                    n = 2
                                elif rect_player == players_rects[3]:
                                    n = 3
                                player_to_be_appended = Player(self.images_players[n], self.players_pos[n], player.number)
                                del self.players[n]
                                self.players.insert(n, player_to_be_appended)

            self.screen.blit(self.background, (250, 250))

            for enemy in self.enemies_1:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_2:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_3:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_4:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_5:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_6:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_7:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_8:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            for enemy in self.enemies_9:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
##
##            for rect in players_rects:
##                pygame.draw.rect(self.screen, (0, 255, 0), rect, 10)
##            for rect in enemies_rects_1:
##                pygame.draw.rect(self.screen, (0, 255, 0), rect, 10)
##            for rect in enemies_rects_2:
##                pygame.draw.rect(self.screen, (0, 255, 0), rect, 10)

##            
            for player in self.players:
                self.screen.blit(player.images[player.image_index], (player.x, player.y))


            if self.timer > 50 and self.timer <= 51: self.screen.blit(self.countdown[0], (250 + 250, 250 + 250))
            elif self.timer > 51 and self.timer <= 52: self.screen.blit(self.countdown[1], (250 + 250, 250 + 250))
            elif self.timer > 52 and self.timer <= 53: self.screen.blit(self.countdown[2], (250 + 250, 250 + 250))
            elif self.timer > 53 and self.timer <= 54: self.screen.blit(self.countdown[3], (250 + 250, 250 + 250))
            elif self.timer > 54 and self.timer <= 55: self.screen.blit(self.countdown[4], (250 + 250, 250 + 250))
            elif self.timer > 55 and self.timer <= 56: self.screen.blit(self.countdown[5], (250 + 250, 250 + 250))
            elif self.timer > 56 and self.timer <= 57: self.screen.blit(self.countdown[6], (250 + 250, 250 + 250))
            elif self.timer > 57 and self.timer <= 58: self.screen.blit(self.countdown[7], (250 + 250, 250 + 250))
            elif self.timer > 58 and self.timer <= 59: self.screen.blit(self.countdown[8], (250 + 250, 250 + 250))
            elif self.timer > 59 and self.timer <= 60: self.screen.blit(self.countdown[9], (250 + 250, 250 + 250))
            elif self.timer >= 60:
                numbers = []
                for player in self.players:
                    if player.appended == False:
                        self.players_ended.append(player)
                        numbers.append(player.number)
                self.end(numbers)
                running = False

            pygame.display.update(250, 250, 600, 600)

            player_ended = 0
            for player in self.players:
                if player.y == 250 and player.appended == False:
                    self.players_ended.append(player)
                    player.appended = True
                    if len(self.players_ended) == 4:
                        self.end()
                        running = False                

    def end(self, tie = None):
        print self.players_ended
        for n in range(4):
            player = self.players_ended[n]
            m = player.number
            if n == 0:
                self.points_ended[m] = 500
            elif n == 1:
                self.points_ended[m] = 300
            elif n == 2:
                self.points_ended[m] = 200
            elif n == 3:
                self.points_ended[m] = 100
        if tie != None:
            for number in tie:
                self.points_ended[number] = 100
        self.screen.blit(self.countdown[10], (250 + 200, 250 + 200))
        pygame.display.update(250, 250, 600, 600)
        pygame.time.wait(2000)
                
##Frogger(pygame.display.set_mode((1080, 1050), 0, 32))


















