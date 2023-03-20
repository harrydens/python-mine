
from PIL import ImageTk, Image, ImageFilter
from io import BytesIO
import tkinter as tk
import requests


size = int(input("크기:"))
board = [[0 for i in range(size)] for i in range(size)]

window = tk.Tk()
canvas = tk.Canvas(window, width =size*20,height=size*20)
canvas.pack()

url = "https://raw.githubusercontent.com/harrydens/python-mine/main/image/f_blcok.png" ## 만약 "https://github.com/harrydens/python-mine/blob/main/image/f_blcok.png"이 코드에서 이미지를 로드하는 URL이라면, 이 URL은 정확한 경로가 아닙니다. GitHub에서 이미지 파일에 직접 링크를 만드는 대신, GitHub는 링크를 로드하면 GitHub 페이지를 반환하고 페이지에 이미지가 포함된 태그가 있는 경우 이미지를 반환합니다.따라서 코드에서 이미지를 로드하려면, 해당 이미지를 호스팅하는 Raw URL을 사용해야 합니다. 이 경우, URL은 "https://raw.githubusercontent.com/harrydens/python-mine/main/image/f_blcok.png"와 같아야 합니다.  ##기억하자!!
respond = requests.get(url)
i_photo = Image.open(BytesIO(respond.content))
re_photo = i_photo.resize((20,20))
photo = ImageTk.PhotoImage(re_photo)

for i in range(0,size):
    for j in range(0,size):
        board[i][j] = photo

def test(i,j):
    print(i,j)

def replace_b(x,y,t):
    global i_photo,re_photo,photo,board
    i_photo = Image.open(t)
    re_photo = i_photo.resize((20,20))
    photo = ImageTk.PhotoImage(re_photo)
    board[x][y] = photo

def rep():
    canvas.delete(tk.ALL)
    for i in range(0,size):
        for j in range(0,size):
            button = canvas.create_image(20*j,20*i,anchor=tk.NW ,image=board[i][j])
            canvas.tag_bind(button, "", lambda event: print("a"))

def p_o(x,y,size_x,size_y,img):
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
        img_tk = ImageTk.PhotoImage(filtered_img)        
while True:
    rep()
    canvas.pack()
    tx,ty= int(input("x:")),int(input("y:"))
    if tx == 20 or ty == 20:
        break
    replace_b(tx,ty,"block.png")

canvas.pack()
window.mainloop()
##label = tk.Image()

'''
window.mainloop()

img = Image.open("roma_2.png")
p_o(250,100,25,25,img)
img = Image.open("flag.png")
p_o(250,50,25,25,img)'''