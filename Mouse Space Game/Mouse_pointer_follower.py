#Calvin Field
#4/28/15
#Spaceship game
import pygame
from livewires import games, color
import math
import random
from Tkinter import *
import RespawnWin
import NameSys


games.init(screen_width = 1600, screen_height = 1000, fps = 50)

#Make all the global variables
global_new_angle = 0
spaceshipX = 0
spaceshipY = 0

enemy_count = 0
user_dead = True

already_made = True

will_respawn = None

score_value = 0

#Load images and sound for explosion
explosion_files = ['Explode.png',
                'Explode2.png',
                'Explode3.png',
                'Explode4.png',
                'Explode5.png',
                'Explode6.png',
                'Explode7.png',
                'Explode8.png',
                'Explode9.png',
                'Explode10.png',
                'Explode11.png',
                'Explode12.png',
                'Explode13.png',
                'Explode14.png',
                'Explode15.png',
                'Explode16.png',
                'Explode17.png']

class Create_spaceship(games.Sprite):
    '''A spaceship controlled by the arrow keys'''
    image = games.load_image('8-bit_Spaceship_withBG.png')
    explosion_sound = games.load_sound('Explosion.wav')
    SHOT_DELAY = 25

    def __init__(self, x, y):
        '''Initiate spaceship'''
        super(Create_spaceship, self).__init__(image = Create_spaceship.image,
                                        x = x,
                                        y = y)
        self.shot_timer = 0
    
    def update(self):
        '''Move the sprite with keystrokes'''
        key = pygame.key.get_pressed()
        dist = 5
     
        if key[pygame.K_w]:
            self.y -= dist
        if key[pygame.K_s]:
            self.y += dist
        if key[pygame.K_a]:
            self.x -= dist
        if key[pygame.K_d]:
            self.x += dist

        #Check to see if the spaceship is oustside boundries
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        if self.top < 0:
            self.top = 0
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height

        #Change global ship variables
        global spaceshipX
        global spaceshipY
        spaceshipX = self.x
        spaceshipY = self.y

        #Fire laser
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                new_laser = Laser(self.x, self.y, self.angle, 25, 150, 80)
                new_laser.sound.play()
                games.screen.add(new_laser)
     
        #Get angle of the sprite
        self.get_mouse_angle()

        #Check to see if the spaceship is has collided with anything
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                print sprite
                sprite.die()
            self.die()

        #Check if all enemies are dead; if so then spawn more, (should make this into seperate function)
        global enemy_count
        if enemy_count == 0:
            create_enemies(self)

    def get_mouse_angle(self):
        '''Will get the angle between the mouse and the image, and then determine the angles that the sprite will turn'''
        #Get both x and y coordinates for the mouse and sprite(spaceship)
        mouseX = games.mouse.x
        mouseY = games.mouse.y
        spaceshipX = self.x
        spaceshipY = self.y

        #Get the vector cooridinates in a tuple
        self.moveVector = (spaceshipX - mouseX, spaceshipY - mouseY)

        #Use the math.atan2() method to get the final angle in radians
        self.new_angle = math.atan2(self.moveVector[0],self.moveVector[1])

        #Convert the radians to degrees and reverse it
        global global_new_angle
        self.new_angle = -(self.new_angle * 57.2957795)
        global_new_angle = self.new_angle
     
        #Start the rotate method
        self.rotate()
     
    def rotate(self):
        '''Rotates the sprite at the angle found in get_angle()'''

        #Turns the sprite at the angle found in the get_angle() method
        self.angle = self.new_angle


    def die(self):
        '''Destroys itself'''
        global user_dead
        self.destroy()
        x = self.x
        y = self.y
        #Play explosion animation
        explosion = games.Animation(images = explosion_files,
                                    is_collideable = False,
                                    x = x,
                                    y = y,
                                    n_repeats = 1,
                                    repeat_interval = 3)
        games.screen.add(explosion)
        Create_spaceship.explosion_sound.play()
        user_dead = True



class Enemy(games.Sprite):
    '''Will create enemy spaceships that fly around and shoots at the player'''
    image = games.load_image('Enemy_ship.png')
    explosion_sound = games.load_sound('Explosion.wav')
    def __init__(self,spaceship_x, spaceship_y):
        '''Will initiate the enemy ship and put it on screen in a random location'''
        x = random.randrange(games.screen.width-20)
        y = random.randrange(games.screen.height-20)

     
        #Create the ship
        super(Enemy, self).__init__(image = Enemy.image,
                                    x = x,
                                    y = y)
     
        self.shot_delay = random.randrange(4.5*games.screen.fps,5.5*games.screen.fps)
        self.chng_direct = 0
        self.jiggle = 50
    def update(self):
        '''Moves the enemy and changes the angle'''
        #Will cause the enemies to move around the screen, randomly changing direction and speed
        if user_dead != True:
            if self.chng_direct == 0:
                x_move = random.randrange(2,3)
                y_move = random.randrange(2,3)

                chances = random.randrange(9)
                if chances == 1:
                    self.dx = x_move
                    self.dy = 0
                elif chances == 2:
                    self.dy = y_move
                    self.dx = 0
                elif chances == 3:
                    self.dx = -(x_move)
                    self.dy = 0
                elif chances == 4:
                    self.dy = -(y_move)
                    self.dx = 0
                elif chances == 5:
                    self.dy = y_move
                    self.dx = x_move
                elif chances == 6:
                    self.dy = -(y_move)
                    self.dx = -(x_move)
                elif chances == 7:
                    self.dy = y_move
                    self.dx = -(x_move)
                elif chances == 8:
                    self.dy = -(y_move)
                    self.dx = x_move
                self.chng_direct = random.randrange(3.5*games.screen.fps, 5.5*games.screen.fps)
            else:
                self.chng_direct -= 1

            #Check to see if the enemy has collided with wall
        if self.right > games.screen.width:
            self.dx = -(self.dx)
        if self.left < 0:
            self.dx = -(self.dx)
        if self.top < 0:
            self.dy = -(self.dy)
        if self.bottom > games.screen.height:
            self.dy = -(self.dy)
         
        #Find new angle and rotate
        self.angle = self.find_angle()

        #Will have a delayed laser shot
        if self.shot_delay > 0:
            self.shot_delay -= 1

        #Will fire laser if shot_delay is 0 and the user is not dead
        if self.shot_delay == 0 and user_dead != True:
            new_laser = Laser(self.x, self.y, self.angle, 7, 100, 230)
            new_laser.sound.play()
            games.screen.add(new_laser)
            self.shot_delay = random.randrange(1.5*games.screen.fps,6*games.screen.fps)
     
        #Will jiggle all enemies on screen if player is dead
        dist = 8
        if user_dead == True and self.jiggle > 0:
            self.dx = 0
            self.dy = 0
         
            num = self.jiggle/5
         
            if num == 10:
                self.x += dist
            if num == 9:
                self.x -= dist
                self.y += dist
            if num == 8:
                self.x += dist
            if num == 7:
                self.x -= dist
                self.y -= dist
            if num == 6:
                self.x += dist
            if num == 5:
                self.x -= dist
                self.y += dist
             
            self.jiggle -= 1
         
    def find_angle(self):
        '''Will allow the enemy to always be looking at the user ship by changing the angle'''
        enemyX = self.x
        enemyY = self.y
        global spaceshipX
        global spaceshipY

        #Get the vector of the spaceship and enemy
        self.moveVector = (enemyX - spaceshipX, enemyY - spaceshipY)

        #Use the math.atan2() method to calculate the angle in radians
        radians = math.atan2(self.moveVector[0], self.moveVector[1])

        #Change to degrees and reverse it
        new_angle = -(radians * 57.2957795)

        return new_angle

    def die(self):
        '''Will destroy itself'''
        global enemy_count
        self.destroy()
        enemy_count -= 1
        x = self.x
        y = self.y
        explosion = games.Animation(images = explosion_files,
                                    is_collideable = False,
                                    x = x,
                                    y = y,
                                    n_repeats = 1,
                                    repeat_interval = 3)
        games.screen.add(explosion)
        Enemy.explosion_sound.play()
        global score_value
        score_value += 50


     
class Cursor(games.Sprite):
    '''Will make the crosshair image be controlled by the cursor'''
    image = games.load_image('Crosshairs.png')

    def __init__(self):
        self.wait = 60
        super(Cursor,self).__init__(image=Cursor.image,
                    is_collideable = False,
                    x = games.mouse.x,
                    y = games.mouse.y)
    def update(self):
        '''Will move the cursor image by the mouse'''
        self.x = games.mouse.x
        self.y = games.mouse.y

        #Will be used to see if the user has died and to open the respawn window
        #The cursor is being used for this because it can never be destroyed and a loop is needed
        global already_made
        if user_dead == True and already_made == False:
            if self.wait > 0:
                self.wait -= 1
            else:
                global will_respawn
                RespawnWin.spawn_window(already_made)
                self.exit = RespawnWin.get_exit()
                if self.exit == 'Yes':
                    pygame.quit()
                will_respawn = RespawnWin.get_respawn()
                if will_respawn == 'Yes':
                    spawn()
                    self.wait = 60
                will_save = RespawnWin.get_save()
                if will_save == 'Yes':
                    NameSys.store(score_value)



            
class Score(games.Text):
    '''Is the text that will display the user's score'''
    def __init__(self):
        '''Will initialize the score'''
        super(Score, self).__init__(value = 0,
                                    is_collideable = False,
                                    size = 60,
                                    color = color.red,
                                    x = 1520,
                                    y = 50)
    def update(self):
        '''Will change the score when enemy is killed'''
        self.value = score_value

        
            
def spawn():
    '''Will spawn a new spaceship and reset some variables'''
    global user_dead
    global already_made
    global score_value
    spaceship = Create_spaceship(x=games.screen.width/2,y=games.screen.height/2)
    games.screen.add(spaceship)
    already_made = False
    user_dead = False
    score_value = 0





class Laser(games.Sprite):
    '''Will create and manage the laser that will be shot out of both the spaceship and enemies'''
    image = games.load_image('Laser_shot.png')
    sound = games.load_sound('Laser_blast.wav')


    def __init__(self,spaceship_x, spaceship_y, spaceship_angle, want_speed, want_dist, life):
        '''Initialize the laser'''
        self.new_angle = spaceship_angle
        #change current ship angle from degrees into radians
        start_angle = spaceship_angle * math.pi / 180

        #Calculate start position
        dist_x = want_dist * math.sin(start_angle)
        dist_y = want_dist* -math.cos(start_angle)
        x = spaceship_x + dist_x
        y = spaceship_y + dist_y

        #Calculate lasers speed
        dx = want_speed * math.sin(start_angle)
        dy = want_speed * -math.cos(start_angle)

        #Create laser sprite
        super(Laser, self).__init__(image = Laser.image,
                                    angle = spaceship_angle,
                                    x = x, y = y,
                                    dx = dx, dy = dy)
     
        self.life = life
    
    def update(self):
        '''updates laser properties'''
        #Check to see if the laser has hit an object
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
     
        #Deals with the life of the laser
        self.life -= 1
        if self.life == 0:
            self.destroy()

    def die(self):
        '''Activates when it hits an object, destroying itself'''
        self.destroy()



def create_enemies(spaceship):
    '''Creates 5 enemies'''
    SPACE = 250
    x_min = random.randrange(SPACE)
    y_min = SPACE - x_min

    x_dist = random.randrange(x_min, games.screen.width - x_min)
    y_dist = random.randrange(y_min, games.screen.height - y_min)

    x = spaceship.x + x_dist
    y = spaceship.y + y_dist
    
    global enemy_count
    #Controls how many enemies will spawn at a time
    for i in range(6):
        enemy = Enemy(x, y)
        games.screen.add(enemy)
    enemy_count = 6

        

def main():
    #Set screen background
    screen_background = games.load_image('stars background.png', transparent = False)
    games.screen.background = screen_background
    
    
    #Play sound
##    red_alert = games.load_sound('Red_alert.wav')
##    red_alert.play()

    
    #Play Music
    music = games.load_sound('Robolympics.wav')
    music.play(-1)
##    pygame.mixer.music.load('Robolympics.mp3')
##    pygame.mixer.music.play(-1)
    #Create spaceship
    spawn()

    #Create the score
    score = Score()
    games.screen.add(score)
    
    #Create cursor sprite controlled by mouse
    cursor = Cursor()
    games.screen.add(cursor)
    games.mouse.is_visible = False


    #Starts mainloop
    games.screen.mainloop()


main()



