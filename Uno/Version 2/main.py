##IMPORTS----------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import game
import sys
##-----------------
def play():
    print("play")
    for widget in root.winfo_children():
        widget.destroy()
    game.playerChoice(root)

def leave():
    root.destroy()
##HEXAS------------
bgHexa = "#C21E1E"
bgActiveHexa = "#B01C1C"
fgHexa = "#F5C928"
fgActiveHexa = "#F4C415"
darkHexa = "#691111"
darkActiveHexa = "#580E0E"
##WINDOWCREATION---
root = Tk()
root.geometry("790x700")
root.title("Uno")
root.configure(bg=bgHexa)
##-----------------
##WIDGETS----------
##---TITLE---------
title_var = StringVar()
title_var.set("   UNO   ")

titleLabel = Label(root,
                   textvariable = title_var,
                   anchor = CENTER,
                   bg = fgHexa,
                   fg = darkHexa,
                   font = ("Arial", 140, "bold")
                   )
##-----------------
##---PLAY----------
playButton = Button(root,
                    text = "Play!",
                    command = play,
                    activebackground = fgActiveHexa,
                    activeforeground = darkActiveHexa,
                    anchor = "center",
                    bg = fgHexa,
                    fg = darkHexa,
                    height = 1,
                    width = 10,
                    border = 0,
                    font = ("Arial", 50, "bold")
                    )
##-----------------
##---LEADERBOARD---
leadButton = Button(root,
                    text = "Leaderboard",
                    command = play,
                    activebackground = fgActiveHexa,
                    activeforeground = darkActiveHexa,
                    anchor = "center",
                    bg = fgHexa,
                    fg = darkHexa,
                    height = 1,
                    width = 10,
                    border = 0,
                    font = ("Arial", 50, "bold")
                    )
##-----------------
##---QUIT----------
quitButton = Button(root,
                    text = "Quit...",
                    command = leave,
                    activebackground = fgActiveHexa,
                    activeforeground = darkActiveHexa,
                    anchor = "center",
                    bg = fgHexa,
                    fg = darkHexa,
                    height = 1,
                    width = 10,
                    border = 0,
                    font = ("Arial", 50, "bold")
                    )
##-----------------
##WIDGETINITIALISE-
titleLabel.pack(pady=20)
playButton.pack()
leadButton.pack(pady=10)
quitButton.pack()
##-----------------
mainloop()
##-----------------
