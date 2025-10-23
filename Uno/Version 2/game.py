##IMPORTS----------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import initialisation
##HEXAS------------
bgHexa = "#C21E1E"
bgActiveHexa = "#B01C1C"
fgHexa = "#F5C928"
fgActiveHexa = "#F4C415"
darkHexa = "#691111"
darkActiveHexa = "#580E0E"
##-----------------
def playGame(root, playerNum):
    def nextPlayer(playerNum, numOfPlayers, order):
        playerNum += order
        if playerNum > (numOfPlayers - 1):
            playerNum -= numOfPlayers
        elif playerNum < 0:
            playerNum += numOfPlayers
        return playerNum
    for widget in root.winfo_children():
        widget.destroy()
    discardPile = []
    deck = initialisation.Deck()
    deck.createDeck()
    deck.shuffleDeck()
    discardPile.append(deck.getFirstNonWildCard())
    playerList = []
    for i in range(0, playerNum):
        playerHand = initialisation.playerHand(playerUserList[i])
        playerHand.drawStartingHand(deck)
        playerList.append(playerHand)

    gamePlaying = True
    playerNum = -1
    orderOfPlay = 1
    newTurn = False

    while gamePlaying == True:
        if newTurn == True:
            for widget in root.winfo_children():
                widget.destroy()
                newTurn = False
        discImage = PhotoImage(file=discardPile[0].getFilename())
        size = int(round(3000/(root.winfo_screenheight()/4), 0))
        discImage = discImage.subsample(size, size)
        discardPileImage = Label(root,
                                 image = discImage,
                                 anchor = CENTER,
                                 bg = bgHexa,
                                 fg = fgHexa
                                 )
        discardPileImage.pack(pady = (root.winfo_screenheight()/8, 0))
        playerNum = nextPlayer(playerNum, len(playerList), orderOfPlay)
        playerLabel_var = StringVar()
        playerLabel_var.set(str(playerList[playerNum].getPlayerName()) + ":")
        playerLabel = Label(root,
                            textvariable = playerLabel_var,
                            anchor = CENTER,
                            bg = bgHexa,
                            fg = fgHexa,
                            font = ("Arial", 40, "bold")
                            )
        playerLabel.pack(pady=5)
        handFrame = Frame(root,
                          width=root.winfo_width(),
                          bd=3,
                          bg=fgHexa
                          )
        handCanvas = Canvas(handFrame,
                            bg=darkHexa)
        handScrollbar = Scrollbar(handFrame,
                                  orient='horizontal'
                                  )
        
        
        handFrame.pack(side='bottom', fill='x')
        handScrollbar.pack(side='bottom', fill='x')
        handCanvas.pack(pady=10, padx=10, side='bottom', fill='x')
        handCanvas.configure(xscrollcommand=handScrollbar.set)

        cardsFrame = Frame(handCanvas,
                           bg=darkHexa
                           )
        for i in range(0, len(playerList[playerNum].getCardList())):
            cardImage = PhotoImage(file=playerList[playerNum].getCardList()[i].getFilename())
            cardImage = cardImage.subsample(size, size)
            cardBtn = (cardsFrame,
                       image = cardImage,
                       anchor = CENTER,
                       bg = bgHexa,
                       fg = fgHexa
                       )
            cardBtn.pack()
        root.mainloop()
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
        fifthScreen = root.winfo_screenheight() // 10
        playerFrame.pack(side = "top",
                         fill = "x",
                         padx = (20),
                         pady = (20)
                         )
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
                          text = " RULES: ",
                          anchor = CENTER,
                          bg = fgHexa,
                          fg = darkHexa,
                          font = ("Arial", 40, "bold")
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
                       ipady = (10)
                    )
        for i in range(0,3):
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
        drawCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = drawChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 15, "bold")
                                    )
        drawCombobox['values'] = ('Draw Once',
                                  'Draw until Playable')

        drawChoices.set('Draw Once')
        drawCombobox.current(0)
        ruleFrame.update_idletasks()
        drawCombobox.grid(row = 1, column = 0, sticky="nsew", padx = 10, ipady = 5)
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
        drawButtonCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = drawButtonChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 15, "bold")
                                    )
        drawButtonCombobox['values'] = ('Have Button',
                                  'Do not have Button')

        drawButtonChoices.set('Have Button')
        drawButtonCombobox.current(0)
        ruleFrame.update_idletasks()
        drawButtonCombobox.grid(row = 1, column = 1, sticky="nsew", padx = 10, ipady = 5)
        ##7-0 RULES
        sevenZeroLabel = Label(ruleFrame,
                          text = "7-0 Rule",
                          anchor = CENTER,
                          justify = "center",
                          bg = darkHexa,
                          fg = fgHexa,
                          font = ("Arial", 20, "bold")
                          )
        sevenZeroLabel.grid(row = 0, column = 2, sticky="nsew", padx = 10, pady=(10,0))
        sevenZeroChoices = StringVar()
        sevenZeroCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = sevenZeroChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 15, "bold")
                                    )
        sevenZeroCombobox['values'] = ('None',
                                       '7s Swap 1 to 1',
                                       '0s Swap Clockwise',
                                       'Both')
        sevenZeroChoices.set('None')
        sevenZeroCombobox.current(0)
        ruleFrame.update_idletasks()
        sevenZeroCombobox.grid(row = 1, column = 2, sticky="nsew", padx = 10, ipady = 5)
        ##STACKING RULES
        stackingLabel = Label(ruleFrame,
                          text = "Stacking",
                          anchor = CENTER,
                          justify = "center",
                          bg = darkHexa,
                          fg = fgHexa,
                          font = ("Arial", 20, "bold")
                          )
        stackingLabel.grid(row = 2, column = 0, sticky="nsew", padx = 10, pady=(10,0))
        stackingChoices = StringVar()
        stackingCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = stackingChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 15, "bold")
                                    )
        stackingCombobox['values'] = ('No Stacking',
                                      'Stack 2s on 2s',
                                      'Stack 4s on 4s',
                                      'Stack Everything',
                                      'All')
        stackingChoices.set('No Stacking')
        stackingCombobox.current(0)
        ruleFrame.update_idletasks()
        stackingCombobox.grid(row = 3, column = 0, sticky="nsew", padx = 10, ipady = 5)
        ##UNO CALL RULES
        unoCallLabel = Label(ruleFrame,
                          text = "UNO!",
                          anchor = CENTER,
                          justify = "center",
                          bg = darkHexa,
                          fg = fgHexa,
                          font = ("Arial", 20, "bold")
                          )
        unoCallLabel.grid(row = 2, column = 1, sticky="nsew", padx = 10, pady=(10,0))
        unoCallChoices = StringVar()
        unoCallCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = unoCallChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 15, "bold")
                                    )
        unoCallCombobox['values'] = ('Call Uno before playing second to last card',
                                     'No need to call Uno')
        unoCallChoices.set('Call Uno before playing second to last card')
        unoCallCombobox.current(0)
        ruleFrame.update_idletasks()
        unoCallCombobox.grid(row = 3, column = 1, sticky="nsew", padx = 10, ipady = 5)
        ##WILD SHUFFLE RULES
        wildShuffleLabel = Label(ruleFrame,
                          text = "Wild Shuffle",
                          anchor = CENTER,
                          justify = "center",
                          bg = darkHexa,
                          fg = fgHexa,
                          font = ("Arial", 20, "bold")
                          )
        wildShuffleLabel.grid(row = 2, column = 2, sticky="nsew", padx = 10, pady=(10,0))
        wildShuffleChoices = StringVar()
        wildShuffleCombobox = ttk.Combobox(ruleFrame,
                                    textvariable = wildShuffleChoices,
                                    justify = "center",
                                    state="readonly",
                                    font=("Arial", 15, "bold")
                                    )
        wildShuffleCombobox['values'] = ('No Shuffle',
                                         'Shuffle Hands on Wild',
                                         'Shuffle Hands on Wild +4',
                                         'Shuffle Hands on Both')
        wildShuffleChoices.set('No Shuffle')
        wildShuffleCombobox.current(0)
        ruleFrame.update_idletasks()
        wildShuffleCombobox.grid(row = 3, column = 2, sticky="nsew", padx = 10, ipady = 5)
        ##-----------------
        playButton = Button(root,
                            text = "Play!",
                            command = lambda: playGame(root, playerNum),
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
        root.mainloop()
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

    playerAmountCombobox.current(0)
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
