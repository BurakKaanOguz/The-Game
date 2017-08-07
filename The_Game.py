import pygame
import time
import random 

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (209,209,224)
dark_green = (0,200,0)
dark_red = (200,0,0)
dark_blue = (0,0,200)
road_green = (2,136,12)

car_widht = 48
car_heigth = 108

display_width = 800
display_height = 600

pause = False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("The Race Game")
clock = pygame.time.Clock()

carımg = pygame.image.load("car.png")
car_brokenımg = pygame.image.load("car_crush.png")
baricadeımg = pygame.image.load("baricade.png")
backgroundımg = pygame.image.load("background.png")

def things(thingx, thingy):
    baricade(thingx,thingy)
    #pygame.draw.rect(gameDisplay, color, [thingx ,thingy, thingw, thingh])

def button(msg,x,y,w,h,ia,a,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + 100 > mouse[0] > x and y + 50 > mouse[1] > y:
            pygame.draw.rect(gameDisplay, a, (x,y,w,h))
            if click[0] == 1 and action != None:
                action()
                 
                
    else:
        pygame.draw.rect(gameDisplay, ia, (x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",20)   
    TextSurf, TextRect = text_objects2(msg, smallText)
    TextRect.center = (x+ (w/2), y + (h/2))
    gameDisplay.blit(TextSurf, TextRect)



def thing_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("things dodged:"  + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def pause_write():
    font = pygame.font.SysFont(None, 25)
    text = font.render("p = pause", True, black)
    gameDisplay.blit(text, (0,25))

def reply_write():
    font = pygame.font.SysFont(None, 25)
    text = font.render("r = reply", True, black)
    gameDisplay.blit(text, (0,50))

def game_quit():
    pygame.quit()
    quit()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",100)   
        TextSurf, TextRect = text_objects2("The Race Game", largeText)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        

        #button(msg,x,y,w,h,ia,a)
        button("GO",150, 450, 100, 50 ,dark_green, green, game_loop)
        button("QUİT",500, 450, 100, 50 ,dark_red, red, game_quit)

        pygame.display.update()


def unpause():
    global pause
    pause = False



def paused():
    global pause    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",100)   
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        

        #button(msg,x,y,w,h,ia,a)
        button("Continue",150, 450, 100, 50 ,dark_green, green, unpause)
        button("QUİT",500, 450, 100, 50 ,dark_red, red, game_quit)

        pygame.display.update()

    
def background():
    gameDisplay.blit(backgroundımg, (0,0))


def car(x,y,ımg):
    gameDisplay.blit(ımg, (x,y))


def baricade(x,y):
    gameDisplay.blit(baricadeımg, (x,y))


def text_objects(text, font):
    textsurface = font.render(text, True, red)
    return textsurface, textsurface.get_rect()
def text_objects2(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",100)   
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    game_loop()


def crash(x,y,y2):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        
        gameDisplay.fill(grey)
        pygame.draw.rect(gameDisplay, road_green, [0, 0, 150, display_height])
        pygame.draw.rect(gameDisplay, road_green, [650, 0, 150, display_height])
        things(x,y2)
        #y2 = y - thing height

        car(x,y ,car_brokenımg)
        largeText = pygame.font.Font("freesansbold.ttf",100)   
        TextSurf, TextRect = text_objects("Your dead", largeText)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        

        #button(msg,x,y,w,h,ia,a)
        button("Play again",200, 450, 100, 50 ,dark_green, green, game_loop)

        button("QUİT",500, 450, 100, 50 ,dark_red, red, game_quit)


        pygame.display.update()

def crash2(x,y,):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        
        gameDisplay.fill(grey)
        pygame.draw.rect(gameDisplay, road_green, [0, 0, 150, display_height])
        pygame.draw.rect(gameDisplay, road_green, [650, 0, 150, display_height])
        
        #y2 = y - thing height

        car(x,y ,car_brokenımg)
        largeText = pygame.font.Font("freesansbold.ttf",100)   
        TextSurf, TextRect = text_objects("Your dead", largeText)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        

        #button(msg,x,y,w,h,ia,a)
        button("Play again",200, 450, 100, 50 ,dark_green, green, game_loop)

        button("QUİT",500, 450, 100, 50 ,dark_red, red, game_quit)


        pygame.display.update()




def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.80)

    x_change = 0
    y_change = 0
    thing_speed_change = 0

    
    thing_starty = -400
    thing_speed = 5
    thing_width = 88
    thing_height = 39
    thing_startx = random.randrange(150, display_width - 150 - thing_width ) 
    y2 = y - thing_height
    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    thing_speed_change = 0.2
                elif event.key == pygame.K_DOWN:
                    thing_speed_change = -0.2
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_r:
                    game_loop()
                    

            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    thing_speed_change = 0
        x += x_change
        #thing_speed += thing_speed_change
        gameDisplay.fill(grey)
        #gameDisplay.blit(backgroundımg, (0,0))
        #background()
        pygame.draw.rect(gameDisplay, road_green, [0, 0, 150, display_height])
        pygame.draw.rect(gameDisplay, road_green, [650, 0, 150, display_height])
        pause_write()
        reply_write()

#things(thingx, thingy, thingw, thingh, color)

        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        if thing_speed >= 60:
            thing_speed = 60
        elif thing_speed <= 0:
            thing_speed = 0
        
        car(x,y, carımg)
        thing_dodged(dodged)
        
        if x > display_width - 150 - car_widht and x < display_width or x > 0 and x < display_width - 650  :
            crash2(x,y)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(150, display_width - 150 - thing_width ) 
            dodged += 1
            thing_speed += 0.2

        if y < thing_starty+thing_height and y > thing_starty:

            if x > thing_startx and x < thing_startx + thing_width or x + car_widht > thing_startx and x + car_widht < thing_startx + thing_width :
                crash(x,y,y2)
        
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
game_quit()
