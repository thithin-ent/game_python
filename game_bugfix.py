from tkinter import *
import time
import random

class draw:
    def __init__(self,x,y,w,h,color = "white"):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__id = canvas.create_rectangle(self.__x,self.__y,self.__x+self.__w,self.__y+self.__h,fill=color)
        
    def setdraw(self,x,y,w,h,color = "white"):
        self.destroy
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h    
        self.__id = canvas.create_rectangle(self.__x,self.__y,self.__x+self.__w,self.__y+self.__h,fill=color)
    
    def getdraw(self):
        return (self.__x,self.__y,self.__w,self.__h)
    
    def getid(self):
        return self.__id
    
    def destroy(self):
        canvas.delete(self.__id)
    
    
def destory():
    for i in range(0,len(obj)):
         obj[i].destroy()
    del obj[:]


def setting_class(n_by_n,color):
    global land_set
    land_set = random.randrange(0,n_by_n**2)
    side_length=(800-10*(n_by_n-1))/n_by_n
    for i in range(0,n_by_n**2):
        if i != land_set:
            obj.append(draw(100+(side_length+10)*(i//n_by_n),100+(side_length+10)*(i%n_by_n),side_length,side_length,color[0]))
        else:
            obj.append(draw(100+(side_length+10)*(i//n_by_n),100+(side_length+10)*(i%n_by_n),side_length,side_length,color[1]))
    
def mouseclick_left(event):
    global count,score,score_text,wrong
    for i in range(len(obj)):
        if event.x > canvas.coords(obj[i].getid())[0] and event.y > canvas.coords(obj[i].getid())[1] and event.x < canvas.coords(obj[i].getid())[2] and event.y < canvas.coords(obj[i].getid())[3]:
            if i == land_set:
                count = 5
                score += 1
                destory()
                color=set_color(score)
                setting_class(score//10+2,color)
                break
            else:
                wrong = 1
                break

def mouseclick_right(event):
    global count,score,wrong
    if count<=0 or score>=40 or wrong == 1:
        canvas.delete(end_text)
        score = 0
        count = 5
        wrong = 0
        color=set_color(score)
        setting_class(score//10+2,color)
        
def press_key(event):
    key_set.add(event.keysym)
    
def Release_key(event):
    key_set.remove(event.keysym)
                  
def set_color(score):
    plus_minus=(-1)**random.randrange(1)
    if score<=30:
        offset=plus_minus*(190-5*score)
    else:
        offset=plus_minus*(70-score)
    main_r=random.randrange(0,256)
    main_g=random.randrange(0,256)
    main_b=random.randrange(0,256)
    main_rgb=[main_r,main_g,main_b]
    point_rgb=[main_r,main_g,main_b]
    main_color='#%02x%02x%02x'%(main_r,main_g,main_b)
    change_parameter=random.randrange(0,3)
    who_is_changed=random.sample(range(0,3),change_parameter+1)
    for i in who_is_changed:
        point_rgb[i]=main_rgb[i]+offset
        if point_rgb[i]>255:
            point_rgb[i]=point_rgb[i]-255
        elif point_rgb[i]<0:
            point_rgb[i]=point_rgb[i]+255
    point_color='#%02x%02x%02x'%(point_rgb[0],point_rgb[1],point_rgb[2]) 
    return [main_color,point_color]
    

#Game Window
game = Tk()
game.title("PALLET")
width=1000
heigh=1000
canvas = Canvas(game,width=width,heigh=heigh,bg="black")
canvas.pack()
canvas.bind("<Button-1>",mouseclick_left)
canvas.bind("<Button-3>",mouseclick_right)
canvas.bind_all("<KeyPress>",press_key)
canvas.bind_all("<KeyRelease>",Release_key)
obj = []
key_set = set()

canvas.create_text(500, 350, text ="색감 테스트 게임입니다\n다른 색깔 하나를 찾아 클릭하세요 ", fill = "white", font = ("맑은 고딕", 30))
canvas.create_text(500, 700, text ="시작하려면 아무키나 누르세요", fill = "red", font = ("맑은 고딕", 30))
while(True):    
    if key_set :
        canvas.delete("all") 
        break
    game.update() 
    time.sleep(0.01)

land_set = 0
score = 0
count = 5
wrong = 0
draw(5,5,55,55)
color=set_color(score)
count_text = canvas.create_text(30,30,text = int(count),fill="black",font=("맑은 고딕",30))
score_text = canvas.create_text(870,50,text = 'SCORE : %d'%score,fill="white",font=("맑은 고딕",30))
end_text = 0
setting_class(score//10+2,color)

while(True):
    canvas.delete(score_text)
    if count<=0:
        destory()
        canvas.delete(end_text)
        end_text = canvas.create_text(500,500,text = '제한시간이 경과하였습니다.\n당신의 점수는 %d점 입니다.\n\n다시하려면 마우스 오른쪽을 클릭해 주세요.\n아무키나 누르면 종료됩니다.'%score,fill="white",font=("맑은 고딕",30))
        if key_set :
            break
    elif score>=40:
        destory()
        canvas.delete(end_text)
        end_text = canvas.create_text(500,500,text = "흠 잡을 것도 없습니다!\n당신은 완벽히 모든 색상을 구분하셨습니다.\n\n다시하려면 마우스 오른쪽을 클릭해 주세요.\n아무키나 누르면 종료됩니다.",fill="white",font=("맑은 고딕",30))
        if key_set :
            break
    elif wrong == 1:
        destory()
        canvas.delete(end_text)
        end_text = canvas.create_text(500,500,text = "당신의 점수는 %d점입니다.\n\n다시하려면 마우스 오른쪽을 클릭해 주세요.\n아무키나 누르면 종료됩니다."%score,fill="white",font=("맑은 고딕",30))
        if key_set :
            break
    else:
        count = count -0.01
        canvas.delete(count_text)
        count_text = canvas.create_text(30,30,text = int(count),fill="black",font=("맑은 고딕",30))
        score_text = canvas.create_text(870,50,text = 'SCORE : %d'%score,fill="white",font=("맑은 고딕",30))
    game.update()
    time.sleep(0.01)
    
    