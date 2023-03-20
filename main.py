from PIL import ImageTk, Image, ImageFilter
import tkinter as tk

size = int(input("크기:"))
board = [[0 for i in range(size)] for i in range(size)]

window = tk.Tk()
canvas = tk.Canvas(window, width =size*20,height=size*20)
canvas.pack()

test = "f_block.png"
i_photo = Image.open(test)
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
            canvas.tag_bind(button, "", lambda event: test(i,j))

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