##IMPORTS----------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
##HEXAS------------
bgHexa = "#ed1c24"
bgActiveHexa = "#E21219"
fgHexa = "#f8da27"
fgActiveHexa = "#F8D512"
darkHexa = "#58585a"
darkActiveHexa = "#515152"
##-----------------
def lobby(root, playersQLabel, playerAmountCombobox, nextButton):
    print("lobby")
    playerNum = playerAmountCombobox.get()
    playersQLabel.forget()
    playerAmountCombobox.forget()
    nextButton.forget()
    root.attributes("-fullscreen", True)
##-----------------
def playerChoice(root):
    root.geometry("300x400")
    playersQ_var = StringVar()
    playersQ_var.set("How many players?")

    playersQLabel = Label(root,
                       textvariable = playersQ_var,
                       anchor = CENTER,
                       bg = bgHexa,
                       fg = fgHexa,
                       font = ("Arial", 14, "bold")
                       )
    ##-----------------
    playerAmountChoices = StringVar()
    playerAmountChoices.set("2")
    playerAmountCombobox = ttk.Combobox(root,
                                        width = 14,
                                        textvariable = playerAmountChoices
                                        )
    playerAmountCombobox['values'] = ('2',
                                      '3',
                                      '4',
                                      '5',
                                      '6',
                                      '7')
    ##-----------------
    nextButton = Button(root,
                        text = "Next",
                        command = lambda: lobby(root, playersQLabel, playerAmountCombobox, nextButton),
                        activebackground = fgActiveHexa,
                        activeforeground = darkActiveHexa,
                        anchor = "center",
                        bg = fgHexa,
                        fg = darkHexa,
                        height = 1,
                        width = 10,
                        border = 0,
                        font = ("Arial", 10, "bold")
                        )             
    ##-----------------
    playersQLabel.pack(pady=50)
    playerAmountCombobox.pack(pady=50)
    nextButton.pack(pady=50)
    mainloop()
