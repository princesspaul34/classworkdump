
import pygame


pygame.init() #start pygame before we ask to make a window
screen = pygame.display.set_mode((600, 600)) #make our 600 by 600 pixel window
pygame.display.set_caption("Snake dash 1")
game_running = True # this labelled box remmbers whether the game is open
x_axis =300
y_axis =300
width = 10
height = 10
while game_running: #keep showing the window until the user closes it
    for event in pygame.event.get(): # check everything since that last turn
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN: # check if a key was pressed
            if event.key == pygame.K_UP:
                y_axis -= 10
            if event.key == pygame.K_DOWN:
                y_axis += 10
            if event.key == pygame.K_LEFT:
                x_axis -= 10
            if event.key == pygame.K_RIGHT:
                x_axis += 10
            
    screen.fill((135, 206, 235)) # paint a calm green background every frame
    pygame.draw.rect(screen, (0, 128, 0), (x_axis, y_axis, width, height)) # draw a green square at x=300, y=300 with width=10 and height=10
    pygame.display.update() # put our drawing on the real window

pygame.quit() #tidy up after the loop ends
