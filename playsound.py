import tkinter as tk
from tkinter import filedialog
import pygame

def choose_track():
    file_path = filedialog.askopenfilename()
    pygame.mixer.music.load(file_path)

def play_track():
    pygame.mixer.music.play()

def pause_track():
    pygame.mixer.music.pause()

def stop_track():
    pygame.mixer.music.stop()

def increase_volume():
    current_volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(min(current_volume + 0.1, 1.0))

def decrease_volume():
    current_volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(max(current_volume - 0.1, 0.0))

def loop_track():
    pygame.mixer.music.play(-1)

root = tk.Tk()
root.title("Audio Player")
root.geometry("300x200")

choose_track_button = tk.Button(root, text="Choose Track", command=choose_track)
choose_track_button.pack()

play_track_button = tk.Button(root, text="Play", command=play_track)
play_track_button.pack()

pause_track_button = tk.Button(root, text="Pause", command=pause_track)
pause_track_button.pack()

stop_track_button = tk.Button(root, text="Stop", command=stop_track)
stop_track_button.pack()

increase_volume_button = tk.Button(root, text="Increase Volume", command=increase_volume)
increase_volume_button.pack()

decrease_volume_button = tk.Button(root, text="Decrease Volume", command=decrease_volume)
decrease_volume_button.pack()

loop_track_button = tk.Button(root, text="Loop", command=loop_track)
loop_track_button.pack()

pygame.mixer.init()
root.mainloop()
