import pygame
from player.player import Player

#initiate pygame
pygame.init()

#colors section
red = (255, 0, 0)
white = (255, 255, 255)

#screen
screen_width = 700 #unit in pixples 
screen_height = 700 
screen  = pygame.display.set_mode((screen_width, screen_height))


# -------------------------------------------------------player class -----------------------------------------------------




player = Player(red, screen) #instance of the player class

def borders_check_left(obj,surface):
    # function to check if an object hits
    # the borders of a surface (screen)
    # arguments (obj, surface)
    # return boolean

    if(obj.x > 0):
            return True
    return False

def borders_check_right(obj,surface):
    # function to check if an object hits
    # the borders of a surface (screen)
    # arguments (obj, surface)
    # return boolean

    if(obj.x + obj._width  < surface.get_width()):
            return True
    return False



def reDraw():
    # function to redraw the screen every frame
    # arguments None 
    # returns None

    screen.fill(white) # fill the screen with white color 
    player.draw() #draw the player


# -------------------------------------------------------main game loop -----------------------------------------------------


#main loop
clock = pygame.time.Clock()
run = True 

while run:
    for event in pygame.event.get(): #gets all the events
        if event.type == pygame.QUIT: #if you click on the x
            run = False #the program stops running 
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_RIGHT]:
                    player.moving_right = True
            
            elif pressed[pygame.K_LEFT]:
                    player.moving_left = True
        
        if event.type == pygame.KEYUP:
            player.moving_left =  False
            player.moving_right = False
    
    
    #player actions
    if borders_check_left(player, screen):
        player.move_left()
    if borders_check_right(player, screen):
        player.move_right()
    
    reDraw() # call our redraw function
    
    pygame.display.flip() # refresh the frames
    clock.tick(60)  # 60 frames per second