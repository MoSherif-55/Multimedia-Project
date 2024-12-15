from tkinter import *
import tkinter as tk
from tkinter import messagebox  
from gtts import gTTS
from playsound import playsound
import os

root = tk.Tk()
root.title("Text To Speech By Mohamed Sherif")
root.geometry("400x300")
root.config(bg="#000")

def play_text():
    text = entry.get()
    if text.strip(): 
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        playsound("output.mp3")
        os.remove("output.mp3") 
    else:
        messagebox.showerror("Error", "The text is empty. Please enter your text.")

def exit_app():
    root.destroy()

def set_text():
    entry.delete(0,tk.END)

label =tk.Label(root, text="Enter your text:", bg="black", fg="white", font=("Arial", 14))
label.pack(pady=10)

entry =tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

button_frame =tk.Frame(root, bg="#000")
button_frame.pack(pady=20)

play_button =tk.Button(button_frame, text="Play", bg="green", fg="white", font=("Arial", 14), width=6, command=play_text)
play_button.pack(side="left", padx=10)

exit_button =tk.Button(button_frame, text="Exit", bg="red", fg="white", font=("Arial", 14), width=6, command=exit_app)
exit_button.pack(side="left", padx=10)

set_button =tk.Button(button_frame, text="Set", bg="blue", fg="white", font=("Arial", 14), width=6, command=set_text)
set_button.pack(side="left", padx=10)

root.mainloop()