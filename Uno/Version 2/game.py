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
def playGame(root):
    root.destroy()
##-----------------
def setNext(root, enterPlayerEntry):
    global Next
    Next = True
    global playerUserList
    playerUserList.append(enterPlayerEntry.get())
    print(playerUserList)
    root.destroy()
##-----------------
def lobby(root, playersQLabel, playerAmountCombobox, nextButton):
    if int(playerAmountCombobox.get()) < 8 and int(playerAmountCombobox.get()) > 1:
        print("lobby")
        playerNum = int(playerAmountCombobox.get())
        root.destroy()
        global playerUserList
        playerUserList = []
        for i in range(0, playerNum):
            global Next
            Next = False
            while Next != True:
                
                root = Tk()
                root.geometry("300x120")
                root.title("Player " + str(i+1))
                root.configure(bg=bgHexa)
                ##-----------------
                enterPlayerLabel_var = StringVar()
                enterPlayerLabel_var.set("Player " + str(i + 1) + "'s username:")
                
                enterPlayerLabel = Label(root,
                                         textvariable = enterPlayerLabel_var,
                                         anchor = CENTER,
                                         bg = bgHexa,
                                         fg = fgHexa,
                                         font = ("Arial", 14, "bold")
                                         )
                ##-----------------
                enterPlayerEntry_var = StringVar()
                enterPlayerEntry_var.set("Username...")
                
                enterPlayerEntry = Entry(root,
                                         textvariable = enterPlayerEntry_var,
                                         font = ("Arial", 14),
                                         bd = 0
                                         )
                ##-----------------
                nextButton = Button(root,
                            text = "Next",
                            command = lambda: setNext(root, enterPlayerEntry),
                            activebackground = fgActiveHexa,
                            activeforeground = darkActiveHexa,
                            anchor = "center",
                            bg = fgHexa,
                            fg = darkHexa,
                            height = 4,
                            width = 10,
                            border = 0,
                            font = ("Arial", 14, "bold")
                            )             
                enterPlayerLabel.pack(pady=(10,0))
                enterPlayerEntry.pack()
                nextButton.pack(pady=10)
                root.mainloop()
        root = Tk()
        root.attributes("-fullscreen", True)
        root.title("UNO")
        root.configure(bg=bgHexa)
        
        playerFrame = Frame(root,
                            width=root.winfo_width(),
                            bd=3,
                            bg=fgHexa   
                            )
        playerFrame.pack(side = "top",
                         fill = "x",
                         padx = (20),
                         pady = (20))
        for i in range(0, playerNum):
            playerFrame.columnconfigure(i, weight=1)
            playerUserLbl_Var = StringVar()
            playerUserLbl_Var.set(playerUserList[i])
            playerUserLbl = Label(playerFrame,
                                  textvariable = playerUserLbl_Var,
                                  anchor = CENTER,
                                  bg = darkHexa,
                                  fg = fgHexa,
                                  font = ("Arial", 30, "bold")
                                  )
            playerUserLbl.grid(row = 0, column = i, sticky="nsew", padx = 10)
        ruleLabel = Label(root,
                          text = "RULES:",
                          anchor = CENTER,
                          bg = fgHexa,
                          fg = darkActiveHexa,
                          font = ("Arial", 20, "bold")
                          )
        ruleLabel.pack()
        ##PUT RULES BEFORE PLAY
        ruleFrame = Frame(root,
                          width=root.winfo_width(),
                          bg = darkHexa
                          )
        ruleFrame.pack(side = "top",
                       fill = "x",
                       padx = (20),
                       pady = (20),
                    )
        for i in range(0,2):
            ruleFrame.columnconfigure(i, weight=1)
        ##DRAWING RULES
        drawLabel = Label(ruleFrame,
                          text = "Draw if unable to play",
                          anchor = CENTER,
                          justify = "center",
                          bg = darkHexa,
                          fg = fgHexa,
                          font = ("Arial", 20, "bold")
                          )
        drawLabel.grid(row = 0, column = 0, sticky="nsew", padx = 10)
        drawChoices = StringVar()
        drawChoices.set("Draw Once")
        drawCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = drawChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 10, "bold")
                                    )
        drawCombobox['values'] = ('Draw Once',
                                  'Draw until Playable')
        drawCombobox.grid(row = 1, column = 0, sticky="nsew", padx = 10, ipady = 20)
        ##-----------------
        drawButtonLabel = Label(ruleFrame,
                          text = "Draw Button",
                          anchor = CENTER,
                          justify = "center",
                          bg = darkHexa,
                          fg = fgHexa,
                          font = ("Arial", 20, "bold")
                          )
        
        drawButtonLabel.grid(row = 0, column = 1, sticky="nsew", padx = 10)
        drawButtonChoices = StringVar()
        drawButtonChoices.set("Have Button")
        drawButtonCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = drawButtonChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 10, "bold")
                                    )
        drawButtonCombobox['values'] = ('Have Button',
                                  'Do not have Button')
        drawButtonCombobox.grid(row = 1, column = 1, sticky="nsew", padx = 10, ipady = 20)
        
        ##drawOptionLabel = 
        playButton = Button(root,
                            text = "Play!",
                            command = lambda: playGame(root),
                            activebackground = fgActiveHexa,
                            activeforeground = darkActiveHexa,
                            anchor = "center",
                            bg = fgHexa,
                            fg = darkHexa,
                            height = 1,
                            width = 10,
                            border = 0,
                            font = ("Arial", 40, "bold")
                            )
        playButton.pack()
##-----------------
def playerChoice(root):
    root.geometry("300x250")
    playersQ_var = StringVar()
    playersQ_var.set(" How many players? ")

    playersQLabel = Label(root,
                       textvariable = playersQ_var,
                       anchor = CENTER,
                       bg = fgHexa,
                       fg = darkHexa,
                       font = ("Arial", 20, "bold")
                       )
    ##-----------------
    playerAmountChoices = StringVar()
    playerAmountChoices.set("2")
    playerAmountCombobox = ttk.Combobox(root,
                                        width = 3,
                                        textvariable = playerAmountChoices,
                                        justify="center",
                                        state="readonly",
                                        font=("Arial", 20)
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
                        font = ("Arial", 20, "bold")
                        )             
    ##-----------------
    playersQLabel.pack(pady=(20,5))
    playerAmountCombobox.pack(pady=20, ipady=10)
    nextButton.pack(pady=(20,0))
    mainloop()
