##IMPORTS----------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import game
import sys
##-----------------
def play():
    print("play")
    titleLabel.forget()
    playButton.forget()
    quitButton.forget()
    game.playerChoice(root)

def leave():
    root.destroy()
##HEXAS------------
bgHexa = "#ed1c24"
bgActiveHexa = "#E21219"
fgHexa = "#f8da27"
fgActiveHexa = "#F8D512"
darkHexa = "#58585a"
darkActiveHexa = "#515152"
##WINDOWCREATION---
root = Tk()
root.geometry("790x560")
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
quitButton.pack(pady=20)
##-----------------
mainloop()
##-----------------
