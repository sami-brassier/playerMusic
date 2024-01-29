import os
import tkinter as tk
from tkinter import filedialog
import pygame

class AudioPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Lecteur Audio")

        self.current_file = None
        self.playing = False
        self.looping = False
        self.volume = 0.5

        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self.master, text="Choisir un fichier", command=self.choose_file)
        self.select_button.pack()

        self.play_button = tk.Button(self.master, text="Lire", command=self.play)
        self.play_button.pack()

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.master, text="Arrêter", command=self.stop)
        self.stop_button.pack()

        self.volume_slider = tk.Scale(self.master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL,
                                       label="Volume", command=self.set_volume)
        self.volume_slider.set(self.volume)
        self.volume_slider.pack()

        self.loop_checkbox = tk.Checkbutton(self.master, text="Lire en boucle", command=self.toggle_loop)
        self.loop_checkbox.pack()

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers audio", "*.mp3;*.wav")])
        if file_path:
            self.current_file = file_path

    def play(self):
        if self.current_file:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play(loops=-1 if self.looping else 0)
            self.playing = True

    def pause(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False

    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

    def set_volume(self, volume):
        self.volume = float(volume)
        if self.playing:
            pygame.mixer.music.set_volume(self.volume)

    def toggle_loop(self):
        self.looping = not self.looping

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
