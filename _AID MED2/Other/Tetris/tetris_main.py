import pygame
from tetris_pieces import PieceTop
from tetris_token import Token

class Game():
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1080, 1080), 0, 32)

        self.background = pygame.image.load('images/background.png')

        self.pieces_list = [ [pygame.image.load('images/I (1).png'), pygame.image.load('images/I (2).png')],
                        
                        [pygame.image.load('images/J (1).png'), pygame.image.load('images/J (2).png'),
                         pygame.image.load('images/J (3).png'), pygame.image.load('images/J (4).png')],
                        
                        [pygame.image.load('images/L (1).png'), pygame.image.load('images/L (2).png'),
                         pygame.image.load('images/L (3).png'), pygame.image.load('images/L (4).png')],
                        
                        [pygame.image.load('images/O (1).png')],

                        
                        [pygame.image.load('images/S (1).png'), pygame.image.load('images/S (2).png')],
                        
                        [pygame.image.load('images/T (1).png'), pygame.image.load('images/T (2).png'),
                         pygame.image.load('images/T (3).png'), pygame.image.load('images/T (4).png')],
                        
                        [pygame.image.load('images/Z (1).png'), pygame.image.load('images/Z (2).png')] ]

        self.token = pygame.image.load('images/block.png')
        self.tokens = []

        self.token_positions = ( ( (450, 470), (470, 470), (490, 470), (510, 470), (530, 470), (550, 470), (570, 470), (590, 470), (610, 470), (630, 470) ),

                                 ( (450, 490), (470, 490), (490, 490), (510, 490), (530, 490), (550, 490), (570, 490), (590, 490), (610, 490), (630, 490) ),

                                 ( (450, 510), (470, 510), (490, 510), (510, 510), (530, 510), (550, 510), (570, 510), (590, 510), (610, 510), (630, 510) ),

                                 ( (450, 530), (470, 530), (490, 530), (510, 530), (530, 530), (550, 530), (570, 530), (590, 530), (610, 530), (630, 530) ) )

        self.checker = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]

        
        self.pieces_pos = [ (250 + 300, 250), (250 + 520, 250 + 300),
                            (250 + 300, 250 + 520), (250, 250 + 300) ]

        self.piece = PieceTop(self.pieces_list, self.pieces_pos[0])

        self.stopped_rects_up = []
        self.stopped_rects_left = []
        self.stopped_rects_right = []
        self.stopped_imgs = []
        self.stopped_coords = []

        self.clock = pygame.time.Clock()
        
        self.running()

    def running(self):
        running = True
        while running:
            time_passed = self.clock.tick(30)

            if self.piece.falling:
                self.piece.falls()
            elif self.piece.stopping and self.piece.once == 0:
                self.round_coordinate()
                self.tokens.append(Token(self.screen, self.token, self.piece.x, self.piece.y, self.piece.choice, self.piece.images_index))
                self.piece.stopping = False
                self.piece.once = 1
            else:
                self.piece = PieceTop(self.pieces_list, self.pieces_pos[0])
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                    if event.key == pygame.K_UP:
                        self.piece.rotates()
                    if event.key == pygame.K_RIGHT:
                        pos = self.piece.x
                        self.piece.moves_right()
                        for token in self.tokens:
                            for rect_left in token.rects_left:
                                for rect_right in rects_right:
                                    if rect_right.colliderect(rect_left):
                                        self.piece.x = pos
                    if event.key == pygame.K_LEFT:
                        pos = self.piece.x
                        self.piece.moves_left()
                        for token in self.tokens:
                            for rect_right in token.rects_right:
                                for rect_left in rects_left:
                                    if rect_left.colliderect(rect_right):
                                        self.piece.x = pos
                    if event.key == pygame.K_DOWN:
                        self.piece.dy = 5
                    if event.key == pygame.K_r:
                        Game()
                    if event.key == pygame.K_p:
                        pygame.time.wait(10000)
                
            self.screen.blit(self.background, (250 + 0, 250 + 0))

            self.screen.blit(self.piece.images[self.piece.images_index], (self.piece.x, self.piece.y))
            self.piece.update_rect() 
                
            rects_down = self.piece.rects_down[self.piece.images_index]
            rects_up = self.piece.rects_up[self.piece.images_index]
            rects_left = self.piece.rects_left[self.piece.images_index]
            rects_right = self.piece.rects_right[self.piece.images_index]
                    
            for token in self.tokens:
                for rect_top in token.rects_top:
                    for rect_down in rects_down:
                        if rect_down.colliderect(rect_top):
                            self.piece.falling = False
                            self.piece.stopping = True
                            break

            print self.tokens
            
            for token in self.tokens:
                for n in range(len(self.token_positions)):
                    positions = self.token_positions[n]
                    for m in range(len(positions)):
                        position = positions[m]
                        if position[0] == token.x and position[1] == token.y:
                            line = self.checker[n]
                            del line[m]
                            line.insert(m, 1)
                token.blit()

            pygame.display.update()

            self.screen.blit(self.background, (250, 250))
            pygame.display.update(250 + 200, 250 + 300, 200, 300)

    def round_coordinate(self):
        if self.piece.y <= 250 + 363 and self.piece.y > 250 + 357:
            self.piece.y = 250 + 360
        elif self.piece.y <= 250 + 343 and self.piece.y > 250 + 337:
            self.piece.y = 250 + 340
        elif self.piece.y <= 250 + 323 and self.piece.y > 250 + 317:
            self.piece.y = 250 + 320
        elif self.piece.y <= 250 + 303 and self.piece.y > 250 + 297:
            self.piece.y = 250 + 300
        elif self.piece.y <= 250 + 283 and self.piece.y > 250 + 277:
            self.piece.y = 250 + 280
        elif self.piece.y <= 250 + 263 and self.piece.y > 250 + 257:
            self.piece.y = 250 + 260
        elif self.piece.y <= 250 + 243 and self.piece.y > 250 + 237:
            self.piece.y = 250 + 240
        elif self.piece.y <= 250 + 223 and self.piece.y > 250 + 217:
            self.piece.y = 250 + 220
        elif self.piece.y <= 250 + 203 and self.piece.y > 250 + 197:
            self.piece.y = 250 + 200
        elif self.piece.y <= 250 + 183 and self.piece.y > 250 + 177:
            self.piece.y = 250 + 180
        elif self.piece.y <= 250 + 163 and self.piece.y > 250 + 157:
            self.piece.y = 250 + 160
        elif self.piece.y <= 250 + 143 and self.piece.y > 250 + 137:
            self.piece.y = 250 + 140
        elif self.piece.y <= 250 + 123 and self.piece.y > 250 + 117:
            self.piece.y = 250 + 120
        elif self.piece.y <= 250 + 103 and self.piece.y > 250 + 97:
            self.piece.y = 250 + 100
        elif self.piece.y <= 250 + 93 and self.piece.y > 250 + 77:
            self.piece.y = 250 + 80
        elif self.piece.y <= 250 + 63 and self.piece.y > 250 + 57:
            self.piece.y = 250 + 60
        elif self.piece.y <= 250 + 43 and self.piece.y > 250 + 37:
            self.piece.y = 250 + 40                    

Game()


























