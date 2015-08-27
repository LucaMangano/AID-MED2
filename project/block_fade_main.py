import pygame
import random
from block_fade_platforms import Platform
from block_fade_players import Player


class BlockFade():
    
    def __init__(self, screen):
        pygame.init()

        self.screen = screen
        w = h = 600

        images_platform = [ pygame.image.load('images/block_fade/1.png'), pygame.image.load('images/block_fade/2.png'),
                            pygame.image.load('images/block_fade/3.png'), pygame.image.load('images/block_fade/4.png'),
                            pygame.image.load('images/block_fade/5.png'), pygame.image.load('images/block_fade/6.png'),
                            pygame.image.load('images/block_fade/7.png'), pygame.image.load('images/block_fade/8.png'),
                            pygame.image.load('images/block_fade/9.png') ]

        self.platform_positions = [ (250 + w/8, 250 + h/8), (250 + (w/8)+150, 250 + h/8), (250 + (w/8)+300, 250 + h/8),
                                    (250 + w/8, 250 + (w/8)+150), (250 + (w/8)+150, 250 + (w/8)+150), (250 + (w/8)+300, 250 + (w/8)+150),
                                    (250 + w/8, 250 + (w/8)+300), (250 + (w/8)+150, 250 + (w/8)+300), (250 + (w/8)+300, 250 + (w/8)+300) ]

        self.platforms = []
        for n in range(0,9):
            image = images_platform[n]
            pos = self.platform_positions[n]
            platform = Platform(image, n, pos)
            self.platforms.append(platform)

        self.images_small_platform = [pygame.image.load('images/block_fade/1.1.png'), pygame.image.load('images/block_fade/2.1.png'),
                                 pygame.image.load('images/block_fade/3.1.png'), pygame.image.load('images/block_fade/4.1.png'),
                                 pygame.image.load('images/block_fade/5.1.png'), pygame.image.load('images/block_fade/6.1.png'),
                                 pygame.image.load('images/block_fade/7.1.png'), pygame.image.load('images/block_fade/8.1.png'),
                                 pygame.image.load('images/block_fade/9.1.png') ]
        self.small_platform_position = (250 + 20, 250 + 20)

        self.platform_disappear = []
        self.small_platform_disappear = []
        self.platform_disappear_index = -1
        for n in range(0,100):
            m = random.randint(0,8)
            platform = self.platforms[m]
            small_platform = self.images_small_platform[m]
            self.platform_disappear.append(platform)
            self.small_platform_disappear.append(small_platform)

        self.images_players = [ pygame.image.load('images/block_fade/player_1.png'),
                           pygame.image.load('images/block_fade/player_2.png'),
                           pygame.image.load('images/block_fade/player_3.png'),
                           pygame.image.load('images/block_fade/player_4.png') ]

        self.starting_pos_players = [ (250 + 300, 250 + 150),
                                      (250 + 450, 250 + 300),
                                      (250 + 300, 250 + 450),
                                      (250 + 150, 250 + 300) ]

        self.players = []
        for n in range(0,4):
            image = self.images_players[n]
            pos = self.starting_pos_players[n]
            x, y = pos
            number = n
            player = Player(image, x, y, number)
            self.players.append(player)

        self.background = pygame.image.load('images/block_fade/background.png')

        self.game_over = pygame.image.load('images/pong4/end.png')

        self.clock = pygame.time.Clock()
        self.timer = 0
        change_once = False

        self.dead_order = []
        self.points = [ 0, 0, 0, 0 ]

        
        self.main()

    def main(self):
        running  = True
        while running:

            time = self.clock.tick(30)
            time_seconds = time/1000.
            self.timer += self.clock.get_rawtime()/1000.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.KEYUP:
                    for player in self.players:
                        if player.number == 0:
                            if event.key == pygame.K_s:
                                player.slides_up = True
                            if event.key == pygame.K_w:
                                player.slides_down = True
                            if event.key == pygame.K_d:
                                player.slides_left = True
                            if event.key == pygame.K_a:
                                player.slides_right = True

                        elif player.number == 1:
                            if event.key == pygame.K_e:
                                player.slides_up = True
                            if event.key == pygame.K_r:
                                player.slides_down = True
                            if event.key == pygame.K_t:
                                player.slides_left = True
                            if event.key == pygame.K_y:
                                player.slides_right = True

                        elif player.number == 2:
                            if event.key == pygame.K_u:
                                player.slides_up = True
                            if event.key == pygame.K_i:
                                player.slides_down = True
                            if event.key == pygame.K_o:
                                player.slides_left = True
                            if event.key == pygame.K_p:
                                player.slides_right = True

                        elif player.number == 3:
                            if event.key == pygame.K_LEFT:
                                player.slides_up = True
                            if event.key == pygame.K_RIGHT:
                                player.slides_down = True
                            if event.key == pygame.K_DOWN:
                                player.slides_left = True
                            if event.key == pygame.K_LEFT:
                                player.slides_right = True

            for player in self.players:
                player.update_rect()

            for player in self.players:
                player.check_collision(self.players)

            key = pygame.key.get_pressed()

            for player in self.players:
                if player.number == 0:
                    if key[pygame.K_s]:
                        player.moves_up(time_seconds)
                    if key[pygame.K_w]:
                        player.moves_down(time_seconds)
                    if key[pygame.K_d]:
                        player.moves_left(time_seconds)
                    if key[pygame.K_a]:
                        player.moves_right(time_seconds)
                    player.slides(time_seconds)

                elif player.number == 1:
                    if key[pygame.K_e]:
                        player.moves_up(time_seconds)
                    if key[pygame.K_r]:
                        player.moves_down(time_seconds)
                    if key[pygame.K_t]:
                        player.moves_left(time_seconds)
                    if key[pygame.K_y]:
                        player.moves_right(time_seconds)
                    player.slides(time_seconds)

                elif player.number == 2:
                    if key[pygame.K_u]:
                        player.moves_up(time_seconds)
                    if key[pygame.K_i]:
                        player.moves_down(time_seconds)
                    if key[pygame.K_o]:
                        player.moves_left(time_seconds)
                    if key[pygame.K_p]:
                        player.moves_right(time_seconds)
                    player.slides(time_seconds)

                elif player.number == 3:
                    if key[pygame.K_LEFT]:
                        player.moves_up(time_seconds)
                    if key[pygame.K_RIGHT]:
                        player.moves_down(time_seconds)
                    if key[pygame.K_DOWN]:
                        player.moves_left(time_seconds)
                    if key[pygame.K_UP]:
                        player.moves_right(time_seconds)
                    player.slides(time_seconds)

            players_rects = []
            for player in self.players:
                player_rect = pygame.Rect(player.x, player.y, 30, 30)
                players_rects.append(player_rect)

            platforms_rects = []
            for n in range(0,9):
                position = self.platform_positions[n]
                x, y = position
                platform_rect = pygame.Rect(x, y, 150, 150)
                platforms_rects.append(platform_rect)

            for player in self.players:
                if player.x + 15 <= 250 + 75 or \
                   player.x + 15 >= 250 + 600 - 75 or \
                   player.y + 15 <= 250 + 75 or \
                   player.y + 15 >= 250 + 600 - 75:
                    player.Dead()

            for platform in self.platforms:
                if platform.visible == False:
                    platforms_rects_1 = []
                    platforms_rects_1.append(platforms_rects[platform.number])
                    for rect in platforms_rects_1:
                        for rect_1 in players_rects:
                            if rect_1.colliderect(rect) == True:
                                if rect_1 == players_rects[0]:
                                    player = self.players[0]
                                    player.Dead()
                                elif rect_1 == players_rects[1]:
                                    player = self.players[1]
                                    player.Dead()
                                elif rect_1 == players_rects[2]:
                                    player = self.players[2]
                                    player.Dead()
                                elif rect_1 == players_rects[3]:
                                    player = self.players[3]
                                    player.Dead()
             
            temp = []
            for player in self.players:
                if player.dead == False:
                    temp.append(player)
                else:
                    self.dead_order.append(player)
            self.players = temp
                            
            self.screen.blit(self.background, (250,250))

            #blit platforms and manages disappearance
##            if (self.timer >= 1 and self.timer <= 2) or\
##               (self.timer >= 4 and self.timer <= 5)or\
##               (self.timer >= 8 and self.timer <= 9) or\
##               (self.timer >= 12 and self.timer <= 13) or\
##               (self.timer >= 16 and self.timer <= 17):
##                
##                if not change_once: 
##                    self.platform_disappear_index += 1
##                    change_once = True
##                small_platform_stays = self.small_platform_disappear[self.platform_disappear_index]
##                self.screen.blit(small_platform_stays, (self.small_platform_position))
##                
##                for platform in self.platforms:
##                    platform.visible = True
##                    self.screen.blit(platform.image, platform.position)
##                
##            elif (self.timer >= 3 and self.timer <= 4) or\
##               (self.timer >= 6 and self.timer <= 7)or\
##               (self.timer >= 10 and self.timer <= 11) or\
##               (self.timer >= 14 and self.timer <= 15) or\
##               (self.timer >= 18 and self.timer <= 19):
##                platform_stays = self.platform_disappear[self.platform_disappear_index]
##                for platform in self.platforms:
##                    if platform_stays != platform:
##                        image = platform.disappear()
##                        self.screen.blit(image, platform.position)
##                    else:
##                        self.screen.blit(platform.image, platform.position)

##            if (self.timer >= 3 and self.timer <= 5) or\
##               (self.timer >= 10 and self.timer <= 12)or\
##               (self.timer >= 17 and self.timer <= 19) or\
##               (self.timer >= 24 and self.timer <= 26) or\
##               (self.timer >= 31 and self.timer <= 33):
##                
##                if not change_once: 
##                    self.platform_disappear_index += 1
##                    change_once = True
##                small_platform_stays = self.small_platform_disappear[self.platform_disappear_index]
##                self.screen.blit(small_platform_stays, (self.small_platform_position))
##                
##                for platform in self.platforms:
##                    platform.visible = True
##                    self.screen.blit(platform.image, platform.position)
##                
##            elif (self.timer >= 5 and self.timer <= 8) or\
##               (self.timer >= 12 and self.timer <= 15)or\
##               (self.timer >= 19 and self.timer <= 22) or\
##               (self.timer >= 26 and self.timer <= 29) or\
##               (self.timer >= 33 and self.timer <= 36):
##                platform_stays = self.platform_disappear[self.platform_disappear_index]
##                for platform in self.platforms:
##                    if platform_stays != platform:
##                        image = platform.disappear()
##                        self.screen.blit(image, platform.position)
##                    else:
##                        self.screen.blit(platform.image, platform.position)

            if (self.timer >= 2 and self.timer <= 5) or\
               (self.timer >= 8 and self.timer <= 11)or\
               (self.timer >= 14 and self.timer <= 17) or\
               (self.timer >= 20 and self.timer <= 22) or\
               (self.timer >= 24 and self.timer <= 26) or \
               (self.timer >= 28 and self.timer <= 30) or\
               (self.timer >= 32 and self.timer <= 34)or\
               (self.timer >= 36 and self.timer <= 37) or\
               (self.timer >= 38 and self.timer <= 39) or\
               (self.timer >= 40 and self.timer <= 41):
                
                if not change_once: 
                    self.platform_disappear_index += 1
                    change_once = True
                small_platform_stays = self.small_platform_disappear[self.platform_disappear_index]
                self.screen.blit(small_platform_stays, (self.small_platform_position))
                
                for platform in self.platforms:
                    platform.visible = True
                    self.screen.blit(platform.image, platform.position)
                
            elif (self.timer >= 5 and self.timer <= 8) or\
               (self.timer >= 11 and self.timer <= 14)or\
               (self.timer >= 17 and self.timer <= 20) or\
               (self.timer >= 22 and self.timer <= 24) or\
               (self.timer >= 26 and self.timer <= 28) or\
               (self.timer >= 30 and self.timer <= 32) or\
               (self.timer >= 34 and self.timer <= 36)or\
               (self.timer >= 37 and self.timer <= 38) or\
               (self.timer >= 39 and self.timer <= 40) or\
               (self.timer >= 41 and self.timer <= 42):
                platform_stays = self.platform_disappear[self.platform_disappear_index]
                for platform in self.platforms:
                    if platform_stays != platform:
                        image = platform.disappear()
                        self.screen.blit(image, platform.position)
                    else:
                        self.screen.blit(platform.image, platform.position)
                        
            else:
                change_once = False
                for platform in self.platforms:
                    platform.visible = True
                    self.screen.blit(platform.image, platform.position)

            for player in self.players:
                self.screen.blit(player.image, (player.x, player.y))

            pygame.display.update(250, 250, 600, 600)

            if len(self.players) == 1:
                self.dead_order.append(self.players[0])
                self.end()
                pygame.time.wait(2000)
                running = False
            elif len(self.players) == 0:
                self.end()
                running = False

            if self.timer >= 43:
                numbers = []
                for player in self.players:
                    self.dead_order.append(player)
                    numbers.append(player.number)
                self.end(numbers)
                running = False
                
    def end(self, tie = None):
        for n in range(4):
            dead = self.dead_order[n]
            m = dead.number
            if n == 0:
                self.points[m] = 100
            elif n == 1:
                self.points[m] = 200
            elif n == 2:
                self.points[m] = 300
            elif n == 3:
                self.points[m] = 500
        if tie != None:
            for number in tie:
                self.points[number] = 500
        self.screen.blit(self.game_over, (250 + 200, 250 + 200))
        pygame.display.update(250, 250, 600, 600)
        pygame.time.wait(2000)

##BlockFade(pygame.display.set_mode((1080, 1050), 0, 32))
