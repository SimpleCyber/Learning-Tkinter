from tkinter import *
from PIL import ImageTk, Image
import os 


def rotate_img():
    global counter
    img_label.config(image=img_array[counter% len(img_array)])
    counter +=1


counter =1
root =Tk()

root.title('Wallpaper Viewer')
root.configure(background='black')

files = os.listdir('Wall paper')

img_array = []
for file in files:
    img = Image.open(os.path.join('Wall paper', file))
    resized_img = img.resize((300,200))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(15,10),padx=(5,5))



next_button =Button(root , text='Next', bg='red',fg='white', width=15, height=2 , command=rotate_img)
next_button.pack()

root.mainloop()