from tkinter import *
import os
from tkinter import filedialog
import pygame
import tkinter as tk
import time
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
from mutagen.mp3 import MP3

root = Tk()
root.configure(bg='black')
root.title('Music Player')

# Intilalize pygame
pygame.mixer.init()

# Global Variable
audiotrack= StringVar()
audioinitialpath = StringVar()
global playlist
playlist =[]
global paused
paused= False
current=0
global filename

''' command for adding and removing '''
# add songs to playlist command
def add_songs():
    songlist = []
    global playlist
    song_box.delete(0,END)
    filename = filedialog.askopenfilenames(title='Select Audio File',filetype=(('MP3','.mp3'),('WAV','.wav')))
    for song in filename:
        if os.path.splitext(song)[1] == '.mp3':
            path= (song).replace('\\','/')
            print(path)
            song= song.replace(".mp3","")
            songlist.append(path)
            audiotrack.set(path)
        song_box.insert(END,os.path.basename(song))
    
    playlist = songlist
    audiotrack.set(filename)
global removed
removed=1
global i
i=1
def remove_song():
    my_slider.config(value = 0)
    status_bar.config(text='')
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()
    global stopped
    stopped= True
    global removed
    global i
    i= i+1
    removed= i
    stopped= True      

global stopped
stopped= False
def remove_songs():
    my_slider.config(value = 0)
    status_bar.config(text='')
    song_box.delete(0,END)
    pygame.mixer.music.stop()
    global stopped
    stopped= True  

# command for Play button
def playmusic():
    current = song_box.curselection()[0]
    global stopped
    global totalsonglength
    song = playlist[current]
    print(song)
    song = MP3(song)
    totalsonglength= int(song.info.length)
    stopped=False 
    audio = pygame.mixer.music.load(playlist[current])
    pygame.mixer.music.play()
    play_time()
    slider_position = int(totalsonglength)
    my_slider.config(to=slider_position,value=0)
    
''' command for play, pause and stop buttons '''
# command for Pause button
def pausemusic(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused= False
    else:
        pygame.mixer.music.pause()
        paused= True

# command for stop button
def stopmusic():
    my_slider.config(value = 0)
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    status_bar.config(text='')
    global stopped
    stopped= True

''' command for next and previous button '''
# command for next button
def next_song():
    global stopped
    stopped=False 
    status_bar.config(text='')
    my_slider.config(value = 0)
    next_one = song_box.curselection()[0]
    global removed
    print(removed)
    if next_one < (len(playlist)-removed):
        next_one = next_one+1
        playlist_song = song_box.get(next_one)
        print(playlist_song)
        pygame.mixer.music.load(playlist[next_one])
        pygame.mixer.music.play()
        song_box.selection_clear(0,END)
        song_box.activate(next_one)
        song_box.selection_set(next_one, last = None)
    else:
        return
    play_time()

# command for previous button
def prev_song():
    global stopped
    stopped=False 
    paused=False
    status_bar.config(text='')
    my_slider.config(value = 0)
    prev_one = song_box.curselection()[0]
    if prev_one > 0:
        prev_one = prev_one-1
        playlist_song = song_box.get(prev_one)
        print(playlist_song)
        pygame.mixer.music.load(playlist[prev_one])
        pygame.mixer.music.play()
        song_box.selection_clear(0,END)
        song_box.activate(prev_one)
        song_box.selection_set(prev_one, last = None)
    else:
        return
    play_time()
   
# grab Song Length Time info
def play_time():
    if stopped== True:
        return
    elif stopped == False:
        current_time =pygame.mixer.music.get_pos() // 1000
        converted_current_time = time.strftime('%M:%S',time.gmtime(current_time))
        current = song_box.curselection()[0]
        song = playlist[current]
        song = MP3(song)
        totalsonglength= int(song.info.length) 
        converted_totalsonglength_time = time.strftime('%M:%S',time.gmtime(totalsonglength))
        current_time+=1
        if int(my_slider.get()) == int(totalsonglength):
            status_bar.config(text=f'Time Elapsed: {converted_totalsonglength_time} of {converted_totalsonglength_time} ')
        elif paused:
            pass
        elif int(my_slider.get()) == int(current_time):
            slider_position = int(totalsonglength)
            my_slider.config(to_=slider_position, value = int(current_time))
        else:
            slider_position = int(totalsonglength)
            my_slider.config(to_=slider_position, value = int(my_slider.get()))
            converted_current_time = time.strftime('%M:%S',time.gmtime(int(my_slider.get())))
            status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_totalsonglength_time} ')   
    
            slider_position = int(totalsonglength)
            next_time = int(my_slider.get()) + 1
            my_slider.config(value= next_time) 
    status_bar.after(1000,play_time)

def slide(X):
    current = song_box.curselection()[0] 
    audio = pygame.mixer.music.load(playlist[current])
    pygame.mixer.music.play(start=int(my_slider.get()))

def change_volume(root, event=None):
    pygame.mixer.music.set_volume(volume_bar.get())
    a= pygame.mixer.music.get_volume()*100

# Create Master Frame
Master_frame = Frame(root,bg='black')
Master_frame.pack(pady = 20)

# Create Volume Frame
Volume_frame =LabelFrame(Master_frame,text='Volume',bg='dark grey')
Volume_frame.grid(row=0,column=1,padx=20)

# create playlist box
song_box = Listbox(Master_frame, bg="dark grey", fg="green", width = 65,height =12, selectbackground = "green", selectforeground="black")
song_box.grid(row =0, column= 0,padx=20) 

# Define player control buttons images
next_ = PhotoImage(file = 'images/next.png')
prev_ = PhotoImage(file='images/prev.png')
play_ = PhotoImage(file='images/play.png')
pause_ = PhotoImage(file='images/pause.png')
stop_ = PhotoImage(file='images/stop.png') 

# create player control frame
controls_frame = Frame(Master_frame,bg='black')
controls_frame.grid(row =1, column= 0,pady=20)

# create player control buttons
prev_btn = Button(controls_frame, bg='black',borderwidth = 0, activebackground ='black',image=prev_,command = prev_song)
next_btn = Button(controls_frame,bg='black', borderwidth = 0,activebackground ='black',image=next_, command = next_song)
play_btn = Button(controls_frame,bg='black', borderwidth = 0,activebackground ='black',image=play_,command = playmusic)
pause_btn = Button(controls_frame,bg='black', borderwidth = 0,activebackground ='black',image=pause_,command = lambda : pausemusic(paused))
stop_btn = Button(controls_frame,bg='black', borderwidth = 0,activebackground ='black',image=stop_,command = stopmusic)

prev_btn.grid(row = 1, column = 0, padx = 10)
next_btn.grid(row = 1, column = 1, padx = 10)
play_btn.grid(row = 1, column = 2, padx = 10)
pause_btn.grid(row = 1, column = 3, padx = 10)
stop_btn.grid(row = 1, column = 4, padx = 10)

# create Menu
my_menu = Menu(root)
root.config(menu = my_menu)

# add add many songs menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label = "Manage Playlist", menu = add_song_menu)
add_song_menu.add_command(label = "Add songs to Playlist", command = add_songs)

# add remove songs menu
add_song_menu.add_command(label = "Delete one song from Playlist", command = remove_song)
add_song_menu.add_command(label = "Delete all songs from Playlist", command = remove_songs)

# create music slider
my_slider = ttk.Scale(Master_frame, from_ = 0, to=100, orient = HORIZONTAL ,value= 0, command= slide, length=400)
my_slider.grid(row =2, column= 0,padx= 20,pady=20)
volume_bar = ttk.Scale(Volume_frame, from_ = 1, to=0,value=0.8, orient = VERTICAL , command= change_volume, length=140)
volume_bar.pack(pady=20)

# create status bar
status_bar = Label(root,text= '', bd =1, relief= GROOVE, anchor = E,bg='black',fg='white')
status_bar.pack(fill= X, side = BOTTOM, ipady =2)

root.iconbitmap('images/music.ico')
root.geometry("550x450")
root.resizable(False,False)
root.mainloop()
