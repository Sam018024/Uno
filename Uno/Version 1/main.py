##IMPORTS-------
import initialisation
import game
import sys
##--------------
##INITIALVALUES-
Choice = "-1"
##--------------
##MAINPROGRAM---
while Choice != "0":
    print("""----UNO----
1 - Play!
0 - Exit...
-----------""")
    Choice = str(input()) ##Main Menu For Users to maneuver
    
    if Choice == "0": ##End the Program
        sys.exit()
        
    elif Choice == "1": ##Start the Game
        game.Game()
                
    else: ##If users don't input 1 or 0
        print(Choice, "isn't an option")


