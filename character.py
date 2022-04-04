import os, os.path
import pygame
from tkinter import *
t = Tk()

class Player:
# Sates: stand, stand_left, stand_right, go_left, go_right, go_up, go_down
#
#
    def __init__(self, name_of_charakter, path_to_sprite, x, y):
        self.STATE = 'stand'
        self.y = y
        self.x = x
        self.left_right_frame = 0
        self.up_down_frame = 0
        self.step = 5
        self.up_list = []
        self.down_list = []
        self.left_list = []
        self.right_list = []
        self.stand_list = []
        for i in range(len(os.listdir(path_to_sprite+'/Up'))):
            image = pygame.image.load(path_to_sprite+'/Up/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.up_list.append(image)
        print('Done with: ', self.up_list)

        for i in range(len(os.listdir(path_to_sprite+'/Down'))):
            image = pygame.image.load(path_to_sprite+'/Down/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.down_list.append(image)
        print('Done with: ', self.down_list)

        for i in range(len(os.listdir(path_to_sprite+'/Left'))):
            image = pygame.image.load(path_to_sprite+'/Left/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.left_list.append(image)
        print('Done with: ', self.left_list)

        for i in range(len(os.listdir(path_to_sprite+'/Right'))):
            image = pygame.image.load(path_to_sprite+'/Right/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.right_list.append(image)
        print('Done with: ', self.right_list)

        for i in range(len(os.listdir(path_to_sprite+'/Stand'))):
            image = pygame.image.load(path_to_sprite+'/Stand/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.stand_list.append(image)
        print('Done with: ', self.stand_list)


        self.image = self.stand_list[2]

    def draw(self, where):
        where.blit(self.image, (self.x-(self.image.get_width()/2), self.y-(self.image.get_height()/2)))
        
    def change_sprites(self):
        if self.STATE == 'go_left':
            try:
                self.image = self.left_list[self.left_right_frame]
                self.left_right_frame +=1
            except:
                self.left_right_frame = 0
                self.image = self.left_list[self.left_right_frame]
                self.left_right_frame += 1
        elif self.STATE == 'go_right':
            try:
                self.image = self.right_list[self.left_right_frame]
                self.left_right_frame +=1
            except:
                self.left_right_frame = 0
                self.image = self.right_list[self.left_right_frame]
                self.left_right_frame += 1
        elif self.STATE == 'go_up':
            try:
                self.image = self.up_list[self.up_down_frame]
                self.up_down_frame +=1
            except:
                self.up_down_frame = 0
                self.image = self.up_list[self.up_down_frame]
                self.up_down_frame += 1
        elif self.STATE == 'go_down':
            try:
                self.image = self.down_list[self.up_down_frame]
                self.up_down_frame +=1
            except:
                self.up_down_frame = 0
                self.image = self.down_list[self.up_down_frame]
                self.up_down_frame += 1
        elif self.STATE == 'stand_left':
            self.image = self.stand_list[0]
        elif self.STATE == 'right_left':
            self.image = self.stand_list[1]
        else:
            self.image = self.stand_list[2]


    def go_left(self):
        pass

    def go_right(self):
        pass

    def go_up(self):
        pass

    def go_down(self):
        pass
    

