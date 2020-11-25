from tkinter import *

class draw:
    def __init__(self,x,y,w,h):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__id = canvas.create_rectangle(self.__x,self.__y,self.__x+self.__w,self.__y+self.__h)
        
    def setdraw(self,x,y,w,h):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h    
        self.__id = canvas.create_rectangle(self.__x,self.__y,self.__x+self.__w,self.__y+self.__h)
    
    def getdraw(self):
        return (self.__x,self.__y,self.__w,self.__h)
    
    def getid(self):
        return self.__id
        
game = Tk()
game.title("게임")
canvas = Canvas(game,width=1000,heigh=1000)
canvas.pack()

test = draw(500,500,100,100)




def move(event):
    if event.keysym == "Up":
        canvas.move(test.getid(), 0, -3)
    elif event.keysym == "Down":
        canvas.move(test.getid(), 0, 3)
    elif event.keysym == "Left":
        canvas.move(test.getid(), -3, 0)
    else:
        canvas.move(test.getid(), 3, 0)

def drawing(event):
    test.setdraw(0,0,100,100)


canvas.bind_all("<KeyPress-Up>"   , move)
canvas.bind_all("<KeyPress-Down>" , move)
canvas.bind_all("<KeyPress-Left>" , move)
canvas.bind_all("<KeyPress-Right>", move)

canvas.bind("<B1-Motion>", drawing)

mainloop()
