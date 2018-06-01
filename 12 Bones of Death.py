## 12 Bones of Doom V001

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600


## Color Pallet #############
black   = (0,0,0)
white   = (255,255,255)
red     = (255,0,0)
blue    = (0,0,255)
orange  = (255,100,0)
yellow  = (200,200,0)
dgrey   = (110,110,110)
#############################

## Hero Stats #########################################
hero_gender = 'Male'
hero_type = 'warrior'
hero_health = 100
hero_armor = 5
hero_hit = 2
hero_magic = 1
hero_wisdom = 1
hero_charisma = 1
hero_intelligence = hero_charisma + hero_wisdom /2
#######################################################

## Enemy Stats ################################################
enemy_l1 = ['Giant Spider','Giant Centipede','Giant Scorpian']
enemy_l2 = ['Kobold','Goblin','Troll']
###############################################################

print (random.choice(enemy_l1))
print (hero_intelligence)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Twelve Bones of Doom")

clock = pygame.time.Clock()

time.sleep(10)

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


