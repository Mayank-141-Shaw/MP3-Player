import os
import pygame as pg
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

win = tk.Tk()
win.title('Harmony Player')
win.resizable(False, False)
pg.init()

play_img = tk.PhotoImage(file = r'Icons/play.png')
pause_img = tk.PhotoImage(file = r'Icons/pause.png')
stop_img = tk.PhotoImage(file = r'Icons/stop.png')
folder_img = tk.PhotoImage(file = r'Icons/folder.png')
next_img = tk.PhotoImage(file = r'Icons/next.png')
prev_img = tk.PhotoImage(file = r'Icons/prev.png')
player_img = tk.PhotoImage(file = r'Icons/now_playing.png')

# resize the images to fit in the buttons
play_img = play_img.subsample(2, 2)
pause_img = pause_img.subsample(2, 2)
stop_img = stop_img.subsample(2, 2)
folder_img = folder_img.subsample(2, 2)
next_img = next_img.subsample(2, 2)
prev_img = prev_img.subsample(2, 2)
player_img = player_img.subsample(2, 2)

list_of_songs = []
realnames = []
index = 0
p = True        # indicator for pause - play

def stop():
    statusLabel['text'] = ''
    pg.mixer_music.stop()

def pause():
    global p
    if p:
        pg.mixer_music.pause()
        p = False
    else:
        pg.mixer_music.unpause()
        p = True

def play():
    global index, list_of_songs
    pg.mixer_music.load(list_of_songs[index])

    #remove the .mp3 from the label
    statusLabel['text'] = list_of_songs[index][0:len(list_of_songs[index])-4]
    pg.mixer_music.play()

def next():
    global index
    index += 1
    index = index % len(list_of_songs)
    pg.mixer_music.load(list_of_songs[index])

    #remove the .mp3 from the label
    statusLabel['text'] = list_of_songs[index][0:len(list_of_songs[index])-4]
    pg.mixer_music.play()

def prev():
    global index
    if index == 0:
        index = len(list_of_songs)-1
    else:
        index -= 1
    pg.mixer_music.load(list_of_songs[index])

    #remove the .mp3 from the label
    statusLabel['text'] = list_of_songs[index][0:len(list_of_songs[index])-4]
    pg.mixer_music.play()

def choose_dir():
    global list_of_songs
    dir = filedialog.askdirectory()
    os.chdir(dir)

    listBox.delete(0, len(list_of_songs)-1)
    list_of_songs = []
    for files in os.listdir(dir):
        if files.endswith('.mp3'):
            #realdir = os.path.realpath(files)
            #audio = EasyID3(realdir)            #brings all metadat assoc with file in the audio
            #audio['TIT2'] is a tag which returns the title of the audio
            # .text[0] converts in text format
            #realnames.append(audio.get('title'))
            list_of_songs.append(files)

    
    for items in list_of_songs:
        listBox.insert(tk.ANCHOR, items+'\n')


label = tk.LabelFrame(win, text='Mp3 Player')
label.grid(row=0, padx=3, pady=3)

listBox = tk.Listbox(label, height=10, width=60)
listBox.grid(row=0, columnspan=4, padx=3, pady=3, sticky='WE')
#scr = sc.ScrolledText(label, height=10)
#scr.grid(row=0, columnspan=4, padx=3, pady=3)

chooseDirButton = tk.Button(label, text='Choose Directory', image=folder_img, compound=tk.LEFT, command=choose_dir)
chooseDirButton.grid(row=1, columnspan=4, padx=3, pady=3, sticky='WE')

nextButton = tk.Button(label, text='Next', image=next_img, compound=tk.LEFT, command=next)
nextButton.grid(row=2, columnspan=2, column=0, pady=3, padx=3, sticky='WE')

previousButton = tk.Button(label, text='Previous', image=prev_img, compound=tk.LEFT, command=prev)
previousButton.grid(row=2, columnspan=2, column=2, pady=3, padx=3, sticky='WE')

stopBtn = tk.Button(label, text='Stop', image=stop_img, compound=tk.LEFT, command=stop)
stopBtn.grid(row=3, column=3, pady=3, padx=3, sticky='WE')

pauseBtn = tk.Button(label, text='Pause', image=pause_img, compound=tk.LEFT, command=pause)
pauseBtn.grid(row=3, column=1, pady=3, padx=3, sticky='WE', columnspan=2)

playBtn = tk.Button(label, text='Play', image=play_img, compound=tk.LEFT, command=play)
playBtn.grid(row=3, column=0, pady=3, padx=3, sticky='WE')

playerFrame = tk.LabelFrame(label, text='Now Playing :')
playerFrame.grid(row=4, padx=3, pady=3, columnspan=4, sticky='WE')

statusLabel = ttk.Label(playerFrame, text='Hello', image=player_img, compound=tk.LEFT)
statusLabel.grid(row=0, padx=3, pady=3, columnspan=4)

win.mainloop()