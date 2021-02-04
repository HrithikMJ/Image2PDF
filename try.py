"""""
code by Dharun C & Hrithik Joseph
title: Image to PDF converter using PYTHON IMAGING LIBRARY
"""""
from PIL import Image #for pdf conversion
import sys#used in exit function
import tkinter as tk#GUI
from tkinter import filedialog#GUI
from tkinter import messagebox#GUI

def process_images(max_range,out_fname):#the pdf conversion function
    prefix=str(filedialog.askopenfilename())
    images = []
    for i in range(0, max_range + 1):
        fname = prefix 
        im = Image.open(fname)
        if im.mode == "RGBA":#pdf cant read RGBA files
            im = im.convert("RGB")
        images.append(im)

    images[0].save(out_fname, save_all = True, quality=100, append_images = images[1:])
    
def createNewWindow():#to create new window
    newWindow = tk.Toplevel(top)
    newWindow.geometry("200x150")
    labelExample = tk.Label(newWindow, text = "select image",bd=5)
    labelExample.place(x=60,y=0)
    buttonExample = tk.Button(newWindow, text = "Start",command=process_images(12,"test.pdf"),bd=5)
    buttonExample.place(x=70,y=100)

def Exit():#exit function
    msgBox = messagebox.askquestion(
        'Exit Application', 'Are you sure wanted to exit', icon='warning')
    if msgBox == 'yes':
        sys.exit()
#main_function          
top = tk.Tk()
top.geometry("300x200")#screen_size
s= tk.Label(top, text="Image to pdf Converter",bd=5).place(x=70,y=0)#Label
a = tk.Button( top, text="img to pdf",command=createNewWindow,bd=5).place(x=100, y=40)#button1
w = tk.Button( top, text="exit",command=Exit,bd=5).place(x=120, y=100)#button2
top.mainloop()
