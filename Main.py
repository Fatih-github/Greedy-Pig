import random
# ---- ALLE VARIABELEN ----
small = set("abcdefghijklmnopqrstuvwxyz ")
big = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
weird = set("!@#$%^&*()/\[]+-_=")
small_big = small.union(big)
allPlayers = []
nrBeurt = 0

p1_safescore = 0
p2_safescore = 0
p3_safescore = 0
p4_safescore = 0
p5_safescore = 0
p6_safescore = 0

p1_unsafescore = 0
p2_unsafescore = 0
p3_unsafescore = 0
p4_unsafescore = 0
p5_unsafescore = 0
p6_unsafescore = 0
gameChoices = {'1', '2'}

rolled_number = 0

# ---- ALL FUNCTIONS ----

def roll():
    global rolled_number
    rolled_number = random.randint(1,6)

def play():
    print('Current player: ' + current_player)
def totalSafeScore(num):
    if num == 2:
        print(str(player_1) + " = " + str(p1_safescore))
        print(str(player_2) + " = " + str(p2_safescore))
    elif num == 3:
        print(str(player_1) + " = " + str(p1_safescore))
        print(str(player_2) + " = " + str(p2_safescore))
        print(str(player_3) + " = " + str(p3_safescore))
    elif num == 4:
        print(str(player_1) + " = " + str(p1_safescore))
        print(str(player_2) + " = " + str(p2_safescore))
        print(str(player_3) + " = " + str(p3_safescore))
        print(str(player_4) + " = " + str(p4_safescore))
    elif num == 5:
        print(str(player_1) + " = " + str(p1_safescore))
        print(str(player_2) + " = " + str(p2_safescore))
        print(str(player_3) + " = " + str(p3_safescore))
        print(str(player_4) + " = " + str(p4_safescore))
        print(str(player_5) + " = " + str(p5_safescore))
    elif num == 6:
        print(str(player_1) + " = " + str(p1_safescore))
        print(str(player_2) + " = " + str(p2_safescore))
        print(str(player_3) + " = " + str(p3_safescore))
        print(str(player_4) + " = " + str(p4_safescore))
        print(str(player_5) + " = " + str(p5_safescore))
        print(str(player_6) + " = " + str(p6_safescore))
def gameChoice():
    global choice
    choice = str(input("please choose the mode of game: '1': Beginners or '2' Advanced   Make your choice --- "))
    if choice not in gameChoices:
        print("\n" + str(choice) + " is not '1' or '2'. Please try again!\n")
        gameChoice()
    return choice
def checkName():
    for letter in (p1_set,p2_set,p3_set,p4_set,p5_set,p6_set):
        if set(letter).issubset(small_big):
            return True
        else:
            print("Use lower and uppercase letter only")
            playerNames()
def currentPlayer():
    print("Current player: " + str(allPlayers[nrBeurt]))
def playerNames():
    global p1_set, p2_set, p3_set, p4_set, p5_set, p6_set, player_1, player_2, player_3, player_4, player_5, player_6
    if players == 2:
        player_1 = str(input("Enter the name of player 1: "))
        player_2 = str(input("Enter the name of player 2: "))
        p1_set = set(player_1)
        p2_set = set(player_2)
        p3_set = set('a')
        p4_set = set('a')
        p5_set = set('a')
        p6_set = set('a')
        allPlayers.append(player_1)
        allPlayers.append(player_2)
        checkName()
    elif players == 3:
        player_1 = str(input("Enter the name of player 1: "))
        player_2 = str(input("Enter the name of player 2: "))
        player_3 = str(input("Enter the name of player 3: "))
        p1_set = set(player_1)
        p2_set = set(player_2)
        p3_set = set(player_3)
        p4_set = set('a')
        p5_set = set('a')
        p6_set = set('a')
        allPlayers.append(player_1)
        allPlayers.append(player_2)
        allPlayers.append(player_3)
        checkName()
    elif players == 4:
        player_1 = str(input("Enter the name of player 1: "))
        player_2 = str(input("Enter the name of player 2: "))
        player_3 = str(input("Enter the name of player 3: "))
        player_4 = str(input("Enter the name of player 4: "))
        p1_set = set(player_1)
        p2_set = set(player_2)
        p3_set = set(player_3)
        p4_set = set(player_4)
        p5_set = set('a')
        p6_set = set('a')
        allPlayers.append(player_1)
        allPlayers.append(player_2)
        allPlayers.append(player_3)
        allPlayers.append(player_4)
        checkName()
    elif players == 5:
        player_1 = str(input("Enter the name of player 1: "))
        player_2 = str(input("Enter the name of player 2: "))
        player_3 = str(input("Enter the name of player 3: "))
        player_4 = str(input("Enter the name of player 4: "))
        player_5 = str(input("Enter the name of player 5: "))
        p1_set = set(player_1)
        p2_set = set(player_2)
        p3_set = set(player_3)
        p4_set = set(player_4)
        p5_set = set(player_5)
        p6_set = set('a')
        allPlayers.append(player_1)
        allPlayers.append(player_2)
        allPlayers.append(player_3)
        allPlayers.append(player_4)
        allPlayers.append(player_5)
        checkName()
    elif players == 6:
        player_1 = str(input("Enter the name of player 1: "))
        player_2 = str(input("Enter the name of player 2: "))
        player_3 = str(input("Enter the name of player 3: "))
        player_4 = str(input("Enter the name of player 4: "))
        player_5 = str(input("Enter the name of player 5: "))
        player_6 = str(input("Enter the name of player 6: "))
        p1_set = set(player_1)
        p2_set = set(player_2)
        p3_set = set(player_3)
        p4_set = set(player_4)
        p5_set = set(player_5)
        p6_set = set(player_6)
        allPlayers.append(player_1)
        allPlayers.append(player_2)
        allPlayers.append(player_3)
        allPlayers.append(player_4)
        allPlayers.append(player_5)
        allPlayers.append(player_6)
        checkName()
def totalPlayers():
    global players
    playersnum = str(input("please enter the number of players (2-6): "))
    for i in playersnum:
        if set(i).issubset(small_big) or set(i).issubset(weird):
            print("Wrong amount of players. Please choose from 2 to 6 players!")
            totalPlayers()
    players = int(playersnum)
    if players < 2 or players > 6:
        print("Wrong amount of players. Please choose from 2 to 6 players!")
        totalPlayers()
    else:
        playerNames()

p1_beurt = 1
def win(speler):
    if choice == '1':
        if p1_safescore >= 50:
            print("you won " + str(speler))
            exit()
    elif choice == '2':
        if p1_safescore >= 100:
            print("you won " + str(speler))
            exit()

def speler_1():
    global p1_unsafescore, p1_beurt, p1_safescore, p2_unsafescore, p2_beurt
    some = True
    if p1_beurt == 1:
        print("Your current score at this turn: " + str(p1_unsafescore) + "\n\n" + str(player_1) +  " your first dice at this turn will be automaticly rolled\n\nReady?\n\n")
        while some:
            p1_unsafescore = 0
            input("Press enter to continue")
            roll()
            print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
            if rolled_number == 1:
                print("Oops! You lose " + str(p1_unsafescore) + " but still keep your previous " + str(p1_safescore))
                p1_unsafescore = 0
                print("-----------------------------------------\n TOTAL SAFE SCORES")
                totalSafeScore(players)
                print("-----------------------------------------")
                print("Current player: " + str(allPlayers[nrBeurt]))
                print("Your current score at this turn: " + str(p1_unsafescore))
                some = False
                p2_unsafescore = 0
                p2_beurt = 1
                speler_2()
            elif rolled_number != 1:
                while True:
                    p1_unsafescore = 0
                    while True:
                        print("new collected score = " + str(p1_unsafescore) + " + " + str(rolled_number) + " = " + str(p1_unsafescore + rolled_number))
                        p1_unsafescore = p1_unsafescore + rolled_number
                        print("-----------------------------------------\n TOTAL SAFE SCORES")
                        totalSafeScore(players)
                        print("-----------------------------------------")
                        print("Current player: " + str(allPlayers[nrBeurt]))
                        print("Your current score at this turn: " + str(p1_unsafescore) + "\n")
                        print("\n")
                        input("Press enter to continue")
                        print("\n")
                        some = False
                        again = str(input(str(player_1) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                        if again == 'r':
                            p1_beurt = p1_beurt + 1
                            speler_1()
                        elif again == 'p':
                            p1_safescore = p1_safescore + p1_unsafescore
                            p2_unsafescore = 0
                            p2_beurt = 1
                            win(player_1)
                            speler_2()
                        else:
                            while again != 'r' or again != 'p':
                                print("choose r or p to continue")
                                again = str(input(str(player_1) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                                if again == 'r':
                                    p1_beurt = p1_beurt + 1
                                    speler_1()
                                elif again == 'p':
                                    p1_safescore = p1_safescore + p1_unsafescore
                                    p2_unsafescore = 0
                                    p2_beurt = 1
                                    win(player_1)
                                    speler_2()
    else:
        roll()
        print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
        if rolled_number == 1:
            print("Oops! You lose " + str(p1_unsafescore) + " but still keep your previous " + str(p1_safescore))
            p1_unsafescore = 0
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[nrBeurt]))
            print("Your current score at this turn: " + str(p1_unsafescore))
            p2_beurt = 1
            speler_2()
        elif rolled_number != 1:
            print("new collected score = " + str(p1_unsafescore) + " + " + str(rolled_number) + " = " + str(p1_unsafescore + rolled_number))
            p1_unsafescore = p1_unsafescore + rolled_number
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[nrBeurt]))
            print("Your current score at this turn: " + str(p1_unsafescore))
            print("\n")
            input("Press enter to continue")
            print("\n")
            again = str(input(str(player_1) + "choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
            if again == 'r':
                p1_beurt = p1_beurt + 1
                speler_1()
            elif again == 'p':
                p1_safescore = p1_safescore + p1_unsafescore
                p2_unsafescore = 0
                p2_beurt = 1
                win(player_1)
                speler_2()
            else:
                while again != 'r' or again != 'p':
                    print("choose r or p to continue")
                    again = str(input(str(
                        player_1) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                    if again == 'r':
                        p1_beurt = p1_beurt + 1
                        speler_1()
                    elif again == 'p':
                        p1_safescore = p1_safescore + p1_unsafescore
                        p2_unsafescore = 0
                        p2_beurt = 1
                        win(player_1)
                        speler_2()


p2_beurt = 1
def speler_2():
    global p2_unsafescore, p2_beurt, p2_safescore, p1_unsafescore, p1_beurt, p3_unsafescore, p3_beurt
    some = True
    if p2_beurt == 1:
        print(str(player_2) + " your first dice at this turn will be automaticly rolled\n\nReady?")
        while some:
            p2_unsafescore = 0
            input("Press enter to continue")
            roll()
            print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
            if rolled_number == 1:
                print("Oops! You lose " + str(p2_unsafescore) + " but still keep your previous " + str(p2_safescore))
                p2_unsafescore = 0
                print("-----------------------------------------\n TOTAL SAFE SCORES")
                totalSafeScore(players)
                print("-----------------------------------------")
                print("Current player: " + str(allPlayers[1]))
                print("Your current score at this turn: " + str(p2_unsafescore))
                some = False
                if players == 2:
                    p1_unsafescore = 0
                    p1_beurt = 1
                    speler_1()
                else:
                    p3_unsafescore = 0
                    p3_beurt = 1
                    speler_3()
            elif rolled_number != 1:
                while True:
                    p2_unsafescore = 0
                    while True:
                        print("new collected score = " + str(p2_unsafescore) + " + " + str(rolled_number) + " = " + str(p2_unsafescore + rolled_number))
                        p2_unsafescore = p2_unsafescore + rolled_number
                        print("-----------------------------------------\n TOTAL SAFE SCORES")
                        totalSafeScore(players)
                        print("-----------------------------------------")
                        print("Current player: " + str(allPlayers[1]))
                        print("Your current score at this turn: " + str(p2_unsafescore))
                        print("\n")
                        input("Press enter to continue")
                        print("\n")
                        some = False
                        again = str(input(str(player_2) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                        if again == 'r':
                            p2_beurt = p2_beurt + 1
                            speler_2()
                        elif again == 'p':
                            if players == 2:
                                p2_safescore = p2_safescore + p2_unsafescore
                                p1_unsafescore = 0
                                p1_beurt = 1
                                win(player_2)
                                speler_1()
                            else:
                                p2_safescore = p2_safescore + p2_unsafescore
                                p3_unsafescore = 0
                                p3_beurt = 1
                                win(player_2)
                                speler_3()
                        else:
                            while again != 'r' or again != 'p':
                                print("choose r or p to continue")
                                again = str(input(str(player_2) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                                if again == 'r':
                                    p2_beurt = p2_beurt + 1
                                    speler_2()
                                elif again == 'p':
                                    if players == 2:
                                        p2_safescore = p2_safescore + p2_unsafescore
                                        p1_unsafescore = 0
                                        p1_beurt = 1
                                        win(player_2)
                                        speler_1()
                                    else:
                                        p2_safescore = p2_safescore + p2_unsafescore
                                        p3_unsafescore = 0
                                        p3_beurt = 1
                                        win(player_2)
                                        speler_3()
    else:
        roll()
        print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
        if rolled_number == 1:
            print("Oops! You lose " + str(p2_unsafescore) + " but still keep your previous " + str(p2_safescore))
            p2_unsafescore = 0
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[1]))
            print("Your current score at this turn: " + str(p2_unsafescore))
            if players == 2:
                p1_unsafescore = 0
                p1_beurt = 1
                speler_1()
            else:
                p3_unsafescore = 0
                p3_beurt = 1
                speler_3()
        elif rolled_number != 1:
            print("new collected score = " + str(p2_unsafescore) + " + " + str(rolled_number) + " = " + str(p2_unsafescore + rolled_number))
            p2_unsafescore = p2_unsafescore + rolled_number
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[1]))
            print("Your current score at this turn: " + str(p2_unsafescore))
            print("\n")
            input("Press enter to continue")
            print("\n")
            again = str(input(str(player_2) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
            if again == 'r':
                speler_2()
                p2_beurt = p2_beurt + 1
                p2_unsafescore = 0
            elif again == 'p':
                if players == 2:
                    p2_safescore = p2_safescore + p2_unsafescore
                    p1_unsafescore = 0
                    p1_beurt = 1
                    win(player_2)
                    speler_1()
                else:
                    p2_safescore = p2_safescore + p2_unsafescore
                    p3_unsafescore = 0
                    p3_beurt = 1
                    win(player_2)
                    speler_3()
            else:
                while again != 'r' or again != 'p':
                    print("choose r or p to continue")
                    again = str(input(str(player_2) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                    if again == 'r':
                        p2_beurt = p2_beurt + 1
                        speler_2()
                        p2_unsafescore = 0
                    elif again == 'p':
                        if players == 2:
                            p2_safescore = p2_safescore + p2_unsafescore
                            p1_unsafescore = 0
                            p1_beurt = 1
                            win(player_2)
                            speler_1()
                        else:
                            p2_safescore = p2_safescore + p2_unsafescore
                            p3_unsafescore = 0
                            p3_beurt = 1
                            win(player_2)
                            speler_3()


p3_beurt = 1
def speler_3():
    global p3_unsafescore, p3_beurt, p3_safescore, p1_beurt, p2_beurt, p1_unsafescore, p4_unsafescore, p4_beurt
    some = True
    if p3_beurt == 1:
        print(str(player_3) + " your first dice at this turn will be automaticly rolled\n\nReady?")
        while some:
            p3_unsafescore = 0
            input("Press enter to continue")
            roll()
            print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
            if rolled_number == 1:
                print("Oops! You lose " + str(p3_unsafescore) + " but still keep your previous " + str(p3_safescore))
                p3_unsafescore = 0
                print("-----------------------------------------\n TOTAL SAFE SCORES")
                totalSafeScore(players)
                print("-----------------------------------------")
                print("Current player: " + str(allPlayers[2]))
                print("Your current score at this turn: " + str(p3_unsafescore))
                some = False
                if players == 3:
                    p1_unsafescore = 0
                    p1_beurt = 1
                    speler_1()
                else:
                    p4_unsafescore = 0
                    p4_beurt = 1
                    speler_4()
            elif rolled_number != 1:
                while True:
                    p3_unsafescore = 0
                    while True:
                        print("new collected score = " + str(p3_unsafescore) + " + " + str(rolled_number) + " = " + str(p3_unsafescore + rolled_number))
                        p3_unsafescore = p3_unsafescore + rolled_number
                        print("-----------------------------------------\n TOTAL SAFE SCORES")
                        totalSafeScore(players)
                        print("-----------------------------------------")
                        print("Current player: " + str(allPlayers[2]))
                        print("Your current score at this turn: " + str(p3_unsafescore))
                        print("\n")
                        input("Press enter to continue")
                        print("\n")
                        some = False
                        again = str(input(str(player_3) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                        if again == 'r':
                            p3_beurt = p3_beurt + 1
                            speler_3()
                        elif again == 'p':
                            if players == 3:
                                p3_safescore = p3_safescore + p3_unsafescore
                                p1_unsafescore = 0
                                p1_beurt = 1
                                speler_1()
                            else:
                                p3_safescore = p3_safescore + p3_unsafescore
                                p4_unsafescore = 0
                                p4_beurt = 1
                                speler_4()
                        else:
                            while again != 'r' or again != 'p':
                                print("choose r or p to continue")
                                again = str(input(str(player_3) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                                if again == 'r':
                                    p3_beurt = p3_beurt + 1
                                    speler_3()
                                elif again == 'p':
                                    if players == 3:
                                        p3_safescore = p3_safescore + p3_unsafescore
                                        p1_unsafescore = 0
                                        p1_beurt = 1
                                        speler_1()
                                    else:
                                        p3_safescore = p3_safescore + p3_unsafescore
                                        p4_unsafescore = 0
                                        p4_beurt = 1
                                        speler_4()

    else:
        roll()
        print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
        if rolled_number == 1:
            print("Oops! You lose " + str(p3_unsafescore) + " but still keep your previous " + str(p3_safescore))
            p3_unsafescore = 0
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[2]))
            print("Your current score at this turn: " + str(p3_unsafescore))
            if players == 3:
                p1_unsafescore = 0
                p1_beurt = 1
                speler_1()
            else:
                p4_unsafescore = 0
                p4_beurt = 1
                speler_4()
        elif rolled_number != 1:
            print("new collected score = " + str(p3_unsafescore) + " + " + str(rolled_number) + " = " + str(p3_unsafescore + rolled_number))
            p3_unsafescore = p3_unsafescore + rolled_number
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[2]))
            print("Your current score at this turn: " + str(p3_unsafescore))
            print("\n")
            input("Press enter to continue")
            print("\n")
            again = str(input(str(player_3) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
            if again == 'r':
                speler_3()
                p3_beurt = p3_beurt + 1
                p3_unsafescore = 0
            elif again == 'p':
                if players == 3:
                    p3_safescore = p3_safescore + p3_unsafescore
                    p1_unsafescore = 0
                    p1_beurt = 1
                    speler_1()
                else:
                    p3_safescore = p3_safescore + p3_unsafescore
                    p4_unsafescore = 0
                    p4_beurt = 1
                    speler_4()
            else:
                while again != 'r' or again != 'p':
                    print("choose r or p to continue")
                    again = str(input(str(
                        player_3) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                    if again == 'r':
                        p3_beurt = p3_beurt + 1
                        speler_3()
                        p3_unsafescore = 0
                    elif again == 'p':
                        if players == 3:
                            p3_safescore = p3_safescore + p3_unsafescore
                            p1_unsafescore = 0
                            p1_beurt = 1
                            speler_1()
                        else:
                            p3_safescore = p3_safescore + p3_unsafescore
                            p4_unsafescore = 0
                            p4_beurt = 1
                            speler_4()


p4_beurt = 1
def speler_4():
    global p4_unsafescore, p4_beurt, p4_safescore, p1_unsafescore, p1_beurt, p5_unsafescore, p5_beurt
    some = True
    if p4_beurt == 1:
        print(str(player_4) + " your first dice at this turn will be automaticly rolled\n\nReady?")
        while some:
            p4_unsafescore = 0
            input("Press enter to continue")
            roll()
            print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
            if rolled_number == 1:
                print("Oops! You lose " + str(p4_unsafescore) + " but still keep your previous " + str(p4_safescore))
                p4_unsafescore = 0
                print("-----------------------------------------\n TOTAL SAFE SCORES")
                totalSafeScore(players)
                print("-----------------------------------------")
                print("Current player: " + str(allPlayers[3]))
                print("Your current score at this turn: " + str(p4_unsafescore))
                some = False
                if players == 4:
                    p1_unsafescore = 0
                    p1_beurt = 1
                    speler_1()
                else:
                    p5_unsafescore = 0
                    p5_beurt = 1
                    speler_5()
            elif rolled_number != 1:
                while True:
                    p4_unsafescore = 0
                    while True:
                        print("new collected score = " + str(p4_unsafescore) + " + " + str(rolled_number) + " = " + str(p4_unsafescore + rolled_number))
                        p4_unsafescore = p4_unsafescore + rolled_number
                        print("-----------------------------------------\n TOTAL SAFE SCORES")
                        totalSafeScore(players)
                        print("-----------------------------------------")
                        print("Current player: " + str(allPlayers[3]))
                        print("Your current score at this turn: " + str(p4_unsafescore))
                        print("\n")
                        input("Press enter to continue")
                        print("\n")
                        some = False
                        again = str(input(str(player_4) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                        if again == 'r':
                            p4_beurt = p4_beurt + 1
                            speler_4()
                        elif again == 'p':
                            if players == 4:
                                p4_safescore = p4_safescore + p4_unsafescore
                                p1_unsafescore = 0
                                p1_beurt = 1
                                speler_1()
                            else:
                                p4_safescore = p4_safescore + p4_unsafescore
                                p5_unsafescore = 0
                                p5_beurt = 1
                                speler_5()
                        else:
                            while again != 'r' or again != 'p':
                                print("choose r or p to continue")
                                again = str(input(str(player_4) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                                if again == 'r':
                                    p4_beurt = p4_beurt + 1
                                    speler_4()
                                elif again == 'p':
                                    if players == 4:
                                        p4_safescore = p4_safescore + p4_unsafescore
                                        p1_unsafescore = 0
                                        p1_beurt = 1
                                        speler_1()
                                    else:
                                        p4_safescore = p4_safescore + p4_unsafescore
                                        p5_unsafescore = 0
                                        p5_beurt = 1
                                        speler_5()

    else:
        roll()
        print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
        if rolled_number == 1:
            print("Oops! You lose " + str(p4_unsafescore) + " but still keep your previous " + str(p4_safescore))
            p4_unsafescore = 0
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[3]))
            print("Your current score at this turn: " + str(p4_unsafescore))
            if players == 4:
                p1_unsafescore = 0
                p1_beurt = 1
                speler_1()
            else:
                p5_unsafescore = 0
                p5_beurt = 1
                speler_5()
        elif rolled_number != 1:
            print("new collected score = " + str(p4_unsafescore) + " + " + str(rolled_number) + " = " + str(p4_unsafescore + rolled_number))
            p4_unsafescore = p4_unsafescore + rolled_number
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[3]))
            print("Your current score at this turn: " + str(p4_unsafescore))
            print("\n")
            input("Press enter to continue")
            print("\n")
            again = str(input(str(player_4) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
            if again == 'r':
                speler_4()
                p4_beurt = p4_beurt + 1
                p4_unsafescore = 0
            elif again == 'p':
                if players == 4:
                    p4_safescore = p4_safescore + p4_unsafescore
                    p1_unsafescore = 0
                    p1_beurt = 1
                    speler_1()
                else:
                    p4_safescore = p4_safescore + p4_unsafescore
                    p5_unsafescore = 0
                    p5_beurt = 1
                    speler_5()
            else:
                while again != 'r' or again != 'p':
                    print("choose r or p to continue")
                    again = str(input(str(player_4) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                    if again == 'r':
                        speler_4()
                        p4_beurt = p4_beurt + 1
                        p4_unsafescore = 0
                    elif again == 'p':
                        if players == 4:
                            p4_safescore = p4_safescore + p4_unsafescore
                            p1_unsafescore = 0
                            p1_beurt = 1
                            speler_1()
                        else:
                            p4_safescore = p4_safescore + p4_unsafescore
                            p5_unsafescore = 0
                            p5_beurt = 1
                            speler_5()


p5_beurt = 1
def speler_5():
    global p5_unsafescore, p5_beurt, p5_safescore, p1_unsafescore, p1_beurt, p6_unsafescore, p6_beurt
    some = True
    if p5_beurt == 1:
        print(str(player_5) + " your first dice at this turn will be automaticly rolled\n\nReady?")
        while some:
            p5_unsafescore = 0
            input("Press enter to continue")
            roll()
            print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
            if rolled_number == 1:
                print("Oops! You lose " + str(p5_unsafescore) + " but still keep your previous " + str(p5_safescore))
                p5_unsafescore = 0
                print("-----------------------------------------\n TOTAL SAFE SCORES")
                totalSafeScore(players)
                print("-----------------------------------------")
                print("Current player: " + str(allPlayers[4]))
                print("Your current score at this turn: " + str(p5_unsafescore))
                some = False
                if players == 5:
                    p1_unsafescore = 0
                    p1_beurt = 1
                    speler_1()
                else:
                    p6_unsafescore = 0
                    p6_beurt = 1
                    speler_6()
            elif rolled_number != 1:
                while True:
                    p5_unsafescore = 0
                    while True:
                        print("new collected score = " + str(p5_unsafescore) + " + " + str(rolled_number) + " = " + str(p5_unsafescore + rolled_number))
                        p5_unsafescore = p5_unsafescore + rolled_number
                        print("-----------------------------------------\n TOTAL SAFE SCORES")
                        totalSafeScore(players)
                        print("-----------------------------------------")
                        print("Current player: " + str(allPlayers[4]))
                        print("Your current score at this turn: " + str(p5_unsafescore))
                        print("\n")
                        input("Press enter to continue")
                        print("\n")
                        some = False
                        again = str(input(str(player_5) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                        if again == 'r':
                            p5_beurt = p5_beurt + 1
                            speler_5()
                        elif again == 'p':
                            if players == 5:
                                p5_safescore = p5_safescore + p5_unsafescore
                                p1_unsafescore = 0
                                p1_beurt = 1
                                speler_1()
                            else:
                                p5_safescore = p5_safescore + p5_unsafescore
                                p6_unsafescore = 0
                                p6_beurt = 1
                                speler_6()
                        else:
                            while again != 'r' or again != 'p':
                                print("choose r or p to continue")
                                again = str(input(str(player_5) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                                if again == 'r':
                                    p5_beurt = p5_beurt + 1
                                    speler_5()
                                elif again == 'p':
                                    if players == 5:
                                        p5_safescore = p5_safescore + p5_unsafescore
                                        p1_unsafescore = 0
                                        p1_beurt = 1
                                        speler_1()
                                    else:
                                        p5_safescore = p5_safescore + p5_unsafescore
                                        p6_unsafescore = 0
                                        p6_beurt = 1
                                        speler_6()

    else:
        roll()
        print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
        if rolled_number == 1:
            print("Oops! You lose " + str(p5_unsafescore) + " but still keep your previous " + str(p5_safescore))
            p5_unsafescore = 0
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[4]))
            print("Your current score at this turn: " + str(p5_unsafescore))
            if players == 5:
                p1_unsafescore = 0
                p1_beurt = 1
                speler_1()
            else:
                p6_unsafescore = 0
                p6_beurt = 1
                speler_6()
        elif rolled_number != 1:
            print("new collected score = " + str(p5_unsafescore) + " + " + str(rolled_number) + " = " + str(p5_unsafescore + rolled_number))
            p5_unsafescore = p5_unsafescore + rolled_number
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[4]))
            print("Your current score at this turn: " + str(p5_unsafescore))
            print("\n")
            input("Press enter to continue")
            print("\n")
            again = str(input(str(player_5) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
            if again == 'r':
                speler_5()
                p5_beurt = p5_beurt + 1
                p5_unsafescore = 0
            elif again == 'p':
                if players == 5:
                    p5_safescore = p5_safescore + p5_unsafescore
                    p1_unsafescore = 0
                    p1_beurt = 1
                    speler_1()
                else:
                    p5_safescore = p5_safescore + p5_unsafescore
                    p6_unsafescore = 0
                    p6_beurt = 1
                    speler_6()
            else:
                while again != 'r' or again != 'p':
                    print("choose r or p to continue")
                    again = str(input(str(player_5) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                    if again == 'r':
                        speler_5()
                        p5_beurt = p5_beurt + 1
                        p5_unsafescore = 0
                    elif again == 'p':
                        if players == 5:
                            p5_safescore = p5_safescore + p5_unsafescore
                            p1_unsafescore = 0
                            p1_beurt = 1
                            speler_1()
                        else:
                            p5_safescore = p5_safescore + p5_unsafescore
                            p6_unsafescore = 0
                            p6_beurt = 1
                            speler_6()


p6_beurt = 1
def speler_6():
    global p6_unsafescore, p6_beurt, p6_safescore, p1_unsafescore, p1_beurt
    some = True
    if p6_beurt == 1:
        print(str(player_6) + " your first dice at this turn will be automatically rolled\n\nReady?")
        while some:
            p6_unsafescore = 0
            input("Press enter to continue")
            roll()
            print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
            if rolled_number == 1:
                print("Oops! You lose " + str(p6_unsafescore) + " but still keep your previous " + str(p6_safescore))
                p6_unsafescore = 0
                print("-----------------------------------------\n TOTAL SAFE SCORES")
                totalSafeScore(players)
                print("-----------------------------------------")
                print("Current player: " + str(allPlayers[5]))
                print("Your current score at this turn: " + str(p6_unsafescore))
                some = False
                p1_unsafescore = 0
                p1_beurt = 1
                speler_1()
            elif rolled_number != 1:
                while True:
                    p6_unsafescore = 0
                    while True:
                        print("new collected score = " + str(p6_unsafescore) + " + " + str(rolled_number) + " = " + str(p6_unsafescore + rolled_number))
                        p6_unsafescore = p6_unsafescore + rolled_number
                        print("-----------------------------------------\n TOTAL SAFE SCORES")
                        totalSafeScore(players)
                        print("-----------------------------------------")
                        print("Current player: " + str(allPlayers[5]))
                        print("Your current score at this turn: " + str(p6_unsafescore))
                        print("\n")
                        input("Press enter to continue")
                        print("\n")
                        some = False
                        again = str(input(str(player_6) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                        if again == 'r':
                            p6_beurt = p6_beurt + 1
                            speler_6()
                        elif again == 'p':
                            p6_safescore = p6_safescore + p6_unsafescore
                            p1_unsafescore = 0
                            p1_beurt = 1
                            speler_1()
                        else:
                            while again != 'r' or again != 'p':
                                print("choose r or p to continue")
                                again = str(input(str(player_6) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                                if again == 'r':
                                    p6_beurt = p6_beurt + 1
                                    speler_6()
                                elif again == 'p':
                                    p6_safescore = p6_safescore + p6_unsafescore
                                    p1_unsafescore = 0
                                    p1_beurt = 1
                                    speler_1()

    else:
        roll()
        print("******************\n**** Rolled " + str(rolled_number) + " ****\n******************")
        if rolled_number == 1:
            print("Oops! You lose " + str(p6_unsafescore) + " but still keep your previous " + str(p6_safescore))
            p6_unsafescore = 0
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[5]))
            print("Your current score at this turn: " + str(p6_unsafescore))
            p1_unsafescore = 0
            p1_beurt = 1
            speler_1()
        elif rolled_number != 1:
            print("new collected score = " + str(p6_unsafescore) + " + " + str(rolled_number) + " = " + str(p6_unsafescore + rolled_number))
            p6_unsafescore = p6_unsafescore + rolled_number
            print("-----------------------------------------\n TOTAL SAFE SCORES")
            totalSafeScore(players)
            print("-----------------------------------------")
            print("Current player: " + str(allPlayers[5]))
            print("Your current score at this turn: " + str(p6_unsafescore))
            print("\n")
            input("Press enter to continue")
            print("\n")
            again = str(input(str(player_6) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
            if again == 'r':
                speler_6()
                p6_beurt = p6_beurt + 1
                p6_unsafescore = 0
            elif again == 'p':
                p6_safescore = p6_safescore + p6_unsafescore
                p1_unsafescore = 0
                p1_beurt = 1
                speler_1()
            else:
                while again != 'r' or again != 'p':
                    print("choose r or p to continue")
                    again = str(input(str(player_6) + " choose your next decision: 'r': roll the dice   'p': pass the turn and safe your score: "))
                    if again == 'r':
                        speler_6()
                        p6_beurt = p6_beurt + 1
                        p6_unsafescore = 0
                    elif again == 'p':
                        p6_safescore = p6_safescore + p6_unsafescore
                        p1_unsafescore = 0
                        p1_beurt = 1
                        speler_1()
# ---- THE GAME ----

stars = "************"
print(stars)
print("Welcome to GAME OF PIG")
print(stars)
print("To start the game, please set up the game: " + '\n')
gameChoice()
totalPlayers()
print("-----------------------------------------\n TOTAL SAFE SCORES")
totalSafeScore(players)
print("-----------------------------------------")
currentPlayer()
speler_1()
