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

car_widht = 48
car_heigth = 108

display_width = 800
display_height = 600

pause = True

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("a bit racey")
clock = pygame.time.Clock()

carımg = pygame.image.load("car.png")
baricadeımg = pygame.image.load("baricade.png")
backgroundımg = pygame.image.load("background.png")

def things(thingx, thingy, thingw, thingh, color):
    baricade(thingx,thingy)
    #pygame.draw.rect(gameDisplay, color, [thingx ,thingy, thingw, thingh])

def button(msg,x,y,w,h,ia,a,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + 100 > mouse[0] > x and y + 50 > mouse[1] > y:
            pygame.draw.rect(gameDisplay, a, (x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "play":
                    game_loop()
                elif action == "quit":
                    pygame.quit()
                    qiut()
                elif action == "unpause":
                    unpaus()
                    #crash_loop(x,y,thing_starty, thing_startx, thing_speed, thing_width,thing_height, display_width, display_height, car_heigth,car_widht, dodged)
                    """if thing_starty > display_height:
                        thing_starty = 0 - thing_height
                        thing_startx = random.randrange(150, display_width - 150 - thing_width ) 
                        dodged += 1
                        thing_speed += 0.2"""
                elif action == "pause":
                    pause = True
                    paused()
                
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

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)   
        TextSurf, TextRect = text_objects2("A bit racey", largeText)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        

        #button(msg,x,y,w,h,ia,a)
        button("GO",150, 450, 100, 50 ,dark_green, green, "play")
        button("QUİT",500, 450, 100, 50 ,dark_red, red, "quit")

        pygame.display.update()


def unpaus():
    global pause
    pause = False



def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)   
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        

        #button(msg,x,y,w,h,ia,a)
        button("Continue",150, 450, 100, 50 ,dark_green, green, "unpause")
        button("QUİT",500, 450, 100, 50 ,dark_red, red, "quit")

        pygame.display.update()

    
def background():
    gameDisplay.blit(backgroundımg, (0,0))


def car(x,y):
    gameDisplay.blit(carımg, (x,y))


def baricade(x,y):
    gameDisplay.blit(baricadeımg, (x,y))


def text_objects(text, font):
    textsurface = font.render(text, True, red)
    return textsurface, textsurface.get_rect()
def text_objects2(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)   
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    game_loop()


def crash():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)   
        TextSurf, TextRect = text_objects("Your dead", largeText)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        

        #button(msg,x,y,w,h,ia,a)
        button("Play again",150, 450, 100, 50 ,dark_green, green, "play")

        button("QUİT",500, 450, 100, 50 ,dark_red, red, "quit")


        pygame.display.update()

def crash_loop(x,y,thing_starty, thing_startx, thing_speed, thing_width,thing_height, display_width, display_height, car_heigth, car_widht, dodged):
    if x > display_width - 150 - car_widht and x < display_width or x > 0 and x < display_width - 650  :
            crash()

    if thing_starty > display_height:
        thing_starty = 0 - thing_height
        thing_startx = random.randrange(150, display_width - 150 - thing_width ) 
        dodged += 1
        thing_speed += 0.2
            #thing_width += (dodged * 0.5)
            #thing_height += (dodged * 0.5)
        
    if y < thing_starty+thing_height and y > thing_starty:

        if x > thing_startx and x < thing_startx + thing_width or x + car_widht > thing_startx and x + car_widht < thing_startx + thing_width :
            crash()



def game_loop():
    global pause
    x = (display_width * 0.41)
    y = (display_height * 0.73)

    x_change = 0
    y_change = 0
    thing_speed_change = 0

    
    thing_starty = -400
    thing_speed = 5
    thing_width = 88
    thing_height = 39
    thing_startx = random.randrange(150, display_width - 150 - thing_width ) 

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
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
        pygame.draw.rect(gameDisplay, green, [0, 0, 150, display_height])
        pygame.draw.rect(gameDisplay, green, [650, 0, 150, display_height])
        pause_write()
        reply_write()
        button ("| |",740, 10, 50, 50, blue, blue, "pause")

#things(thingx, thingy, thingw, thingh, color)

        things(thing_startx, thing_starty, thing_width, thing_height, green)
        thing_starty += thing_speed
        if thing_speed >= 60:
            thing_speed = 60
        elif thing_speed <= 0:
            thing_speed = 0
        
        car(x,y)
        thing_dodged(dodged)
        
        if x > display_width - 150 - car_widht and x < display_width or x > 0 and x < display_width - 650  :
            crash()

        crash_loop(x,y,thing_starty, thing_startx, thing_speed, thing_width, thing_height, display_width, display_height, car_heigth, car_widht, dodged)
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(150, display_width - 150 - thing_width ) 
            dodged += 1
            thing_speed += 0.2
        
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
