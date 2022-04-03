import pygame 
import sys 
import pyautogui
from character import Player
p = pygame
width, height = pyautogui.size()

#######################################     Itizialithation
p.init() 

size = (width, height) 
screen = p.display.set_mode(size) 
black = (0, 0, 0) 
screen.fill(black)
  
######################################      Functions

p.draw.rect(screen, (250, 0, 0), p.Rect(width-20, 0, width, 20))
player = Player(name_of_charakter='Baky', path_to_sprite='./sprites/Baky')



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




                    
        

            pygame.display.flip()
            pygame.display.update() 

