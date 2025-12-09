##IMPORTS----------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path
import time
import initialisation
##HARDCODEDDATE----
global colours
colours = ["Red", "Green", "Blue", "Yellow"]
##HEXAS------------
bgHexa = "#C21E1E"
bgActiveHexa = "#B01C1C"
fgHexa = "#F5C928"
fgActiveHexa = "#F4C415"
darkHexa = "#691111"
darkActiveHexa = "#580E0E"
##-----------------
def finish(root):
    root.destroy()

def playGame(root, drawRule, drawButtonRule, sevenZeroRule, stackingRule, unoCallRule, wildShuffleRule):
    
    def playCard(playedCardList, num):
        global order
        nonlocal root, playerNum

        def wildColour(colourNum):
            nonlocal choosingColour
            discardPile[0].setColour(colours[colourNum])
            discardPile[0].setFilename()
            choosingColour = False
            root.quit()

        def swapHands(playerTarget):
            targetHand = playerList[playerTarget].getCardList()
            playerHand = playerList[playerNum].getCardList()
            playerList[playerTarget].setCardList(playerHand)
            playerList[playerNum].setCardList(targetHand)
            updateUI()

        if num != "draw":
            playedCard = playedCardList[num]
            print("Card played:", playedCard.getFilename())
            
            if playedCard.getColour() == discardPile[0].getColour() or playedCard.getValue() == discardPile[0].getValue() or playedCard.getColour() == "Wild":

                discardPile.append(playerList[playerNum].getCardList()[num])
                del discardPile[0]
                del playerList[playerNum].getCardList()[num]
                
                if discardPile[0].getValue() == "Skip":
                    nextPlayer()

                elif discardPile[0].getValue() == "Reverse":
                    if len(playerList) == 2:
                        nextPlayer()
                    order *= -1

                elif discardPile[0].getValue()[0] == "+":
                    nextPlayer()
                    for i in range(int(discardPile[0].getValue()[1])):
                        playerList[playerNum].drawCard(deck)

                if sevenZeroRule == '7s Swap 1 to 1' or sevenZeroRule == 'Both':
                    if discardPile[0].getValue()[0] == "7":
                        for widget in root.winfo_children():
                            widget.destroy()
                        infoLabel = Label(root, text = "Choose who you want to swap hands with:", font = ("Arial", 40, "bold"), bg = bgHexa, fg = fgHexa, anchor = CENTER)
                        infoLabel.pack(pady = 20)

                        playersFrame = Frame(root,
                                             width = root.winfo_width(),
                                             bg = fgHexa
                                             )
                        playersFrame.pack(fill='x', pady = 20, padx = 20)
                        num = -1
                        for i in range(0, len(playerList)):
                            num += 1
                            if i == playerNum:
                                print("SCRW")
                                num += 1
                            else:
                                print("Yaabab")
                                playersLbl_Var = StringVar()
                                playersLbl_Var.set(playerList[i].getPlayerName())
                                playerButton = Button(playersFrame,
                                                      textvariable = playersLbl_Var,
                                                      anchor = CENTER,
                                                      command = lambda id=num: swapHands(id-1),
                                                      bd = 0,
                                                      font = ("Arial", 30, "bold"),
                                                      fg = fgHexa,
                                                      bg = darkHexa
                                                      )
                                
                                playerButton.grid(column = 0, row = i, sticky="NSEW", padx = 10, pady = 10)
                                playersFrame.rowconfigure(i, weight = 1)
                                playersFrame.columnconfigure(0, weight = 1)
                        root.mainloop()
                if sevenZeroRule == '0s Swap Clockwise' or sevenZeroRule == 'Both':
                    if discardPile[0].getValue()[0] == "0":
                        hand1 = playerList[0].getCardList()
                        for i in range(1, len(playerList)):
                            hand2 = playerList[i].getCardList()
                            num = i
                            if i == len(playerList):
                                num = i - len(playerList)
                            playerList[num].setCardList(hand1)
                            hand1 = hand2
                            print("Swap", str(num))
                        playerList[0].setCardList(hand1)
                    
                            
                choosingColour = True
                if discardPile[0].getColour() == "Wild":
                    for widget in root.winfo_children():
                        widget.destroy()
                    quarterScreen = int(round((root.winfo_screenheight()/4), 0))
                    for i in range(0,4):
                        colourButton = Button(root,
                                            text = colours[i],
                                            anchor = CENTER,
                                            command = lambda id=i: wildColour(id),
                                            bd = 0,
                                            width = int(root.winfo_screenwidth()),
                                            font = ("Arial", 10, "bold"),
                                            fg = darkHexa,
                                            bg = colours[i]
                                            )
                        root.rowconfigure(i, weight=1)
                        colourButton.grid(column = 0, row = i, sticky="NSEW")
                    root.mainloop()
                print("rrr")
                newTurn = True
                updateUI()
        else:
            playerList[playerNum].drawCard(deck)
            print("ghgh")
            newTurn = True
            updateUI()
            

    def nextPlayer():
        nonlocal playerNum
        playerNum += order
        if playerNum > (len(playerList) - 1):
            playerNum = 0
        elif playerNum < 0:
            playerNum += len(playerList)

    def updateUI():
        nonlocal root
        if len(playerList[playerNum].getCardList()) != 0:
            nextPlayer()
            canGo = False
            for i in range(0, len(playerList[playerNum].getCardList())):
                checkCard = playerList[playerNum].getCardList()[i]
                if checkCard.getColour() == discardPile[0].getColour() or checkCard.getValue() == discardPile[0].getValue() or checkCard.getColour() == "Wild":
                    canGo = True
            if canGo == True:
                print(discardPile[0].getFilename())
                for widget in root.winfo_children():
                    widget.destroy()
                script_dir = Path(__file__).parent
                image_path = script_dir / "assets" / discardPile[0].getFilename()
                discImage = PhotoImage(file=image_path)
                size = int(round(3000/(root.winfo_screenheight()/3), 0))
                discImage = discImage.subsample(size, size)
                discardPileImage = Label(root,
                                         image = discImage,
                                         anchor = CENTER,
                                         bg = bgHexa,
                                         fg = fgHexa
                                         )
                discardPileImage.pack(pady = (root.winfo_screenheight()/8, 0))

                playerLabel_var = StringVar()
                playerLabel_var.set(str(playerList[playerNum].getPlayerName()) + ":")
                playerLabel = Label(root,
                                    textvariable = playerLabel_var,
                                    anchor = CENTER,
                                    bg = bgHexa,
                                    fg = fgHexa,
                                    font = ("Arial", 40, "bold")
                                    )
        
                handFrame = Frame(root,
                                  width=root.winfo_width(),
                                  bd=0,
                                  bg=fgHexa
                                  )
                handCanvas = Canvas(handFrame,
                                    bg=darkHexa,
                                    bd = 0)
                handScrollbar = Scrollbar(handFrame,
                                          orient='horizontal',
                                          command=handCanvas.xview
                                          )
                handCanvas.configure(xscrollcommand=handScrollbar.set)

                handScrollbar.pack(side='bottom', fill='x')
                handCanvas.pack(pady=10, padx=10, side='bottom', fill='x')
                handFrame.pack(side='bottom', fill='x')
        
                cardsFrame = Frame(handCanvas,
                                   bg=darkHexa,
                                   bd = 0
                                   )
                handCanvas.create_window((0, 0), window=cardsFrame, anchor='nw')
        
                playerLabel.pack(pady=5, side='bottom')

                if drawButtonRule == 'Have Button':
                    script_dir = Path(__file__).parent
                    drawCardImage_path = script_dir / "assets" / "Draw.png"
                    drawCardImage = PhotoImage(file=drawCardImage_path)
                    drawCardImage = drawCardImage.subsample(size, size)
                    drawCardBtn = Button(cardsFrame,
                                         command = lambda: playCard(playerList[playerNum].getCardList(), "draw"),
                                         image = drawCardImage,
                                         anchor = CENTER,
                                         border = 0,
                                         bg = bgHexa,
                                         fg = fgHexa
                                         )
                    drawCardBtn.grid(row = 0, column = 0)
                cardList = []
                cardImageList = []
                for i in range(0, len(playerList[playerNum].getCardList())):
                    script_dir = Path(__file__).parent
                    image_path = script_dir / "assets" / playerList[playerNum].getCardList()[i].getFilename()
                    cardImage = PhotoImage(file=image_path)
                    cardImage = cardImage.subsample(size, size)
                    cardImageList.append(cardImage)
                    num = i
                    cardBtn = Button(cardsFrame,
                                     command = lambda id=i: playCard(playerList[playerNum].getCardList(), id),
                               image = cardImageList[i],
                               anchor = CENTER,
                               border = 0,
                               bg = bgHexa,
                               fg = fgHexa
                               )
                    cardList.append(cardBtn)
                    if drawButtonRule == 'Have Button':
                        cardList[i].grid(row = 0, column = i+1)
                    else:
                        cardList[i].grid(row = 0, column = i)
                cardsFrame.update_idletasks()
                handCanvas.configure(scrollregion=handCanvas.bbox("all"))
        
                if newTurn != True:
                    root.after(100, updateUI)
                root.mainloop()
            else:
                print("67")
                if drawRule == 'Draw Once':
                    playerList[playerNum].drawCard(deck)
                    print(playerList[playerNum].getPlayerName(), "drew")
                elif drawRule == 'Draw until Playable':
                    canGo = False
                    print("EEE")
                    while canGo == False:
                        for i in range(0, len(playerList[playerNum].getCardList())):
                            print("000")
                            checkCard = playerList[playerNum].getCardList()[i]
                            print("aaa")
                            if checkCard.getColour() == discardPile[0].getColour() or checkCard.getValue() == discardPile[0].getValue() or checkCard.getColour() == "Wild":
                                canGo = True
                                print("bbb")
                        if canGo == False:
                            print("ccc")
                            playerList[playerNum].drawCard(deck)
                            print("ddd")
                            print(playerList[playerNum].getPlayerName(), "drew")
                else:
                    print("djkjdfijhjvkdfjjio")
                root.after(10, updateUI)
        else:
            for widget in root.winfo_children():
                widget.destroy()
            winningLabel_var = StringVar()
            winningLabel_var.set(" " + str(playerList[playerNum].getPlayerName()) + " has won!!! ")
            winningLabel = Label(root,
                                 textvariable = winningLabel_var,
                                 anchor = CENTER,
                                 bg = fgHexa,
                                 fg = darkHexa,
                                 font = ("Arial", 100, "bold")
                                 )

            quitButton = Button(root,
                                text = "Quit",
                                command = lambda: finish(root),
                                activebackground = fgActiveHexa,
                                activeforeground = darkActiveHexa,
                                anchor = "center",
                                bg = fgHexa,
                                fg = darkHexa,
                                bd = 0,
                                font = ("Arial", 50, "bold")
                                )
            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)
            root.grid_rowconfigure(1, weight=1)
            winningLabel.grid(column = 0, row = 0)
            quitButton.grid(column = 0, row = 1)


    global playerList, discardPile, order, newTurn
    playerNum = 0
    order = 1
    newTurn = True
    
    discardPile = []
    deck = initialisation.Deck()
    deck.createDeck()
    deck.shuffleDeck()
    discardPile.append(deck.getFirstNonWildCard())
    playerList = []
    for i in range(0, NumOfPlayers):
        playerHand = initialisation.playerHand(playerUserList[i])
        playerHand.drawStartingHand(deck)
        playerList.append(playerHand)

    

    updateUI()
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
        global NumOfPlayers
        NumOfPlayers = int(playerAmountCombobox.get())
        root.destroy()
        global playerUserList
        playerUserList = []
        for i in range(0, NumOfPlayers):
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
        for i in range(0, NumOfPlayers):
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
                            command = lambda: playGame(root, drawCombobox.get(), drawButtonCombobox.get(), sevenZeroCombobox.get(), stackingCombobox.get(), unoCallCombobox.get(), wildShuffleCombobox.get()),
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
