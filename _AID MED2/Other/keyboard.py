import pygame

def beginning():
    keys = [ [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p' ],
             [ 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l' ],
             [ 'z', 'x', 'c', 'v', 'b', 'n', 'm' ] ]
    screen = pygame.display.set_mode((810, 520), 0, 32)
    player = 1
    pygame.font.init()
    font = pygame.font.SysFont( "times", 64)
    font_1 = pygame.font.SysFont('times', 50)
    text_name = font_1.render("Write your name - ", True, (0, 0, 255))
    player_n = font_1.render("Player "+str(player), True, (0, 0, 255))
    players_names = []
    z, k = 100, 110
    name = ''
    
    beginning = True
    while beginning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if k == 110:
                        if z == 100:
                            name += 'q'
                        elif z == 164:
                            name += 'w'
                        elif z == 228:
                            name += 'e'
                        elif z == 292:
                            name += 'r'
                        elif z == 356:
                            name += 't'
                        elif z == 420:
                            name += 'y'
                        elif z == 484:
                            name += 'u'
                        elif z == 548:
                            name += 'i'
                        elif z == 612:
                            name += 'o'
                        elif z == 676:
                            name += 'p'
                    elif k == 210:
                        if z == 132:
                            name += 'a'
                        elif z == 196:
                            name += 's'
                        elif z == 260:
                            name += 'd'
                        elif z == 324:
                            name += 'f'
                        elif z == 388:
                            name += 'g'
                        elif z == 452:
                            name += 'h'
                        elif z == 516:
                            name += 'j'
                        elif z == 580:
                            name += 'k'
                        elif z == 644:
                            name += 'l'
                    elif k == 310:
                        if z == 164:
                            name += 'z'
                        elif z == 228:
                            name += 'x'
                        elif z == 292:
                            name += 'c'
                        elif z == 356:
                            name += 'v'
                        elif z == 420:
                            name += 'b'
                        elif z == 484:
                            name += 'n'
                        elif z == 548:
                            name += 'm'
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                if event.key == pygame.K_ESCAPE:
                    players_names.append(name)
                    player += 1
                    player_n = font_1.render("Player "+str(player), True, (0, 0, 255))
                    name = ''
                    if player == 5:
                        return players_names
                if event.key == pygame.K_UP:
                    k -= 100
                    z -= 32
                    if k < 110:
                        k = 110
                        z += 32
                if event.key == pygame.K_DOWN:
                    k += 100
                    z += 32
                    if z >= 676 and k == 210:
                        z = 644
                        k = 210
                    elif z >= 516 and k == 310:
                        z = 548
                        k = 310
                    elif k > 310:
                        z -= 32
                        k = 310
                if event.key == pygame.K_RIGHT:
                    z += 64
                    if z >= 676 and k == 110: z = 676
                    if z >= 644 and k == 210: z = 644
                    if z >= 548 and k == 310: z = 548
                if event.key == pygame.K_LEFT:
                    z -= 64
                    if z <= 100 and k == 110: z = 100
                    if z <= 132 and k == 210: z = 132
                    if z <= 164 and k == 310: z = 164
                    
        screen.fill((0,0,0))
        x, y = 100, 100
        for n in range(len(keys)):
            key = keys[n]
            for m in range(len(keys[n])):
                text = font.render(key[m], True, (255, 255, 0))
                screen.blit(text, (x, y))
                x += 64
            if n == 0: x = 132
            elif n == 1: x = 164
            y += 100
        pygame.draw.rect(screen, (0, 255, 0), (z, k, 64, 64), 1)
        screen.blit(text_name, (100, 25))
        screen.blit(player_n, (500, 25))
        text = font.render(name, True, (0, 0, 255))
        screen.blit(text, (100, 390))
        pygame.draw.rect(screen, (255, 0, 0), (100, 400, 610, 64), 1)
        pygame.display.update()

beginning()
