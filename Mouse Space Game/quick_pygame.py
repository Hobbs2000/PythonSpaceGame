#Calvin Field
#4/26/15
#This is the same game as the quick_game.py, but using pygame, and not PIL
import random
from Tkinter import *
import pygame
from livewires import games, color
import math

#Creating screen window
games.init(screen_width = 700, screen_height = 650, fps = 50)

#Make the class for creating the player controlled spaceship
class Spaceship(games.Sprite):
    '''A spaceship controlled by the arrow keys'''
    image = games.load_image('8-bit_Spaceship_withBG.png')
    def __init__(self, y = 590):
        '''Initiates the spaceship object and score text'''
        super(Spaceship, self).__init__(image = Spaceship.image,
                                        x = 350,
                                        y = y,)

        self.score = games.Text(value = 0, size = 30, color = color.red,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
    def update(self):
        '''Move the spaceship by pressing keys'''
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_a]:
            self.x -= dist
        if key[pygame.K_d]:
            self.x += dist

        #Check to see if the player is at the edge of the screen
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        #Check to see if the spaceship hit any lava
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
            
            

    def die(self):
        '''Will destroy spaceship object if it runs into any lava'''
        self.destroy()
        

class Lava(games.Sprite):
    '''A lava icicle that falls and can destroy the player'''
    image = games.load_image('Lava_icicle_withBG.png')
    speed = 3

    def __init__(self, x, y = 50):
        '''Initiates a new lava icicle object'''
        super(Lava, self).__init__(image = Lava.image,
                                   x = x, y = y,
                                   dy = Lava.speed)
    def update(self):
        '''Will destroy itself when it reaches bottom'''
        if self.top > games.screen.height:
            self.destroy()

    def die(self):
        '''Will destroy itself if it hits the spaceship'''
        self.destroy()
        
class Lava_spawner(games.Sprite):
    '''Will spawn lava'''
    image = games.load_image('small_White_rectangle.png')
    
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        '''Initializes the spawner'''
        super(Lava_spawner, self).__init__(image = Lava_spawner.image,
                                           x = games.screen.width / 2,
                                           y = y,
                                           dx = speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        '''Determines if the direction of the spawners movement needs to be reversed'''
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.drop()

    def drop(self):
        '''Countsdown until drop then resests countdown and does it over again'''
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_lava = Lava(x = self.x)
            games.screen.add(new_lava)
            self.time_til_drop = 100
        
    

def main():
    '''Plays the game'''
    #Load the background image
    background_image = games.load_image('resized_stars background.png',
                                        transparent = False)
    games.screen.background = background_image

    #Create the spaceship
    player = Spaceship()
    games.screen.add(player)

    #Start lava flow
    spawner = Lava_spawner()
    games.screen.add(spawner)
    
    #Start mainloop
    games.screen.mainloop()

main()




