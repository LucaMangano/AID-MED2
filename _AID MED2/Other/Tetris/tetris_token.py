import pygame

class Token():
    def __init__(self, screen, image, x, y, piece, piece_index):
        self.screen = screen
        self.x = x
        self.y = y

        self.image = image

        self.rects_top = []
        self.rects_left = []
        self.rects_right = []

        grids = ( ( ( (1, 0, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0) ),

                 ( (1, 1, 1, 1), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0) ) ),

               ( ( (0, 1, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0) ),

                 ( (1, 0, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (1, 1, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (1, 1, 1, 0), (0, 0, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0) ) ),

               ( ( (1, 0, 0, 0), (1, 0, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0) ),
                 
                 ( (1, 1, 1, 0), (1, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (1, 1, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0) ),
                 
                 ( (0, 0, 1, 0), (1, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0) ) ),

               ( ( (1, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (1, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0) ) ),

               ( ( (0, 1, 1, 0), (1, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (1, 0, 0, 0), (1, 1, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0) ) ),

               ( ( (1, 1, 1, 0), (0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (0, 1, 0, 0), (1, 1, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0) ),

                 ( (0, 1, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0) ) ),

               ( ( (1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0) ),

                 ( (0, 1, 0, 0), (1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0) ) ) )

        grid = grids[piece]
        self.grid = grid[piece_index]
        self.once = True
        
        self.create_rects()

    def create_rects(self):
        self.dx = self.x
        self.dy = self.y
        for row in self.grid:
            for piece in row:
                if piece == 1:
                    rect = pygame.Rect(self.x, self.y, 20, 3)
                    self.rects_top.append(rect)
                    rect = pygame.Rect(self.x - 3, self.y + 1, 3, 19)
                    self.rects_left.append(rect)
                    rect = pygame.Rect(self.x + 19, self.y + 1, 3, 19)
                    self.rects_right.append(rect)
                    self.x += 20
                else:
                    self.x += 20
            self.y += 20
            self.x = self.dx
            
    def blit(self):
        self.x = self.dx
        self.y = self.dy
        for row in self.grid:
            for piece in row:                    
                if piece == 1:
                    self.screen.blit(self.image, (self.x, self.y))
                    self.x += 20
                else:
                    self.x += 20
            self.y += 20
            self.x = self.dx
            
                

        
        
        
        
        
