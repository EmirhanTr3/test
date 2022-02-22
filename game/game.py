import pygame
from pygame.constants import K_KP_MINUS

def block_moment(screen, block, x, y):
    screen.blit(block,(x,y))
    pygame.display.flip()

def message_display(screen, text, boyut, center):
    font = pygame.font.Font('freesansbold.ttf', boyut)
    TextSurf = font.render(text, True, (0,0,0))
    TextRect = TextSurf.get_rect()
    TextRect.center = center #(512,250)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def game():

    pygame.init()

    size = (1024,550)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Emirhan")
    pygame.display.set_icon(pygame.image.load("resources\\icon.png").convert())
    

    color = (220,90,200)

    screen.fill(color)

    block = pygame.image.load("resources\\image.png").convert()
    x = 0
    y = 0
    screen.blit(block, (x,y))

    running = True
    paused = False
    multi = 2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if paused == False:
                        paused = True
                        print("game paused")
                        message_display(screen, "PAUSED", 60, ((pygame.display.Info().current_w/2),200))
                        message_display(screen, "Press ESC to continue." , 30, ((pygame.display.Info().current_w/2),270))
                    elif paused == True:
                        paused = False
                        print("game resumed")
                if paused == False:
                    if event.key == pygame.K_KP_PLUS:
                        multi += 1
                    elif event.key == pygame.K_KP_MINUS:
                        multi -= 1
        if paused == False:
            keys = pygame.key.get_pressed()

            if multi <= 0:
                multi = 1

            x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * multi
            y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * multi
            x += (keys[pygame.K_d] - keys[pygame.K_a]) * multi
            y += (keys[pygame.K_s] - keys[pygame.K_w]) * multi

            x = x % screen.get_width()
            y = y % screen.get_height()

            screen.fill(color)
            block_moment(screen,block,x,y)

            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    game()