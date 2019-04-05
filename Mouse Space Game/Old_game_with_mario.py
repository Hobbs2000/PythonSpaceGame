#Calvin Field
#4/22/15
#Guick game using images and Tkinter canvas
import random
from Tkinter import *
import Tkinter
import tkFont
from PIL import Image, ImageTk
x = 0
x2 = 0
x_coord = 350
y = 530
y_coord = 0
######CREATE SUB-ROOT WHERE THE USER WILL CONFIRM TO START GAME########
sub_root = Tk()
sub_root.title('Start Game')


########## WHERE THE ACTUAL GAME STARTS ###############################
def Start_Game():
    '''Will start the main game'''
    sub_root.destroy()
    root = Tk()
    root.geometry('700x600')

    im = Image.open('stars background.jpg')
    tkimage = ImageTk.PhotoImage(im)
    canvas = Canvas(root,width=700,height=600,bg='white')
    canvas.place(x=0,y=0)
    background = canvas.create_image(0,0,image=tkimage)

    obj = -1

    
    class Icicle_sprite(object):
        '''Creates an icicle sprite'''
        def __init__(self):
            '''Imports the image and puts it on the canvas'''
            self.im = Image.open('Lava_icicle.png')
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.x_coord = random.randrange(0,701)
            self.sprite = canvas.create_image(self.x_coord,0,image=self.tkimage,tags='Icicle')
            self.move_down()
            
        def move_down(self):
            '''Will move the sprite down'''
            canvas.move(self.sprite,0,10)
            global y_coord
            y_coord = canvas.coords(self.sprite)
            if y_coord[1] > 650:
                canvas.delete(self.sprite)
            else:
                root.after(50,self.move_down)
            canvas.update()

                


    class Character_sprite(object):
        '''Creates the users sprite and handles the events'''
        def __init__(self):
            self.im = Image.open('invert_mario 3 tanooki_small.png')
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.char_sprite = canvas.create_image((350,530),image=self.tkimage)
            root.bind('<Left>', self.moveLeft)
            root.bind('<Right>', self.moveRight)
            root.bind('<a>', self.moveLeft)
            root.bind('<d>', self.moveRight)
            
        def moveLeft(self,event):
            '''Handles the left arrow key press event, moves char_sprite to the left'''
            self.im = Image.open('invert_mario 3 tanooki_small_left.png')
            self.tkimage = ImageTk.PhotoImage(self.im)
            global x_coord
            x_coord = -20 + canvas.coords(self.char_sprite)[x]
            if x_coord < 0:
                self.char_sprite = canvas.create_image((700,530),image=self.tkimage)
            else:
                self.char_sprite = canvas.create_image((x_coord,530),image=self.tkimage)
            canvas.update()
                
        def moveRight(self,event):
            '''Handles the right arrow key press event, moves the char_sprite to the right'''
            self.im = Image.open('invert_mario 3 tanooki_small.png')
            self.tkimage = ImageTk.PhotoImage(self.im)
            global x_coord
            x_coord = 20 + canvas.coords(self.char_sprite)[x]
            if x_coord > 700:
                self.char_sprite = canvas.create_image((10,530),image=self.tkimage)
            else:
                self.char_sprite = canvas.create_image((x_coord,530),image=self.tkimage)
            canvas.update()
            
            
            
    def make_icicle():
        '''Initiates the icicle sprite and tells it what to do'''
        icicle = Icicle_sprite()
        root.after(600,make_icicle)
        
    user = Character_sprite()
    make_icicle()
    make_icicle()
    root.mainloop()


#################### WHERE THE SUB-ROOT WIDGETS ARE############################

custom_font = tkFont.Font(family='Helvetic', size=20)
    
Label(sub_root,text='Use either the "a" and "d" keys to move left and right',
      font=custom_font
      ).pack()
Label(sub_root,text='Or use the left and right arrow keys to move',
      font=custom_font
      ).pack()
Label(sub_root,text='Do your best to dodge the falling lava icicles!',
      font=custom_font
      ).pack()
start = Button(sub_root,text='Start Game',font=custom_font,
               width=30,
               height=5,
               bg='grey',
               fg='red',
               command=Start_Game)
start.pack()

sub_root.mainloop()



