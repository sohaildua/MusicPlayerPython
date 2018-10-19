from tkinter import *
from pygame import mixer

window = Tk()

mixer.init()
window.geometry('300x300')
window.title('My Music Player')


textLabel = Label(window,text="This is a Play button");
textLabel.pack()

def play_music():
    print("i am being played")
    mixer.music.load('sd.mp3')
    mixer.music.play()

playphoto = PhotoImage(file="play-button.png")
playbutton = Button(window, image = playphoto, command = play_music)
playbutton.pack()

def stop_music():
    print("i am being stopped")
    mixer.music.stop()


stopphoto = PhotoImage(file="pause-button.png")
stopbutton = Button(window, image = stopphoto, command = stop_music)
stopbutton.pack()

def set_value(value):
    print(value)
    volume = int(value)/100
    mixer.music.set_volume(volume)

scale = Scale(window,from_ =0 , to = 100 , orient = HORIZONTAL ,command = set_value)
scale.set(70)
scale.pack()
window.mainloop()