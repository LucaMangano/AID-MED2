import random
import pygame
##from pieces_rects import pieces_rects

class PieceTop():
    def __init__(self, pieces_list, pos):
        self.x, self.y = pos

        self.dy = 1
        self.dx_right = self.dx_left = 20
        
        I = pieces_list[0]
        J = pieces_list[1]
        L = pieces_list[2]
        O = pieces_list[3]
        S = pieces_list[4]
        T = pieces_list[5]
        Z = pieces_list[6]
        
        pieces = [ I, J, L, O, S, T, Z ]
        list_index = 0
        
        self.choice = random.randint(0,6)
        self.images = pieces[self.choice]
        self.images_index = 0

        self.once = 0
        
        self.falling = True
        self.stopping = False
        self.rotate = True
        self.right_locked = False
        self.left_locked = False
        self.ereased = False

    def falls(self):
        self.y += self.dy
        height = self.images[self.images_index].get_height()
        if self.y >= 250 + 300 - height:
            self.dy = 0
            self.dx = 0
            self.y = 250 + 300 - height
            self.falling = False
            self.stopping = True

    def moves_right(self):
        self.x += self.dx_right
        width = self.images[self.images_index].get_width()
        if self.x >= 250 + 400 - width:
            self.x = 250 + 400 - width

    def moves_left(self):
        self.x -= self.dx_left
        if self.x <= 250 + 200:
            self.x = 250 + 200


    def rotates(self):
        width = self.images[self.images_index].get_width()
        if self.x >= 250 + 400 - width:
            if self.images[self.images_index] == self.images[-1]:
                self.images_index = 0
            else:
                self.images_index += 1

            width = self.images[self.images_index].get_width()
            if self.x + width >= 250 + 400:
                if self.images[self.images_index] == self.images[0]:
                    self.images_index = -1
                else:
                    self.images_index -= 1
            self.rotate = False
        else:
            self.rotate = True
            
        if self.rotate:
            if self.images[self.images_index] == self.images[-1]:
                self.images_index = 0
            else:
                self.images_index += 1

    def update_rect(self):
        pieces_rects_up = [ [ [ pygame.Rect(self.x, self.y, 20, 3) ], #I 1
                           [ pygame.Rect(self.x, self.y, 80, 3) ] ], #I 2

                         [ [ pygame.Rect(self.x + 20, self.y, 20, 3), #J 1
                             pygame.Rect(self.x, self.y + 40, 20, 3) ],
                           [ pygame.Rect(self.x, self.y, 20, 3), #J 2
                             pygame.Rect(self.x + 20, self.y + 20, 40, 3) ],
                           [ pygame.Rect(self.x, self.y, 40, 3) ], #J 3
                           [ pygame.Rect(self.x, self.y, 60, 3) ] ], #J 4

                         [ [ pygame.Rect(self.x, self.y, 20, 3), #L 1
                             pygame.Rect(self.x + 20, self.y + 40, 20, 3) ],
                           [ pygame.Rect(self.x, self.y, 60, 3) ], #L 2
                           [ pygame.Rect(self.x, self.y, 40, 3) ], #L 3
                           [ pygame.Rect(self.x + 40, self.y, 20, 3), #L 4
                             pygame.Rect(self.x, self.y + 20, 40, 3) ] ],

                         [ [ pygame.Rect(self.x, self.y, 40, 3) ] ], #O

                         [ [ pygame.Rect(self.x + 20, self.y, 40, 3), #S 1
                             pygame.Rect(self.x, self.y + 20, 20, 3) ],
                           [ pygame.Rect(self.x, self.y, 20, 3), #S 2
                             pygame.Rect(self.x + 20, self.y + 20, 20, 3) ] ],

                         [ [ pygame.Rect(self.x, self.y, 60, 3) ], #T 1
                           [ pygame.Rect(self.x + 20, self.y, 20, 3), #T 2
                             pygame.Rect(self.x, self.y + 20, 20, 3) ],
                           [ pygame.Rect(self.x + 20, self.y, 20, 3), #T 3
                             pygame.Rect(self.x, self.y + 20, 20, 3),
                             pygame.Rect(self.x + 40, self.y + 20, 20, 3) ],
                           [ pygame.Rect(self.x, self.y, 20, 3), #T 4
                             pygame.Rect(self.x + 20, self.y + 20, 20, 3) ] ],

                         [ [ pygame.Rect(self.x, self.y, 40, 3), #Z 1
                             pygame.Rect(self.x + 40, self.y + 20, 20, 3) ],
                           [ pygame.Rect(self.x + 20, self.y, 20, 3), #Z 2
                             pygame.Rect(self.x, self.y + 20, 20, 3) ] ] ]
        
        pieces_rects_down = [ [ [ pygame.Rect(self.x, self.y + 79, 20, 3) ], #I 1
                                [ pygame.Rect(self.x, self.y + 20, 80, 3) ] ], #I 2
                              [ [ pygame.Rect(self.x, self.y + 59, 40, 3) ],
                                [ pygame.Rect(self.x, self.y + 39, 60, 3) ],
                                [ pygame.Rect(self.x + 20, self.y + 19, 20, 3),
                                  pygame.Rect(self.x, self.y + 59, 20, 3) ], #J 3
                                [ pygame.Rect(self.x, self.y + 19, 40, 3),
                                  pygame.Rect(self.x + 40, self.y + 39, 20, 3) ] ], #J 4
                              [ [ pygame.Rect(self.x, self.y + 59, 40, 3) ],
                                [ pygame.Rect(self.x + 20, self.y + 19, 40, 3),
                                  pygame.Rect(self.x, self.y + 39, 20, 3) ], #L 2
                                [ pygame.Rect(self.x, self.y + 19, 20, 3),
                                  pygame.Rect(self.x + 20, self.y + 59, 20, 3) ], #L 3
                                [ pygame.Rect(self.x, self.y + 39, 60, 3) ] ],
                              [ [ pygame.Rect(self.x, self.y + 39, 40, 3) ] ], #O
                              [ [ pygame.Rect(self.x + 40, self.y + 19, 20, 3),
                                  pygame.Rect(self.x, self.y + 39, 40, 3) ],
                                [ pygame.Rect(self.x, self.y + 39, 20, 3),
                                  pygame.Rect(self.x + 20, self.y + 59, 20, 3) ] ],
                             [ [ pygame.Rect(self.x, self.y + 19, 20, 3),
                                 pygame.Rect(self.x + 40, self.y + 19, 20, 3),
                                 pygame.Rect(self.x + 20, self.y + 39, 20, 3) ], #T 1
                               [ pygame.Rect(self.x, self.y + 39, 20, 3),
                                 pygame.Rect(self.x + 20, self.y + 59, 20, 3) ],
                               [ pygame.Rect(self.x, self.y + 39, 60, 3) ],
                               [ pygame.Rect(self.x + 20, self.y + 39, 20, 3),
                                 pygame.Rect(self.x, self.y + 59, 20, 3) ] ],
                             [ [ pygame.Rect(self.x, self.y + 19, 20, 3),
                                 pygame.Rect(self.x + 20, self.y + 39, 40, 3) ],
                               [ pygame.Rect(self.x + 20, self.y + 39, 20, 3),
                                 pygame.Rect(self.x, self.y + 59, 20, 3) ] ] ]

        pieces_rects_left = [ [ [ pygame.Rect(self.x, self.y, 3, 80) ],
                                [ pygame.Rect(self.x, self.y, 3, 20) ] ],
                              
                              [ [ pygame.Rect(self.x + 20, self.y, 3, 40),
                                  pygame.Rect(self.x, self.y + 40, 3, 20)],
                                [ pygame.Rect(self.x, self.y, 3, 40) ],
                                [ pygame.Rect(self.x, self.y, 3, 60) ],
                                [ pygame.Rect(self.x, self.y, 3, 20),
                                  pygame.Rect(self.x + 40, self.y + 20, 3, 20) ] ],

                              [ [ pygame.Rect(self.x, self.y, 3, 60) ],
                                [ pygame.Rect(self.x, self.y, 3, 40) ],
                                [ pygame.Rect(self.x, self.y, 3, 20),
                                  pygame.Rect(self.x + 20, self.y + 20, 3, 40) ],
                                [ pygame.Rect(self.x, self.y + 20, 3, 20),
                                  pygame.Rect(self.x + 40, self.y, 3, 20) ] ],

                              [ [ pygame.Rect(self.x, self.y, 3, 40) ] ],

                              [ [ pygame.Rect(self.x, self.y + 20, 3, 20),
                                  pygame.Rect(self.x + 20, self.y, 3, 20) ],
                                [ pygame.Rect(self.x, self.y, 3, 40),
                                  pygame.Rect(self.x + 20, self.y + 40, 3, 20) ] ],

                              [ [ pygame.Rect(self.x, self.y, 3, 20),
                                  pygame.Rect(self.x + 20, self.y + 20, 3, 20) ],
                                [ pygame.Rect(self.x, self.y + 20, 3, 20),
                                  pygame.Rect(self.x + 20, self.y, 3, 20),
                                  pygame.Rect(self.x + 20, self.y + 40, 3, 20) ],
                                [ pygame.Rect(self.x, self.y + 20, 3, 20),
                                  pygame.Rect(self.x + 20, self.y, 3, 20) ],
                                [ pygame.Rect(self.x, self.y, 3, 60) ] ],

                              [ [ pygame.Rect(self.x, self.y, 3, 20),
                                  pygame.Rect(self.x + 20, self.y + 20, 3, 20) ],
                                [ pygame.Rect(self.x, self.y + 20, 3, 40),
                                  pygame.Rect(self.x + 20, self.y, 3, 20) ] ] ]
                                  

        pieces_rects_right = [ [ [ pygame.Rect(self.x + 19, self.y, 3, 80) ],
                                 [ pygame.Rect(self.x + 79, self.y, 3, 20) ] ],
                               
                               [ [ pygame.Rect(self.x + 39, self.y, 3, 60) ],
                                 [ pygame.Rect(self.x + 19, self.y, 3, 20),
                                   pygame.Rect(self.x + 59, self.y + 20, 3, 20) ],
                                 [ pygame.Rect(self.x + 19, self.y + 20, 3, 40),
                                   pygame.Rect(self.x + 39, self.y, 3, 20) ],
                                 [ pygame.Rect(self.x + 59, self.y, 3, 40) ] ],

                               [ [ pygame.Rect(self.x + 19, self.y, 3, 40),
                                   pygame.Rect(self.x + 39, self.y + 40, 3, 20) ],
                                 [ pygame.Rect(self.x + 19, self.y + 20, 3, 20),
                                   pygame.Rect(self.x + 59, self.y, 3, 20) ],
                                 [ pygame.Rect(self.x + 39, self.y, 3, 60) ],
                                 [ pygame.Rect(self.x + 59, self.y, 3, 40) ] ],

                               [ [ pygame.Rect(self.x + 39, self.y, 3, 40) ] ],

                               [ [ pygame.Rect(self.x + 39, self.y + 20, 3, 20),
                                   pygame.Rect(self.x + 59, self.y, 3, 20) ],
                                 [ pygame.Rect(self.x + 19, self.y, 3, 20),
                                   pygame.Rect(self.x + 39, self.y + 20, 3, 40) ] ],

                               [ [ pygame.Rect(self.x + 39, self.y + 20, 3, 20),
                                   pygame.Rect(self.x + 59, self.y, 3, 20) ],
                                 [ pygame.Rect(self.x + 39, self.y, 3, 60) ],
                                 [ pygame.Rect(self.x + 39, self.y, 3, 20),
                                   pygame.Rect(self.x + 59, self.y + 20, 3, 20) ],
                                 [ pygame.Rect(self.x + 19, self.y, 3, 20),
                                   pygame.Rect(self.x + 19, self.y + 40, 3, 20),
                                   pygame.Rect(self.x + 39, self.y + 20, 3, 20) ] ],

                               [ [ pygame.Rect(self.x + 39, self.y, 3, 20),
                                   pygame.Rect(self.x + 59, self.y + 20, 3, 20) ],
                                 [ pygame.Rect(self.x + 19, self.y + 40, 3, 20),
                                   pygame.Rect(self.x + 39, self.y, 3, 40) ] ] ]

                                   
        self.rects_up = pieces_rects_up[self.choice]
        self.rects_down = pieces_rects_down[self.choice]
        self.rects_left = pieces_rects_left[self.choice]
        self.rects_right = pieces_rects_right[self.choice]

        
        
        
        




























        
