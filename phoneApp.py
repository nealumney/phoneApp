from tkinter import *

class Phone:

    def __init__(self, gui, keys):
        self.gui = gui
        self.keys = {}
        self.buttons = {}
        self.keyTops=(("1","   ", 3, 0),
             ("2","ABC", 3, 1),
             ("3","DEF", 3 , 2),
                ("4", "GHI", 4, 0),
                ("5", "JKL", 4, 1),
                ("6", "MNO", 4, 2),
                ("7", "PQRS", 5, 0),
                ("8", "TUV", 5, 1),
                ("9", "WXYZ", 5, 2),
                ("0", " ", 6, 1))
        self.background = PhotoImage(file="background.png")
        for k in self.keyTops:
            value, letters, row, column = k
            # print(k)
            self.addKey(value, letters, row, column)

    def addKey(self, value, letters, row, column):
        # letters is a list
        # value is the main display value
        self.keys[value] = letters
        self.buttons[value] = Button(self.gui, relief=RAISED, text = value+"\n"+letters,
                                     height=40, width=40, image=self.background,
                                     compound=CENTER,
                                     command=lambda: self.display(value))
        self.buttons[value].grid(row=row,column=column)

    def display(self, value):
        content=self.buttons[value].cget()
        print(content)
        
        






if __name__ == "__main__":
    gui = Tk()                                 
    phone = Phone(gui, 10)
    gui.mainloop()
                                     
                                     
