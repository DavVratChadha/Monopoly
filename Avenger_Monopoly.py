#Avenger's Monopoly Game
#By Dav Vrat Chadha
#This is a modified version of the actual monopoly game. All new rules will be clearly stated when you start playing the game

import random
import time

#Game heading ASCII-art by an ASCII-art Generator
print("""                                        _       __  __                               _       
    /\                                 ( )     |  \/  |                             | |      
   /  \__   _____ _ __   __ _  ___ _ __|/ ___  | \  / | ___  _ __   ___  _ __   ___ | |_   _ 
  / /\ \ \ / / _ \ '_ \ / _` |/ _ \ '__| / __| | |\/| |/ _ \| '_ \ / _ \| '_ \ / _ \| | | | |
 / ____ \ V /  __/ | | | (_| |  __/ |    \__ \ | |  | | (_) | | | | (_) | |_) | (_) | | |_| |
/_/    \_\_/ \___|_| |_|\__, |\___|_|    |___/ |_|  |_|\___/|_| |_|\___/| .__/ \___/|_|\__, |
                         __/ |                                          | |             __/ |
                        |___/                                           |_|            |___/""")

#ASCII-art by Dav Vrat Chadha
print("""
 ____________________      ____________________
!\                    \   !\                    \ 
! \      CHANCE        \  ! \   COMMUNITY CHEST  \ 
 \ \    DVC\u2122 GAMES      \  \ \     DVC\u2122 GAMES     \ 
  \ \____________________\  \ \____________________\  
   \|_____________________|  \|_____________________|

                               /\  
            ^                 / \u25A0\  
           /_\               /____\  
   Houses |   |   Hotels    |   _  |  
          |___|             |  |.| |  
                            |__|_|_|""")

#Global variable
winner = "none"
alive = 1 #1 = True, 0 = False
deathCounter = 0 #number of players who have lost during the game
numPlayers = 0 #number of players playing the game
rent = 0
indexList = []
indexList2 = []

#boardTiles list is of the following syntax:
#[Tile Name, owner, type, status, price, building cost, defaultRent, 1 house, 2 house, 3 house, 4 house, hotel, colourSet index, currentBuild, code for colour set, buyable tile number]
    #(if special tile like Tax, Chance, or Community Chest, etc., owner = "spl" I.e. special)
    #currentBuild = number of houses built (5 for hotel)
    #The names are exactly 30 characters long with center of alignment for 15 characters in a line (important for printBoard function)
"""
boardTiles = [
              ["      Go                      ", "spl",  "go"],
              ["    Ruins of        Titan     ", "Player1", "property", "open", 60, 50, 2, 10, 30, 90, 160, 250, 0, 0, "br", 1],
              ["   Community        Chest     ", "spl",  "ccCard"],
              ["    Gulmira      Afghanistan  ", "Player1", "property", "open", 60, 50, 4, 20, 60, 180, 320, 450, 1, 0, "br", 2],
              [" Pay Income Tax    of $200    ", "spl",  "tax", 200],
              ["     London        Sanctum    ", "Player1", "sanc",     "open", 200, 0, "s",23],
              ["Raft-Underwater     Prison    ", "Player1", "property", "open", 100, 50, 6, 30, 90, 270, 400, 550, 0, 0, "lb",3],
              ["     Chance                   ", "spl",  "chCard"],
              ["    Sokovia                   ", "Player1", "property", "open", 100, 50, 6, 30, 90, 270, 400, 550, 1, 0, "lb",4],
              ["     Sakaar                   ", "Player1", "property", "open", 120, 50, 8, 40, 100, 300, 450, 600, 2, 0, "lb",5],
              ["   Kyln Nova      Corps Jail  ", "spl",  "jail", 50],
              ["      Kree          Empire    ", "Player1", "property", "open", 140, 100, 10, 50, 150, 450, 625, 750, 0, 0, "p",6],
              ["   Util:Dark      dimension   ", "Player1", "util",     "open", 150, 0, "u",27],
              ["     Ego's          planet    ", "Player1", "property", "open", 140, 100, 10, 50, 150, 450, 625, 750, 1, 0, "p",7],
              ["    Knowhere                  ", "Player1", "property", "open", 160, 100, 12, 60, 180, 500, 700, 900, 2, 0, "p",8],
              ["    New York       sanctum    ", "Player1", "sanc",     "open", 200, 1, "s",24],
              ["     Planet         Morag     ", "Player1", "property", "open", 180, 100, 14, 70, 200, 550, 750, 950, 0, 0, "o",9],
              ["   Community        Chest     ", "spl",  "ccCard"],
              ["     Planet         Vormir    ", "Player1", "property", "open", 180, 100, 14, 70, 200, 550, 750, 950, 1, 0, "o",10],
              ["     Xandar                   ", "Player1", "property", "open", 200, 100, 16, 80, 200, 600, 800, 1000, 2, 0, "o",11],
              ["      Free         Parking    ", "bank", "parking"],
              ["     Hydra      Headquarters  ", "Player2", "property", "open", 220, 150, 18, 90, 250, 700, 875, 1050, 0, 0, "r",12],
              ["     Chance                   ", "spl",  "chCard"],
              ["   Nidavellir                 ", "Player2", "property", "open", 220, 150, 18, 90, 250, 700, 875, 1050, 1, 0, "r",13],
              ["    Bifröst                   ", "Player2", "property", "open", 240, 150, 20, 100, 300, 750, 925, 1100, 2, 0, "r",14],
              ["   Hong Kong       sanctum    ", "Player2", "sanc",     "open", 200, 2, "s",25],
              ["   Jotunheim                  ", "Player2", "property", "open", 260, 150, 22, 110, 330, 800, 975, 1150, 0, 0, "y",15],
              ["      New           Asgard    ", "Player2", "property", "open", 260, 150, 22, 110, 330, 800, 975, 1150, 1, 0, "y",16],
              ["  Util:Mirror     Dimension   ", "Player2", "util",     "open", 150, 1, "u",28],
              ["     Asgard                   ", "Player2", "property", "open", 280, 150, 24, 120, 360, 850, 1025, 1200, 2, 0, "y",17],
              ["     Go To        Kyln Jail   ", "spl",  "goToJail"],
              ["     SHIELD      Helicarrier  ", "Player3", "property", "open", 300, 200, 26, 130, 390, 900, 1100, 1275, 0, 0, "g",18],
              ["    Quantum         realm     ", "Player3", "property", "open", 300, 200, 26, 130, 390, 900, 1100, 1275, 1, 0, "g",19],
              ["   Community        Chest     ", "spl",  "ccCard"],
              ["    Wakanda                   ", "Player3", "property", "open", 320, 200, 28, 150, 450, 1000, 1200, 1400, 2, 0, "g",20],
              ["     Kamar           Taj      ", "Player3", "sanc",     "open", 200, 3, "s",26],
              ["     Chance                   ", "spl",  "chCard"],
              ["     Stark          Tower     ", "Player3", "property", "open", 350, 200, 35, 175, 500, 1100, 1300, 1500, 0, 0, "db",21],
              ["   Luxary Tax      Pay $100   ", "spl",  "tax", 100],
              ["   Avenger's       upstate    ", "Player3", "property", "open", 400, 200, 50, 200, 600, 1400, 1700, 2000, 1, 0, "db",22]]


"""
boardTiles = [["      Go                      ", "spl",  "go"],
              ["    Ruins of        Titan     ", "bank", "property", "open", 60, 50, 2, 10, 30, 90, 160, 250, 0, 0, "br",1],
              ["   Community        Chest     ", "spl",  "ccCard"],
              ["    Gulmira      Afghanistan  ", "bank", "property", "open", 60, 50, 4, 20, 60, 180, 320, 450, 1, 0, "br",2],
              [" Pay Income Tax    of $200    ", "spl",  "tax", 200],
              ["     London        Sanctum    ", "bank", "sanc",     "open", 200, 0, "s",23],
              ["Raft-Underwater     Prison    ", "bank", "property", "open", 100, 50, 6, 30, 90, 270, 400, 550, 0, 0, "lb",3],
              ["     Chance                   ", "spl",  "chCard"],
              ["    Sokovia                   ", "bank", "property", "open", 100, 50, 6, 30, 90, 270, 400, 550, 1, 0, "lb",4],
              ["     Sakaar                   ", "bank", "property", "open", 120, 50, 8, 40, 100, 300, 450, 600, 2, 0, "lb",5],
              ["   Kyln Nova      Corps Jail  ", "spl",  "jail", 50],
              ["      Kree          Empire    ", "bank", "property", "open", 140, 100, 10, 50, 150, 450, 625, 750, 0, 0, "p",6],
              ["   Util:Dark      dimension   ", "bank", "util",     "open", 150, 0, "u",27],
              ["     Ego's          planet    ", "bank", "property", "open", 140, 100, 10, 50, 150, 450, 625, 750, 1, 0, "p",7],
              ["    Knowhere                  ", "bank", "property", "open", 160, 100, 12, 60, 180, 500, 700, 900, 2, 0, "p",8],
              ["    New York       sanctum    ", "bank", "sanc",     "open", 200, 1, "s",24],
              ["     Planet         Morag     ", "bank", "property", "open", 180, 100, 14, 70, 200, 550, 750, 950, 0, 0, "o",9],
              ["   Community        Chest     ", "spl",  "ccCard"],
              ["     Planet         Vormir    ", "bank", "property", "open", 180, 100, 14, 70, 200, 550, 750, 950, 1, 0, "o",10],
              ["     Xandar                   ", "bank", "property", "open", 200, 100, 16, 80, 200, 600, 800, 1000, 2, 0, "o",11],
              ["      Free         Parking    ", "bank", "parking"],
              ["     Hydra      Headquarters  ", "bank", "property", "open", 220, 150, 18, 90, 250, 700, 875, 1050, 0, 0, "r",12],
              ["     Chance                   ", "spl",  "chCard"],
              ["   Nidavellir                 ", "bank", "property", "open", 220, 150, 18, 90, 250, 700, 875, 1050, 1, 0, "r",13],
              ["    Bifröst                   ", "bank", "property", "open", 240, 150, 20, 100, 300, 750, 925, 1100, 2, 0, "r",14],
              ["   Hong Kong       sanctum    ", "bank", "sanc",     "open", 200, 2, "s",25],
              ["   Jotunheim                  ", "bank", "property", "open", 260, 150, 22, 110, 330, 800, 975, 1150, 0, 0, "y",15],
              ["      New           Asgard    ", "bank", "property", "open", 260, 150, 22, 110, 330, 800, 975, 1150, 1, 0, "y",16],
              ["  Util:Mirror     Dimension   ", "bank", "util",     "open", 150, 1, "u",28],
              ["     Asgard                   ", "bank", "property", "open", 280, 150, 24, 120, 360, 850, 1025, 1200, 2, 0, "y",17],
              ["     Go To        Kyln Jail   ", "spl",  "goToJail"],
              ["     SHIELD      Helicarrier  ", "bank", "property", "open", 300, 200, 26, 130, 390, 900, 1100, 1275, 0, 0, "g",18],
              ["    Quantum         realm     ", "bank", "property", "open", 300, 200, 26, 130, 390, 900, 1100, 1275, 1, 0, "g",19],
              ["   Community        Chest     ", "spl",  "ccCard"],
              ["    Wakanda                   ", "bank", "property", "open", 320, 200, 28, 150, 450, 1000, 1200, 1400, 2, 0, "g",20],
              ["     Kamar           Taj      ", "bank", "sanc",     "open", 200, 3, "s",26],
              ["     Chance                   ", "spl",  "chCard"],
              ["     Stark          Tower     ", "bank", "property", "open", 350, 200, 35, 175, 500, 1100, 1300, 1500, 0, 0, "db",21],
              ["   Luxary Tax      Pay $100   ", "spl",  "tax", 100],
              ["   Avenger's       upstate    ", "bank", "property", "open", 400, 200, 50, 200, 600, 1400, 1700, 2000, 1, 0, "db",22]]


#following lists contain name and owner of properties in a colour set.
#syntax = [name, owner]

brownSet = [["Ruins of Titan", "bank"],["Gulmira Afghanistan","bank"]] 
lightBlueSet = [["Raft-Underwater Prison","bank"],["Sokovia","bank"],["Sakaar","bank"]]
pinkSet= [["Kree Empire","bank"],["Ego's planet","bank"],["Knowhere","bank"]] 
orangeSet= [["Planet Morag","bank"],["Planet Vormir","bank"],["Xandar","bank"]]
redSet = [["Hydra Headquarters","bank"],["Nidavellir","bank"],["Bifröst","bank"]] 
yellowSet = [["Jotunheim","bank"],["New Asgard","bank"],["Asgard","bank"]]
greenSet = [["SHIELD Helicarrier","bank"],["Quantum realm","bank"],["Wakanda","bank"]]
darkBlueSet = [["Stark Tower","bank"],["Avenger's upstate","bank"]]
sanctumSet = [["London Sanctum","bank"],["New York sanctum","bank"],["Hong Kong sanctum","bank"],["Kamar Taj","bank"]]
dimensionSet = [["Dark dimension","bank"],["Mirror Dimension","bank"]]

"""
brownSet = [["Ruins of Titan", "Player1"],["Gulmira Afghanistan","Player1"]] 
lightBlueSet = [["Raft-Underwater Prison","Player1"],["Sokovia","Player1"],["Sakaar","Player1"]]
pinkSet= [["Kree Empire","Player1"],["Ego's planet","Player1"],["Knowhere","Player1"]] 
orangeSet= [["Planet Morag","Player1"],["Planet Vormir","Player1"],["Xandar","Player1"]]
redSet = [["Hydra Headquarters","Player2"],["Nidavellir","Player2"],["Bifröst","Player2"]] 
yellowSet = [["Jotunheim","Player2"],["New Asgard","Player2"],["Asgard","Player2"]]
greenSet = [["SHIELD Helicarrier","Player3"],["Quantum realm","Player3"],["Wakanda","Player3"]]
darkBlueSet = [["Stark Tower","Player3"],["Avenger's upstate","Player3"]]
sanctumSet = [["London Sanctum","Player1"],["New York sanctum","Player1"],["Hong Kong sanctum","Player2"],["Kamar Taj","Player3"]]
dimensionSet = [["Dark dimension","Player1"],["Mirror Dimension","Player2"]]
"""

#function for community chest cards
def communityChest(player, location, playerList, tile):#all ASCII-art cards have been built by Dav Vrat Chadha
    alive = 1
    usedCP = "no"#player has not used control panel
    print("You pick up a Community Chest Card.")
    time.sleep(2)
    index = random.randint(1,10) #choosing a random number to pick a card
    #if-else statements to simulate cards
    if index == 0:
        print("""Card states:
 ______________________________
|                              |
|                              |
|    Thanos didn't like your   |
|   gameplay and snapped you.  |
|          You lose!!          |
|                              |
|______________________________|""")
        time.sleep(1.5)
        print("Thank you for playing the game.")
        print("=============================================")
        alive, player, playerList = removePlayer(player, playerList) #player removed from the game
    elif index == 1:
        print("""Card States:
 ______________________________
|                              |
|                              |
|          Get out of          |
|      Intergalactic Kyln      |
|         JailFreeCard         |
|                              |
|______________________________|""")
        player[5] += 1 #one JailFreeCard being added to player's hand
        time.sleep(.8)
        print("Total number of JailFreeCards in your hand = " + str(player[5]))
    elif index == 2:
        print("""Card States:
 ______________________________
|                              |
|                              |
|          You get $50         |
|       for selling extra      |
|        Space-Ship fuel.      |
|                              |
|______________________________|""")
        player[2] += 50 #player gets $50
        time.sleep(.8)
        balance = int(player[2])
        print("New Balance = $" + str(balance))
    elif index == 3:
        print("""Card States:
 ______________________________
|                              |
|                              |
|        You found $100        |
|      floating in space.      |
|                              |
|                              |
|______________________________|""")
        player[2] += 100 #player gets $50
        balance = int(player[2])
        print("New Balance = $" + str(balance))
    elif index == 4:
        print("""Card States:
 ______________________________
|                              |
|                              |
|       Advance to GO and      |
|         Collect $200         |
|                              |
|                              |
|______________________________|""")
        player[2] += 200 #player gets $50
        player[1] = 0 #location = GO
        time.sleep(2)
        location = player[1]
        printBoard(player, location) #printing board another time to show new location
        balance = int(player[2])
        print("New Balance = $" + str(balance))
    elif index == 5:
        print("""Card States:
 ______________________________
|                              |
|                              |
|        Refueling fees.       |
|           Pay $150.          |
|                              |
|                              |
|______________________________|""")
        time.sleep(.8)
        if player[2] - 150 < 0: #if player does not have enough money
            balance = int(player[2])
            print("You only have $" + str(balance))
            print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
            print("=============================================")
            alive, player, playerList = removePlayer(player, playerList) #player removed from game
        else:
            player[2] -= 150 #player pays $150
            balance = int(player[2])
            print("New Balance = $" + str(balance))
    elif index == 6:
        print("""Card States:
 ______________________________
|                              |
|                              |
|    Hulk is smashing things   |
|        because of you.       |
|        Pay fine of $50       |
|                              |
|______________________________|""")
        time.sleep(.8)
        if player[2] - 50 < 0:#if player does not have enough money
            balance = int(player[2])
            print("You only have $" + str(balance))
            print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
            print("=============================================")
            alive, player, playerList = removePlayer(player, playerList)#player removed from game
        else:
            player[2] -= 50  #player pays $50
            balance = int(player[2])
            print("New Balance = $" + str(balance))
    elif index == 7:
        print("""Card States:
 ______________________________
|                              |
|                              |
|    Because of ountstanding   |
|  gameplay, Stark Industries  |
|         gave you $50.        |
|                              |
|______________________________|""")
        player[2] += 50 #player gets $50
        time.sleep(.8)
        balance = int(player[2])
        print("New Balance = $" + str(balance))
    elif index == 8:
        print("""Card States:
 ______________________________
|                              |
|        Go directly to        |
|   Intergalactic Kyln Jail.   |
|        Do not pass Go.       |
|     Do not collect $200.     |
|                              |
|______________________________|""")
        player[1] = 10 #location = Jail
        player[3] = "y" #player in jail
        time.sleep(2)
        location = player[1]
        printBoard(player, location) #printing board another time to show new location
        print("You are in Jail.")
        
    elif index == 9:
        print("""Card States:
 ______________________________
|                              |
|       You are assessed       |
|      for space repairs.      |
|     Pay $40 per house and    |
|    $115 per hotel you own.   |
|                              |
|______________________________|""")
        amount = 0
        for i in boardTiles: #for loop to count total amount to be paid by the player
            if i[1] == player[0] and i[2] == "property": #if player's property
                if i[13] < 5: #if only houses have been built
                    amount += (i[13]*40) #fee = number of houses*$40
                elif i[13] == 5: #if hotal has been built
                    amount += 115 #fee = $115
        print("You have to pay $" + str(amount) +".")
        time.sleep(.8)
        if player[2] - amount < 0: #if players lacks money
            balance = int(player[2])
            print("You only have $" + str(balance))
            print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
            print("=============================================")
            alive, player, playerList = removePlayer(player, playerList) #player removed from game
            
        else:
            player[2] -= amount #player pays the amount
            balance = int(player[2])
            print("New Balance = $" + str(balance))
    elif index == 10:
        print("""Card States:
 ______________________________
|                              |
|        Go to Knowhere.       |
|    The collector wants to    |
|       show his amazing       |
|    Intergalactic Creature    |
|          collection.         |
|______________________________|""")
        player[1] = 14 #location = Knowhere
        time.sleep(2)
        location = player[1]
        printBoard(player, location) #printing board another time to display new location
        alive, winner, player, location, playerList, tile = action(player, location, playerList, tile) #action function if player can buy tile or has to pay rent
        usedCP = "yes"#player has used control panel
   
    winner, playerList = victoryDeterminer(playerList) #winner being determined
    return alive, winner, usedCP, player, location, playerList, tile



def chance(player, location, playerList, tile): #all ASCII-art cards have been built by Dav Vrat Chadha
    alive = 1
    usedCP = "no" #player has not use the control panel
    print("You pick up a Chance Card.")
    time.sleep(2)
    index = random.randint(0,9)#choosing random number to pick a card
    
    if index == 0:
        print("""Card States:
 ______________________________
|                              |
|    Go to New York Sanctum.   |
|     Doctor Strange wants     |
|        to have a cup of      |
|          tea with you.       |
|                              |
|______________________________|""")
        if player[1] > 5: #if player has already passed New York Sanctum, they will pass go
            print("You passed GO on your way, and earned $200.")
            player[2] += 200#player gets $200 for passing go
            balance = int(player[2])
            print("New Balance = $" + str(balance))
        player[1] = 5 #location = New York Sanctum
        time.sleep(.8)
        location = player[1]
        printBoard(player, location) #printing board to display new location
        alive, winner, player, location, playerList, tile = action(player, location, playerList, tile)
        usedCP = "yes"#player has used control panel

    elif index == 1:
        print("""Card States:
 ______________________________
|                              |
|        Go to the next        |
|       nearest Dimension.     |
|       You may buy it if      |
|      unowned. If owned,      |
|    pay the owner the rent.   |
|______________________________|""")
        if player[1] > 27: #if player has passed 2nd Dimension, but hasn not passed go, they will go to the first Dimension and pass Go on theor way
            print("You advanced to the Dark dimension.")
            time.sleep(1.5)
            print("You passed GO on your way, and earned $200.")
            player[2] += 200 #player gets $200 for passing GO
            balance = int(player[2])
            print("New Balance = $" + str(balance))
            player[1] = 12 #location = Dark Dimension
        elif player[1] < 12: #if player lies between GO and Dark Dimension
            print("You advanced to the Dark dimension.")
            player[1] = 12 #location = Dark Dimension
        elif player[1] > 11 and player[1] < 28: #if player lies between Dark Dimension and Mirror Dimension
            print("You advanced to the Mirror dimension.")
            player[1] = 28 #location = Mirror Dimension
        time.sleep(1.5)
        location = player[1]
        printBoard(player, location) #printing board to display new location
        alive, winner, player, location, playerList, tile = action(player, location, playerList, tile)
        usedCP = "yes"#player has used control panel
    elif index == 2:
        print("""Card States:
 ______________________________
|                              |
|                              |
|      Travel back in time     |
|              and             |
|     go back three spaces.    |
|                              |
|______________________________|""")
        player[1] -= 3 #location 3 spaces back
        time.sleep(1.5)
        location = player[1]
        printBoard(player, location) #printing board to display new location
        alive, winner, player, location, playerList, tile = action(player, location, playerList, tile)
        usedCP = "yes"#player has used control panel
    elif index == 3:
        print("""Card States:
 ______________________________
|                              |
|                              |
|           You were           |
|      speeding in space.      |
|       Pay fine of $15.       |
|                              |
|______________________________|""")
        time.sleep(.8)
        if player[2] - 15 < 0: #if player lacks money
            balance = int(player[2])
            print("You only have $" + str(balance))
            print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
            print("=============================================")
            alive, player, playerList = removePlayer(player, playerList) #player loses and removed from game
        else: #if player has the money
            player[2] -= 15 #player pays the money
            balance = int(player[2])
            print("New Balance = $" + str(balance))

    elif index == 4:
        print("""Card States:
 ______________________________
|                              |
|                              |
|     Make general repairs.    |
|     Pay $25 per house and    |
|    $100 per hotel you own.   |
|                              |
|______________________________|""")
        amount = 0
        #for loop to calculate the amount to be paid for repairs
        for i in boardTiles:
            if i[1] == player[0] and i [2] == "property": #if player owns the property
                if i[13] < 5: #if only houses are built
                    amount += (i[13]*25) #amount = number of houses*25
                elif i[13] == 5: #if hotel is built
                    amount += 100 #amount = $100 for a hotel
        print("You have to pay $" + str(amount) +".")
        time.sleep(1)
        if player[2] - amount < 0: #if player lacks money
            balance = int(player[2])
            print("You only have $" + str(balance))
            print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
            print("=============================================")
            alive, player, playerList = removePlayer(player, playerList) #player loses and removed from the game
            
        else: #if player has the money
            player[2] -= amount #player pays the money
            balance = int(player[2])
            print("New Balance = $" + str(balance))

    elif index == 5:
        print("""Card States:
 ______________________________
|                              |
|                              |
|        Your spaceship        |
|         loan matures.        |
|         Collect $150.        |
|                              |
|______________________________|""")
        player[2] += 150 #player gets $150
        time.sleep(.8)
        balance = int(player[2])
        print("New Balance = $" + str(balance))

    elif index == 6:
        print("""Card States:
 ______________________________
|                              |
|        Go directly to        |
|   Intergalactic Kyln Jail.   |
|        Do not pass Go.       |
|     Do not collect $200.     |
|                              |
|______________________________|""")
        
        player[1] = 10 #location = Jail
        player[3] = "y" #player in Jail
        time.sleep(2)
        location = player[1]
        printBoard(player, location) #printing board to display the new location
        print("You are in Jail.")

    elif index == 7:
        print("""Card States:
 ______________________________
|                              |
|                              |
|           Go to the          |
|         Quantum Realm        |
|      to collect energy.      |
|                              |
|______________________________|""")
        if player[1] > 32: #if player has already passed Quantum Realm, they will pass Go on their way
            print("You passed GO on your way, and earned $200.")
            player[2] += 200 #player gets $200 for passing Go
            balance = int(player[2])
            print("New Balance = $" + str(balance))
        player[1] = 32 #location = Quantum Realm
        time.sleep(.8)
        location = player[1]
        printBoard(player, location) #printing board to display new location
        alive, winner, player, location, playerList, tile = action(player, location, playerList, tile)
        usedCP = "yes"#player has used control panel
    elif index == 8:
        print("""Card States:
 ______________________________
|                              |
|                              |
|   You won the Intergalactic  |
|        Beast contest.        |
|         Collect $50.         |
|                              |
|______________________________|""")
        player[2] += 50 #player gets $50
        time.sleep(.8)
        balance = int(player[2])
        print("New Balance = $" + str(balance))

    elif index == 9:
        print("""Card States:
 ______________________________
|                              |
|                              |
|          Advance to          |
|       Avenger's Upstate      |
|                              |
|                              |
|______________________________|""")
        player[1] = 39 #location = Avenger's Upstate
        time.sleep(1)
        location = player[1]
        printBoard(player, location) #printing board to display new location
        alive, winner, player, location, playerList, tile = action(player, location, playerList, tile)
        usedCP = "yes"#player has used control panel
    
    winner, playerList = victoryDeterminer(playerList) #determing winner
    return alive, winner, usedCP, player, location, playerList, tile




#Function to choose a random number from 1 to 6, to simulate a die
def dieRoll():
    roll = random.randint(1,6) #randint generates a random number from 1 to 6
    return roll

#Function to assign ASCII-art to the die roll
#ASCII-art by Dav Vrat Chadha
def assignDieASCIIart(num): #The die ASCII-art is arranged in a single line to make it easy to print 2 die together
    if num == 1:
        return("""+-------+|       ||   o   ||       |+-------+""")

    elif num == 2:
        return("""+-------+|  o    ||       ||    o  |+-------+""")

    elif num == 3:
        return("""+-------+|  o    ||   o   ||    o  |+-------+""")

    elif num == 4:
        return("""+-------+|  o o  ||       ||  o o  |+-------+""")

    elif num == 5:
        return("""+-------+|  o o  ||   o   ||  o o  |+-------+""")

    elif num == 6:
        return("""+-------+|  o o  ||  o o  ||  o o  |+-------+""")

#Function to print the dice    
def printDice(a,b):
    while a and b:#While the ASCII-art exists
        print(a[:9] + "  " + b[:9]) #Printing the first nine characters of the ASCII-art of both dice 
        a = a[9:] #and then removing those to print next line via same method
        b = b[9:]
    time.sleep(.5)
    return

# ["    Ruins of        Titan     ", "Player1", "property", "open", 60, 50, 2, 10, 30, 90, 160, 250, 0, 0, "br", 1]
#function to assign color to print the board
def colorAssigner(place):
    color = "               "
    if place[2] == "property":
        if place[14] == "br":
            color = "     Brown     "
        elif place[14] == "lb":
            color = "  Light  Blue  "
        elif place[14] == "p":
            color = "     Pink      "
        elif place[14] == "o":
            color = "    Orange     "
        elif place[14] == "r":
            color = "      Red      "
        elif place[14] == "y":
            color = "    Yellow     "
        elif place[14] == "g":
            color = "     Green     "
        elif place[14] == "db":
            color = "   Dark Blue   "
    return color


#function to assign number of houses/hotel on a tile to print the board
def houseAssigner(place):
    status = "               " #if nothing exists or non-buildable tile
    if place[2] == "property":
        if place[13] == 1:
            status = "    1 House    "
        elif place[13] == 2:
            status = "   2 Houses    "
        elif place[13] == 3:
            status = "   3 Houses    "
        elif place[13] == 4:
            status = "   4 Houses    "
        elif place[13] == 5:
            status = "    1 Hotel    "
    return status

#Function to print part of the board in ASCII-art form, with respect to the player's location
def printBoard(player, location): #ASCII-art by Dav Vrat Chadha
    #Assigning tile names to the variable
    #.copy() to create duplicates of the names and not changing the original in the boardTiles during the process of printing them
    tile1 = (boardTiles.copy())[location-2][0] #Two tiles before player's location
    tile2 = (boardTiles.copy())[location-1][0] #One tile before player's location
    tile3 = (boardTiles.copy())[location][0] #Tile on which player is located
    if location > 37:
        tile4 = (boardTiles.copy())[location+1-40][0] #One tile after player's location
        tile5 = (boardTiles.copy())[location+2-40][0] #Two tiles after player's location
        color4 = colorAssigner((boardTiles.copy())[location+1-40])
        color5 = colorAssigner((boardTiles.copy())[location+2-40])
        house4 = houseAssigner((boardTiles.copy())[location+1-40])
        house5 = houseAssigner((boardTiles.copy())[location+2-40])
    else:
        tile4 = (boardTiles.copy())[location+1][0] #One tile after player's location
        tile5 = (boardTiles.copy())[location+2][0] #Two tiles after player's location
        color4 = colorAssigner((boardTiles.copy())[location+1])
        color5 = colorAssigner((boardTiles.copy())[location+2])
        house4 = houseAssigner((boardTiles.copy())[location+1])
        house5 = houseAssigner((boardTiles.copy())[location+2])
        
    color1 = colorAssigner((boardTiles.copy())[location-2])
    color2 = colorAssigner((boardTiles.copy())[location-1])
    color3 = colorAssigner((boardTiles.copy())[location])

    house1 = houseAssigner((boardTiles.copy())[location-2])
    house2 = houseAssigner((boardTiles.copy())[location-1])
    house3 = houseAssigner((boardTiles.copy())[location])
    
    #printing the beginning of the tiles
    print("""
 _______________ _______________ _______________ _______________ _______________
|""" + color1 + """|""" + color2 + """|""" + color3 + """|""" + color4 + """|""" + color5 + """|
|""" + house1 + """|""" + house2 + """|""" + house3 + """|""" + house4 + """|""" + house5 + """|
|---------------|---------------|---------------|---------------|---------------|
|               |               |               |               |               |""")

    #while function to print names of the tiles
    while tile1: #While the tile name exists
        print("|" + tile1[:15] + "|" + tile2[:15] + "|" + tile3[:15] + "|" + tile4[:15] + "|" + tile5[:15] + "|") #Printing the first 15 characters of the names of all tiles
        tile1 = tile1[15:]
        tile2 = tile2[15:]
        tile3 = tile3[15:]
        tile4 = tile4[15:]
        tile5 = tile5[15:]
    print("""|_______________|_______________|_______________|_______________|_______________|
|               |               |  You are here |               |               |
|               |               |       \u2193       |               |               |
|               |               |    """ + player[0] + """    |               |               |
|_______________|_______________|_______________|_______________|_______________|""")
    return


#Function to remove player from the game
def removePlayer(player, playerList):
    for i in range(0, len(boardTiles)):
        tile = ' '.join((boardTiles[i][0]).split()) #This removes all extra white-spaces from the name of the tile
        if boardTiles[i][1] == player[0]: #property owned matches to tile in boardTiles
            boardTiles[i][1] = "bank" #new owner is bank
   #         boardTiles[i][3] = "open" #tile set to open for other players to buy it
            if boardTiles[i][2] == "property": #type of tile is property
                boardTiles[i][13] = 0 #all builings on the tile removed
                #changing owner in colour set list
                if boardTiles[i][14] == "br":
                    brownSet[boardTiles[i][12]][1] = "bank"
                elif boardTiles[i][14] == "lb":
                    lightBlueSet[boardTiles[i][12]][1] = "bank"
                elif boardTiles[i][14] == "p":
                    pinkSet[boardTiles[i][12]][1] = "bank"
                elif boardTiles[i][14] == "o":
                    orangeSet[boardTiles[i][12]][1] = "bank"
                elif boardTiles[i][14] == "r":
                    redSet[boardTiles[i][12]][1] = "bank"
                elif boardTiles[i][14] == "y":
                    yellowSet[boardTiles[i][12]][1] = "bank"
                elif boardTiles[i][14] == "g":
                    greenSet[boardTiles[i][12]][1] = "bank"
                elif boardTiles[i][14] == "db":
                    darkBlueSet[boardTiles[i][12]][1] = "bank"
                    
            elif boardTiles[i][2] == "sanc": #type of tile is a sanctum
                sanctumSet[boardTiles[i][5]][1] = "bank"
            elif boardTiles[i][2] == "util": #type of tile is a dimension
                dimensionSet[boardTiles[i][5]][1] = "bank"
    alive = 0                
    playerList.remove(player) #player removed from playerList
    return alive, player, playerList

#function to determine if someone has one the game
def victoryDeterminer(playerList):
    playersLeft = len(playerList)
    if playersLeft == 1: #If only one player is left
        winner = playerList[0][0]
    elif playersLeft > 1: #if more than one player is left
        winner = "none"
    return winner, playerList

def payRent(player, location, playerList, tile):
    alive = 1 #used in while loop in monopoly function
    winner = "none"
    owner = []
    rent = 0
    location = player[1]
    balance = int(player[2])
    #syntax of lists in playerList: [player name, location, money, jail status(if player in jail: n = no and y = yes), number of turns in Jail, number of JailFreeCards, owned properties...]
    for j in playerList: #To match the owner in playerList
        if str(boardTiles[location][1]) == str(j[0]):
            owner = j #owner of tile
        
    if boardTiles[location][3] == "open" and player[0] != boardTiles[location][1]: #If property is open and player is not the owner
        print("Current Balance(before paying rent) = $" + str(balance))
        cSet = []
        if boardTiles[location][2] == "property" and boardTiles[location][13] == 0: #If type = property and nothing has been built
        #determining set for doubling rent if all tile in the set are bought
            if boardTiles[location][14] == "br":
                cSet  = brownSet
            elif boardTiles[location][14] == "lb":
                cSet  = lightBlueSet
            elif boardTiles[location][14] == "p":
                cSet  = pinkSet
            elif boardTiles[location][14] == "o":
                cSet  = orangeSet
            elif boardTiles[location][14] == "r":
                cSet  = redSet
            elif boardTiles[location][14] == "y":
                cSet  = yellowSet
            elif boardTiles[location][14] == "g":
                cSet  = greenSet
            elif boardTiles[location][14] == "db":
                cSet  = darkBlueSet
                        
        elif boardTiles[location][2] == "sanc": #type of tile is a sanctum
            cSet  = sanctumSet
        elif boardTiles[location][2] == "util": #type of tile is a dimension
            cSet  = dimensionSet

        #to check is all properties are owned by the same person
        counter = 0
        for i in range(0, len(cSet)):
            if cSet[i][1] == owner[0]:
                counter += 1
#    [Tile Name, owner, type, status, price, building cost, defaultRent, 1 house, 2 house, 3 house, 4 house, hotel, colourSet index, currentBuild, code for colour set, buyable tile number]

        if boardTiles[location][2] == "property": #type of tile is property
            if counter == len(cSet) and boardTiles[location][13] == 0: #all properties in the set are owned by the current owner
                rent = 2*boardTiles[location][6] # 2 time default rent because of complete set
                print("You landed at " + owner[0] + "'s property and have to pay rent of $" + str(rent))
            elif counter!=len(cSet) and boardTiles[location][13] == 0:
                rent = boardTiles[location][6] #default rent
                print("You landed at " + owner[0] + "'s property and have to pay rent of $" + str(rent))
            elif boardTiles[location][13] > 0: #If type = property and something has been built
                levelBuildings= boardTiles[location][13] + 6
                rent = boardTiles[location][levelBuildings] #rent according to level of building
                print("You landed at " + owner[0] + "'s property and have to pay rent of $" + str(rent))
            
        elif boardTiles[location][2] == "sanc": #type of tile is a sanctum
            if counter == 1: #rent for 1 sanctum
                rent = 25
                print("You landed at " + owner[0] + "'s property and have to pay rent of $" + str(rent))
            elif counter == 2: #rent for 2 sanctum
                rent = 50
                print("You landed at " + owner[0] + "'s property and have to pay rent of $" + str(rent))
            elif counter == 3: #rent for 3 sanctum
                rent = 100
                print("You landed at " + owner[0] + "'s property and have to pay rent of $" + str(rent))
            elif counter == 4: #rent for 4 sanctum
                rent = 200
                print("You landed at " + owner[0] + "'s property and have to pay rent of $" + str(rent))

        elif boardTiles[location][2] == "util": #type of tile is a dimension
            #rolling dice to determine the rent
            rollAction = "NULL"
            print("You landed at " + owner[0] + "'s property")
            rollAction = input("Press Enter to roll the dice and determine the rent:")
            if rollAction == "":
                time.sleep(.5)
                die1 = dieRoll() #Calling dieRoll function to get a number for first die
                die2 = dieRoll() #Calling dieRoll function to get a number for second die
                rollTotal = die1 + die2
                #print dice in ASCII-art form
                printDice(assignDieASCIIart(die1), assignDieASCIIart(die2))
                print("You rolled " + str(rollTotal))
            elif rollAction != "":
                print("Invalid Input. Thanos got angry and has told you to pay $120.")
                counter = 100
            if counter == 1: #rent for 1 dimension
                rent = 4*rollTotal
                print("You have to pay rent of $" + str(rent))
            elif counter == 2: #rent for 1 dimension
                rent = 10*rollTotal
                print("You have to pay rent of $" + str(rent))
            elif counter == 100:
                rent = 120
                print("You have to pay rent of $" + str(rent))
        if player[2] - rent < 0: #Player does not have enough money
            balance = int(player[2])
            print("You only have $" + str(balance)+ " (before paying the rent)") #printing current balance
            time.sleep(1.5)
            print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
            print("=============================================")
            alive, player, playerList = removePlayer(player, playerList) #player loses
            winner, playerList = victoryDeterminer(playerList)
            owner[2] += rent #owner gets the rent
            return alive, winner, player, location, playerList, tile
        elif player[2] - rent >= 0:
            owner[2] += rent #owner gets the rent
            player, playerList = printRent(rent, player, playerList)

        
            
    elif player[0] == boardTiles[location][1]:#player is the owner
        print("You are the owner of this property.")
    return alive, winner, player, location, playerList, tile

def printRent(rent, player, playerList):
    player[2] -= rent #player pays the rent
    balance = int(player[2])
    print("You paid rent of $" + str(rent))
    print("New Balance = $" + str(balance))
    return player, playerList

#Function to buy a tile
def buyTile(player, location, tile, playerList):
    location = player[1]
    balance = int(player[2])
    print("Current Balance = $" + str(balance))
    tile = ' '.join((boardTiles[location][0]).split()) #This removes all extra white-spaces from the name of the tile
    if (boardTiles[location][2] == "property") or (boardTiles[location][2] == "sanc") or (boardTiles[location][2] == "util"): #if tile can be baught
        cost = boardTiles[location][4] #price of property
        if player[2] >= cost: #if owner is bank and player has sufficient money to buy the property
                #asking if user wannts to buy the property
            print("It is a unowned property. Would you like to buy " + tile + " from the bank? Cost = $" + str(cost))
            ans = input("""Choose from the following options (enter the index):
(1) Yes
(2) No\n""")
            if ans.isdigit():
                ans = int(ans)
                if ans == 1: #player wants to buy the property
                    print("Congratulations!! You are the new owner of this property.\n")
                    boardTiles[location][1] = player[0] #changing owner name
                    player[2] -= cost #deducting cost from player's money
                    balance = int(player[2])
                    print("New Balance = $" + str(balance))
                    player.append(tile) #appending tile name to the list player to add the tile as a bought property
                    if boardTiles[location][2] == "property": #type of tile is property
                        boardTiles[location][13] = 0 #all builings on the tile removed
                        #changing owner in colour set list
                        if boardTiles[location][14] == "br":
                            brownSet[boardTiles[location][12]][1] = player[0]
                        elif boardTiles[location][14] == "lb":
                            lightBlueSet[boardTiles[location][12]][1] = player[0]
                        elif boardTiles[location][14] == "p":
                            pinkSet[boardTiles[location][12]][1] = player[0]
                        elif boardTiles[location][14] == "o":
                            orangeSet[boardTiles[location][12]][1] = player[0]
                        elif boardTiles[location][14] == "r":
                            redSet[boardTiles[location][12]][1] = player[0]
                        elif boardTiles[location][14] == "y":
                            yellowSet[boardTiles[location][12]][1] = player[0]
                        elif boardTiles[location][14] == "g":
                            greenSet[boardTiles[location][12]][1] = player[0]
                        elif boardTiles[location][14] == "db":
                            darkBlueSet[boardTiles[location][12]][1] = player[0]
                            
                    if boardTiles[location][2] == "sanc": #type of tile is a sanctum
                        sanctumSet[boardTiles[location][5]][1] = player[0]
                    elif boardTiles[location][2] == "util": #type of tile is a dimension
                        dimensionSet[boardTiles[location][5]][1] = player[0]
                            
                else: #player doesn't wants/cannot buy the property
                    print("Oops! you lost your chance to buy " + tile + ".")
            else:
                print("Invalid Input!!")
                print("Oops! you lost your chance to buy " + tile + ".")
        elif player[2] < cost: #if owner is bank but player does not have sufficient money to buy the property
                print("You don't have enough money to buy the this tile.")
    return player, location, tile, playerList

def payTax(player, location, playerList, tile):
    alive = 1 #used in while loop in monopoly function
    amount = boardTiles[location][3]
    winner = "none"
    if player[2] - amount < 0: #Player does not have enough money
        print("You have to pay tax of $" + str(amount) + ".")
        balance = int(player[2])
        print("Current Balance = $" + str(balance))
        time.sleep(1.5)
        print("""Because of lack of money, Gullible Thanos snaps you. You lost the battle against Gullible Thanos.
Thank you for playing the game.""")
        print("=============================================")
        alive, player, playerList = removePlayer(player, playerList) #player loses
        winner, playerList = victoryDeterminer(playerList)
        return alive, winner, player, location, playerList, tile
    else:
        player[2] -= amount
        print("Tax of $" + str(amount) + " has been deducted from your account.")
        balance = int(player[2])
        print("New Balance = $" + str(balance))
    return alive, winner, player, location, playerList, tile

#Function to print status of the game
def gameStatus(player, location, playerList, tile):
    #printing headings
    print("\n\nGame status is as follows:\n")
    print("--------------------------------------------------")
    print("Owners based upon sets")
    #printing names of properties and owners in a color set
    print("--------------------------------------------------")
    print("Brown Set:") 
    print("Owner\t\tTile Name")
    for i in brownSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Light Blue Set:") 
    print("Owner\t\tTile Name")
    for i in lightBlueSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Pink Set:") 
    print("Owner\t\tTile Name")
    for i in pinkSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Orange Set:") 
    print("Owner\t\tTile Name")
    for i in orangeSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Red Set:") 
    print("Owner\t\tTile Name")
    for i in redSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Yellow Set:") 
    print("Owner\t\tTile Name")
    for i in yellowSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Green Set:") 
    print("Owner\t\tTile Name")
    for i in greenSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Dark Blue Set:") 
    print("Owner\t\tTile Name")
    for i in darkBlueSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Sanctum Set:") 
    print("Owner\t\tTile Name")
    for i in sanctumSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])

    print("\n--------------------------------------------------")
    print("Dimension Set:") 
    print("Owner\t\tTile Name")
    for i in dimensionSet: #for loop to print all tiles in the set
        print(i[1] + "\t\t" + i[0])
    print("--------------------------------------------------")

    #printing number of houses/hotels buitl on each property
    print("\n\n--------------------------------------------------")
    print("Level of buildings on properties:")
    print("--------------------------------------------------")
    print("Buildings\t\tName of Property")
    #for loop to print data for all properties by searching in boardsTiles list
    for tile1 in boardTiles:
        if tile1[2] == "property":
            name = ' '.join((tile1[0]).split()) #This removes all extra white-spaces from the name of the tile
            if tile1[13] == 1:#if only 1 house
                level = "1 house"
                print(level + "\t\t\t" + name)
            elif tile1[13] < 5:#if only houses but not one
                level = str(tile1[13]) + " houses" #string cocatination
                print(level + "\t\t" + name)
            elif tile1[13] == 5:#if hotel is built
                level = "1 hotel"
                print(level + "\t\t\t" + name)
    print("--------------------------------------------------\n")
                  

    #printing data related to current player
    print("--------------------------------------------------")
    balance = int(player[2])
    print("Money you have = $" + str(balance))
    loc = ' '.join((boardTiles[location][0]).split()) #This removes all extra white-spaces from the name of the tile
    print("\nCurrent location: " + loc)
    if player[1] == 10 and player[3] == "n": #player just visiting jail
        print("Just visting jail")
    if player[1] == 10 and player[3] == "y": #player stuck in jail
        print("Stuck in jail for " + str(player[4]) + " turns.")
    print("\nNumber of JailFreeCards you have = " + str(player[5]))

    print("--------------------------------------------------")
    return player, location, playerList, tile

#funtion to build houses/hotels on properties
def build(player, location, playerList, tile):
    indexList = []#to rule out invalid input while choosing property to build upon
    indexList.clear()
    #printing headings
    print("\n--------------------------------------------------")
    print("Welcome to the Build Station")
    print("--------------------------------------------------")
    balance = int(player[2])
    print("Current Balance = $" + str(balance))
    print("""\nTo build a house/hotel, you need to own full colour set.
Because of Thanos's will, there is no restriction on builing stuff on owned properties.
I.e. you can build as many houses as you want, even on a single property, without building any on others.""")
    print("--------------------------------------------------")
    print("""Follow is the Price Chart for 1 house on the following index:
Index       Cost
1-5         $50
6-11        $100
12-17       $150
18-22       $200""")
    print("--------------------------------------------------\n")
    print("Following are the properties in your complete colour set:\n")
    print("Index\t\tColor\t\tName Of Property")
    print("--------------------------------------------------------")
    counter = 0
    #if-else statements to find available properties to build upon
    if brownSet[0][1] == brownSet[1][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name1 = ' '.join((boardTiles[1][0]).split()) #name of tile as per location on board
        name3 = ' '.join((boardTiles[3][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[1][15]) + "\t\tBrown          \t" + name1) 
        print(str(boardTiles[3][15]) + "\t\tBrown          \t" + name3)
        #appending indices available in the list
        indexList.append(boardTiles[1][15])
        indexList.append(boardTiles[3][15])
        
    if lightBlueSet[0][1] == lightBlueSet[1][1] == lightBlueSet[2][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name6 = ' '.join((boardTiles[6][0]).split()) #name of tile as per location on board
        name8 = ' '.join((boardTiles[8][0]).split()) #name of tile as per location on board
        name9 = ' '.join((boardTiles[9][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[6][15]) + "\t\tLight Blue     \t" + name6)
        print(str(boardTiles[8][15]) + "\t\tLight Blue     \t" + name8)
        print(str(boardTiles[9][15]) + "\t\tLight Blue     \t" + name9)
        #appending indices available in the list
        indexList.append(boardTiles[6][15])
        indexList.append(boardTiles[8][15])
        indexList.append(boardTiles[9][15])

    if pinkSet[0][1] == pinkSet[1][1] == pinkSet[2][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name11 = ' '.join((boardTiles[11][0]).split()) #name of tile as per location on board
        name13 = ' '.join((boardTiles[13][0]).split()) #name of tile as per location on board
        name14 = ' '.join((boardTiles[14][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[11][15]) + "\t\tPink           \t" + name11)
        print(str(boardTiles[13][15]) + "\t\tPink           \t" + name13)
        print(str(boardTiles[14][15]) + "\t\tPink           \t" + name14)
        #appending indices available in the list
        indexList.append(boardTiles[11][15])
        indexList.append(boardTiles[13][15])
        indexList.append(boardTiles[14][15])

    if orangeSet[0][1] == orangeSet[1][1] == orangeSet[2][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name16 = ' '.join((boardTiles[16][0]).split()) #name of tile as per location on board
        name18 = ' '.join((boardTiles[18][0]).split()) #name of tile as per location on board
        name19 = ' '.join((boardTiles[19][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[16][15]) + "\t\tOrange         \t" + name16)
        print(str(boardTiles[18][15]) + "\t\tOrange         \t" + name18)
        print(str(boardTiles[19][15]) + "\t\tOrange         \t" + name19)
        #appending indices available in the list
        indexList.append(boardTiles[16][15])
        indexList.append(boardTiles[18][15])
        indexList.append(boardTiles[19][15])

    if redSet[0][1] == redSet[1][1] == redSet[2][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name21 = ' '.join((boardTiles[21][0]).split()) #name of tile as per location on board
        name23 = ' '.join((boardTiles[23][0]).split()) #name of tile as per location on board
        name24 = ' '.join((boardTiles[24][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[21][15]) + "\t\tRed            \t" + name21)
        print(str(boardTiles[23][15]) + "\t\tRed            \t" + name23)
        print(str(boardTiles[24][15]) + "\t\tRed            \t" + name24)
        #appending indices available in the list
        indexList.append(boardTiles[21][15])
        indexList.append(boardTiles[23][15])
        indexList.append(boardTiles[24][15])

    if yellowSet[0][1] == yellowSet[1][1] == yellowSet[2][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name26 = ' '.join((boardTiles[26][0]).split()) #name of tile as per location on board
        name27 = ' '.join((boardTiles[27][0]).split()) #name of tile as per location on board
        name29 = ' '.join((boardTiles[29][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[26][15]) + "\t\tYellow         \t" + name26)
        print(str(boardTiles[27][15]) + "\t\tYellow         \t" + name27)
        print(str(boardTiles[29][15]) + "\t\tYellow         \t" + name29)
        #appending indices available in the list
        indexList.append(boardTiles[26][15])
        indexList.append(boardTiles[27][15])
        indexList.append(boardTiles[29][15])

    if greenSet[0][1] == greenSet[1][1] == greenSet[2][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name31 = ' '.join((boardTiles[31][0]).split()) #name of tile as per location on board
        name32 = ' '.join((boardTiles[32][0]).split()) #name of tile as per location on board
        name34 = ' '.join((boardTiles[34][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[31][15]) + "\t\tGreen          \t" + name31)
        print(str(boardTiles[32][15]) + "\t\tGreen          \t" + name32)
        print(str(boardTiles[34][15]) + "\t\tGreen          \t" + name34)
        #appending indices available in the list
        indexList.append(boardTiles[31][15])
        indexList.append(boardTiles[32][15])
        indexList.append(boardTiles[34][15])

    if darkBlueSet[0][1] == darkBlueSet[1][1] == player[0]: #player is owner of the complete color set
        counter += 1
        name37 = ' '.join((boardTiles[37][0]).split()) #name of tile as per location on board
        name39 = ' '.join((boardTiles[39][0]).split()) #name of tile as per location on board
        #printing property name with index
        print(str(boardTiles[37][15]) + "\t\tDark Blue      \t" + name37)
        print(str(boardTiles[39][15]) + "\t\tDark Blue      \t" + name39)
        #appending indices available in the list
        indexList.append(boardTiles[37][15])
        indexList.append(boardTiles[39][15])
    print("--------------------------------------------------------")
    
    if counter == 0:
        print("You don't have any complete colour set. Thus, you cannot build.")
        return player, location, playerList, tile
    
    ans9 = input("Type the index of the property you want to build upon, else type '100' to exit Build Station: ")
    if ans9.isdigit():
        ans9 = int(ans9)
        if ans9 == 100:
            print("Command Successful")
            print("Returning back to Command Center...")
            print("--------------------------------------------------")
            time.sleep(1.5)
            return player, location, playerList, tile
        elif indexList.count(ans9) > 0: #Item exists in the list. (It counts how many times an element is there in a list)
            for tile2 in boardTiles:
                if tile2[2] == "property":#type = property
                    if tile2[15] == ans9:#matching tile in the boardTiles
                        if tile2[13] < 5:
                            print("Current build status = " + str(tile2[13]) + " houses.")
                            #asking for user input
                            ans10 = input("How many more houses do you want to add? (Note: number of houses need to be 5 in order to turn it into a hotel\n")
                            if ans10.isdigit():
                                ans10 = int(ans10)
                                if ans10 >= 0: #only positive number allowed
                                    if (ans10 + tile2[13]) > 5:#demand above limit
                                        print("That is above the limit. Command cancelled.")
                                        print("--------------------------------------------------")
                                        return player, location, playerList, tile
                                    elif ans10 == 0:
                                        print("Ok. Exiting the Build Station...")
                                        print("--------------------------------------------------")
                                        return player, location, playerList, tile
                                    else:
                                        cost = ans10*tile2[5] #cost of construction
                                        print("Total cost = $" + str(cost))
                                        ans11 = input("Are you sure? Type 'y' for yes or 'n' for no:")
                                        if (str(ans11)).lower() == "y":
                                            if player[2] - cost < 0: #player does not have enough money
                                                print("You don't have enough money. Command Cancelled.")
                                                print("--------------------------------------------------")
                                                return player, location, playerList, tile
                                            else:#player pays the money
                                                player[2] -= cost 
                                                tile2[13] += ans10 #build level increased
                                                #printing revised data
                                                print("Command Successful!!")
                                                balance = int(player[2])
                                                print("New Balance = $" + str(balance))
                                                if tile2[13] < 5: #only houses exist
                                                    print("Current build status = " + str(tile2[13]) + " houses.")
                                                elif tile2[13] == 5: #hotel exists
                                                    print("Current build status = 1 hotel.")
                                        else:
                                            print("Order Cancelled.")
                                            print("--------------------------------------------------")
                                            return player, location, playerList, tile
                                else:#invaild input
                                    print("Invalid Input")
                                    print("--------------------------------------------------")
                                    return player, location, playerList, tile
                            else:#invaild input
                                    print("Invalid Input")
                                    print("--------------------------------------------------")
                                    return player, location, playerList, tile
                
                            
                        elif tile2[13] == 5:#hotel already exists
                            print("Current build status = 1 hotel. Nothing more can be built here.")
                            print("--------------------------------------------------")
                            return player, location, playerList, tile
        else:
            print("Invalid Input")
            print("--------------------------------------------------")
            return player, location, playerList, tile
    else:
        print("Invalid Input")
        print("--------------------------------------------------")
        return player, location, playerList, tile
    
    return player, location, playerList, tile

#["     Xandar                   ", "bank", "property", "open", 200, 100, 16, 80, 200, 600, 800, 1000, 2, 0, "o"],
#[Tile Name, owner, type, status, price, building cost, defaultRent, 1 house, 2 house, 3 house, 4 house, hotel, colourSet index, currentBuild, code for colour set]
#[Player, 0, 2500, "n", 0, 0]
#[player name, location, money, jail status(if player in jail: n = no and y = yes), number of turns in Jail, number of JailFreeCards, owned properties...]


#function to buy tiles form other players
def trade(player, location, playerList, tile):
    winner = "none"
    returnValue = 0 #money the previous owner gets back
    totalValue = 0
    alive = 1 #used in while loop in monopoly function
    color = "               "
    payment = 0
    indexList2 = []#to rule out invalid input while choosing property to trade
    indexList2.clear()
    origValue = 0 #originalvalue of the property
    currBuildStatus = 0#code to show can't build
    returnValue = 0
    newBuildStatus = 0
    #printing heading
    print("\n--------------------------------------------------")
    print("Trade Center")
    print("--------------------------------------------------")
    balance = int(player[2])
    print("Current balance = $" + str(balance))
    print("During trade, the new owner gets the property with all houses/hotel removed. The previous owner gets half of the building cost back.")
    print("""Trading only one property of a color set, will FREEZE (and not REMOVE) the buildings on any other property of the same color set.
To continue the building process, you must aquire complete color set.""")
    print("\nFollowing is the list of properties that are owned by other players:\n")
    print("Owner\t\tIndex\t\tColor\t\tName")
    print("-----------------------------------------------------------------------")
    counter = 0#counting number of available properties
    for prop in boardTiles: #for loop to print all buyable properties owned by other players 
        if prop[1] != "bank" and prop[1] != "spl" and prop[1] != player[0]:#if buyable tile not owned by current player or bank
            if prop[2] == "property": #if tile is a property
                name = ' '.join((prop[0]).split()) #This removes all extra white-spaces from the name of the tile
                color = ' '.join((colorAssigner(prop)).split())#printing color of the tile
                if len(color) < 15:#for proper allignment, width of color name = 15 characters
                    numSpaces = 15 - len(color) #num of addition characters
                    for i in range(numSpaces):
                        color += " " #adding additing characters to reach proper width
                owner = prop[1]
                index = prop[15]
                print(owner + "\t\t" + str(index) + "\t\t" + color + "\t" + name) #printing data
                indexList2.append(index)
                counter += 1
            elif prop[2] == "util" or prop[2] == "sanc": #if tile is a dimension or sanctum
                name = ' '.join((prop[0]).split()) #This removes all extra white-spaces from the name of the tile
                owner = prop[1]
                index = prop[7]
                color = "               "
                print(owner + "\t\t" + str(index) + "\t\t" + color + "\t" + name) #printing data
                indexList2.append(index)
                counter += 1

    print("--------------------------------------------------")
    #asking for user input
    if counter > 0: #some tiles are avialable
        ans5 = input("To buy a property, enter it's index value else enter '100' to exit Trade Center: ")
        if ans5.isdigit():
            ans5 = int(ans5)
            if ans5 == 100:
                print("Command Successful")
                print("Returning back to Command Center...")
                print("----------------------------------------------------------------")
                time.sleep(1.5)
                winner, playerList = victoryDeterminer(playerList)
                return alive, player, location, playerList, tile, winner
            elif ans5 < 29 and ans5 > 0 and indexList2.count(ans5) > 0:
                ind = 0
                for props in boardTiles:
                    if props[2] == "property": #if tile is a property
                        ind = props[15]
                        origValue = props[4] #originalvalue of the property
                        currBuildStatus = props[13]#code to show can't build
                        returnValue = props[13]*props[5]/2 #money the previous owner gets back
                    elif props[2] == "util" or props[2] == "sanc": #if tile is a dimension or sanctum
                        ind = props[7]
                        origValue = props[4] #originalvalue of the property
                        currBuildStatus = 1000#code to show can't build
                        returnValue = 0
                               
                    if ind == ans5: #tile index matched
                        ans6 = input("Enter money value you are willing to pay (Must be greater than 0): ")
                        if ans6.isdigit():
                            ans6 = int(ans6)
                            if ans6 > 0 and player[2] - ans6 < 0:#player does not have enough money
                                print("""Because of lack of money, Gullible Thanos snaps you. You lost the battle against Gullible Thanos.
Thank you for playing the game.""")
                                print("=============================================")
                                alive, player, playerList = removePlayer(player, playerList) #player loses
                                winner, playerList = victoryDeterminer(playerList)
                                return alive, player, location, playerList, tile, winner
                            
                            elif ans6 > 0 and player[2] - ans6 >= 0:#player has enough money as much entered
                                payment = ans6
                                print("\nData for " + props[1] + ":")
                                print("Original Value of the property = $" + str(origValue))
                                if currBuildStatus == 1000:
                                    totalValue = returnValue + ans6
                                    print("Nothing can be built on this property")
                                    print("Total Value you will get for this Property = $" + str(int(totalValue)))
                                elif currBuildStatus == 1:
                                    print("1 House is built on this property.")
                                    print("Return value of the building = $" + str(int(returnValue)))
                                    totalValue = returnValue + ans6
                                    print("Total Value you will get for this Property = $" + str(int(totalValue)))
                                elif currBuildStatus < 5:
                                    print(str(currBuildStatus) + " Houses are built on this property.")
                                    print("Return value of the building = $" + str(int(returnValue)))
                                    totalValue = returnValue + ans6
                                    print("Total Value you will get for this Property = $" + str(int(totalValue)))
                                elif currBuildStatus == 5:
                                    print("1 Hotel is built on this property.")
                                    print("Return value of the building = $" + str(int(returnValue)))
                                    totalValue = returnValue + ans6
                                    print("Total Value you will get for this Property = $" + str(int(totalValue)))
                                print("")
                                
                                #asking for owner's input
                                ans7 = input(props[1] + """, do you agree to this offer?
Choose from the following options (enter option number):
(1) Yes
(2) No\n""")
                                if ans7.isdigit():
                                    ans7 = int(ans7)
                                    if ans7 == 1: #owner agrees to sell the the tile
                                        for k in playerList: #for loop to pay the owner
                                            if k[0]  == props[1]: #owner matched
                                                oldPlayerBalance = int(player[2])
                                                oldOwnerBalance = int(k[2])
                                                print("Former Owner's old Balance = $" + str(oldOwnerBalance))
                                                print("Current player's old Balance = $" + str(oldPlayerBalance))
                                                if props[2] == "util" or props[2] == "sanc": #if tile is a dimension or sanctum
                                                    player[2] -= totalValue #player pays the money
                                                    newBuildStatus = 0
                                                elif props[2] == "property": #if tile is a dimension or sanctum
                                                    player[2] -= payment #player pays the money
                                                    props[13] = 0 #all buildings removed
                                                    newBuildStatus = props[13]
                                                k[2] += totalValue #owner paid the money
                                                newPlayerBalance = int(player[2])
                                                newOwnerBalance = int(k[2])
                                                print("")
                                                print("Former Owner's new Balance = $" + str(newOwnerBalance))
                                                print("Current player's new Balance = $" + str(newPlayerBalance))
                                                print("Build Status on the property = " + str(newBuildStatus) + " houses")
                                        props[1] = player[0] #ownership transfer
                                        #changing ownership in tile sets
                                        if props[2] == "property": #If type = property
                                            if props[14] == "br":
                                                cSet  = brownSet
                                            elif props[14] == "lb":
                                                cSet  = lightBlueSet
                                            elif props[14] == "p":
                                                cSet  = pinkSet
                                            elif props[14] == "o":
                                                cSet  = orangeSet
                                            elif props[14] == "r":
                                                cSet  = redSet
                                            elif props[14] == "y":
                                                cSet  = yellowSet
                                            elif props[14] == "g":
                                                cSet  = greenSet
                                            elif props[14] == "db":
                                                cSet  = darkBlueSet
                                                        
                                        elif props[2] == "sanc": #type of tile is a sanctum
                                            cSet  = sanctumSet
                                        elif props[2] == "util": #type of tile is a dimension
                                            cSet  = dimensionSet
                                        namePrime = ' '.join((props[0]).split()) #This removes all extra white-spaces from the name of the tile
                                        for x in cSet:
                                            if namePrime == x[0]:#property matched in set
                                                x[1] = player[0] #owner changed
                                        print("Offer Completed!! Ownership has been transferred.")
                                        print("--------------------------------------------------")
                                        return alive, player, location, playerList, tile, winner
                                    else:
                                        print("Invalid Input.")
                                        print("=====================================")
                                        return alive, player, location, playerList, tile, winner
                                else:
                                    print("Offer rejected.")
                                    print("=====================================")
                                    return alive, player, location, playerList, tile, winner
                        else:
                            print("Invalid Input.")
                            print("=====================================")
                            return alive, player, location, playerList, tile, winner
                else:
                    print("""Because of invalid input, Gullible Thanos snaps you. You lost the battle against Gullible Thanos.
Thank you for playing the game.""")
                    print("=============================================")
                    alive, player, playerList = removePlayer(player, playerList) #player loses
                    winner, playerList = victoryDeterminer(playerList)
                    return alive, player, location, playerList, tile, winner
            else:
                print("""Because of invalid input, Gullible Thanos snaps you. You lost the battle against Gullible Thanos.
Thank you for playing the game.""")
                print("=============================================")
                alive, player, playerList = removePlayer(player, playerList) #player loses
                winner, playerList = victoryDeterminer(playerList)
                return alive, player, location, playerList, tile, winner
        else:
            print("""Because of invalid input, Gullible Thanos snaps you. You lost the battle against Gullible Thanos.
Thank you for playing the game.""")
            print("=============================================")
            alive, player, playerList = removePlayer(player, playerList) #player loses
            winner, playerList = victoryDeterminer(playerList)
            return alive, player, location, playerList, tile, winner
        
    else: #no tile is available for trade
        print("No tile is available for trade.")
    return alive, player, location, playerList, tile, winner


    
#Function to take action based upon the location and user's input
def action(player, location, playerList, tile):
    winner = "none"
    chCounter = 0
    ccCounter = 0
    usedCP = "no" #player has not used  the Control Panel(options to check status, build, or trade, that are below)
    alive = 1 #used in while loop in monopoly function
    if player[1] == 30:#player at GoToJail Tile
        player[1] = 10 #location = jail
        location = player[1]
        player[3] = "y" #player put in jail
        print("You are put in Jail.")
        printBoard(player, location)
        
        
    elif boardTiles[location][1] == "bank": #Player can buy the property
        player, location, tile, playerList = buyTile(player, location, tile, playerList)

    elif boardTiles[location][1] == "spl": #Tile is special I.e. Tax, jail or parking
        if boardTiles[location][2] == "tax": #player has to pay tax
            alive, winner, player, location, playerList, tile = payTax(player, location, playerList, tile)
            if alive == 0:
                winner, playerList = victoryDeterminer(playerList)
                return alive, winner, player, location, playerList, tile
        elif boardTiles[location][2] == "jail" and player[3] == "n":#player is just visiting the jail
            print("You are just visiting the jail")
        elif boardTiles[location][2] == "parking":#player is at parking
            print("You are in free parking.")
        elif boardTiles[location][2] == "ccCard":#player picks Community Chest card
            alive, winner, usedCP, player, location, playerList, tile = communityChest(player, location, playerList, tile)
            ccCounter += 1
            if alive == 0:
                winner, playerList = victoryDeterminer(playerList)
                return alive, winner, player, location, playerList, tile
        elif boardTiles[location][2] == "chCard":#player picks Chance card
            alive, winner, usedCP, player, location, playerList, tile = chance(player, location, playerList, tile)
            chCounter += 1
            if alive == 0:
                winner, playerList = victoryDeterminer(playerList)
                return alive, winner, player, location, playerList, tile
    elif boardTiles[location][1] != "spl": #if owner is another player
        alive, winner, player, location, playerList, tile = payRent(player, location, playerList, tile)
        if alive == 0:
                winner, playerList = victoryDeterminer(playerList)
                return alive, winner, player, location, playerList, tile
    flag5 = True
    while flag5 and usedCP == "no": #player did not get Chance or Community Chest cards because of which he did not get to access the control panel
        #usedCP is being used to avoid player from using control panel twice
        #following options are Control Panel
        print("\n----------------------------------------------")
        print("Command Center")
        print("----------------------------------------------\n")
        ans4 = input("""\nWhat would you like to do?
Choose from the following option (index of choice):
(1) Show game status (money you have, properties, colour sets etc.)
(2) Build houses/hotels
(3) Trade
(4) No, Thank You. I would like to pass\n""")
        if ans4.isdigit():
            ans4 = int(ans4)
            if ans4 == 1:
                player, location, playerList, tile = gameStatus(player, location, playerList, tile)
            elif ans4 == 2:
                player, location, playerList, tile = build(player, location, playerList, tile)
            elif ans4 == 3:
                alive, player, location, playerList, tile, winner = trade(player, location, playerList, tile)
                if alive == 0:
                    flag5 = False
                if winner != "none":
                    return alive, winner, player, location, playerList, tile
            elif ans4 == 4:
                print("Ok. Next Turn")
                flag5 = False
            else:
                print("Invaild input")
        else:
            print("Invaild input")
    return alive, winner, player, location, playerList, tile



#function to control the game
def monopoly():
    winner = "none"
    flag = True #Used for while loop in the game
    playerList = []#list of players in game
    numPlayers = input("Please enter the number of player(atleast 2 required): ")
    if numPlayers.isdigit():
        numPlayers = int(numPlayers)
        if numPlayers > 1:
            for num in range(1, numPlayers + 1):
                playerName = "Player" + str(num)
                #syntax of lists in playerList: [player name, location, money, jail status(if player in jail: n = no and y = yes), number of turns in Jail, number of JailFreeCards, owned properties...]
                playerList.append([playerName, 0, 2500, "n", 0, 0])
            print("You and your friends have got high-tech spaceships to travel from one place to another at speed of light. Best Of Luck!!\n")
            print("=================================================")
        else:
            print("Invalid Input.")
            time.sleep(1.5)
            print("Game shuting down.")
            flag = False
    else:
        print("Invalid Input.")
        time.sleep(1.5)
        print("Game shuting down.")
        flag = False
        
    while flag:
        for player in playerList: #for each player
            print (player[0] + "'s turn")
            flag2 = True
            alive = 1 #used in while loop in monopoly function
            winner = "none" #no one has one the gaem yet
            doubleCounter = 0 #used for counting number of double rolls in one turn
            if winner != "none":
                return winner

            if player[3] == "y": #if player is in Jail
                player[1] = 10
                location = player[1]
                balance = int(player[2])
                print("Current Balance = $" + str(balance))
                print("Number of JailFreeCards you have = " + str(player[5]))
                #asking player what they want to do to get out of jail
                flag7 = True
                while flag7:
                    ans3 = input("""You are in Jail. You will be getting you options on every turn in jail.
There are 3 ways to get out. Choose from the folloing options (index of choice):
(1) Pay $50
(2) JailFreeCard
(3) Wait 3 turns and pay then pay $50, or roll a double to get out.
(Note the double number rolled will not be considered as your steps moved.)\n""")
                    if str(ans3) == "1" or str(ans3) == "2" or str(ans3) == "3":
                        flag7 = False
                    else:
                        print("Invalid input. Because of Thanos's generosity, you get another try for this question.")
                if ans3.isdigit():
                    ans3 = int(ans3)
                    if ans3 == 1:#player want to pay $50
                        print("")
                        if player[2] - 50 < 0:#player doesn't have enough money
                            print("You don't have enough money. That was a wrong move!")
                            print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
                            print("=============================================")
                            alive, player, playerList = removePlayer(player, playerList) #player loses
                            winner, playerList = victoryDeterminer(playerList)
                        else:#player pays and gets out
                            print("You paid $50 and are out of jail.")
                            player[2] -= 50 #paying fee
                            balance = int(player[2])
                            print("New Balance = $" + str(balance))
                            player[3] = "n" #player no longer in jail
                            player[4] = 0 #player no longer in jail
                    elif ans3 == 2:#player wants to use JailFreeCard
                        print("")
                        if player[5] == 0:#player doesn't have any JailFreeCards
                            print("You don't have any JailFreeCards. That was a wrong move!")
                            print("Because of your wrong move, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
                            print("=============================================")
                            alive, player, playerList = removePlayer(player, playerList) #player loses
                            winner, playerList = victoryDeterminer(playerList)
                        else:#player uses card and gets out
                            print("You used you card and are out of jail.")
                            player[5] -= 1 #using card
                            print("New number of JailFreeCards = " + str(player[5]))
                            player[3] = "n" #player no longer in jail
                            player[4] = 0 #player no longer in jail
                    elif ans3 == 3:#player wants to take 3 turns and try to roll a double
                        print("")
                        player[4] += 1
                        if player[4] < 4:
                            print("Try " + str(player[4]) + " to get out of jail.")
                            rollAction = input("Press Enter to roll the dice.\n")
                            if rollAction == "":
                                time.sleep(.5)
                                die1 = dieRoll() #Calling dieRoll function to get a number for first die
                                die2 = dieRoll() #Calling dieRoll function to get a number for second die
                                #print dice in ASCII-art form
                                printDice(assignDieASCIIart(die1), assignDieASCIIart(die2))
                                if die1 == die2: #if a double is rolled, player gets out of the jail
                                    print("Congrats!! It's your lucky day. You rolled a double and got out of the Jail.")
                                    player[3] = "n" #player no longer in jail
                                    player[4] = 0 #player no longer in jail
                                else:#if not a double
                                    print("It's not a double. Better luck next time.")
                                if player[4] < 3:#first two tries
                                    alive, winner, player, location, playerList, tile = action(player, location, playerList, tile) #Things that can be done while in jail
                                    if winner != "none":
                                        return winner
                                    flag2 = False
                                    print("============================================")
                            else:
                                print("Invalid Input. You lost the turn.")
                                print("============================================")
                        if player[4] == 3:#after 3rd try
                            print("3 tries are over. You have to pay $50 to get out.")
                            time.sleep(2)
                            if player[2] - 50 < 0:#player doesn't have enough money
                                balance = int(player[2])
                                print("Current balance = $" + str(balance))
                                print("You don't have enough money.")
                                print("Because of lack of money, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
                                print("=============================================")
                                alive, player, playerList = removePlayer(player, playerList) #player loses
                                winner, playerList = victoryDeterminer(playerList)
                            else:#player pays and gets out
                                print("You paid $50 and are out of jail.")
                                player[2] -= 50 #paying fee
                                balance = int(player[2])
                                print("New Balance = $" + str(balance))
                                player[3] = "n" #player no longer in jail
                                player[4] = 0 #player no longer in jail
                    else: #invalid input
                        print("Wrong answer!!")
                        print("Because of your mistake, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
                        print("=============================================")
                        alive, player, playerList = removePlayer(player, playerList) #player loses
                        winner, playerList = victoryDeterminer(playerList)
                    
                else: #invalid input
                    print("Wrong answer!!")
                    print("Because of your mistake, Gullible Thanos snaps you and you lose. Thank you for playing the game.")
                    print("=============================================")
                    alive, player, playerList = removePlayer(player, playerList) #player loses
                    winner, playerList = victoryDeterminer(playerList)
            
            while flag2 and alive and player[3] == "n" and winner == "none": #player alive and not in jail and no one has won the game             
                rollAction = "NULL"
                rollAction = str(input("Press Enter to roll the dice.\n"))
                if rollAction == "":
                    time.sleep(.5)
                    die1 = dieRoll() #Calling dieRoll function to get a number for first die
                    die2 = dieRoll() #Calling dieRoll function to get a number for second die
                    rollTotal = die1 + die2
   #                 rollTotal = 9
                    #print dice in ASCII-art form
                    printDice(assignDieASCIIart(die1), assignDieASCIIart(die2))
                    player[1] += rollTotal #modifying player location in playerList
                    
                    if player[1] > 39: #If a round is completed, (39 because board only consists of tiles with coordinates from 0 to 39)
                        player[1] -= 40 #subtracting 40 to correct the location coordinate
                        player[2] += 200 #addind $200 to player's money balance
                        print("You passed on GO and collected $200")
                    location = player[1]
                    tile = ' '.join((boardTiles[location][0]).split()) #This removes all extra white-spaces from the name of the tile
                    print("You rolled a " + str(rollTotal) + " and landed at " + tile)
                    time.sleep(.8)
                    printBoard(player, location) #printing board to display current location
                    
                    if die1 == die2: #if roll is a double
                        doubleCounter += 1
                        if doubleCounter > 2: #if double is rolled more than twice in a single turn, person sent to jail
                            print("You rolled double for 3 times in a single turn. You are sent directly to Jail.")
                            flag2 = False
                            player[1] = 10 #Location = Jail
                            location = player[1]
                            player[3] = "y" #Person in Jail = Yes
                            time.sleep(1.5)
                            printBoard(player, location)
                            alive, winner, player, location, playerList, tile = action(player, location, playerList, tile)
                            if winner != "none":
                                return winner
                            print("==============================================")
                            
                        elif doubleCounter < 3 and player[3] == "n" and winner == "none": #less than 3 doubles rolled and person not sent to jail, and no one has won the game
                            if player[1] == 30:#player at GoToJail Tile
                                player[1] = 10 #location = jail
                                location = player[1]
                                player[3] = "y" #player put in jail
                                print("You are put in Jail.")
                                printBoard(player, location)
                            elif boardTiles[location][1] == "bank" and boardTiles[location][2] != "parking": #bank is current owner
                                player, location, tile, playerList = buyTile(player, location, tile, playerList)
                            elif boardTiles[location][1] == "spl": #Tile is special I.e. Tax, jail or parking
                                if boardTiles[location][2] == "tax": #player has to pay tax
                                    alive, winner, player, location, playerList, tile = payTax(player, location, playerList, tile)

                                elif boardTiles[location][2] == "ccCard":
                                    alive, winner, usedCP, player, location, playerList, tile = communityChest(player, location, playerList, tile)
                                elif boardTiles[location][2] == "chCard":#player picks Chance card
                                    alive, winner, usedCP, player, location, playerList, tile = chance(player, location, playerList, tile)
                            elif boardTiles[location][1] != "spl": #another player is current owner
                                alive, winner, player, location, playerList, tile = payRent(player, location, playerList, tile)

                            if winner != "none":
                                return winner
                            elif player[3] == "y" or alive == 0:#person in jail or someone one the game
                                flag2 = False
                                print("==============================================")
                            elif player[3] == "n" and winner == "none" and alive == 1:
                                print("It was a double roll. You will get another turn.")
                            
                    else: #if not a double
                        alive, winner, player, location, playerList, tile = action(player, location, playerList, tile)
                        if winner != "none":
                            return winner
                        flag2 = False
                        doubleCounter = 0 #setting equal to zero for next player's turn
                        print("============================================")
                    

                elif rollAction == "quit": #cheat code to remove player from game and restart the turn cycle
                    alive, player, playerList = removePlayer(player, playerList) #player loses
                    winner, playerList = victoryDeterminer(playerList)
                    print("============================================")
                    if winner != "none": #if someone is the winner
                        return winner
                elif rollAction == "dvcisking": #cheat code to win directly
                    winner = player[0]
                    print("============================================")
                    return winner
                else: #If player gives a invalid input
                    print("Invalid Input")
                    time.sleep(1.5)
                    print("You lose the turn!")
                    print("============================================")
                    flag2 = False
        if winner != "none":
            flag = False
    return winner

#function to start the game
def game():
    #printing the storyline
    print("Welcome to Avenger's Monopoly.")
    time.sleep(1.5) #to create delay and add suspense to the game
    print("Few years after Tony Stark's death, scientists discovered a way to travel into alternate dimensions by building Cross-Dimension Bridges.")
    time.sleep(5)
    print("""By misusing this technology, one scientist, who was actually HYDRA'S agent in disguise, summons Thanos from the alternate
dimension, while all avengers are either busy or away. So, the protection of Earth is your responsibility.""")
    time.sleep(5)
    print("Being from an alternate dimension, this Thanos is gullible, but still cruel.")
    time.sleep(4)
    print("He is fond of Monopoly game and has brought one to play.")
    time.sleep(4)
    print("Because of your clever talk, Thanos has agreed to grant a wish to the winner.")
    time.sleep(4)
    print("Your friends' and your task is to win the game and ask Gullible Thanos to snap himself.")
    print("******************************************************")
    time.sleep(4)
    #printing the rules
    print("""Rules:
1) Thanos is the banker.
2) You begin with $2500. The currency of the game is 'Galacto' (represented by $), the most valuable currency in the entire Cosmos.
3) Thanos believes that only he can be the destroyer. So, option of destroying/removing houses and mortgaging property does not exist in this game.
4) This Monopoly needs to be played VERY SERIOUSLY!! One WRONG move and you are DEAD.
5) Lack of money, or even the Chance and Community Chest cards can make you lose and remove you from the game.
6) You can buy other players' properties by using Trade option. But, you cannot sell yours until someone else asks for it in their turn.
7) Whenever someone dies or is removed from the game, the turn might go to any person, depending on Thanos's decision!
8) If you make a mistake in inputting a value(I.e. give Invalid Input), killing you or not is Thanos's decision!

Play Wisely!""")
    time.sleep(10)
    #asking for user input
    ans4 = input("""Do you agree to the Rules/Terms set by Thanos and agree to risk your life to play?
Choose from the following options (index of choice):
(1) Yes
(2) No\n""")
    if ans4.isdigit():
        ans4 = int(ans4)
        if ans4 == 1: #if player wants to play
            winner = monopoly()
            if winner != "none":
                print("""******************************************************
******************************************************
Congratulations """ + winner + """!! You have proven yourself as the best Avenger Monopoly player in the entire cosmos.
Gullible Thanos is happy from you and as promised, agreed to grant a wish of yours with his Infinity Gauntlet.
You ask Thanos to snap himself and bring back other players he killed, and he does so.
The Cosmos is again safe from another Dimension's Thanos.
You have won the game.


P.S. You are worthy enough to finally lift Thor's Stormbreaker!!""")
            
        else: #player does not want to play
            print("That was wrong choice. Thanos snaps you and is the ruler of the entire cosmos.")
    else: #player does not want to play
            print("Invalid Input. Thanos snaps you and is the ruler of the entire cosmos.")

    print("""\n******************************************************
Thank You for playing Avenger's Monopoly, a project of DVC\u2122 GAMES Enterprice.
******************************************************""")
    return


game()#this is where game actually starts
#winner = monopoly()

#print(winner + " is the winner!!")
