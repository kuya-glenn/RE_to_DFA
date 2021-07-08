import tkinter as tk
from tkinter import ttk
from tkinter import *
from typing import ByteString
import RE_2_DFA
from pdf2image import convert_from_path
from PIL import Image, ImageTk
import tkinter
import pdf
##from PDFViewer import image_view
import tkinter.font as font
import os
import time 
root = tk.Tk()




bg = '#263D42'
root.title("RE to DFA")
root.configure(background=bg)
root.geometry("800x600")


##Functions for Button_Clicks
        
def click():
    RE_2_DFA.first_dfa(input1.get())
    os.system("TASKKILL /F /IM msedge.exe")
    pdf.convert()
    image1 = Image.open("C:/THESIS/page0.jpg")
    image1 = image1.resize((800, 300), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label4 = tkinter.Label(tab1,image=test)
    label4.image = test
    label4.place( x=0, y=0)
    Font_tuple = ("Montserrat", 7, "normal")
    label11=tk.Label(tab1,text=RE_2_DFA.dfa0.input_check(input1.get()))
    label11.configure(font = Font_tuple)
    label11.grid(row=150, column=300)
    label11.place(x=20, y=310)
    time.sleep(3)
    label11.destroy()




   

def click2():
    RE_2_DFA.second_dfa(input2.get())
    os.system("TASKKILL /F /IM msedge.exe")
    pdf.convert()
    image1 = Image.open("C:/THESIS/page0.jpg")
    image1 = image1.resize((800, 300), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label4 = tkinter.Label(tab2,image=test)
    label4.image = test
    label4.place( x=0, y=0)
    Font_tuple = ("Montserrat", 7, "normal")
    label11=tk.Label(tab2,text=RE_2_DFA.dfa1.input_check(input2.get()))
    label11.configure(font = Font_tuple)
    label11.grid(row=150, column=300)
    label11.place(x=20, y=310)
    


tabControl =ttk.Notebook(root) 
#parent widget for tabs class, cursor,padding,relief,style,takefocus,height,width
##Tab Declaration
tab1= ttk.Frame(tabControl)
tabControl.add (tab1,text='Regex 1')

tab2= ttk.Frame(tabControl)
tabControl.add (tab2,text='Regex 2')

tabControl.pack (expand=1,fill='both')

image1 = Image.open("C:/THESIS/Number1.jpg")
image1 = image1.resize((800, 300), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label4 = tkinter.Label(tab1,image=test)
label4.image = test
label4.place( x=0, y=0)

image1 = Image.open("C:/THESIS/Number2.jpg")
image1 = image1.resize((800, 300), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label4 = tkinter.Label(tab2,image=test)
label4.image = test
label4.place( x=0, y=0)



#Tab1
Font_tuple = ("Roboto", 12, "normal")
label1=tk.Label(tab1,text="Problem: ( a + b ) ( a + b )* ( aa + bb ) ( ab + ba ) ( a + b )* ( aba + baa )")
label1.configure(font = Font_tuple)
label1.grid(row=150, column=300)
label1.place(x=20, y=550)

input1=tk.Entry(tab1)
input1.grid(row=150, column=600)
input1.place(x=500, y=450)
My_Font = font.Font(size=12)
button1=tk.Button(tab1, text="Simulate", command = click, width = 10, height = 4
            , bg='#4E54B0',fg='#E4E6FF', font = 'Sans-serif')
button1['font'] = My_Font
button1.grid(row=800, column=400)
button1.place(x=650, y=415)

#Tab2

label2=tk.Label(tab2,text="Problem: ( 11 + 00 ) ( 1 + 0 )* ( 101 + 111 + 01 ) ( 00* + 11* ) ( 1 + 0 + 11 )")
label2.configure(font = Font_tuple)
label2.grid(row=150, column=300)
label2.place(x=20, y=550)

input2=tk.Entry(tab2)
input2.grid(row=200, column=300)
input2.place(x=500, y=450)
button2=tk.Button(tab2, text="Simulate", command = click2, width = 10, height = 4
            , bg='#4E54B0',fg='#E4E6FF', font = 'Sans-serif')
button2.grid(row=200, column=500)
button2.place(x=650, y=415)



root.mainloop()