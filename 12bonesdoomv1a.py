## 12 Bones of Doom V001

## Import and Initialize ###
import pygame
import time
import random
pygame.init()
############################

## Display Variables ##
display_width = 800
display_height = 600
splash = pygame.image.load('skull2.png')
#######################

## Color Pallet #######
black       = (0,0,0)
white       = (255,255,255)
red         = (255,0,0)
blue        = (0,0,255)
orange      = (255,100,0)
yellow      = (200,200,0)
light_gray  = (210,210,210)
dark_gray   = (20,20,29)
########################

## Display Manifest ##################################################
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Twelve Bones of Doom")
clock = pygame.time.Clock()
######################################################################

def text_objects(text, font):
    textSurface = font.render(text, True, red) # text color
    return textSurface, textSurface.get_rect()

def print_lgtxt (text,y_pos):  #Centered Text
    largeText = pygame.font.Font('week.TTF',90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(y_pos))
    gameDisplay.blit(TextSurf, TextRect)

def print_smtxt(text, y_pos):
    smallText = pygame.font.Font('week.TTF',18)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((display_width/2),(y_pos))
    gameDisplay.blit(TextSurf, TextRect)

def print_mdtxt(text, y_pos):
    medText = pygame.font.Font('week.TTF',40)
    TextSurf, TextRect = text_objects(text, medText)
    TextRect.center = ((display_width/2),(y_pos))
    gameDisplay.blit(TextSurf, TextRect)

def game_intro():
    gameDisplay.blit(splash,(10,10))
    print_lgtxt ("12 Bones of Doom",525)
    print_smtxt ("The Most Terrifyting RPG You Can Play !",580)
    pygame.display.update()
    pygame.display.update()
    time.sleep(2)

def main_menu ():
    mainMenu = True
    
    while mainMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_quit ()
                if event.key == pygame.K_p:
                    game_play ()

        gameDisplay.fill (dark_gray)
        print_lgtxt ("Main Menu",50)
        print_mdtxt ("(P) Play Game (Q) Quit Game",200)
        pygame.display.update()
        clock.tick(30)
        
def game_quit ():
    pygame.quit()
    quit ()

def game_play ():

    gamePlaying = True

    while gamePlaying:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    main_menu ()
##                if event.key == pygame.K_g:
##                    game_play ()

        gameDisplay.fill (red)
        pygame.display.update()
        clock.tick(30)

game_intro()
main_menu()

##  End Game
pygame.quit()
quit()

################################################################
##enemy_l1 = ['Giant Spider','Giant Centipede','Giant Scorpian']
##enemy_l2 = ['Kobold','Goblin','Troll']
##
####print (random.choice(enemy_l1))
####print ('testing')
##
##
##print("                  ___====-_  _-====___")
##print("            _--^^^#####//      \\#####^^^--_")
##print("         _-^##########// (    ) \\##########^-_")
##print("        -############//  |\^^/|  \\############-")
##print("      _/############//   (@::@)   \\############\_")
##print("     /#############((     \\//     ))#############\ ") 
##print("    -###############\\    (oo)    //###############-")
##print("   -#################\\  / VV \  //#################-")
##print("  -###################\\/      \//###################-")
##print(" _#/|##########/\######(   /\   )######/\##########|\#_")
##print(" |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|")
##print(" `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '")
##print("    `   `  `      `   / | |  | | \   '      '  '   '")
##print("                     (  | |  | |  )")
##print("                    __\ | |  | | /__")
##print("                   (vvv(VVV)(VVV)vvv)")
##
###################################################################


