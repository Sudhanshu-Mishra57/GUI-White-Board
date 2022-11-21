#step-1:-> Import required modules
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from turtle import color
from matplotlib.ft2font import BOLD

from scipy.__config__ import show


root = Tk()
root.title("White board")
root.geometry("1050x570+130+50")
root.resizable(False,False)

current_x = 0
current_y = 0
color = "black"

def locate_xy(work):
    global current_y,current_x 
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_y,current_x 
    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color)
    current_x = work.x
    current_y =work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete("all")
    color_palete()


#load images
logo = PhotoImage(file="logo.png")
root.iconphoto(False,logo)

color_panel = PhotoImage(file="color_panel.png")
Label(root,image=color_panel,bg="#f2f3f5").place(x=10,y=20)

eraser = PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#737373",command=new_canvas).place(x=30,y=400)

colors = Canvas(root,bg="#d9d9d9",width=37,height=300,border=10,bd=0)
colors.place(x=30,y=60)

#Board
canvas = Canvas(root,bg="#d9d9d9",width=930,height=500,cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind("<Button-1>",locate_xy)
canvas.bind("<B1-Motion>",addLine)

#fill color in color panel
def color_palete():
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>', lambda x:show_color("black"))

    id = colors.create_rectangle((10,40,30,60),fill="grey")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('grey'))

    id = colors.create_rectangle((10,70,30,90),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('red'))

    id = colors.create_rectangle((10,100,30,120),fill="orange")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('orange'))

    id = colors.create_rectangle((10,130,30,150),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('yellow'))

    id = colors.create_rectangle((10,160,30,180),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('green'))

    id = colors.create_rectangle((10,190,30,210),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('blue'))

    id = colors.create_rectangle((10,220,30,240),fill="purple")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('purple'))

    id = colors.create_rectangle((10,250,30,270),fill="brown4")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('brown4'))

    id = colors.create_rectangle((10,280,30,300),fill="sky blue")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('sky blue'))

color_palete()


#add slider
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root,from_=0,to=100,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=30,y=520)


value_label = ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=545)

root.mainloop()

