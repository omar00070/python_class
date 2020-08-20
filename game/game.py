import pygame
import math

backgound_color = (137, 223, 158)
screen_width = 500
screen_height = 500
screen  = pygame.display.set_mode((screen_width, screen_height))
screen.fill(backgound_color)
run = True
rect_color = (150, 150, 150)
rectangle = (100, 45, 50, 50)
grey = (150, 150, 150)

class Mario:
    def __init__(self):
        self.x_pos = 150
        self.y_pos = 50
        self.height = 100
        self.width = 100
        self.color = grey


    def draw(self):
        rectangle = (self.x_pos, self.y_pos, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)

    def move_right(self):
        self.x_pos += 10

    def move_left(self):
        self.x_pos -= 10
    
    def jump(self):
        vel = 30
        angle = math.pi/4
        vel_x = int(vel * math.cos(angle))
        vel_y = int(vel * math.sin(angle))
        self.x_pos += vel_x
        self.y_pos += vel_y - 0.5 * 9.81
        print(vel_x, vel_y)


mario1 = Mario()


while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT]:
                if mario1.x_pos <= screen_width - mario1.width:
                    mario1.move_right()
            if pressed[pygame.K_LEFT]:
                if mario1.x_pos >= 0:
                    mario1.move_left()
                    mario1.jump()
    screen.fill(backgound_color)
    mario1.draw()
    
    pygame.display.update()