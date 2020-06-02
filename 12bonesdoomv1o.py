## 12 Bones of Doom V001m

## Import and Initialize ###
import pygame
import time
import random
pygame.init()
#######################

## Display and Audio File Load ##
display_width = 800
display_height = 600
splash      = pygame.image.load('skull2.png')
sword_fight = pygame.mixer.Sound("sword_fight.wav")
sword_clash = pygame.mixer.Sound("sword_clash.wav")
magic_blast = pygame.mixer.Sound("magic_blast.wav")
pygame.mixer.music.load('fugedmin.mid')

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
gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
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
    
    pygame.mixer.music.play(-1)
    
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

    pygame.mixer.music.stop()
    
    ##    Create Enemy    
    enemy_l1 = ['Giant Spider','Giant Centipede','Giant Scorpian', 'Giant Rat', 'Jr. Troll']
    enemy_species = (random.choice(enemy_l1))    
##    magic_attack=0    
    if enemy_species == 'Giant Rat':
        enemy_health    = random.randrange(15, 30)
        enemy_strength  = random.randrange(4,10)
        enemy_armor     = random.randrange(1,5)
        enemy_magic     = 0
        enemy_wisdom    = random.randrange(1,3)
        enemy_charisma  = random.randrange(1,2)
        enemy_const     = random.randrange(2,7)
        enemy_pic = pygame.image.load('giantrat.png')
        
    if enemy_species == 'Giant Spider':
        enemy_health    = random.randrange(5, 10)
        enemy_strength  = random.randrange(4,12)
        enemy_armor     = 1
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 1
        enemy_const     = 1
        enemy_pic = pygame.image.load('giantspider.png')
        
    if enemy_species == 'Jr. Troll':
        enemy_health    = random.randrange(20, 40)
        enemy_strength  = random.randrange(4,10)
        enemy_armor     = 10
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 1
        enemy_const     = 1
        enemy_pic = pygame.image.load('jrtroll.png')
        
    if enemy_species == 'Giant Centipede':
        enemy_health    = random.randrange(25, 50)
        enemy_strength  = random.randrange(6,13)
        enemy_armor     = 15
        enemy_magic     = 1
        enemy_wisdom    = 3
        enemy_charisma  = 1
        enemy_const     = 1
        enemy_pic = pygame.image.load('centepede.png')

    if enemy_species == 'Giant Scorpian':
        enemy_health    = random.randrange(30, 60)
        enemy_strength  = random.randrange(8,15)
        enemy_armor     = random.randrange(4, 10)
        enemy_magic     = 0
        enemy_wisdom    = random.randrange(1,3)
        enemy_charisma  = 0
        enemy_const     = random.randrange(4,10)
        enemy_pic = pygame.image.load('giantscorpian.jpeg')
    
##    End Enemy Creator

##      Hero Creator
    hero_class      = ['Fighter', 'Mage', 'Ranger','Thief','Paladin','Shaman']    
    hero_type       = (random.choice(hero_class)) 
    hero_health     = random.randrange(60,100)
    hero_strength   = random.randrange(3,10)
    hero_armor      = random.randrange(3,6)
    hero_magic      = random.randrange(0,10)
    hero_wisdom     = random.randrange(6,13)
    hero_charisma   = random.randrange(8,20)
    hero_const      = random.randrange(4,9)
    hero_potions    = 3
    hero_pic        = pygame.image.load('herom.png')
    
##   End Hero Creator

    gamePlaying = True

    while gamePlaying:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    main_menu ()

                if event.key==pygame.K_a:
##                    Attack
                    pygame.mixer.Sound.play(sword_clash)
                    attack_damage = hero_strength
                    new_ehealth = enemy_health - attack_damage 
                    enemy_health=new_ehealth
##                    Counter Attack    
                    enemy_damage=enemy_strength
                    new_hero_health = hero_health - enemy_damage + hero_armor
                    hero_health = new_hero_health
                    
                    if enemy_health < 1:
                        gameDisplay.fill (yellow)
                        print_lgtxt ("Enemy Defeated !",285)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        gameDisplay.fill (yellow)
                        print_lgtxt ("Creating Enemy!",285)
                        pygame.display.update()
                        pygame.time.delay(2000)

##                        Enemy CREATOR
                        enemy_l1 = ['Giant Spider','Giant Centipede','Giant Scorpian', 'Giant Rat', 'Jr. Troll']
                        enemy_species = (random.choice(enemy_l1))    
##    magic_attack=0    
                        if enemy_species == 'Giant Rat':
                            enemy_health    = random.randrange(15, 30)
                            enemy_strength  = random.randrange(4,10)
                            enemy_armor     = random.randrange(1,5)
                            enemy_magic     = 0
                            enemy_wisdom    = random.randrange(1,3)
                            enemy_charisma  = random.randrange(1,2)
                            enemy_const     = random.randrange(2,7)
                            enemy_pic = pygame.image.load('giantrat.png')
        
                        if enemy_species == 'Giant Spider':
                            enemy_health    = random.randrange(5, 10)
                            enemy_strength  = random.randrange(4,12)
                            enemy_armor     = 1
                            enemy_magic     = 1
                            enemy_wisdom    = 3
                            enemy_charisma  = 1
                            enemy_const     = 1
                            enemy_pic = pygame.image.load('giantspider.png')
                            
                        if enemy_species == 'Jr. Troll':
                            enemy_health    = random.randrange(20, 40)
                            enemy_strength  = random.randrange(4,10)
                            enemy_armor     = 10
                            enemy_magic     = 1
                            enemy_wisdom    = 3
                            enemy_charisma  = 1
                            enemy_const     = 1
                            enemy_pic = pygame.image.load('jrtroll.png')
                            
                        if enemy_species == 'Giant Centipede':
                            enemy_health    = random.randrange(25, 50)
                            enemy_strength  = random.randrange(6,13)
                            enemy_armor     = 15
                            enemy_magic     = 1
                            enemy_wisdom    = 3
                            enemy_charisma  = 1
                            enemy_const     = 1
                            enemy_pic = pygame.image.load('centepede.png')

                        if enemy_species == 'Giant Scorpian':
                            enemy_health    = random.randrange(30, 60)
                            enemy_strength  = random.randrange(8,15)
                            enemy_armor     = random.randrange(4, 10)
                            enemy_magic     = 0
                            enemy_wisdom    = random.randrange(1,3)
                            enemy_charisma  = 0
                            enemy_const     = random.randrange(4,10)
                            enemy_pic = pygame.image.load('giantscorpian.jpeg')
                    ##    End Enemy Creator
                            
                    if hero_health < 1:
                        gameDisplay.fill(yellow)
                        print_lgtxt("You Died!", 285)
                        pygame.display.update()
                        pygame.time.delay(4000)
                        main_menu()

                if event.key==pygame.K_s: # Cast Spell
                    if hero_magic < 5:
                        gameDisplay.fill(dark_gray)
                        print_mdtxt("You Can Not", 285)
                        print_mdtxt("Use Magic" , 365)
                        pygame.display.update()
                        pygame.time.delay(2000)

##                    Cast Magic Spell
                    if hero_magic > 4:
                        pygame.mixer.Sound.play(magic_blast)
                        magic_attack = hero_magic
                        new_ehealth = enemy_health - magic_attack 
                        enemy_health=new_ehealth

                        gameDisplay.fill(dark_gray)
                        print_mdtxt("You Cast Lightning", 285)
                        print_mdtxt("It does " + str(magic_attack) + " Damage", 365)
                        pygame.display.update()
                        pygame.time.delay(2000)

                        if enemy_health < 1:
                            gameDisplay.fill (yellow)
                            print_lgtxt ("Enemy Defeated !",285)
                            pygame.display.update()
                            pygame.time.delay(2000)
##                              Enemy CREATOR
                            gameDisplay.fill (yellow)
                            print_lgtxt ("Creating Enemy!",285)
                            pygame.display.update()
                            pygame.time.delay(2000)

                            enemy_l1 = ['Giant Spider','Giant Centipede','Giant Scorpian', 'Giant Rat', 'Jr. Troll']
                            enemy_species = (random.choice(enemy_l1))
                            
                            if enemy_species == 'Giant Rat':
                                enemy_health    = random.randrange(15, 30)
                                enemy_strength  = random.randrange(4,10)
                                enemy_armor     = random.randrange(1,5)
                                enemy_magic     = 0
                                enemy_wisdom    = random.randrange(1,3)
                                enemy_charisma  = random.randrange(1,2)
                                enemy_const     = random.randrange(2,7)
                                enemy_pic = pygame.image.load('giantrat.png')
        
                            
                            if enemy_species == 'Jr. Troll':
                                enemy_health    = random.randrange(20, 40)
                                enemy_strength  = random.randrange(4,10)
                                enemy_armor     = 10
                                enemy_magic     = 1
                                enemy_wisdom    = 3
                                enemy_charisma  = 1
                                enemy_const     = 1
                                enemy_pic = pygame.image.load('jrtroll.png')
                                
                            if enemy_species == 'Giant Centipede':
                                enemy_health    = random.randrange(25, 50)
                                enemy_strength  = random.randrange(6,13)
                                enemy_armor     = 15
                                enemy_magic     = 1
                                enemy_wisdom    = 3
                                enemy_charisma  = 1
                                enemy_const     = 1
                                enemy_pic = pygame.image.load('centepede.png')

                            if enemy_species == 'Giant Scorpian':
                                enemy_health    = random.randrange(30, 60)
                                enemy_strength  = random.randrange(8,15)
                                enemy_armor     = random.randrange(4, 10)
                                enemy_magic     = 0
                                enemy_wisdom    = random.randrange(1,3)
                                enemy_charisma  = 0
                                enemy_const     = random.randrange(4,10)
                                enemy_pic = pygame.image.load('giantscorpian.jpeg')
                            
                    ##    End Enemy Creator

                        if hero_health < 1:
                            gameDisplay.fill(yellow)
                            print_lgtxt("You Died!", 285)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            main_menu()

##        Render Menu              
        gameDisplay.fill (dark_gray)
        print_mdtxt("12 Bones of Doom",60)
##        Hero Pic
        pygame.draw.rect(gameDisplay, light_gray, [25, 150, 120, 200])
##        Hero Data Box
        pygame.draw.rect(gameDisplay, yellow, [155, 150, 240,200])
##        Enemy Picture box
        pygame.draw.rect(gameDisplay, light_gray, [415, 150, 120,200])
##        Enemy Data Box
        pygame.draw.rect(gameDisplay, yellow, [545, 150, 240,200])


##        Command Screen
        pygame.draw.rect(gameDisplay, black, [25,375,765,200])
        print_smtxt_white("Command Screen:", 100,400)
        print_smtxt_white("a = Attack", 75,425)
        print_smtxt_white("s = Cast Spell", 90,450)
        print_smtxt_white("h = Heal Potion", 95,475)
        print_smtxt_white("q = Quit Game", 95,500)


##        Enemy Data and Display
        print_smtxt_black(enemy_species,630, 160)
        print_smtxt_black("Health: "    + str(enemy_health), 593,180)
        print_smtxt_black("Strength: "  + str(enemy_strength),602,200)
        print_smtxt_black("Armor: "     + str(enemy_armor),586,220)
        print_smtxt_black("Magic: "     + str(enemy_magic),586,240)
        print_smtxt_black("Wisdom: "    + str(enemy_wisdom),589,260)
        print_smtxt_black("Charisma: "  + str(enemy_charisma),602,280)
        print_smtxt_black("Const: "     + str(enemy_const),586,300)
        gameDisplay.blit(enemy_pic,(415,150))
##        Hero data and display
        print_smtxt_black(hero_type,200,160)
        print_smtxt_black("Health: "    + str(hero_health), 200,180)
        print_smtxt_black("Strength: "  + str(hero_strength),200,200)
        print_smtxt_black("Armor: "     + str(hero_armor),200,220)
        print_smtxt_black("Magic: "     + str(hero_magic),200,240)
        print_smtxt_black("Wisdom: "    + str(hero_wisdom),200,260)
        print_smtxt_black("Charisma: "  + str(hero_charisma),200,280)
        print_smtxt_black("Const: "     + str(hero_const),200,300)
        gameDisplay.blit(hero_pic, (25,150))
##        Refresh Screen
        pygame.display.update()
        clock.tick(30)

##  Run Game
game_intro()

##  End Game
pygame.quit()
quit()
