# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:20:17 2021

@author: Romeo
"""

import pygame
import time
import sys
from constantes import*
from functions import*

class Bouton:
    
    def __init__(self,screen,posX,posY,width,height,texte,text_size = 36):
        self.screen = screen
        self.posX = posX
        self.posY = posY
        self.texte = texte
        self.height = height
        self.width = width
        self.t_size = text_size
        
        
    def display(self,col =(24,24,24,200),t_col = WHITE):
        """
        Display the Button instance

        Parameters
        ----------
        col : TYPE, optional
            DESCRIPTION. The default is (24,24,24,200).
        t_col : TYPE, optional
            DESCRIPTION. The default is WHITE.

        Returns
        -------
        None.

        """
        #Dessiner un rectangle avec transparence
        shape_surf = pygame.Surface(pygame.Rect(self.posX,self.posY,self.width,self.height).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, col, shape_surf.get_rect(),border_radius=20)
        self.screen.blit(shape_surf, (self.posX,self.posY,self.width,self.height))
        
        #Chargement de la police et du rendu du texte
        police = pygame.font.SysFont('calibri',self.t_size,bold=2)
        output = police.render(self.texte, True, t_col)
        out_X = self.posX + (self.width - output.get_width())/2
        out_Y = self.posY + (self.height - output.get_height())/2
        self.screen.blit(output,(out_X,out_Y))
        
        
    
    def check_click(self,sentX,sentY):
        if self.posX <= sentX <= self.posX + self.width and self.posY <= sentY <= self.posY + self.height:
            return 1
        return 0  
    
    
    
class Pages:
    
    #Attributs de classe
    opponent = 0
    player_pion = ()
    dim_grille = 0
    nom_joueur = ['','']
    score = [0,0]
    next_player = 0
    
    def __init__(self,screen):
        self.screen = screen
        self.bg = pygame.image.load("fond.jpg").convert()
        self.avatar = pygame.image.load("avatar.png").convert_alpha()
        
    def page1(self):
        Pages.score = [0,0]
        Pages.nom_joueur = ['','']
        self.screen.blit(self.bg,(0,0))
        police = pygame.font.SysFont('arial',50,bold=5)
        output = police.render("JOUER CONTRE:", True,(0,0,0))
        self.screen.blit(output,((W - output.get_width())/2,90))
        
        b = [Bouton(self.screen,125,170,250,80,"IA"), Bouton(self.screen,125,280,250,80,"HUMAIN")] 
        b[0].display()
        b[1].display()
        
        draw_text(self.screen,15,"Made by Roméo KAKPO",H-18)
        
        loop = True
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(0,2):
                        if b[i].check_click(event.pos[0], event.pos[1]):
                            Pages.opponent = i
                            b[i].display(BLACK,(153,102,51,200))
                            pygame.display.flip()
                            time.sleep(0.1)
                            self.page2()
            pygame.display.flip()
    
    def page2(self):
        Pages.score = [0,0]
        Pages.next_player = 0
        self.screen.blit(self.bg,(0,0))
        back_icon(self.screen)
        
        if not Pages.opponent:
            Pages.nom_joueur[1] = 'IA'
            
            draw_text(self.screen,25,"Entrez votre nom(facultatif):",110)
            draw_rect_alpha(self.screen,(24,24,24,200),(100,150,300,50),border_radius=15)
            pygame.draw.rect(self.screen,(255,255,255),(105,155,290,40),0,15)
            draw_text(self.screen, 20, Pages.nom_joueur[0], 165)
            
            b = [Bouton(self.screen,175,225,150,50,"Continuer",20)] 
            b[0].display()
            
        else:
            draw_text(self.screen,20,"Joueur 1 entrez votre nom(facultatif):",110)
            draw_rect_alpha(self.screen,(24,24,24,200),(100,150,300,50),border_radius=15)
            pygame.draw.rect(self.screen,(255,255,255),(105,155,290,40),0,15)
            draw_text(self.screen, 20, Pages.nom_joueur[0], 165)
    
            draw_text(self.screen,20,"Joueur 2 entrez votre nom(facultatif):",260)
            draw_rect_alpha(self.screen,(24,24,24,200),(100,300,300,50),border_radius=15)
            pygame.draw.rect(self.screen,(255,255,255),(105,305,290,40),0,15)
            draw_text(self.screen, 20, Pages.nom_joueur[1], 315)
            
            b = [Bouton(self.screen,175,375,150,50,"Continuer",20)] 
            b[0].display()
            
        loop = True
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if  15 <= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                        back_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page1()
                    elif 105 <= event.pos[0] <= 395 and 155 <= event.pos[1] <= 195:
                        Pages.nom_joueur[0] = get_name(self.screen,(105,155,290,40),Pages.nom_joueur[0])
                    elif 105 <= event.pos[0] <= 395 and 305 <= event.pos[1] <= 345 and Pages.opponent:
                        Pages.nom_joueur[1] = get_name(self.screen,(105,305,290,40),Pages.nom_joueur[1])
                    elif b[0].check_click(event.pos[0], event.pos[1]):
                        if Pages.nom_joueur[0] == '' and not Pages.opponent:
                            Pages.nom_joueur[0] = 'Joueur'
                        elif Pages.nom_joueur[0] == '' and Pages.opponent:
                            Pages.nom_joueur[0] = 'Joueur 1'
                        if Pages.nom_joueur[1] == '' :
                            Pages.nom_joueur[1] = 'Joueur 2'
                        if Pages.nom_joueur[0] != '' and Pages.nom_joueur[1] != '':
                            self.page3()
                    if len(Pages.nom_joueur[0]) == 11 or len(Pages.nom_joueur[1]) == 11:
                        self.page1()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        if Pages.nom_joueur[0] == '' and not Pages.opponent:
                            Pages.nom_joueur[0] = 'Joueur'
                        elif Pages.nom_joueur[0] == '' and Pages.opponent:
                            Pages.nom_joueur[0] = 'Joueur 1'
                        if Pages.nom_joueur[1] == '':
                            Pages.nom_joueur[1] = 'Joueur 2'
                        if Pages.nom_joueur[0] != '' and Pages.nom_joueur[1] != '':
                            self.page3()
                            
            pygame.display.flip()
    
    def page3(self):
        self.screen.blit(self.bg,(0,0))
        back_icon(self.screen)
        home_icon(self.screen)
        
        if(Pages.opponent):
            draw_text(self.screen,40,Pages.nom_joueur[0],90)
        draw_text(self.screen,40,"Choisissez votre pion:",130)
        
        b = [Bouton(self.screen,120,200,100,100,""), Bouton(self.screen,280,200,100,100,"")] 
        b[0].display()
        b[1].display()
        pygame.draw.circle(self.screen,RED,(330,250),30,4)
        draw_cross(self.screen,[150,190,150,190],[225,225,275,275])
        
        draw_text(self.screen,15,"Made by Roméo KAKPO",H-18)
        
        loop = True
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if  15<= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                        back_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page2()
                    elif W-60 <= event.pos[0] <= W - 20 and 8 <= event.pos[1] <= 43:
                        home_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page1()
                    else:
                        for i in range(0,2):
                            if b[i].check_click(event.pos[0], event.pos[1]):
                                b[i].display(BLACK,(153,102,51,200))
                                if i == 0:
                                    Pages.player_pion = ('X','O')
                                    draw_cross(self.screen,[150,190,150,190],[225,225,275,275])
                                else:
                                    Pages.player_pion = ('O','X')
                                    pygame.draw.circle(self.screen,RED,(330,250),30,4)
                                pygame.display.flip()
                                time.sleep(0.1)
                                self.page4()
            pygame.display.flip()
    
    def page4(self):
        self.screen.blit(self.bg,(0,0))
        back_icon(self.screen)
        home_icon(self.screen)
        
        draw_text(self.screen,40,'Choix de Grille:',50)
        
        b = [Bouton(self.screen,150,110,200,80,"3 x 3"), Bouton(self.screen,150,225,200,80,"4 x 4"), Bouton(self.screen,150,340,200,80,"5 x 5")] 
        b[0].display()
        b[1].display()
        b[2].display()
        
        draw_text(self.screen,15,"Made by Roméo KAKPO",H-18)
        
        loop =True
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if  15<= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                        back_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page3()
                    elif W-60 <= event.pos[0] <= W - 20 and 8 <= event.pos[1] <= 43:
                        home_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page1()
                    else:
                        for i in range(0,3):
                            if b[i].check_click(event.pos[0], event.pos[1]):
                                Pages.dim_grille = i + 3
                                b[i].display(BLACK,(153,102,51,200))
                                pygame.display.flip()
                                time.sleep(0.1)
                                self.page5()
            pygame.display.flip()
    
    def page5(self):
        self.screen.blit(self.bg,(0,0))
        back_icon(self.screen)
        home_icon(self.screen)
        
        if Pages.dim_grille == 3:
            draw_text(self.screen,15,"But: Aligner "+str(Pages.dim_grille)+" pions identiques",5)
        elif Pages.dim_grille == 4:
            draw_text(self.screen,15,"But: Aligner "+str(Pages.dim_grille-1)+" pions identiques",5)
        elif Pages.dim_grille == 5:
            draw_text(self.screen,15,"But: Aligner "+str(Pages.dim_grille-1)+" pions identiques",5)
        
        police = pygame.font.SysFont('consolas',50)
        output = police.render(Pages.player_pion[0], True,BLACK)
        self.screen.blit(output,(100,28))
        output = police.render(Pages.player_pion[1], True,BLACK)
        self.screen.blit(output,(375,28))
        
        pygame.draw.rect(self.screen,(24,24,24,200),(150,25,200,50))
        output = police.render(str(Pages.score[0])+" : "+str(Pages.score[1]), True,WHITE)
        self.screen.blit(output,(150+(200 - output.get_width())/2,28))
        
        grille = Grille(self.screen,Pages.dim_grille)
        grille.display()
        
        self.screen.blit(self.avatar,(25,150))
        police = pygame.font.SysFont('consolas',20,italic=True)
        output = police.render(Pages.nom_joueur[0], True,(0,0,0))
        self.screen.blit(output,((100 - output.get_width())/2,200))
        
        self.screen.blit(self.avatar,(425,150))
        output = police.render(Pages.nom_joueur[1], True,(0,0,0))
        self.screen.blit(output,(400+(100 - output.get_width())/2,200))
        
        draw_text(self.screen,15,"Made by Roméo KAKPO",H-18)
        pygame.display.flip()
        loop = True
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if  15<= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                        back_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page4()
                    elif W-60 <= event.pos[0] <= W - 20 and 8 <= event.pos[1] <= 43:
                        home_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page1()
            
            winner = game_manager(self.screen,grille,Pages.opponent,Pages.player_pion,Pages.nom_joueur,Pages.next_player)
            #On va gérer les évènements qui se sont déroulés dans la fonction ici
            if not winner['winner']:
                if winner['event']:
                    if winner['event'] == 1:
                        self.page4()
                    elif winner['event'] == 2:
                        self.page1()
            else:
                Pages.score[winner['winner']-1] += 1
            Pages.next_player = winner['old']
            self.popup(winner['winner'])
    
    def popup(self,winner):
        pygame.draw.rect(self.screen,(24,24,24,200),(150,25,200,50))
        
        police = pygame.font.SysFont('consolas',50)
        output = police.render(str(Pages.score[0])+" : "+str(Pages.score[1]), True,WHITE)
        self.screen.blit(output,(150+(200 - output.get_width())/2,28))
        
        draw_rect_alpha(self.screen,(24,24,24,24),(0,0,W,H))
        
        if not winner:
            texte = "Nul !!!"
        elif winner == 1:
            texte = Pages.nom_joueur[0]+" a gagné"
        else:
            texte = Pages.nom_joueur[1]+" a gagné"
        
        draw_rect_alpha(self.screen,(24,24,24,225),(0,225,W,50))
        police = pygame.font.SysFont('consolas',30)
        output = police.render(texte, True,WHITE)
        self.screen.blit(output,((W - output.get_width())/2,235))
        
        
        b = [Bouton(self.screen,125,425,100,50,"Rejouer",20), Bouton(self.screen,275,425,100,50,"Quitter",20)] 
        b[0].display()
        b[1].display()
        
        loop = True
        while loop:
            pygame.time.Clock().tick(30)#30 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if  15<= event.pos[0] <= 59 and 10 <= event.pos[1] <=40:
                        pygame.draw.rect(self.screen,(200,200,200,200),(150,25,200,50))
                        pygame.display.flip()
                        time.sleep(0.1)
                        back_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page4()
                    elif W-60 <= event.pos[0] <= W - 20 and 8 <= event.pos[1] <= 43:
                        pygame.draw.rect(self.screen,(200,200,200,200),(150,25,200,50))
                        pygame.display.flip()
                        time.sleep(0.1)
                        home_icon(self.screen,(153,102,51))
                        pygame.display.flip()
                        time.sleep(0.1)
                        self.page1()
                    else:
                        if b[0].check_click(event.pos[0], event.pos[1]):
                            self.page5()
                        elif b[1].check_click(event.pos[0], event.pos[1]):
                            pygame.quit()
                            sys.exit()
            pygame.display.flip()
    
class Grille:
    
    def __init__(self,screen,dimension):
        self.screen = screen
        self.dimension = dimension
        self.contenant = [[0]*dimension for _ in range(0,dimension)]
        self.subdivision = 300/self.dimension
    
    def display(self):
        draw_rect_alpha(self.screen,(24,24,24,200),(100,100,300,300))
        for i in range(1,self.dimension):
            pygame.draw.line(self.screen, WHITE, (100 + i*self.subdivision,100), (100 + i*self.subdivision,400))
            pygame.draw.line(self.screen, WHITE, (100,100 + i*self.subdivision), (400,100 + i*self.subdivision))
        
    def check_click(self,sentX,sentY):
        """
        Grace à cette fonction on peut obtenir l'indice de la case du tableau qui à été cliqué
        """
        if 100 <= sentX <= 400 and 100 <= sentY <= 400:
                return 1
        return 0
    
    def os_set(self,ind_i,ind_j,pion):
        if self.contenant[ind_i][ind_j] == 0:
            self.contenant[ind_i][ind_j] = pion
        else:
            return 0
        intervalX = [100, 100 + self.subdivision]
        intervalY = [100, 100 + self.subdivision]
        for i in range(0,ind_i):
            intervalY[0] += self.subdivision
            intervalY[1] += self.subdivision
        for j in range(0,ind_j):
            intervalX[0] += self.subdivision
            intervalX[1] += self.subdivision        
            
        if pion == 'O':
            if self.dimension == 5:
                pygame.draw.circle(self.screen,RED,((intervalX[0]+intervalX[1])/2,(intervalY[0]+intervalY[1])/2),20,3)
            else:
                pygame.draw.circle(self.screen,RED,((intervalX[0]+intervalX[1])/2,(intervalY[0]+intervalY[1])/2),25,3)
        else:
            if self.dimension == 3:
                draw_cross(self.screen,[intervalX[0]+30,intervalX[1]-30,intervalX[0]+30,intervalX[1]-30],[intervalY[0]+25,intervalY[0]+25,intervalY[1]-25,intervalY[1]-25])
            elif self.dimension == 4:
                draw_cross(self.screen,[intervalX[0]+20,intervalX[1]-20,intervalX[0]+20,intervalX[1]-20],[intervalY[0]+15,intervalY[0]+15,intervalY[1]-15,intervalY[1]-15])
            else:
                draw_cross(self.screen,[intervalX[0]+15,intervalX[1]-15,intervalX[0]+15,intervalX[1]-15],[intervalY[0]+12,intervalY[0]+12,intervalY[1]-12,intervalY[1]-12])
        return 1
    
    def set_in_click_pos(self,sentX,sentY,pion):
        """
        Set the player choice in the grille

        Parameters
        ----------
        sentX : TYPE
            DESCRIPTION.
        sentY : TYPE
            DESCRIPTION.
        pion : TYPE
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        intervalX = [100, 100 + self.subdivision]
        intervalY = [100, 100 + self.subdivision]
        for i in range(0,self.dimension):
            for j in range(0,self.dimension):
                
                if intervalX[0] <= sentX <= intervalX[1] and intervalY[0] <= sentY <= intervalY[1]:
                    if self.contenant[i][j] == 0:
                        self.contenant[i][j] = pion
                        if pion == 'O':
                            if self.dimension == 5:
                                pygame.draw.circle(self.screen,RED,((intervalX[0]+intervalX[1])/2,(intervalY[0]+intervalY[1])/2),20,3)
                            else:
                                pygame.draw.circle(self.screen,RED,((intervalX[0]+intervalX[1])/2,(intervalY[0]+intervalY[1])/2),25,3)
                        else:
                            if self.dimension == 3:
                                draw_cross(self.screen,[intervalX[0]+30,intervalX[1]-30,intervalX[0]+30,intervalX[1]-30],[intervalY[0]+25,intervalY[0]+25,intervalY[1]-25,intervalY[1]-25])
                            elif self.dimension == 4:
                                draw_cross(self.screen,[intervalX[0]+20,intervalX[1]-20,intervalX[0]+20,intervalX[1]-20],[intervalY[0]+15,intervalY[0]+15,intervalY[1]-15,intervalY[1]-15])
                            else:
                                draw_cross(self.screen,[intervalX[0]+15,intervalX[1]-15,intervalX[0]+15,intervalX[1]-15],[intervalY[0]+12,intervalY[0]+12,intervalY[1]-12,intervalY[1]-12])
                        return 1
                intervalX[0] += self.subdivision
                intervalX[1] += self.subdivision        
            #Incrémentation et initialisation avant passage au tour de boucle suivant
            intervalY[0] += self.subdivision
            intervalY[1] += self.subdivision
            intervalX = [100, 100 + self.subdivision]     
        return 0