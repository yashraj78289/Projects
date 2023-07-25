import  tkinter as tk
from tkinter import filedialog
from pygame import mixer

class Player:
    def __init__(self, window):
        window.geometry("320x100"); window.title("Python tiny Player"); window.resizable(0, 0)
        Load = tk.Button(window, text = "Load", width = 10, font = ("Times", 10), command = self.load)
        Play = tk.Button(window, text = "Play", width = 10, font = ("Times", 10), command = self.play)
        Pause = tk.Button(window, text = "Pause", width = 10, font = ("Times", 10), command = self.pause)
        Stop = tk.Button(window, text = "Stop", width = 10, font = ("Times", 10), command = self.stop)

        Load.place(x = 0, y = 20); Play.place(x = 110, y = 20); Pause.place(x = 220, y = 20);Stop.place(x = 110, y = 60)
        self.musicfile = False
        self.playing_state = False
    
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file :
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state = True

    def pause(self):
        if self.playing_state:
            mixer.music.pause()
            self.playing_state = False
        else:
            mixer.music.unpause()
            self.playing_state = True

    def stop(self):
        mixer.music.stop()

new_root = tk.Tk()
Player_app = Player(new_root)
new_root.mainloop()
