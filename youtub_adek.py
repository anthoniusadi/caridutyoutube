
#!! requierment modul
from tkinter import *
import webbrowser
import PIL
from PIL import Image
import os

#? URL youtube
url1 = 'https://www.youtube.com/results?search_query=baby+bus'
url2 = 'https://www.youtube.com/results?search_query=TAYO'
url3 = 'https://www.youtube.com/results?search_query=cocomelon'
url4 = 'https://www.youtube.com/results?search_query=dave+and+ava+nursery+rhymes'
url5 = 'https://www.youtube.com/results?search_query=sunny+bunny'

root = Tk()
root.title("YOUTUBE ADEK")
root.geometry("900x780")
root.configure(bg='pink')
frame = Frame(root)
frame.pack()

##! path_foto
foto_babybus=PhotoImage(file="/root/adek/bus.png")
foto_tayo=PhotoImage(file="/root/adek/tayo.png")
foto_cocomelon = PhotoImage(file="/root/adek/cocomelon.png")
foto_dave = PhotoImage(file='/root/adek/dave.png')
foto_suny = PhotoImage(file='/root/adek/sunny.png')
##!fungsi 
def babybus():
    webbrowser.open_new(url1)
def tayo():
    webbrowser.open_new(url2)
def cocomelon():
    webbrowser.open_new(url3)
def dave():
    webbrowser.open_new(url4)
def suny():
    webbrowser.open_new(url5)

button1 = Button(frame, text="Baby Bus", command=babybus,image=foto_babybus,compound=LEFT,bg='pink')
button2 = Button(frame, text="Hei Tayo", command=tayo,image=foto_tayo,compound=LEFT,bg='pink')
button3 = Button(frame, text="coco melon", command=cocomelon,image=foto_cocomelon,compound=LEFT,bg='pink')
button4 = Button(frame, text="dave n ava", command=dave,image=foto_dave,compound=LEFT,bg='pink')
button5 = Button(frame, text="sunny", command=suny,image=foto_suny,compound=LEFT,bg='pink')


button4.pack()
button3.pack()
button2.pack()
button5.pack()
button1.pack()
root.mainloop()