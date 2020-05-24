import pygame


#initlize the game
pygame.init()

#set caption and icon 
screen = pygame.display.set_mode((800, 600))
caption = pygame.display.set_caption("pong game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
player = pygame.image.load('player.png')

#enemy
enemy = pygame.image.load('player.png')

#ball
ball = pygame.image.load('ball.png')


running = True
while running :
    # add player
    screen.blit(player, (50, 60))
    #add enemy
    screen.blit(enemy, (10, 20))
    #add ball
    screen.blit(ball, (9, 15))


    pygame.display.update()