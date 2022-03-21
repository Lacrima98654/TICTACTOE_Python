# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:19:12 2021

@author: Romeo
"""

import pygame
from constantes import*
from classes import*

pygame.init()

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("TIC TAC TOE")
pygame.display.set_icon(pygame.image.load("tic-tac-toe.ico").convert_alpha())

loop = True
page = Pages(screen)

while loop:
    pygame.time.Clock().tick(30)#30 fps
    page.page1()
    loop = False
        
pygame.quit()