from tkinter import *
import time

class draw:
    def __init__(self,x,y,w,h):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__id = canvas.create_rectangle(self.__x,self.__y,self.__x+self.__w,self.__y+self.__h,fill="white")
        
    def setdraw(self,x,y,w,h):
        canvas.delete(self.__id)
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h    
        self.__id = canvas.create_rectangle(self.__x,self.__y,self.__x+self.__w,self.__y+self.__h,fill="white")
    
    def getdraw(self):
        return (self.__x,self.__y,self.__w,self.__h)
    
    def getid(self):
        return self.__id
    
game = Tk()
game.title("게임")
width=1000
heigh=900
canvas = Canvas(game,width=width,heigh=heigh,bg="black")
canvas.pack()
move_set = set()

mx,my=0,0
test = draw(500,500,100,100)

def move(event):
    move_set.add(event.keysym)
    
def move_del(event):
    move_set.remove(event.keysym)

def drawing(event):
    test.setdraw(0,0,100,100)
    
def mouseclick(event):
    mx,my=event.x,event.y
    if event.x > canvas.coords(test.getid())[0] and event.y > canvas.coords(test.getid())[1] and event.x < canvas.coords(test.getid())[2] and event.y < canvas.coords(test.getid())[3]:
        test.setdraw(0,0,100,100)
    
canvas.bind_all("<KeyPress>", move)
canvas.bind_all("<KeyRelease>", move_del)
canvas.bind("<Button-1>",mouseclick)

while(1):
    for i in move_set:
        if i == "Up" and canvas.coords(test.getid())[1]>0:
            canvas.move(test.getid(),0,-5)
        if i == "Down" and canvas.coords(test.getid())[3]<heigh:
            canvas.move(test.getid(),0,5)
        if i == "Left" and canvas.coords(test.getid())[0]>0:
            canvas.move(test.getid(),-5,0)
        if i == "Right" and canvas.coords(test.getid())[2]<width:
            canvas.move(test.getid(),5,0)
    
    game.update()
    time.sleep(0.01)
