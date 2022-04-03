import pygame 
import sys 
import pyautogui
from character import Player

width, height = pyautogui.size()

#######################################     Itizialithation
pygame.init() 

size = (width, height) 
screen = pygame.display.set_mode(size) 
color = (0, 0, 0) 
  

#######################################     Running
running = True
while running:           
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if running == False:
            pygame.quit()

        else:
            pass


                  
      

      
    pygame.display.update() 

