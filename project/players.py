class Player():
    def __init__(self, number, image, start_pos, pos, all_pos, x_pos):
        self.number = number
        self.image = image
        self.start_pos = start_pos
        self.pos = pos
        self.all_pos = all_pos
        self.moved = False
        self.home = False
        self.mini_games = [ 0, 0, 0, 0 ]
        self.x_pos = x_pos
        self.animation = False
        self.points = 1000
        self.winner = False

    def Animation(self, steps):
        self.animation = True
        self.poss = []
        initial_pos = None
        for n in range(0, len(self.all_pos)):
            pos = self.all_pos[n]
            if pos == self.pos:
                initial_pos = n + 1
                if initial_pos >= 26:
                    initial_pos -= 26 
        for n in range(steps):
            self.poss.append(self.all_pos[initial_pos])
            initial_pos += 1
            if initial_pos >= 26: initial_pos -= 26
        
    def move(self, steps):
        self.moved = True
        initial_pos = None
        for n in range(0, len(self.all_pos)):
            pos = self.all_pos[n]
            if pos == self.pos:
                initial_pos = n

        change = initial_pos + steps
        if change >= 26: change -= 26
        self.pos = self.all_pos[change]

        self.check_points()

    def check_points(self):
        if self.pos == self.all_pos[1] or \
           self.pos == self.all_pos[12] or \
           self.pos == self.all_pos[14] or \
           self.pos == self.all_pos[25]:
            self.points += 100
        elif  self.pos == self.all_pos[6] or \
             self.pos == self.all_pos[8] or \
             self.pos == self.all_pos[19] or \
             self.pos == self.all_pos[21]:
            self.points -= 100        
