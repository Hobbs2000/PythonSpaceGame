#Calvin Field
#5/18/15
#Name sys
#Will store the names of player along with their score in a text file
import cPickle
from Tkinter import *
import tkFont

Score = None
name = None
def store(score):
    '''Will create a window that will prompt the user to enter his/her name'''
    global Score
    Score = score
    class Application(Frame):
        '''Is a GUI application that will make and control all the widgets'''
        def __init__(self, master):
            '''Creates the frame'''
            Frame.__init__(self, master)
            self.grid()
            self.create_widget()
            
        def create_widget(self):
            '''Will create all the widgets'''
            font = ("Times", "24", "bold")

            self.nameEntry = Entry(self, font = font,
                              bg='grey')
            self.nameEntry.grid(row=0,column=0)

            self.lbl = Label(self, font = font,
                        text = 'Score:')
            self.lbl.grid(row=1, column=0, sticky = W)
            
            self.scorelbl = Label(self, font =font,
                             text=Score)
            self.scorelbl.grid(row=1, column=0)

            self.submit = Button(self, font = font,
                            text = 'Save',
                            bg = 'grey',
                            command = self.save)
            self.submit.grid(row=2)

        def save(self):
            '''Will take the name entered in the entry and save it as a global variable'''
            global name
            name = self.nameEntry.get()
            root.quit()

    root = Tk()
    root.geometry('220x130')
    root.title('Respawn')

    app = Application(root)
                       
    root.mainloop()

#Will make/open a text file to save the list of the name and score of the player
    addName = []
    addName.append(name)
    addName.append(score)
    print addName
    try:
        nameList_file = open('Pickles.dat', 'r')
        all_items = cPickle.load(nameList_file)
        print all_items
        nameList_file.close()
        
        nameList_file = open('Pickles.dat', 'w')
        all_items.append(addName)
        cPickle.dump(all_items, nameList_file)
        nameList_file.close()
    except:
        nameList_file = open('Pickles.dat','w')
        cPickle.dump(addName, nameList_file)
        nameList_file.close()

        
    root.destroy()
    


