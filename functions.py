# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:20:34 2021

@author: Romeo
"""
import pygame
import random
from classes import*

def game_manager(screen,grille,adv,pion,nom,beginer = 0):
    """
    Game manager

    Parameters
    ----------
    screen : TYPE
        DESCRIPTION.
    grille : TYPE
        DESCRIPTION.
    adv : TYPE
        DESCRIPTION.
    pion : TYPE
        DESCRIPTION.
    nom : TYPE
        DESCRIPTION.
    beginer : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    winner : TYPE
        DESCRIPTION.

    """
    winner = {'winner':0,'event':0}
    loop = True
    player = beginer
    if adv:
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            pygame.draw.rect(screen,(255,255,255),(0,405,500,50))
            texte = "C'est le tour de "+nom[player]+"..."
            if not player:
                pygame.draw.rect(screen,0x990099,(40,230,20,10))
                pygame.draw.rect(screen,WHITE,(440,230,20,10))
            else:
                pygame.draw.rect(screen,0x990099,(440,230,20,10))
                pygame.draw.rect(screen,WHITE,(40,230,20,10))
            draw_text(screen, 25, texte, 500-75)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if  15<= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                            back_icon(screen,(153,102,51))
                            pygame.display.flip()
                            time.sleep(0.1)
                            winner['event'] = 1
                            return winner
                        elif W-60 <= event.pos[0] <= W - 20 and 8 <= event.pos[1] <= 43:
                            home_icon(screen,(153,102,51))
                            pygame.display.flip()
                            time.sleep(0.1)
                            winner['event'] = 2
                            return winner
                        elif grille.check_click(event.pos[0],event.pos[1]):
                            if grille.set_in_click_pos(event.pos[0],event.pos[1],pion[player]):
                                pygame.display.flip()
                                if check_win(grille):
                                    pygame.draw.rect(screen,(255,255,255),(0,405,500,50))
                                    winner['old'] = 0 if player else 1
                                    winner['winner'] = player + 1
                                    pygame.draw.rect(screen,(255,255,255),(0,405,500,50))
                                    return winner
                                elif check_full(grille):
                                    winner['old'] = 0 if player else 1
                                    pygame.draw.rect(screen,(255,255,255),(0,405,500,50))
                                    return winner
                                player = 0 if player else 1
            pygame.display.flip()
    else:#Partie avec l'ordinateur
        os_coup = 0
        premier_coup = 0
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            pygame.draw.rect(screen,(255,255,255),(0,405,500,50))
            if not player:
                texte = "C'est le tour de "+nom[player]+"..."
                pygame.draw.rect(screen,0x990099,(40,230,20,10))
                pygame.draw.rect(screen,WHITE,(440,230,20,10))
            else:
                texte = "C'est le tour de l'IA"
                pygame.draw.rect(screen,0x990099,(440,230,20,10))
                pygame.draw.rect(screen,WHITE,(40,230,20,10))
            draw_text(screen, 25, texte, 500-75)
            pygame.display.flip()
            
            if player:
                ok_os = 0
                if grille.dimension == 3:
                    rand = check_os_set(grille)
                    if rand != 'none':
                        i,j = n2ij(grille.dimension,rand)
                        ok_os = grille.os_set(i,j,pion[player])
                    else:
                        if os_coup == 0:
                            while not ok_os:
                                rand = random.randint(0,8)
                                i,j = n2ij(grille.dimension,rand)
                                premier_coup = rand
                                ok_os = grille.os_set(i,j,pion[player])
                        elif os_coup == 1:
                            while not ok_os:
                                if premier_coup == 0:
                                    rand = random.choice([1,2,3,6,4,8])
                                elif premier_coup == 1:
                                    rand = random.choice([0,2,4,7])
                                elif premier_coup == 2:
                                    rand = random.choice([0,1,4,6,5,8])
                                elif premier_coup == 3:
                                    rand = random.choice([0,6,4,5])
                                elif premier_coup == 4:
                                    rand = random.randint(0,8)
                                elif premier_coup == 5:
                                    rand = random.choice([2,8,3,4])
                                elif premier_coup == 6:
                                    rand = random.choice([0,3,2,4,7,8])
                                elif premier_coup == 7:
                                    rand = random.choice([1,4,6,8])
                                elif premier_coup == 8:
                                    rand = random.choice([0,4,2,5,6,7])
                                i,j = n2ij(grille.dimension,rand)
                                ok_os = grille.os_set(i,j,pion[player])
                        else:
                            while not ok_os:
                                rand = random.randint(0,8)
                                i,j = n2ij(grille.dimension,rand)
                                ok_os = grille.os_set(i,j,pion[player])
                    os_coup += 1 
                if grille.dimension == 4:
                    pass
                if grille.dimension == 5:
                    pass
                player = 0
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if  15<= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                            back_icon(screen,(153,102,51))
                            pygame.display.flip()
                            time.sleep(0.1)
                            winner['event'] = 1
                            return winner
                        elif W-60 <= event.pos[0] <= W - 20 and 8 <= event.pos[1] <= 43:
                            home_icon(screen,(153,102,51))
                            pygame.display.flip()
                            time.sleep(0.1)
                            winner['event'] = 2
                            return winner
                        elif grille.check_click(event.pos[0],event.pos[1]):
                            if grille.set_in_click_pos(event.pos[0],event.pos[1],pion[player]):
                                pygame.display.flip()
                                if check_win(grille):
                                    pygame.draw.rect(screen,(255,255,255),(0,405,500,50))
                                    winner['old'] = 0 if player else 1
                                    winner['winner'] = player + 1
                                    return winner
                                elif check_full(grille):
                                    pygame.draw.rect(screen,(255,255,255),(0,405,500,50))
                                    winner['old'] = 0 if player else 1
                                    return winner
                                player = 1
            pygame.display.flip()
            

def check_os_set(grille):
    case = grille.contenant
    if (case[0][1] == case[0][2] != 0 or case[1][0] == case[2][0] != 0 or case[1][1] == case[2][2] != 0) and not case[0][0]:
        return 0
    elif (case[0][0] == case[0][2] != 0 or case[1][1] == case[2][1] != 0) and not case[0][1]:
        return 1
    elif (case[0][0] == case[0][1] != 0 or case[1][2] == case[2][2] != 0 or case[1][1] == case[2][0] != 0) and not case[0][2]:
        return 2
    elif (case[0][0] == case[2][0] != 0 or case[1][1] == case[1][2] != 0) and not case[1][0]:
        return 3
    elif (case[0][0] == case[2][2] != 0 or case[0][2] == case[2][0] != 0 or case[0][1] == case[2][1] != 0 or case[1][0] == case[1][2] != 0) and not case[1][1]:
        return 4
    elif (case[0][2] == case[2][2] != 0 or case[1][0] == case[1][1] != 0) and not case[1][2]:
        return 5
    elif (case[0][0] == case[1][0] != 0 or case[1][1] == case[0][2] != 0 or case[2][1] == case[2][2] != 0) and not case[2][0]:
        return 6
    elif (case[2][0] == case[2][2] != 0 or case[0][1] == case[1][1] != 0) and not case[2][1]:
        return 7
    elif (case[0][0] == case[1][1] != 0 or case[2][0] == case[2][1] != 0 or case[0][2] == case[1][2] != 0) and not case[2][2]:
        return 8
    else:
        return 'none'
    
    
def n2ij(dimension,n):
    indice = 0
    
    if dimension == 3:
        for i in range(0,3):
            for j in range(0,3):
                if indice == n:
                    return i,j
                indice += 1
    elif dimension == 4:
        for i in range(0,4):
            for j in range(0,4):
                if indice == n:
                    return i,j
                indice += 1
    elif dimension == 5:
        for i in range(0,5):
            for j in range(0,5):
                if indice == n:
                    return i,j
                indice += 1
                
                
def get_name(screen,rec,name):
    """
    Prendre le nom à travers un formulaire

    Parameters
    ----------
    screen : TYPE
        DESCRIPTION.
    rec : TYPE
        DESCRIPTION.
    name : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    new_name = name
    cur = [rec[0]+5,rec[1]+5]
    pygame.draw.rect(screen,(200,200,200),rec,0,15)
    draw_text(screen, 20, new_name, cur[1]+5)
    loop = 1
    while loop:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 15<= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                    back_icon(screen,(153,102,51))
                    pygame.display.flip()
                    time.sleep(0.1)
                    return "11111111111"
                else:
                    pygame.draw.rect(screen,(255,255,255),rec,0,15)
                    draw_text(screen, 20, new_name, cur[1]+5)
                    return new_name
                
            elif event.type == pygame.KEYDOWN:
                if 97 <= event.key <= 123 and len(new_name) <= 10:
                    new_name += chr(event.key)
                elif event.key == 8:
                    new_name = new_name[0:len(new_name)-1]
                elif event.key == 13:
                    pygame.draw.rect(screen,(255,255,255),rec,0,15)
                    draw_text(screen, 20, new_name, cur[1]+5)
                    return new_name
                new_name = new_name.capitalize()
                pygame.draw.rect(screen,(200,200,200),rec,0,15)
                draw_text(screen, 20, new_name, cur[1]+5)
        pygame.display.flip()
                    
def check_win(grille):
    case = grille.contenant
    if grille.dimension == 3:
        if case[0][0] == case[1][1] == case[2][2] != 0 or case[0][2] == case[1][1] == case[2][0] != 0 or case[0][0] == case[0][1] == case[0][2] != 0 or case[1][0]== case[1][1] == case[1][2] != 0 or case[2][0] == case[2][1] == case[2][2] != 0 or case[0][0] == case[1][0] == case[2][0] != 0 or case[0][1] == case[1][1] == case[2][1] != 0 or case[0][2] == case[1][2] == case[2][2] != 0:
            return 1
    elif grille.dimension == 4:
        if clone_check_win(grille, 0, 0):
            return 1
        elif clone_check_win(grille, 0, 1):
            return 1
        elif clone_check_win(grille, 1, 0):
            return 1
        elif clone_check_win(grille, 1, 1):
            return 1
    else:
        if clone_check_win(grille, 0, 0):
            return 1
        elif clone_check_win(grille, 0, 1):
            return 1
        elif clone_check_win(grille, 1, 0):
            return 1
        elif clone_check_win(grille, 1, 1):
            return 1
    return 0
    
def clone_check_win(grille,i,j):
    case = grille.contenant
    if grille.dimension == 4:
        if case[i][j] == case[i+1][j+1] == case[i+2][j+2] != 0 or case[i][j+2] == case[i+1][j+1] == case[i+2][j] != 0 or case[i][j] == case[i][j+1] == case[i][j+2] != 0 or case[i+1][j]== case[i+1][j+1] == case[i+1][j+2] != 0 or case[i+2][j] == case[i+2][j+1] == case[i+2][j+2] != 0 or case[i][j] == case[i+1][j] == case[i+2][j] != 0 or case[i][j+1] == case[i+1][j+1] == case[i+2][j+1] != 0 or case[i][j+2] == case[i+1][j+2] == case[i+2][j+2] != 0:
            return 1
    elif grille.dimension == 5:
        if case[i][j] == case[i+1][j+1] == case[i+2][j+2] == case[i+3][j+3] != 0 or case[i][j+3] == case[i+1][j+2] == case[i+2][j+1] == case[i+3][j] != 0 or case[i][j] == case[i][j+1] == case[i][j+2] == case[i][j+3] != 0 or case[i+1][j]== case[i+1][j+1] == case[i+1][j+2] == case[i+1][j+3] != 0 or case[i+2][j] == case[i+2][j+1] == case[i+2][j+2] == case[i+2][j+3] !=0 or case[i+3][j] == case[i+3][j+1] == case[i+3][j+2] == case[i+3][j+3] != 0 or case[i][j] == case[i+1][j] == case[i+2][j] == case[i+3][j] != 0 or case[i][j+1] == case[i+1][j+1] == case[i+2][j+1] == case[i+3][j+1] != 0 or case[i][j+2] == case[i+1][j+2] == case[i+2][j+2] == case[i+3][j+2] != 0 or case[i][j+3] == case[i+1][j+3] == case[i+2][j+3] == case[i+3][j+3] != 0:
            return 1
    
def check_full(grille):
    for i in range(grille.dimension):
        for j in range(grille.dimension):
            if grille.contenant[i][j] == 0:
                return False
    return True

def draw_cross(screen,x,y,color = 0x66FF00):
    pygame.draw.line(screen,color, (x[0],y[0]), (x[3],y[3]),4)
    pygame.draw.line(screen, color, (x[1],y[1]), (x[2],y[2]),4)

def draw_text(screen,p_size,texte,y):
    police = pygame.font.SysFont('consolas',p_size)
    output = police.render(texte, True,(0,0,0))
    screen.blit(output,((W - output.get_width())/2,y))

def back_icon(screen, col = (0,0,0)):
    pygame.draw.rect(screen,col,(15,10,44,30),1,3)
    icon = pygame.draw.polygon(screen, col, [(20,25),(30,15),(30,20),(50,20),(50,30),(30,30),(30,35)])
    
def home_icon(screen,col = (0,0,0)):
    pygame.draw.rect(screen,col,(500-60,8,40,35),1,3)
    pygame.draw.polygon(screen, col, [(500-25,25),(500-40,10),(500-55,25),(500-50,25),(500-50,40),(500-30,40),(500-30,25)],1)
    pygame.draw.rect(screen,col,(500-45,30,8,10))
    
def draw_rect_alpha(surface, color, rect,border_radius = -1):
    #Source StackOverflow
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect(),0,border_radius)
    surface.blit(shape_surf, rect)
    