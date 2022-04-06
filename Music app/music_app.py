import os
from tkinter import *
from pygame import mixer
from tkinter import filedialog, messagebox, ttk
import time

def time1():
    current_time = mixer.music.get_pos()/1000
    convert_current_time=time.strftime("%M:%S",time.gmtime(current_time))
    status.config(text=convert_current_time)
    status.after(1000,time1)

def play():
    a = playlist.get(ACTIVE)
    e1.delete(0, END)
    e1.insert(0,str(a))
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    time1()
def open():
        file_name = filedialog.askdirectory()
        str = ""
        if file_name:
            os.chdir(file_name)
            songs=os.listdir(file_name)
            for file in songs:
                if file.endswith(".mp3"):
                    str += file + "\n"
                    playlist.insert(END,file)
        else:
            messagebox.showinfo("Your selections", "You did not select any file")

def volume(val):
    mixer.music.set_volume(float(val)/100)
def stop():
    mixer.music.stop()
def pause():
    mixer.music.pause()
def resume():
    mixer.music.unpause()
def rewind():
    mixer.music.rewind()

f1 =Tk()
f1.geometry('1180x750+300+100')
f1.config(bg="black")
f1.title('Music Player')
f1.resizable(0,0)
mixer.init()

f2=Frame(f1)
f2.place(width=670,height=50,x=50,y=665)
bgofbutton = "deep sky blue"
b1 = Button(f2, text="Play", bg=bgofbutton, width=10, height=2,font=15,command=play)
b2 = Button(f2, text="Pause", bg=bgofbutton, width=10, height=2,font=15,command=pause)
b3 = Button(f2, text="Resume", bg=bgofbutton, width=10, height=2,font=15,command=resume)
b4 = Button(f2, text="Rewind", bg=bgofbutton, width=10, height=2,font=15,command=rewind)
b5 = Button(f2, text="Stop",bg=bgofbutton, width=10, height=2,font=15, command=stop)
b1.grid(row=1,column=0,padx=0,pady=0)
b2.grid(row=1,column=1,padx=0,pady=0)
b3.grid(row=1,column=2,padx=0,pady=0)
b4.grid(row=1,column=3,padx=0,pady=0)
b5.grid(row=1,column=4,padx=0,pady=0)

vol = Scale(f2, from_=0, to=100,orient=HORIZONTAL,length=100,resolution=0, bg=bgofbutton, width=20,font=12,command=volume)
vol.set(50)
vol.grid(row=1,column=5,columnspan=2,ipadx=34)

img=PhotoImage(file="C:\\Users\\sathesm\\PycharmProjects\\demo\\FSD_tution tkinter projects\\image4.PNG")
l2=Label(f1, image=img,compound=CENTER)
l2.place(width=670,height=515,x=50,y=50)

songs_frame = LabelFrame(text="Song playlist", font="Arial 16 bold", borderwidth=7, relief="groove",bg="black",fg="white")
songs_frame.place(width=400, height=665, x=745, y=50)
b5 = Button(songs_frame, text="Open file",bg=bgofbutton , borderwidth=7,width=14, height=1,font=17, command=open)
b5.pack(fill=BOTH)
scroll_y = Scrollbar(songs_frame, orient=VERTICAL)
playlist = Listbox(songs_frame, yscrollcommand=scroll_y.set, selectmode=SINGLE,bg="black",fg="white",height=36)
print(playlist)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=playlist.yview())
playlist.pack(fill=BOTH)

l3 = Label(f1, text="Song track",font="arial 16",borderwidth=5, relief="groove",width=20,bg=bgofbutton,fg="black")
l3.place(width=120, height=40, x=50, y=575)
e1 = Entry(f1,font="arial  16 ", relief="groove",borderwidth=5,bg=bgofbutton,fg="black")
e1.place(width=550, height=40, x=170, y=575)

status = Label(f1,text=" ",borderwidth=3, font=16, relief="groove",bg="orange",fg="black")
status.place(width=670, height=25, x=50, y=625)

f1.mainloop()