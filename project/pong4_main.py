import pygame
from pong4_players import Player
from pong4_balls import Ball
from pong4_players_token import Token

class Pong4():
    
    def __init__(self, screen):
        pygame.init()

        self.screen = screen
        w = h = 600

        self.background = pygame.image.load('images/pong4/background.png')

        self.alpha = 0

        self.galaxies_img = [ pygame.image.load('images/pong4/galx_1.png'),
                         pygame.image.load('images/pong4/galx_2.png'),
                         pygame.image.load('images/pong4/galx_3.png'),
                         pygame.image.load('images/pong4/galx_4.png') ]

        players_img = [ pygame.image.load('images/pong4/player_horiz.png'),
                        pygame.image.load('images/pong4/player_vert.png'),
                        pygame.image.load('images/pong4/player_horiz.png'),
                        pygame.image.load('images/pong4/player_vert.png') ]

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
        
        players_pos = [ (250 + 250, 250 + 30),
                        (250 + 550, 250 + 250),
                        (250 + 250, 250 + 550),
                        (250 + 30, 250 + 250) ]

        self.ball_img = pygame.image.load('images/pong4/ball.png')

        self.balls_pos = ( (250 + 300 - 50, 250 + 300 - 50),
                           (250 + 300 + 50, 250 + 300 - 50),
                           (250 + 300 - 50, 250 + 300 + 50),
                           (250 + 300 + 50, 250 + 300 + 50) )
                                         
        self.players = []
        for n in range(0,4):
            img = players_img[n]
            pos = players_pos[n]
            player = Player(n, img, pos)
            self.players.append(player)

        self.dead_order = []
        self.points_ended = [ 0, 0, 0, 0 ]

        self.balls = []
        ball = Ball(0, self.ball_img, self.balls_pos[0])
        ball.generate_speed()
        self.balls.append(ball)

        self.corners_rects_x = ( pygame.Rect(250 + 48, 250 + 0, 2, 50),
                                 pygame.Rect(250 + 550, 250 + 0, 2, 50),
                                 pygame.Rect(250 + 48, 250 + 550, 2, 50),
                                 pygame.Rect(250 + 550, 250 + 550, 2, 50) )
        self.corners_rects_y = ( pygame.Rect(250 + 0, 250 + 49, 48, 2),
                                 pygame.Rect(250 + 552, 250 + 49, 48, 2),
                                 pygame.Rect(250 + 0, 250 + 550, 48, 2),
                                 pygame.Rect(250 + 552, 250 + 550, 48, 2) )

        self.font = pygame.font.SysFont( "times", 16)

        self.clock = pygame.time.Clock()
        self.timer = 0

        self.once_5 = True
        self.once_10 = True
        self.once_15 = True

        self.speed_1 = False

        self.speed_up_ball_1 = False
        self.speed_up_ball_2 = False
        self.speed_up_ball_3 = False
        self.speed_up_ball_4 = False
        
        self.main()

    def main(self):
        running  = True
        while running:

            time = self.clock.tick(60)
            time_seconds = time/1000.
            self.timer += self.clock.get_rawtime()/1000.

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_n:
                        player = self.players[1]
                        player.speed = 250
                    if event.key == pygame.K_m:
                        player = self.players[2]
                        player.speed = 250
                    if event.key == pygame.K_SPACE:
                        player = self.players[3]
                        player.speed = 250
                if event.type == pygame.MOUSEMOTION:
                    self.speed_1 = True
                    pos = pygame.mouse.get_pos()
                    if pos[1] <= 10:
                        pygame.mouse.set_pos(500, 500)
                else:
                    player = self.players[0]
                    player.speed = 250
                    self.speed_1 = False

            if pygame.mouse.get_pressed()[0]:
                self.speed_up_ball_1 = True
            else:
                self.speed_up_ball_1 = False
            if pygame.mouse.get_pressed()[2]:
                self.speed_up_ball_4 = True
            else:
                self.speed_up_ball_4 = False
                        
            key = pygame.key.get_pressed()
            for player in self.players:
                if player.number == 0:
                    if key[pygame.K_d]:
                        player.moves_left(time_seconds)
                    if key[pygame.K_a]:
                        player.moves_right(time_seconds)
                    if self.speed_1:
                        player.speed_up()
                elif player.number == 1:
                    if key[pygame.K_e]:
                        player.moves_up(time_seconds)
                    if key[pygame.K_r]:
                        player.moves_down(time_seconds)
                    if key[pygame.K_n]:
                        player.speed_up()
                    if key[pygame.K_z]:
                        self.speed_up_ball_2 = True
                    else:
                        self.speed_up_ball_2 = False
                elif player.number == 2:
                    if key[pygame.K_o]:
                        player.moves_left(time_seconds)
                    if key[pygame.K_p]:
                        player.moves_right(time_seconds)
                    if key[pygame.K_m]:
                        player.speed_up()
                    if key[pygame.K_x]:
                        self.speed_up_ball_3 = True
                    else:
                        self.speed_up_ball_3 = False
                elif player.number == 3:
                    if key[pygame.K_LEFT]:
                        player.moves_up(time_seconds)
                    if key[pygame.K_RIGHT]:
                        player.moves_down(time_seconds)
                    if key[pygame.K_SPACE]:
                        player.speed_up()

            for ball in self.balls:
                ball.moves(time_seconds)
                for player in self.players:
                    ball.check_bounces_players(player.x, player.y, player.number, player.token,
                                               self.speed_up_ball_1, self.speed_up_ball_2,
                                               self.speed_up_ball_3, self.speed_up_ball_4)

                if ball.dead:
                    player = self.players[ball.pos]
                    player.points -= 1
                    number = ball.number
                    del self.balls[number]
                    ball = Ball(number, self.ball_img, self.balls_pos[number])
                    ball.generate_speed()
                    self.balls.insert(number, ball)

            self.screen.blit(self.background, (250,250))

            for img, pos in zip(self.galaxies_img, self.balls_pos):
                self.alpha -= 0.5
                img = self.rot_center(img, self.alpha)
                x = pos[0] - 25
                y = pos[1] - 25
                self.screen.blit(img, (x, y))

            if self.timer > 80 and self.timer <= 81: self.screen.blit(self.countdown[0], (250 + 250, 250 + 250))
            elif self.timer > 81 and self.timer <= 82: self.screen.blit(self.countdown[1], (250 + 250, 250 + 250))
            elif self.timer > 82 and self.timer <= 83: self.screen.blit(self.countdown[2], (250 + 250, 250 + 250))
            elif self.timer > 83 and self.timer <= 84: self.screen.blit(self.countdown[3], (250 + 250, 250 + 250))
            elif self.timer > 84 and self.timer <= 85: self.screen.blit(self.countdown[4], (250 + 250, 250 + 250))
            elif self.timer > 85 and self.timer <= 86: self.screen.blit(self.countdown[5], (250 + 250, 250 + 250))
            elif self.timer > 86 and self.timer <= 87: self.screen.blit(self.countdown[6], (250 + 250, 250 + 250))
            elif self.timer > 87 and self.timer <= 88: self.screen.blit(self.countdown[7], (250 + 250, 250 + 250))
            elif self.timer > 88 and self.timer <= 89: self.screen.blit(self.countdown[8], (250 + 250, 250 + 250))
            elif self.timer > 89 and self.timer <= 90: self.screen.blit(self.countdown[9], (250 + 250, 250 + 250))
            if self.timer >= 90:
                for player in self.players:
                    if not player.token:
                        self.dead_order.append(player)
                self.end()
                running = False
            
            for player in self.players:
                self.screen.blit(player.img, (player.x, player.y))

            if self.timer >= 5 and self.once_5 == True:
                ball = Ball(1, self.ball_img, self.balls_pos[1])
                ball.generate_speed()
                self.balls.append(ball)
                self.once_5 = False
            if self.timer >= 10 and self.once_10 == True:
                ball = Ball(2, self.ball_img, self.balls_pos[2])
                ball.generate_speed()
                self.balls.append(ball)
                self.once_10 = False
            if self.timer >= 15 and self.once_15 == True:
                ball = Ball(3, self.ball_img, self.balls_pos[3])
                ball.generate_speed()
                self.balls.append(ball)
                self.once_15 = False
                
            for m in range(len(self.balls)):
                ball = self.balls[m]
                self.screen.blit(self.ball_img, (ball.x, ball.y))

            rects_x = []
            rects_y = []
            for ball in self.balls:
                rects_x.append(ball.rect_x)
                rects_y.append(ball.rect_y)

            for ball in self.balls:
                for ball_rect in ball.rect_x:
                    for rect in self.corners_rects_x:
                        if ball_rect.colliderect(rect):
                            ball.reverse_x()
                    for rects in rects_x:
                        if rects != ball.rect_x:
                            for rect in rects:
                                if ball_rect.colliderect(rect):
                                    ball.reverse_x()
                for ball_rect in ball.rect_y:
                    for rect in self.corners_rects_y:
                        if ball_rect.colliderect(rect):
                            ball.reverse_y()
                    for rects in rects_y:
                        if rects != ball.rect_y:
                            for rect in rects:
                                if ball_rect.colliderect(rect):
                                    ball.reverse_y()

            for player in self.players:
                if not player.token:
                    text = self.font.render(str(player.points), True, (255, 255, 255)) #text point
                    if player.number == 0:
                        text = pygame.transform.rotate(text, 180)
                        self.screen.blit(text, (250 + 290, player.y - 25))
                    elif player.number == 1:
                        text = pygame.transform.rotate(text, 90)
                        self.screen.blit(text, (player.x + 25, 250 + 290))
                    elif player.number == 2:
                        self.screen.blit(text, (250 + 290, player.y + 25))
                    elif player.number == 3:
                        text = pygame.transform.rotate(text, -90)
                        self.screen.blit(text, (player.x - 25, 250 + 290))

            for player in self.players:
                if player.points <= 0 and not player.token:
                    n = player.number
                    self.dead_order.append(player)
                    del self.players[player.number]
                    self.players.insert(n, Token(n))

##            for pos in self.balls_pos:
##                pygame.draw.circle(self.screen, (255, 255, 255), pos, 15, 15)
##                    
            pygame.display.update(250, 250, 600, 600)

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

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
                
    def end(self):
        ranking = []
        for player in self.dead_order:
            ranking.append(player.points)
        ranking.sort()
        
        for n in range(4):
            player = self.dead_order[n]
            m = player.number
            if ranking[0] == player.points:
                self.points_ended[m] = 100
            elif ranking[1] == player.points:
                self.points_ended[m] = 200
            elif ranking[2] == player.points:
                self.points_ended[m] = 300
            elif ranking[3] == player.points:
                self.points_ended[m] = 500
        for player in self.players:
            if player.token:
                self.points_ended[player.number] = 100
        self.screen.blit(self.countdown[10], (250 + 200, 250 + 200))
        pygame.display.update(250, 250, 600, 600)
        pygame.time.wait(2000)
                
##Pong4(pygame.display.set_mode((1080, 1050), 0, 32))
