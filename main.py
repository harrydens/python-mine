## 1.맵 크기 정하기       2.지뢰 개수 정하기 이후 지뢰 설치       3.지뢰 주변으로 번호? 매기기      4.좌클릭 확인 우클릭 지뢰 핑 만약에 모든 지뢰에 지뢰핑을 하고 지뢰를 제외한 모든 블럭을 확인했다면 클리어
from PIL import ImageTk, Image, ImageFilter
from io import BytesIO
import tkinter as tk
import requests
import random

bool=1
bool_1=1
click=0

size = int(input("크기:"))
board = [[0 for j in range(size)] for i in range(size)]

m_size = int(input("지뢰 개수:"))

keep = m_size

while m_size > 0:
    j = random.randint(0,size-1)
    i = random.randint(0,size-1)
    if board[i][j] != 2:
        board[i][j] = 2
        m_size -= 1
m_size = keep



window = tk.Tk()
canvas = tk.Canvas(window, width =size*30,height=size*30)
canvas.pack()

## 만약 "htts://github.com/harrydens/python-mine/blob/main/image/f_blcok.png"이 코드에서 이미지를 로드하는 URL이라면, 이 URL은 정확한 경로가 아닙니다. GitHub에서 이미지 파일에 직접 링크를 만드는 대신, GitHub는 링크를 로드하면 GitHub 페이지를 반환하고 페이지에 이미지가 포함된 태그가 있는 경우 이미지를 반환합니다.따라서 코드에서 이미지를 로드하려면, 해당 이미지를 호스팅하는 Raw URL을 사용해야 합니다. 이 경우, URL은 "https://raw.githubusercontent.com/harrydens/python-mine/main/image/f_blcok.png"와 같아야 합니다.  ##기억하자!!



def check_around(y,x): ## a<0 a>=size block
    global board,size
    count = 0
    if board[y][x] == 2 or board[y][x] == 3:

        return 0
    
    for i in range(9):

        if ((y-1+(i //3) >= 0 and y-1+(i//3) < size) and (x-1+(i%3) >= 0 and x-1+(i%3) < size)):

            if(board[y-1+(i//3)][x-1+(i%3)] == 2 or board[y-1+(i//3)][x-1+(i%3)] == 3):

                count += 1

    if count >0:
        board[y][x] = 3+count



def search(y,x): ## a<0 a>=size block
    global board,size
    count = 0
    
    for i in range(9):

        if ((y-1+(i //3) >= 0 and y-1+(i//3) < size) and (x-1+(i%3) >= 0 and x-1+(i%3) < size)):

            if(board[y-1+(i//3)][x-1+(i%3)] == 0  or board[y-1+(i//3)][x-1+(i%3)] == 4 or board[y-1+(i//3)][x-1+(i%3)] == 5 or board[y-1+(i//3)][x-1+(i%3)] == 6 or board[y-1+(i//3)][x-1+(i%3)] == 7 or board[y-1+(i//3)][x-1+(i%3)] == 8 or board[y-1+(i//3)][x-1+(i%3)] == 9 or board[y-1+(i//3)][x-1+(i%3)] == 10 or board[y-1+(i//3)][x-1+(i%3)] == 11): ##
                replace_a((x-1+(i%3)),(y-1+(i//3)))
    



def print_url_pic(url):
    respond = requests.get(url)
    i_photo = Image.open(BytesIO(respond.content))
    re_photo = i_photo.resize((30,30))
    photo = ImageTk.PhotoImage(re_photo)
    return photo


b_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/blcok.png")
fb_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/f_blcok.png")
bomb_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/bomb.png")
r1_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_1.png")
r2_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_2.png")
r3_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_3.png")
r4_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_4.png")
r5_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_5.png")
r6_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_6.png")
r7_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_7.png")
r8_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/n_8.png")
fl_p = print_url_pic("https://raw.githubusercontent.com/harrydens/python-mine/main/image/b_flags.png")

def w_c(event):
    replace_b(event.x//30,event.y//30)

def w_c2(event):
    flag_on(event.x//30,event.y//30)



def flag_on(x,y):
    print("work")
    if(board[y][x] == 0):
        board[y][x] = 20
    elif(board[y][x] == 20):
        board[y][x] = 0
    if(board[y][x] == 2):
        board[y][x] = 21 ## 2,2 18,18 , 한변의 길이:16 ,폭이 5
    elif(board[y][x] == 21):
        board[y][x] = 2 ## 2,2 18,18 , 한변의 길이:16 ,폭이 5
    if(board[y][x] == 4):
        board[y][x] = 22
    elif(board[y][x] == 22):
        board[y][x] = 4
    if(board[y][x] == 5):
        board[y][x] = 23
    elif(board[y][x] == 23):
        board[y][x] = 5
    if(board[y][x] == 6):
        board[y][x] = 24
    elif(board[y][x] == 24):
        board[y][x] = 6
    if(board[y][x] == 7):
        board[y][x] = 25
    elif(board[y][x] == 25):
        board[y][x] = 7    
    
    if(board[y][x] == 8):
        board[y][x] = 26
    elif(board[y][x] == 26):
        board[y][x] = 8
    if(board[y][x] == 9):
        board[y][x] = 27
    elif(board[y][x] == 27):
        board[y][x] = 9
    if(board[y][x] == 10):
        board[y][x] = 28
    elif(board[y][x] == 28):
        board[y][x] = 10
    if(board[y][x] == 11):
        board[y][x] = 29
    elif(board[y][x] == 29):
        board[y][x] = 11
        
    
    
    
    
    
    
    
    
    
    

    
    window.quit()

def replace_a(x,y):
    global bool_1
    if(board[y][x] == 0):
        board[y][x] = 1
        search(y,x)
    if(board[y][x] == 2):
        board[y][x] = 3 ## 2,2 18,18 , 한변의 길이:16 ,폭이 5
        return 0
    if(board[y][x] == 4):
        board[y][x] = 12
        return 0
    if(board[y][x] == 5):
        board[y][x] = 13
        return 0
    if(board[y][x] == 6):
        board[y][x] = 14
        return 0
    if(board[y][x] == 7):
        board[y][x] = 15
        return 0
    if(board[y][x] == 8):
        board[y][x] = 16
        return 0
    if(board[y][x] == 9):
        board[y][x] = 17
        return 0
    if(board[y][x] == 10):
        board[y][x] = 18
        return 0
    if(board[y][x] == 11):
        board[y][x] = 19
        return 0

    
    window.quit()

def replace_b(x,y):
    print("work")
    global bool_1
    if(board[y][x] == 0):
        board[y][x] = 1
        search(y,x)
    if(board[y][x] == 2):
        board[y][x] = 3 ## 2,2 18,18 , 한변의 길이:16 ,폭이 5
    if(board[y][x] == 4):
        board[y][x] = 12
        
    if(board[y][x] == 5):
        board[y][x] = 13
    if(board[y][x] == 6):
        board[y][x] = 14
    if(board[y][x] == 7):
        board[y][x] = 15
    if(board[y][x] == 8):
        board[y][x] = 16
    if(board[y][x] == 9):
        board[y][x] = 17
    if(board[y][x] == 10):
        board[y][x] = 18
    if(board[y][x] == 11):
        board[y][x] = 19

    
    window.quit()


def check_board_img(y,x): ## 블럭 = 1 , 꽉찬 블럭=0 숨폭= 2 폭=3 숨1=4,숨2=5,숨3=6,숨4=7,숨5=8,숨6=9,숨7=10,숨8=11,블1=12,블2=13,블3=14,블4=15,블5=16,블6=17,블7=18,블8=19,블깃=20,폭깃=21,1깃=22,2깃=23,3깃=24,4깃=25,5깃=26,6깃=27,7깃=28,8깃=29
    if(board[y][x] == 0 or board[y][x] == 2 or board[y][x] == 4 or board[y][x] == 5 or board[y][x] == 6 or board[y][x] == 7 or board[y][x] == 8 or board[y][x] == 9 or board[y][x] == 10 or board[y][x] == 11):
        return fb_p
    
    if(board[y][x] == 1):
        return b_p
    
    if(board[y][x] == 3):
        return bomb_p
    
    if(board[y][x] == 12):
        return r1_p
    
    if(board[y][x] == 13):
        return r2_p
    
    if(board[y][x] == 14):
        return r3_p
    
    if(board[y][x] == 15):
        return r4_p
    
    if(board[y][x] == 16):
        return r5_p
    
    if(board[y][x] == 17):
        return r6_p
    
    if(board[y][x] == 18):
        return r7_p
    
    if(board[y][x] == 19):
        return r8_p

    if(board[y][x] == 20 or board[y][x] == 21 or board[y][x] == 22 or board[y][x] == 23 or board[y][x] == 24 or board[y][x] == 25 or board[y][x] == 26 or board[y][x] == 27 or board[y][x] == 28 or board[y][x] == 29):
        return fl_p

def scane():
    count=int(0)
    for i in range(size):
        for j in range(size):
            if board[i][j] in [0,4,5,6,7,8,9,10,11]:
                count += 1
    print("1 : ",count)
    print("1,2 : ",m_size)
    return count

def scane1():
    count=int(0)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 21:
                count += 1
    print("2 : ",count)
    return count

def scane2():
    count=int(0)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 3:
                count += 1
    print("3 : ",count)
    return count


def win():
    global bool

    if m_size == scane1() and 0 == scane():
        print("you win")
        bool=0
    
    if scane2():
        print("you lose")
        bool=0





def rep(): ## 1
    try:
        canvas.delete(tk.ALL)
        for i in range(0,size):
            for j in range(0,size):
                button = canvas.create_image(30*j,30*i,anchor=tk.NW ,image=check_board_img(i,j))
                canvas.tag_bind(button, "<Button-1>", w_c)
                canvas.tag_bind(button, "<Button-3>", w_c2)
        win()
    except:
        global bool
        bool=0
        

'''def p_o(x,y,size_x,size_y,img):
    resized_img = img.resize((size_x,size_y), Image.LANCZOS)

    if resized_img.mode != "RGB":
        resized_img = resized_img.convert("RGBA")

    filtered_img = resized_img.filter(ImageFilter.DETAIL)

    if img.mode != "RGBA":
        filtered_img = filtered_img.convert("RGBA")




    if img.mode == "RGBA":
        blank_image = Image.new("RGBA",filtered_img,(255,255,255,0))
        img_tk = ImageTk.PhotoImage(Image.alpha_composite(blank_image,filtered_img))
    else:
        img_tk = ImageTk.PhotoImage(filtered_img)'''

for i in range(size):
    for j in range(size):
        print(board[i][j],end="")
    
    print("")



for i in range(size):
    for j in range(size):
        check_around(i,j)




while bool:
    rep()
    try:
        canvas.pack()
        window.mainloop()
    except:
        break

##canvas.pack()
##window.mainloop()
##label = tk.Image()

'''
window.mainloop()

img = Image.open("roma_2.png")
p_o(250,100,25,25,img)
img = Image.open("flag.png")
p_o(250,50,25,25,img)'''