from tkinter import *

class draw:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def getdraw(self):
        return (self.x,self.y,self.w,self.h)
        
game = Tk()
game.title("게임")
canvas = Canvas(game,width=1000,heigh=1000)
canvas.pack()

a = draw(500,500,100,100)

canvas.create_rectangle(a.getdraw())

mainloop()