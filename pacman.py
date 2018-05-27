
import pygame
import spritesheet
from sprite_strip_anim import SpriteStripAnim

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pacman_width = 35
pacman_height = 35

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()



ss = spritesheet.spritesheet("todos.png")

def pacman(x,y,img): # se define la funcion pacman,
    gameDisplay.blit(img,(x,y)) # se muestra el pacman en el display

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    image = ss.image_at((3, 90, 16, 16))


    img = image

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not x < 0:
                    x_change = -3
                elif event.key == pygame.K_RIGHT and not x > display_width - pacman_width:
                    x_change = 3
                elif event.key == pygame.K_UP and not y < 0:
                    y_change = -3
                elif event.key == pygame.K_DOWN and not y > display_height - pacman_height:
                    y_change = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            print(event)

        x += x_change
        y += y_change

        gameDisplay.fill(black) #tiene que ir antes de las imagenes, es el color del fondo
        pacman(x,y,img) # se muestra donde se coloca el pacman

        if x > display_width - pacman_width or x < 0:
            x_change = 0
        if y > display_height - pacman_height or y < 0:
            y_change = 0



        pygame.display.update()

        clock.tick(60) #frames per seccond



game_loop()
pygame.quit()
quit()
