import pygame
import random
from players import Player
from block_fade_main import BlockFade
from pong4_main import Pong4
from frogger_main import Frogger
from shooter_main import Shooter

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1080, 1050), 0, 32 )

        self.background = pygame.image.load("images/board/Board_8.png")

        players = [ pygame.image.load('images/board/player_1.png'),
                    pygame.image.load('images/board/player_2.png'),
                    pygame.image.load('images/board/player_3.png'),
                    pygame.image.load('images/board/player_4.png') ]

        self.ring = pygame.image.load('images/board/ring.png')

        self.blue_button = [ pygame.image.load('images/board/blue_button_0.png'),
                             pygame.image.load('images/board/blue_button_1.png'),
                             pygame.image.load('images/board/blue_button_2.png'),
                             pygame.image.load('images/board/blue_button_3.png') ]

        self.blue_button_pos = ( (250 + 250, 250 + 100),
                                 (250 + 400, 250 + 250),
                                 (250 + 250, 250 + 400),
                                 (250 + 100, 250 + 250) )

        self.centre_0 = pygame.image.load('images/board/center_0.png')
        self.centre_1 = pygame.image.load('images/board/center_1.png')
    
        players_starting_pos = [ (78, 115), (887, 99), (907, 824), (118, 835) ]

        self.home = False

        self.positions = [ (78, 115), (253, 115), (351, 77), (470, 49), (594, 50), (699, 65),
                      (817, 102), (887, 99), (964, 257), (976, 363), (973, 485), (941, 609),
                      (937, 732), (907, 824), (856, 930), (757, 969), (638, 998), (515, 1000),
                      (411, 984), (293, 950), (118, 835), (106, 777), (94, 672), (97, 549),
                      (92, 428), (112, 306) ]
        
        self.xs = [ pygame.image.load('images/board/x_white.png'),
                    pygame.image.load('images/board/t_white_0.png'),
                    pygame.image.load('images/board/t_white_1.png'),
                    pygame.image.load('images/board/t_white_2.png'),
                    pygame.image.load('images/board/t_white_3.png') ]
        
        x_pos = [ (250 + 50, 250 + 50), (250 + 500, 250 + 50),
                  (250 + 500, 250 + 500), (250 + 50, 250 + 500) ]

        self.icon_games = pygame.image.load('images/board/icon_games.png')

        self.icon_pos = [ (250 + 50, 250 + 125), (250 + 450, 250 + 50),
                          (250 + 350, 250 + 450), (250 + 125, 250 + 350) ]

        self.turn_token = pygame.image.load('images/board/die.png')

        self.turn_token_pos = [ (250 + 350, 250 + 50), (250 + 500, 250 + 350),
                                (250 + 250, 250 + 500), (250 + 50, 250 + 250) ]
        self.token_index = 0

        self.turn_index = 0

        self.player_path = pygame.image.load('images/board/player_move.png')

        self.animation = False
        
        self.players = []
        for n in range(0,4):
            player = Player(n, players[n], players_starting_pos,
                            players_starting_pos[n], self.positions,
                            x_pos[n])
            self.players.append(player)
        
        self.dice = [ pygame.image.load('images/board/1.png'),
                      pygame.image.load('images/board/2.png'),
                      pygame.image.load('images/board/3.png'),
                      pygame.image.load('images/board/4.png'),
                      pygame.image.load('images/board/5.png'),
                      pygame.image.load('images/board/6.png') ]

        self.round = -1

        self.font = pygame.font.SysFont('arial', 32)
        self.font_small = pygame.font.SysFont('arial', 10)
        
        self.score_pos = ( (250 + 50, 250 + 5),
                           (250 + 560, 250 + 50),
                           (250 + 490, 250 + 555),
                           (250 + 5, 250 + 490) )

        self.part_score_pos = ( (250 + 300 - 100, 250 + 50),
                                (250 + 550, 250 + 300 - 100),
                                (250 + 300 - 100, 250 + 550),
                                (250 + 50, 250 + 300 - 100) )
                                 
        self.clock = pygame.time.Clock()
        self.timer = 0

        pygame.mouse.set_visible(0)

        self.old_index = 0
        
        self.main()
        
    def roll_dice(self):
        roll = None
        picks = [ 1, 2, 3, 4, 5, 6 ]
        previous = [ 0 ]
        temp = []
        for n in range(0, 20):
            die = random.choice(picks)
            previous.append(die)
            
            if die == previous[-1]:
                for pick in picks:
                    if pick != die:
                        temp.append(pick)
                die = random.choice(temp)
                
            image = self.dice[die - 1]
            self.screen.blit(image, (440, 440))
            pygame.display.update(440, 440, 200, 200)
            pygame.time.wait(100)
            
            if n == 19:
                roll = die
                self.screen.blit(image, (440, 440))
                pygame.display.update(440, 440, 200, 200)
                
        return roll

##    rollList = [5, 6, 2, 2, 5, 6, 2, 2, 5, 6, 2, 2]
##    def roll_dice(self):
##        return Game.rollList.pop(0)

    def open_mini_game(self, pos, start_pos, player):
        for n in range(4):
            if (pos == start_pos[n] and player.mini_games[n] == 0):
                if n == 0:
                    block_fade = BlockFade(self.screen)
                    points_temp = list(block_fade.points)
                    self.add_points(points_temp)
                if n == 1:
                    frogger = Frogger(self.screen)
                    points_temp = list(frogger.points_ended)
                    self.add_points(points_temp)
                if n == 2:
                    pong = Pong4(self.screen)
                    points_temp = list(pong.points_ended)
                    self.add_points(points_temp)
                if n == 3:
                    shooter = Shooter(self.screen)
                    points_temp = list(shooter.points_ended)
                    self.add_points(points_temp)
                player.mini_games[n] = 1

        counter_end = 0
        for player in self.players:
            for n in range(4):
                if player.mini_games[n] == 1:
                    counter_end += 1
                    if counter_end == 16:
                        self.end_screen()
                    

    def add_points(self, points_temp):
        for m in range(4):
            player_temp = self.players[m]
            points_t = points_temp[m]
            player_temp.points += points_t
        self.show_points(points_temp)

    def show_points(self, points_temp):
        entry = False
        while not entry:
            self.screen.blit(self.centre_1, (250, 250))
            for score in points_temp:
                points = str(score)
                text = self.font.render(('Du fik: '+points+' point'), True, (255, 255, 255))
                rotation, pos = self.rotate(score, points_temp, text, self.part_score_pos)
                self.screen.blit(rotation, pos)

            self.screen.blit(self.blue_button[self.turn_index], self.blue_button_pos[self.turn_index])
            
            pygame.display.update(250, 250, 600, 600)
        
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ( event.button == 1 and self.turn_index == 0 ) or \
                       ( event.button == 3 and self.turn_index == 3 ):
                        entry = True  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                    if ( event.key == pygame.K_z and self.turn_index == 1) or \
                        ( event.key == pygame.K_x and self.turn_index == 2 ):
                        entry = True

    def rotate(self, element, list, surface, positions):
        rotation = surface
        pos = None
        if element == list[0]:
            pos = positions[0]
            rotation = pygame.transform.rotate(surface, 180)
        elif element == list[1]:
            pos = positions[1]
            rotation = pygame.transform.rotate(surface, 90)
        elif element == list[2]:
            pos = positions[2]
        elif element == list[3]:
            pos = positions[3]
            rotation = pygame.transform.rotate(surface, -90)
        return rotation, pos

    def end_screen(self):
        scores = []
        for player in self.players:
            scores.append(player.points)
        winner_score = max(scores)
        for n in range(4):
            score = scores[n]
            if winner_score == score:
                self.players[n].winner = True
                
        end = False
        while not end:
            
            self.screen.blit(self.centre_1, (250, 250))            
            for player in self.players:
                points = str(player.points)
                if player.winner == True:
                    message = 'Du vandt med: '
                else:
                    message = 'Du tabte med: '
                text = self.font.render((message+points+' point'), True, (255, 255, 255))
                rotation, pos = self.rotate(player, self.players, text, self.part_score_pos)
                self.screen.blit(rotation, pos)
                
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ( event.button == 1 and self.players[0].winner ) or \
                       ( event.button == 3 and self.players[3].winner ):
                        end = False
                        pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                    if ( event.key == pygame.K_z and self.players[1].winner ) or \
                        ( event.key == pygame.K_x and self.players[2].winner ):
                        end = False
                        pygame.display.quit()
   
    def main(self):
        while True:
            
            time = self.clock.tick(30)
            time_seconds = time/1000.
            self.timer += self.clock.get_rawtime()/1000.
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                    if ( event.key == pygame.K_f and self.turn_index == 0 ) or \
                        ( event.key == pygame.K_1 and self.turn_index == 1 ) or \
                        ( event.key == pygame.K_2 and self.turn_index == 2 ) or \
                        ( event.key == pygame.K_g and self.turn_index == 3 ):
                        self.round += 1
                        if self.round == 4: self.round = 0
                        number = self.roll_dice()
                        pygame.time.wait(2000)
                        self.players[self.round].Animation(number)
                        t = self.timer 
                        
            self.screen.blit(self.background, (0,0))

            self.screen.blit(self.centre_0, (250, 250))
    
            for player in self.players:

                x, y = player.x_pos
                for n in range(4):
                    mini_game = player.mini_games[n]
                    if mini_game == 0:
                        self.screen.blit(self.xs[0], (x, y))
                    else:
                        if player.number == 0: self.screen.blit(self.xs[1], (x, y))
                        elif player.number == 1: self.screen.blit(self.xs[2], (x, y))
                        elif player.number == 2: self.screen.blit(self.xs[3], (x, y))
                        elif player.number == 3: self.screen.blit(self.xs[4], (x, y))
                    if player.number == 0: x += 50
                    elif player.number == 1: y += 50
                    elif player.number == 2: x -= 50
                    elif player.number == 3: y -= 50

                rotation, pos = self.rotate(player, self.players, self.icon_games, self.icon_pos)
                self.screen.blit(rotation, pos)

                self.screen.blit(self.turn_token, self.turn_token_pos[self.token_index])

                points = player.points
                text = self.font.render(str(points), True, (255, 0, 0))
                rotation, pos = self.rotate(player, self.players, text, self.score_pos)
                self.screen.blit(rotation, pos)

                if player.animation:
                    timer = float(str(self.timer)[:4])
                    try:
                        pos = player.poss[0]
                        if timer >= t + 0.7: pos = player.poss[0]
                        if timer >= t + 4 + 0.7: pos = player.poss[1]
                        if timer >= t + 4 + 1.4: pos = player.poss[2]
                        if timer >= t + 4 + 2.1: pos = player.poss[3]
                        if timer >= t + 4 + 2.8: pos = player.poss[4]
                        if timer >= t + 4 + 3.5: pos = player.poss[5]

                        for pos_1 in player.start_pos:
                            if pos_1 == pos:
                                self.home = True
                        if self.home: d = 50
                        else: d = 7
                        self.home = False
                        x = pos[0] + d
                        y = pos[1] + d
                        self.screen.blit(self.player_path, (x, y))
                        
                        if timer >= t + 4 + 3: raise IndexError
                                               
                    except IndexError:
                        pygame.time.wait(500)
                        player.move(number)
                        self.turn_index += 1
                        if self.turn_index == 4: self.turn_index = 0
                        self.token_index = self.turn_index
                        player.animation = False

                for pos in player.start_pos:
                    if pos == player.pos:
                        player.home = True
                if player.home:
                    d_x = 35
                    d_y = 25
                else:
                    d_x = -15
                    d_y = -10
                player.home = False
                x = player.pos[0] + d_x
                y = player.pos[1] + d_y
                self.screen.blit(player.image, (x, y))

            player = self.players[self.turn_index]
            if int(self.timer)%2 == 0:
                for pos in player.start_pos:
                    if pos == player.pos:
                        player.home = True
                if player.home:
                    d_x = 5
                    d_y = 15
                else:
                    d_x = 55
                    d_y = 50
                player.home = False
                self.screen.blit(self.ring, (player.pos[0] - d_x, player.pos[1] - d_y))


            pygame.display.update()

            for player in self.players:
                if player.pos == self.positions[5] or \
                   player.pos == self.positions[11]:
                    player.pos = self.positions[0]
                elif player.pos == self.positions[2] or \
                     player.pos == self.positions[22]:
                    player.pos = self.positions[7]
                elif player.pos == self.positions[18] or \
                     player.pos == self.positions[24]:
                    player.pos = self.positions[13]
                elif player.pos == self.positions[9] or \
                     player.pos == self.positions[15]:
                    player.pos = self.positions[20]                     
                elif player.pos == self.positions[3]:
                    player.pos = self.positions[1]
                    player.check_points()
                elif player.pos == self.positions[4]:
                    player.pos = self.positions[6]
                    player.check_points()
                elif player.pos == self.positions[16]:
                    player.pos = self.positions[19]
                    player.check_points()
                elif player.pos == self.positions[17]:
                    player.pos = self.positions[14]
                    player.check_points()

            for player in self.players:
                for pos in player.start_pos:
                    if pos == player.pos and player.moved:
                        self.open_mini_game(player.pos, player.start_pos, player)
                    
Game()
