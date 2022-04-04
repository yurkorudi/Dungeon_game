import pygame 
import sys 
import pyautogui
from character import Player
from pygame.locals import *
p = pygame
width, height = pyautogui.size()

#######################################     Itizialithation
p.init() 

size = (width, height) 
screen = pygame.display.set_mode(size) 
screen.set_alpha(128)
black = (0, 50, 100) 
clock = pygame.time.Clock()
screen.fill(black)
  
######################################      Functions
def button1():
    p.draw.rect(screen, (250, 0, 0), p.Rect(width-20, 0, width, 20))


player = Player(name_of_charakter='Baky', path_to_sprite='./sprites/Baky', x=width/2, y=height/2)



#######################################     Running
running = True
while running:        
    for event in p.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            p.quit()
        else:
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                if pos[0] >= width-20 and pos[0] <= width and pos[1] >= 0 and pos[1] <= 20:
                    pygame.quit()
                    sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x = player.x - player.step
        player.STATE = 'go_left'
    if keys[pygame.K_RIGHT]:
        player.x = player.x + player.step
        player.STATE = 'go_right'
    if keys[pygame.K_DOWN]:
        player.y = player.y + player.step
        player.STATE = 'go_down'
    if keys[pygame.K_UP]:
        player.y = player.y - player.step
        player.STATE = 'go_up'

    if event.type == pygame.KEYUP:
        if player.STATE == 'go_left':
            player.STATE = 'stand_left'
        elif player.STATE == 'go_right':
            player.STATE = 'stand_right'
        else:
            player.state = 'stand'
                

    player.change_sprites()
    screen.fill(black)
    player.draw(screen)
    button1()




                    
        

    pygame.display.flip()
    clock.tick(30)
    pygame.display.update() 

