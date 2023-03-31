## 1.맵 크기 정하기       2.지뢰 개수 정하기 이후 지뢰 설치       3.지뢰 주변으로 번호? 매기기      4.좌클릭 확인 우클릭 지뢰 핑 만약에 모든 지뢰에 지뢰핑을 하고 지뢰를 제외한 모든 블럭을 확인했다면 클리어
from PIL import ImageTk, Image, ImageFilter
from io import BytesIO
import tkinter as tk
import requests
import random

bool=1


size = int(input("크기:"))
board = [[0 for j in range(size)] for i in range(size)]

m_size = int(input("지뢰 개수:"))

while m_size > 0:
    j = random.randint(0,size-1)
    i = random.randint(0,size-1)
    if board[i][j] != 2:
        board[i][j] = 2
        m_size -= 1
    



window = tk.Tk()
canvas = tk.Canvas(window, width =size*30,height=size*30)
canvas.pack()

## 만약 "htts://github.com/harrydens/python-mine/blob/main/image/f_blcok.png"이 코드에서 이미지를 로드하는 URL이라면, 이 URL은 정확한 경로가 아닙니다. GitHub에서 이미지 파일에 직접 링크를 만드는 대신, GitHub는 링크를 로드하면 GitHub 페이지를 반환하고 페이지에 이미지가 포함된 태그가 있는 경우 이미지를 반환합니다.따라서 코드에서 이미지를 로드하려면, 해당 이미지를 호스팅하는 Raw URL을 사용해야 합니다. 이 경우, URL은 "https://raw.githubusercontent.com/harrydens/python-mine/main/image/f_blcok.png"와 같아야 합니다.  ##기억하자!!



def check_around(y,x): ## a<0 a>=size block
    global board
    count = 0
    if board[y][x] != 2 or board[y][x] != 3:
        return 0
    for i in range(9):
        if((board[y-1+i//3][x-1+i%3] == 2 or board[y+i//3][x+i%3] == 3 ) and not(y-1<0 or y+1 >= size or x-1<0 or x+1 >= size)):
            count += 1
    if count >0:
        board[y][x] = 3+count
    




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

def w_c(event):
    replace_b(event.x//30,event.y//30)

def replace_b(x,y):
    if(board[y][x] == 0):
        board[y][x] = 1
    if(board[y][x] == 2):
        board[y][x] = 3 ## 2,2 18,18 , 한변의 길이:16 ,폭이 5
    window.quit()


def check_board_img(y,x): ## 블럭 = 0 , 꽉찬 블럭=1 숨폭= 2 폭=3 숨1=4,숨2=5,숨3=6,숨4=7,숨5=8,숨6=9,숨7=10,숨8=11,블1=12,블2=13,블3=14,블4=15,블5=16,블6=17,블7=18,블8=19
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


def rep(): ## 1
    try:
        canvas.delete(tk.ALL)
        for i in range(0,size):
            for j in range(0,size):
                button = canvas.create_image(30*j,30*i,anchor=tk.NW ,image=check_board_img(i,j))
                canvas.tag_bind(button, "<Button-1>", w_c)
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
        check_around(board[i][j])



for i in range(size):
    for j in range(size):
        print(board[i][j],end="")
    
    print("")


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