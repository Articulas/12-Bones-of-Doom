## 12 Bones of Doom V001d

## Import and Initialize ###
import pygame
import time
import random
pygame.init()
############################

## Display Variables ##
display_width = 800
display_height = 600
splash      = pygame.image.load('skull2.png')
##giantrat    = pygame.image.load('giantrat.png')
##giantscorpian = pygame.image.load('giantscorpian.jpeg')
#######################

## Color Pallet #######
black       = (0,0,0)
white       = (255,255,255)
red         = (255,0,0)
green       = (0,255,0)
blue        = (0,0,255)
purple      = (100,0,100)
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

def text_objects_white (text, font):
    textSurface = font.render(text, True,white) # text color
    return textSurface, textSurface.get_rect()

def text_objects_black (text, font):
    textSurface = font.render(text, True,black) # text color
    return textSurface, textSurface.get_rect()

def print_smtxt_white(text, x_pos, y_pos):
    smallText = pygame.font.Font('week.TTF',18)
    TextSurf, TextRect = text_objects_white(text, smallText)
    TextRect.center = ((x_pos),(y_pos))
    gameDisplay.blit(TextSurf, TextRect)
    
def print_smtxt_black(text, x_pos, y_pos):
    smallText = pygame.font.Font('week.TTF',18)
    TextSurf, TextRect = text_objects_black(text, smallText)
    TextRect.center = ((x_pos),(y_pos))
    gameDisplay.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True,red) # text color
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
    gameIntro = True

    while gameIntro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_quit ()
                if event.key == pygame.K_p:
                    main_menu ()
            
        gameDisplay.blit(splash,(10,10))
        
        print_smtxt ("The Most Terrifyting RPG You Can Play !",580)
        print_smtxt ("Press (p) To PLay",540)

        pygame.display.update()
        clock.tick(30)

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

    ##    Create Enemy    
    enemy_l1 = ['Giant Spider','Giant Centipede','Giant Scorpian', 'Giant Rat', 'Jr. Troll']
    enemy_species = (random.choice(enemy_l1))    

    if enemy_species == 'Giant Rat':
        enemy_health    = 30
        enemy_armor     = 2
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 2
        enemy_const     = 1
        enemy_pic = pygame.image.load('giantrat.png')
        
    if enemy_species == 'Giant Spider':
        enemy_health    = 10
        enemy_armor     = 1
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 1
        enemy_const     = 1
        enemy_pic = pygame.image.load('giantspider.png')
        
    if enemy_species == 'Jr. Troll':
        enemy_health    = 40
        enemy_armor     = 10
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 1
        enemy_const     = 1
        enemy_pic = pygame.image.load('jrtroll.png')
        
    if enemy_species == 'Giant Centipede':
        enemy_health    = 50
        enemy_armor     = 15
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 1
        enemy_const     = 1
        enemy_pic = pygame.image.load('centepede.png')

    if enemy_species == 'Giant Scorpian':
        enemy_health    = 60
        enemy_armor     = 30
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 1
        enemy_const     = 1
        enemy_pic = pygame.image.load('giantscorpian.jpeg')
    
##    End Enemy Creator

    gamePlaying = True

    while gamePlaying:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    main_menu ()

        gameDisplay.fill (dark_gray)
        print_mdtxt("12 Bones of Doom",60)

##      Hero Pic
        pygame.draw.rect(gameDisplay, light_gray, [25, 150, 120, 200])
##      Hero Data Box
        pygame.draw.rect(gameDisplay, light_gray, [155, 150, 240,200])
##      Enemy Picture box
        pygame.draw.rect(gameDisplay, light_gray, [415, 150, 120,200])
##      Enemy Data Box
        pygame.draw.rect(gameDisplay, light_gray, [545, 150, 240,200])
##      Combat Report Screen
        pygame.draw.rect(gameDisplay, black, [25,375,765,200])
##      Event Theatre
        print_smtxt_white(enemy_species,100, 400)
        gameDisplay.blit(enemy_pic,(415,150))
##        print_smtxt_black('Giant Rat',600,165)
        print (enemy_health)

##      Refresh Screen
        pygame.display.update()
        clock.tick(30)

##  Run Game
game_intro()

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
