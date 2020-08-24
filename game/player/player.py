#this file is to host the player class
#the player is able to move to the right and the left
import pygame

class Player:
    def __init__(self, color, screen): # initiate the player with its attributes 
        self.x = 30             #position x
        self.y = 50             #position y
        self._speed = 15        #speed of moving to the right
        self._height = 15       
        self._width = 15
        self.color = color
        self.moving_right = False
        self.moving_left = False
        self.surface = screen
    def draw(self):
        pygame.draw.rect(self.surface, self.color,(self.x, self.y, self._width, self._height)) # draw the player on the screen


    def move_right(self):
        if(self.moving_right):
            self.x += self._speed

    def move_left(self):
        if(self.moving_left):
            self.x -= self._speed