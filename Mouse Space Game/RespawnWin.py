#Calvin Field
#To be imported into a game, used in Calvin's final independent game
#Will loop to see if the player has died, and will open the respawn window if so
from Tkinter import *
import tkFont
import NameSys
import cPickle
import HighScores

respawn = 'No'
Exit = 'No'
save = 'No'
all_items = None
def spawn_window(already_made):
    '''Creates a tkinter window asking if the user wants to respawn'''
    class Application(Frame):
        '''Is a GUI application that will make and control all the widgets'''
        def __init__(self, master, main):
            '''Creates the frame'''
            Frame.__init__(self, master)
            self.grid()
            if main == True:
                self.create_main_widgets()
            else:
                self.create_sub_widgets()
            
        def create_main_widgets(self):
            '''Will create all the widgets'''
            font = ("Times", "24", "bold")
            
            self.spawnbttn = Button(self, text='Respawn',
                                    font = font,
                                    command=self.spawn)
            self.spawnbttn.grid(row=1,column=1)

            self.exitbttn = Button(self, text='Exit Program',
                                   font = font,
                                  command=self.quitter)
            self.exitbttn.grid(row=2,column=1)

            self.savebttn = Button(self, text='Save Score',
                                   font = font,
                                   command=self.save_score)
            self.savebttn.grid(row=3,column=1)

            self.high_scores = Button(self, text='See high scores',
                                      font = font,
                                      command=self.show_high_scores)
            self.high_scores.grid(row=4, column=1)
            
        def create_sub_widgets(self):
            '''Will create the widgets to be used in the window for high scores'''
            font = ("Times", "24", "bold")

            score_lbl = Label(self, font=font)
            score_lbl.pack()


        def show_high_scores(self):
            '''Will display the high scores'''
            HighScores.start()
                
            
        def spawn(self):
            '''Will make a variable that will be used to spawn a new ship'''
            global respawn
            global Exit
            global save
            save = 'No'
            Exit = 'No'
            respawn = 'Yes'
            root.destroy()
            root.quit()
                               
        def quitter(self):
            '''Will exit the entire program when the button clicks items'''
            global Exit
            global respawn
            global save
            save = 'No'
            respawn = 'No'
            Exit = 'Yes'
            root.destroy()
            root.quit()

        def save_score(self):
            '''Will save the name and score of the player'''
            global Exit
            global respawn
            global save
            respawn = 'No'
            Exit = 'No'
            save = 'Yes'
            root.destroy()
            root.quit()


    root = Tk()
    root.geometry('220x250')
    root.title('Respawn')

    app = Application(root, True)
                       
    root.mainloop()


def get_exit():
    '''Will return the exit variable'''
    global Exit
    return Exit

def get_respawn():
    '''Will get the respawn variable'''
    global respawn
    return respawn

def get_save():
    '''Will return the save variable'''
    global save
    return save
    
    


