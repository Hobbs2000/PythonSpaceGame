#Calvin Field
#5/22/15
#High Scores
#Will show the high scores for the game
from Tkinter import *
import tkFont
import cPickle
from operator import itemgetter


def start():
    '''Will start the program'''
    class Application(Frame):
        '''Is the gui application that will display the high scores'''
        def __init__(self, master):
            '''Will intialize the fram'''
            Frame.__init__(self, master)
            self.grid()
            self.create_widgets()

        def create_widgets(self):
            '''Createst the widgets for the program'''
            font = ("Times", "24", "bold")

            text = ''
            scores_file = open('Pickles.dat', 'r')
            all_items = cPickle.load(scores_file)
            print all_items
            scores_file.close()
            first_name = all_items[0]
            first_score = all_items[1]
            entry=[first_name,first_score]
            all_items.append(entry)
##            text += first_name+':  '+str(first_score)+'\n'
            all_items.remove(first_name)
            all_items.remove(first_score)
            print all_items
            all_items.sort(key=itemgetter(1))
            all_items.reverse()
            print all_items
            for item in all_items:
                name, score = item
                text += name+':  '+str(score)+'\n'
        
            score_lbl = Label(self, text = text,
                              font=font)
            score_lbl.pack()

        
    root = Tk()
    root.title('High Scores')
    root.geometry('400x400')

    app = Application(root)

    root.mainloop()
    
            
    


