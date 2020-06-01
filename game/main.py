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
playerY = 100
playerY_change = 0

def playerChange(y):
    screen.blit(player, (100, y))

#enemy
enemy = pygame.image.load('player.png')

#ball
ball = pygame.image.load('ball.png')


running = True
while running :

    #if you want to close the window and pressed X
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    #if you pressed the key :
    if (event.type == pygame.KEYDOWN ):
        if (event.key == pygame.K_UP):
            playerY_change -= 10
        if (event.key == pygame.K_DOWN):
            playerY_change += 10

    #if you take your hand of the key
    if (event.type == pygame.KEYUP):
        if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
            playerY_change = 0

    #add player
    playerChange(playerY+ playerY_change)

    #add enemy
    screen.blit(enemy, (70,90))

    #add ball
    screen.blit(ball, (46, 250))

    pygame.display.update()

