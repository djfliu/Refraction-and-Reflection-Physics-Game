import pygame
import time
import math
import random

pygame.init() #initiate pygame DUH

displayWidth = 800 #display width variable
displayHeight = 600 #display height variable

black = (0,0,0)#colours
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))#create window
pygame.display.set_caption("Laser Simulation")#create title
clock = pygame.time.Clock()#set clock

font14 = pygame.font.SysFont("monospace",14)#create font size 14
font20 = pygame.font.SysFont("monospace",20)#create font size 20
font30 = pygame.font.SysFont("monospace",30)#create font size 30
font40 = pygame.font.SysFont("monospace",40)#create font size 40

laserImage = pygame.image.load('laser.png')

clippyImage = pygame.image.load('clippy.png') #hello im clippy
clippyImage2 = pygame.image.load('clippy2.png') #talk through console

clippyImage3 = pygame.image.load('clippy3.png') #hello friends
clippyImage4 = pygame.image.load('clippy4.png') #...
clippyImage5 = pygame.image.load('clippy5.png') #:)

clippyImage6 = pygame.image.load('clippy6.png') #reflection stuff
clippyImage12 = pygame.image.load('clippy12.png') #
clippyImage7 = pygame.image.load('clippy7.png') #
clippyImage8 = pygame.image.load('clippy8.png') #
clippyImage9 = pygame.image.load('clippy9.png') #
clippyImage10 = pygame.image.load('clippy10.png') #
clippyImage11 = pygame.image.load('clippy11.png')
clippyImage13 = pygame.image.load('clippy13.png')#

clippyImage14 = pygame.image.load('clippy14.png')#refraction stuff
clippyImage15 = pygame.image.load('clippy15.png')
clippyImage16 = pygame.image.load('clippy16.png')
clippyImage17 = pygame.image.load('clippy17.png')
clippyImage18 = pygame.image.load('clippy18.png')
clippyImage19 = pygame.image.load('clippy19.png')
clippyImage20 = pygame.image.load('clippy20.png')
clippyImage21 = pygame.image.load('clippy21.png')
clippyImage22 = pygame.image.load('clippy22.png')
clippyImage23 = pygame.image.load('clippy23.png')
clippyImage24 = pygame.image.load('clippy24.png')
clippyImage25 = pygame.image.load('clippy25.png')
clippyImage26 = pygame.image.load('clippy26.png')
clippyImage27 = pygame.image.load('clippy27.png')
clippyImage28 = pygame.image.load('clippy28.png')
clippyImage29 = pygame.image.load('clippy29.png')
clippyImage30 = pygame.image.load('clippy30.png')
clippyImage31 = pygame.image.load('clippy31.png')

clippyImage32 = pygame.image.load('clippy32.png')#optometrist/optical technician stuff
clippyImage33 = pygame.image.load('clippy33.png')
clippyImage34 = pygame.image.load('clippy34.png')
clippyImage35 = pygame.image.load('clippy35.png')
clippyImage36 = pygame.image.load('clippy36.png')
clippyImage37 = pygame.image.load('clippy37.png')
clippyImage38 = pygame.image.load('clippy38.png')
clippyImage39 = pygame.image.load('clippy39.png')
clippyImage40 = pygame.image.load('clippy40.png')
clippyImage41 = pygame.image.load('clippy41.png')
optoImage1 = pygame.image.load ('opto1.png')
optoImage2 = pygame.image.load ('opto2.png')
optoImage3 = pygame.image.load ('opto3.png')
optoImage4 = pygame.image.load ('opto4.png')
optoImage5 = pygame.image.load ('opto5.png')
optoImage6 = pygame.image.load ('opto6.png')
optoImage7 = pygame.image.load ('opto7.png')
optoImage8 = pygame.image.load ('opto8.png')

reflectImage = pygame.image.load('refl.png')
reflectImage2 = pygame.image.load('refl2.png')
reflectImage3 = pygame.image.load('refl3.png')
reflectImage4 = pygame.image.load('refl4.png')
reflectImage5 = pygame.image.load('refl5.png')
reflectImage6 = pygame.image.load('refl6.png')

refractImage = pygame.image.load('refr.png')
refractImage2 = pygame.image.load('refr2.png')
refractImage3 = pygame.image.load('refr3.png')
refractImage4 = pygame.image.load('refr4.png')
refractImage5 = pygame.image.load('refr5.png')
refractImage6 = pygame.image.load('refr6.png')
refractImage7 = pygame.image.load('refr7.png')
refractImage8 = pygame.image.load('refr8.png')
refractImage9 = pygame.image.load('refr9.png')
refractImage10 = pygame.image.load('refr10.png')
refractImage11 = pygame.image.load('refr11.png')

userQuit = 0 #detect quit variable

def rot_center(image, angle): #rotates images
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def quitMenu(userQuit): #quit menu options
        
    quitPrompt = font14.render("WOULD YOU LIKE TO QUIT?",1,black)
    quitYes = font20.render("YES",1,black)
    quitNo = font20.render("NO",1,black)

    while True:

        for event in pygame.event.get(): #get user events
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    userQuit = 1

                if event.key == pygame.K_RIGHT:
                    userQuit = 0

                if event.key == pygame.K_RETURN:
                    if userQuit == 1:
                        exitGame = True
                        quit()

                    else:
                        return
    
        pygame.draw.rect(gameDisplay,black,(300,265,200,70))
        pygame.draw.rect(gameDisplay,white,(302,267,196,66))
    
        gameDisplay.blit(quitPrompt,(309,273))#print user prompt quit?(Y/N)
        gameDisplay.blit(quitYes,(335,300))
        gameDisplay.blit(quitNo,(435,300))
                
        if userQuit == 1: #user selection box
            pygame.draw.rect(gameDisplay,black,(333,301,40,20),1)

        if userQuit == 0:
            pygame.draw.rect(gameDisplay,black,(431,301,31,20),1)

        pygame.display.update()

def returnMenu():

    returnSelect = 0 #return menu var

    returnText = font14.render("WOULD YOU LIKE TO RETURN",1,black)
    returnText1 = font14.render("TO THE MAIN MENU?",1,black)

    returnYes = font20.render("YES",1,black)
    returnNo = font20.render("NO",1,black)
    
    while True:

        for event in pygame.event.get(): #get user events
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    returnSelect = 1

                if event.key == pygame.K_RIGHT:
                    returnSelect = 0

                if event.key == pygame.K_RETURN:
                    if returnSelect == 1:
                        menu()

                    else:
                        return

        pygame.draw.rect(gameDisplay,black,(295,265,210,90))
        pygame.draw.rect(gameDisplay,white,(297,267,206,86))

        gameDisplay.blit(returnText,(304,273))
        gameDisplay.blit(returnText1,(331,288))

        gameDisplay.blit(returnYes,(341,315))
        gameDisplay.blit(returnNo,(431,315))

        if returnSelect == 1:
            pygame.draw.rect(gameDisplay,black,(338,315,42,21),1)
            
        if returnSelect == 0:
            pygame.draw.rect(gameDisplay,black,(427,315,31,21),1)
        
        pygame.display.update()#refresh

def helpMenu():

    helpText = font14.render("MOVE: LEFT ARROW RIGHT ARROW",1,black)
    helpText1 = font14.render("ROTATE: A D",1,black)
    helpText2 = font14.render("TURN ON OFF LASER: ENTER",1,black)
    helpText3 = font14.render("SELECT: UP ARROW DOWN ARROW",1,black)
    helpText4 = font14.render("SELECT: ENTER",1,black)
    helpText5 = font14.render("RETURN: ESCAPE",1,black)
    
    while True:

        for event in pygame.event.get(): #gets all events and user input

            if event.type == pygame.QUIT:
                quitMenu(userQuit)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnMenu()

        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay,black,(275,100,250,400))
        pygame.draw.rect(gameDisplay,white,(277,102,246,396))

        gameDisplay.blit(helpText,(286,110))
        gameDisplay.blit(helpText1,(285,130))
        gameDisplay.blit(helpText2,(285,150))
        gameDisplay.blit(helpText3,(285,170))
        gameDisplay.blit(helpText4,(285,190))
        gameDisplay.blit(helpText5,(285,210))
        
        
        pygame.display.update()#refresh

def menu():

    menuSelect = 1 #menu select var

    menuText0 = font20
    
    menuText = font40.render("LASER",1,black)
    menuText1 = font40.render("SIMULATOR",1,black)
    menuText2 = font30.render("REFLECTION",1,black)
    menuText3 = font30.render("REFRACTION",1,black)
    menuText4 = font30.render("DEFRACTION",1,black)
    menuText5 = font30.render("HELP",1,black)
    menuText6 = font30.render("QUIT",1,black)

    rand = random.randint(1,3)
    
    while True:

        for event in pygame.event.get(): #gets all events and user input

            if event.type == pygame.QUIT:
                quitMenu(userQuit)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if menuSelect > 1:
                        menuSelect = menuSelect - 1

                if event.key == pygame.K_DOWN:
                    if menuSelect < 5:
                        menuSelect = menuSelect + 1

                if event.key == pygame.K_RETURN:
                    if menuSelect == 1:
                        game = "reflection"
                        reflectionText()
                        reflection(game)
                        
                    elif menuSelect == 2:
                        game = "refraction"
                        refractionText()
                        refraction(game)
                        
                    elif menuSelect == 4:
                        helpMenu()
                    
                    elif menuSelect == 5:
                        quitMenu(userQuit)
                        
        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay,black,(275,100,250,400))
        pygame.draw.rect(gameDisplay,white,(277,102,246,396))

        if menuSelect == 1:
            pygame.draw.rect(gameDisplay,black,(306,230,190,31))
            pygame.draw.rect(gameDisplay,white,(308,232,186,27))
        
        elif menuSelect == 2:
            pygame.draw.rect(gameDisplay,black,(306,280,190,31))
            pygame.draw.rect(gameDisplay,white,(308,282,186,27))

        elif menuSelect == 3:
            pygame.draw.rect(gameDisplay,black,(306,330,190,31))
            pygame.draw.rect(gameDisplay,white,(308,332,186,27))

        elif menuSelect == 4:
            pygame.draw.rect(gameDisplay,black,(356,380,81,31))
            pygame.draw.rect(gameDisplay,white,(358,382,77,27))

        elif menuSelect == 5:
            pygame.draw.rect(gameDisplay,black,(356,430,81,34))
            pygame.draw.rect(gameDisplay,white,(358,432,77,30))

        gameDisplay.blit(menuText,(340,110)) #title
        gameDisplay.blit(menuText1,(293,150))

        gameDisplay.blit(menuText2,(310,230))
        gameDisplay.blit(menuText3,(310,280))
        gameDisplay.blit(menuText4,(310,330))
        gameDisplay.blit(menuText5,(360,380))
        gameDisplay.blit(menuText6,(360,430))

        if rand == 1:
            gameDisplay.blit(clippyImage3,(550,434))
        elif rand == 2:
            gameDisplay.blit(clippyImage4,(550,434))
        elif rand == 3:
            gameDisplay.blit(clippyImage5,(550,434))

        pygame.display.update()#refresh

def reflectionText():
    print("In many instances, light travels in straight lines.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(reflectImage,(200,150))
        gameDisplay.blit(clippyImage6,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh

    print("REFLECTION is a change in direction after meeting an obstacle, where the original ray and the reflected ray are on the same side of the obstacle.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(reflectImage2,(200,150))
        gameDisplay.blit(clippyImage12,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh
        
    print("The normal line is drawn at a right angle to the surface of the obstacle where the light ray striked.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(reflectImage3,(200,150))
        gameDisplay.blit(clippyImage7,(550,362))
        clock.tick(59)
        pygame.display.update()#refresh

    print("The angle of incidence is the angle between the incoming, or incident, ray and the normal.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(reflectImage4,(200,150))
        gameDisplay.blit(clippyImage8,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh

    print("The angle of reflection is the angle between the outgoing, or reflected, ray and the normal.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(reflectImage5,(200,150))
        gameDisplay.blit(clippyImage9,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("Light, then, behaves according to the LAW OF REFLECTION.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(reflectImage6,(200,150))
        gameDisplay.blit(clippyImage10,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("LAW OF REFLECTION: The law of reflection states that for reflection from a flat surface, the angle of incidence is always equal to the angle of reflection.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(reflectImage6,(200,150))
        gameDisplay.blit(clippyImage11,(550,362))
        clock.tick(59)
        pygame.display.update()#refresh

    print("Here is a simulation of how reflection works.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(clippyImage13,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh

def refractionText():
    print("When a light wave strikes a transparent material, some of the light passes, or transmits, through the material.\n")#4
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage,(200,150))
        gameDisplay.blit(clippyImage14,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh
        
    print("The original ray that travels into the material is called the refracted ray.\n")#2
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage,(200,150))
        gameDisplay.blit(clippyImage15,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("The direction of the refracted ray is different from the direction of the incident ray.\n")#3
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage,(200,150))
        gameDisplay.blit(clippyImage16,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("This effect is called REFRACTION.\n")#1
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage,(200,150))
        gameDisplay.blit(clippyImage17,(550,434))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("The ratio of the speed of light in  a vacuum to the speed of light in another medium is called index of refraction.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage2,(200,150))
        gameDisplay.blit(clippyImage18,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("It is calculated by the formula: n = c / v\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage3,(200,150))
        gameDisplay.blit(clippyImage19,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("When light travels from one medium to another medium that has a higher index of refraction, the light is refracted towards the normal.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage,(200,150))
        gameDisplay.blit(clippyImage20,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("When light travels from one medium to another with a lower index of refraction, light is refracted away from the normal.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage4,(200,150))
        gameDisplay.blit(clippyImage21,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("The angle of refraction can be calculated using Snell's Law.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(clippyImage22,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("Snell's Law: n1sinθ1 = n2sinθ2\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage5,(200,150))
        gameDisplay.blit(clippyImage23,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("When light travels from a denser medium to a less dense medium, the angle of refraction will be greater than the angle of incidence.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage6,(200,150))
        gameDisplay.blit(clippyImage24,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("When the angle of refraction reaches 90°, the refracted ray will be parallel to the surface.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage7,(200,150))
        gameDisplay.blit(clippyImage25,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh
        
    print("The value of the angle of incidence at which this occurs is called the critical angle.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage8,(200,150))
        gameDisplay.blit(clippyImage26,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("If the angle of incidence increases beyond the critical angle, no refraction occurs.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage9,(200,150))
        gameDisplay.blit(clippyImage27,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("Instead, the incident ray is reflected at the boundary.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage10,(200,150))
        gameDisplay.blit(clippyImage28,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("This is called total internal reflection.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage10,(200,150))
        gameDisplay.blit(clippyImage29,(550,434))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("The critical angle can be calculated using this formula: sinθ = n2 / n1\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(refractImage11,(200,150))
        gameDisplay.blit(clippyImage30,(550,398))
        clock.tick(59)
        pygame.display.update()#refresh
    
    print("Here is a simulation of how refraction and total internal reflection works.\n")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(clippyImage31,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh

def optomText ():
    print ("Knowledege on refraction, defraction and reflection can be applied to jobs such as an optometrist.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(clippyImage32,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh

    print ("An optometrist is a person who's job is to diagnose and treat medical conditions that involve the visual system.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto1,(200,150))
        gameDisplay.blit(clippyImage33,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh

    print ("Another career that involves optics is an optical technician.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(clippyImage34,(550,416))
        clock.tick(59)
        pygame.display.update()#refresh

    print ("An optical technician is a specialist whose job is to produce eyeglasses according to their prescriptions.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto2,(200,150))
        gameDisplay.blit(clippyImage35,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh

    print ("To become an optical technician, you must complete an optometry program at a university.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto3,(200,150))
        gameDisplay.blit(clippyImage36,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh
        
    print ("Since optics play an important role in making eyeglasses we will briefly cover how the lenses in glasses work.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto4,(100,100))
        gameDisplay.blit(clippyImage37,(550,380))
        clock.tick(59)
        pygame.display.update()#refresh
        
    print ("The first type of lens is called the convex lens. Convex lens bend light rays inward causing them to converge at one spot which is called the focal point.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto5,(100,100))
        gameDisplay.blit(clippyImage38,(550,360))
        clock.tick(59)
        pygame.display.update()#refresh

        
    print ("The second type of lens is called the concave lens. Concave lens make parallel light rays curve outward or diverge")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto6,(100,100))
        gameDisplay.blit(clippyImage39,(550,360))
        clock.tick(59)
        pygame.display.update()#refresh

    print ("An optometrist may diagnose someone with nearsightedness. Nearsightedness is a refractive error where close objects appear clearly, but distant objects appear blurry. This is usually treated with convex lens.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto7,(100,100))
        gameDisplay.blit(clippyImage40,(550,330))
        clock.tick(59)
        pygame.display.update()#refresh

    print ("Farsightedness is a refractive error where distant objects may be seen more clearly than objects that are near. This is usually treated with concave lens.")
    for x in range(0,240):
        gameDisplay.fill(white)
        gameDisplay.blit(opto8,(100,100))
        gameDisplay.blit(clippyImage41,(550,330))
        clock.tick(59)
        pygame.display.update()#refresh
    
    
def reflectLaser(endx,playery,laserAngle):
    pygame.draw.line(gameDisplay,green,(endx,(playery - 325)),(endx - (465 * math.tan(math.radians(laserAngle))),(playery + 140)),2)

    pygame.draw.line(gameDisplay,black,(endx,(playery - 325)),(endx,(playery - 275)),1)
    pygame.draw.line(gameDisplay,black,(endx,(playery - 250)),(endx,(playery - 200)),1)
    pygame.draw.line(gameDisplay,black,(endx,(playery - 175)),(endx,(playery - 125)),1)

def refractLaser(endx,playery,laserAngle,n1,n2):
    
    refractAngle = math.asin(n1 * math.sin(math.radians(laserAngle))/n2)
    endx2 = endx - 200 * math.tan(refractAngle)
    
    pygame.draw.line(gameDisplay,green,(endx,(playery - 125)),((endx - 200 * math.tan(refractAngle)),150),2)
    pygame.draw.line(gameDisplay,green,(endx2,150),(endx2 - 150 * math.tan(math.radians(laserAngle)),0),2)

    pygame.draw.line(gameDisplay,green,)

def mirror():
    pygame.draw.rect(gameDisplay,black,(27,100,746,50))

def lens():
    pygame.draw.rect(gameDisplay,black,(5,150,790,200),2)

def player(playerx,playery,rot_image): #player's laser
    gameDisplay.blit(rot_image,(playerx,playery))

def shootLaser(playerx,playery,laserAngle,game):

    if game == "reflection":
        y = 465

    elif game == "refraction":
        y = 265
        
    endx = playerx + 139 - (y * math.tan(math.radians(laserAngle)))
    
    if game == "reflection" and endx > 27 and endx < 773:
        pygame.draw.line(gameDisplay,green,((playerx + 139),(playery + 140)),(endx,(playery - 325)),2)
        reflectLaser(endx,playery,laserAngle)

    elif game == "refraction" and endx > 5 and endx < 795:
        pygame.draw.line(gameDisplay,green,((playerx + 139),(playery + 140)),(endx,(playery - 125)),2)
        refractLaser(endx,playery,laserAngle,n1,n2)
    
    else:
        pygame.draw.line(gameDisplay,green,((playerx + 139),(playery + 140)),((playerx + 139 - (620 * math.tan(math.radians(laserAngle)))),(playery - 480)),2)

def reflection(game):

    exitGame = False #game loop variable

    laserState = -1 #laser on/off
    laserAngle = 0

    playerx = displayWidth/2 - 140#player x
    playery = 475 #y

    moveLeft = 0 #player movement variable
    moveRight = 0

    leftTilt = 0 #player angular movement var
    rightTilt = 0

    while not exitGame:

        for event in pygame.event.get(): #gets all events and user input

            if event.type == pygame.QUIT:
                quitMenu(userQuit)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnMenu()
                
                if event.key == pygame.K_LEFT:
                    moveLeft = 5

                if event.key == pygame.K_RIGHT:
                    moveRight = 5

                if event.key == pygame.K_RETURN:
                    laserState = laserState * -1

                if event.key == pygame.K_a:
                    leftTilt = 1

                if event.key == pygame.K_d:
                    rightTilt = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moveLeft = 0

                if event.key == pygame.K_RIGHT:
                    moveRight = 0

                if event.key == pygame.K_a:
                    leftTilt = 0
                    
                if event.key == pygame.K_d:
                    rightTilt = 0

        gameDisplay.fill(white)

        mirror()

        if laserState == 1:
            shootLaser(playerx,playery,laserAngle,game)

        if laserAngle < 70:
            laserAngle = laserAngle + leftTilt
            
        if laserAngle > -70:
            laserAngle = laserAngle - rightTilt

        player(playerx,playery,rot_center(laserImage,laserAngle))

        if playerx > -115: #user movement logic
            playerx = playerx - moveLeft

        if playerx < 635:
            playerx = playerx + moveRight

        pygame.display.update()#refresh
        clock.tick(59)

def refraction(game):
    
    exitGame = False #game loop variable

    laserState = -1 #laser on/off
    laserAngle = 0

    playerx = displayWidth/2 - 140#player x
    playery = 475 #y

    moveLeft = 0 #player movement variable
    moveRight = 0

    leftTilt = 0 #player angular movement var
    rightTilt = 0

    while not exitGame:

        for event in pygame.event.get(): #gets all events and user input

            if event.type == pygame.QUIT:
                quitMenu(userQuit)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnMenu()
                
                if event.key == pygame.K_LEFT:
                    moveLeft = 5

                if event.key == pygame.K_RIGHT:
                    moveRight = 5

                if event.key == pygame.K_RETURN:
                    laserState = laserState * -1

                if event.key == pygame.K_a:
                    leftTilt = 1

                if event.key == pygame.K_d:
                    rightTilt = 1

                if event.key == pygame.K_o:
                    n1 = input("Enter index of refraction for first medium: ")

                if event.key == pygame.K_p:
                    n2 = input("Enter index of refraction for second medium: ")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moveLeft = 0

                if event.key == pygame.K_RIGHT:
                    moveRight = 0

                if event.key == pygame.K_a:
                    leftTilt = 0
                    
                if event.key == pygame.K_d:
                    rightTilt = 0

        gameDisplay.fill(white)

        lens()

        if laserState == 1:
            shootLaser(playerx,playery,laserAngle,game)

        if laserAngle < 70:
            laserAngle = laserAngle + leftTilt
            
        if laserAngle > -70:
            laserAngle = laserAngle - rightTilt

        player(playerx,playery,rot_center(laserImage,laserAngle))

        if playerx > -115: #user movement logic
            playerx = playerx - moveLeft

        if playerx < 635:
            playerx = playerx + moveRight

        pygame.display.update()#refresh
        clock.tick(59)
    
def main(): #gameloop

    exitGame = False #game loop variable

    while not exitGame:

        for event in pygame.event.get(): #gets all events and user input

            if event.type == pygame.QUIT:
                quitMenu(userQuit)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returnMenu()

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,(356,430,81,34))
        
        pygame.display.update()#refresh
        clock.tick(59)

print("Hello, I'm Clippy!\n")        
for x in range(0,240):
    gameDisplay.fill(white)
    gameDisplay.blit(clippyImage,(550,434))
    clock.tick(59)
    pygame.display.update()#refresh

print("I'll be talking to you through the CONSOLE, so please have it open.\n")
for x in range(0,240):
    gameDisplay.fill(white)
    gameDisplay.blit(clippyImage2,(550,416))
    clock.tick(59)
    pygame.display.update()#refresh
    
menu()
quit()
