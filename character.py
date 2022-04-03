import os, os.path
import pygame

class Player:

    def __init__(self, name_of_charakter, path_to_sprite):
        self.up_list = []
        self.down_list = []
        self.left_list = []
        self.right_list = []
        for i in range(os.listdir(path_to_sprite+'\Up')):
            image = pygame.image.load(path_to_sprite+'\Up'+str(i)).convert()
            self.up_list.append(image)
        print('Done')



    

