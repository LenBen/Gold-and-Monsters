from ctypes.wintypes import HPALETTE
from itertools import filterfalse
import random


import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc

import time


player = vlc.MediaPlayer('C:/Users/Marc/OneDrive/Documents/118Kanto.wav')
player = vlc.MediaPlayer('C:/Users/lenny/OneDrive/Documents/118Kanto.wav') 
end = vlc.MediaPlayer('C:/Users/Marc/OneDrive/Documents/YAY.mp3')
end = vlc.MediaPlayer('C:/Users/lenny/OneDrive/Documents/YAY.mp3')
boss = vlc.MediaPlayer('C:/Users/Marc/OneDrive/Documents/Legendary.mp3')
boss = vlc.MediaPlayer('C:/Users/lenny/OneDrive/Documents/Legendary.mp3')
boss2 = vlc.MediaPlayer('C:/Users/Marc/OneDrive/Documents/B2.mp3')
boss2 = vlc.MediaPlayer('C:/Users/lenny/OneDrive/Documents/B2.mp3')
ncc = vlc.MediaPlayer('C:/Users/Marc/OneDrive/Documents/ncc.mp3')
ncc = vlc.MediaPlayer('C:/Users/lenny/OneDrive/Documents/ncc.mp3')


BLANK = "-"
BOARDSIZE = 10
BOARDCHARS = ["M","G","C","T"]
MONSTERS = 5
GOLD = 0
GOLDT = 3
WIN = 5
MONTYPES = [["Brute",2,3],["Scout",0,1],["Peon",1,1]]
PCHEST = [["BOB - Increases attack by 5",7,10,""],["Jerome - Increases HP by 6",0,6,"B"],["Sandwich - restores a chunk of health\n\tIT is said some rare beast in Spain loves these",0,50,""],["Chocolate bar - Increases your attack and health",3,5,""],["Atomic bomb - Vastly increases your attack, but deceases your health a lot\n\tAlso causes radiation sickness to bosses",50,-50,"B"],["2009 Ford Focus - Does what it says on the tin",10,10,""],["AC - 130: Big thing that goes kill",10,0,"B"]]


Attack = 50
HP = 10
Inventory = [["BOB - Increases attack by 5",7,10,""],["Jerome - Increases HP by 6",0,6,"B"],["Sandwich - restores a chunk of health\n\tIt is said some rare beast in Spain loves these",0,50,""]]
Active = []
Gold = 0
Chest = []

for i in range(2):
    rand = random.randint(0,len(PCHEST)-1)
    Chest.append(PCHEST[rand])

# TO DO:
# - Maybe adda  second boss
# - Add different difficulties

def BOSS():
    print(r"""

                      __
                    //` `\
          _,-"\%   // /``\`\
     ~^~ >__^  |% // /  } `\`\
            )  )%// / }  } }`\`\
           /  (%/'/.\_/\_/\_/\`/
          (    '         `-._`
           \   ,     (  \   _`-.__.-;%>
          /_`\ \      `\ \." `-..-'`
         ``` /_/`"-=-'`/_/
            ```       ```
  """)

def SetUpBoard():
    Board = []
    for Row in range(BOARDSIZE):
        BoardRow = []
        for Column in range(BOARDSIZE):
            BoardRow.append(BLANK)
        Board.append(BoardRow)
    return Board

def PrintBoard(Board,Monsters):
    global Gold
    print()
    print("The board looks like this:")
    print()
    print(" ", end="")
    for Column in range(BOARDSIZE):
        print(" " + str(Column) + "   ", end="")
    print()
    for Row in range(BOARDSIZE):
        if Row < 10:
            print(str(Row) + " ", end="")
        else:
            print(str(Row) + "", end="")
        for Column in range(BOARDSIZE):
            if Row < 10:
                if Board[Row][Column] == BLANK:#changes the - into a space when printing, so places not revelsed      ##########REMEMBER TO REMOVE THESE COMMENT BEFORE THE ACTUAL RUN
                    print(" ", end="")
                    print(" ", end="")          
                elif Board[Row][Column] in BOARDCHARS:#changes the ships into spaces so not revealed
                    print(Board[Row][Column], end=" ")     
                elif Board[Row][Column] == "P":
                    print("P ", end="")
                else:
                    print(Board[Row][Column], end="")
                if Column != 9:
                    print(" | ", end="")#columns on side
            else:
                if Board[Row][Column] == BLANK:#changes the - into a space when printing, so places not revelsed      ##########REMEMBER TO REMOVE THESE COMMENT BEFORE THE ACTUAL RUN
                    print(" ", end="")
                    print(" ", end="")          
                elif Board[Row][Column] in BOARDCHARS:#changes the ships into spaces so not revealed
                    print(Board[Row][Column], end="")     
                elif Board[Row][Column] == "P":
                    print("P ", end="")
                else:
                    print(Board[Row][Column], end="")
                if Column != 9:
                    print(" | ", end="")#columns on side
        print()
    print(f"\nYou have {Gold} gold and there are {Monsters} monsters left")

def PlaceRandomCharacters(Board):
    for monsters in range(MONSTERS):
        Valid = False
        while not Valid:
            Row = random.randint(0,BOARDSIZE-1)
            Column = random.randint(0,BOARDSIZE-1)
            if ValidateMonsterGold(Board,Row,Column):
                PlaceCharacters(Board,Row,Column,0)
                Valid = True
    for gold in range(GOLDT):
        Valid = False
        while not Valid:
            Row = random.randint(0,BOARDSIZE-1)
            Column = random.randint(0,BOARDSIZE-1)
            if ValidateMonsterGold(Board,Row,Column):
                PlaceCharacters(Board,Row,Column,1)
                Valid = True
    for chests in range(random.randint(1,2)):
        Valid = False
        while not Valid:
            Row = random.randint(0,BOARDSIZE-1)
            Column = random.randint(0,BOARDSIZE-1)
            if ValidateMonsterGold(Board,Row,Column):
                PlaceCharacters(Board,Row,Column,2)
                Valid = True
    for ports in range(random.randint(0,2)):
        Valid = False
        while not Valid:
            Row = random.randint(0,BOARDSIZE-1)
            Column = random.randint(0,BOARDSIZE-1)
            if ValidateMonsterGold(Board,Row,Column):
                PlaceCharacters(Board,Row,Column,3)
                Valid = True
    return Board

def ValidateMonsterGold(Board,Row,Column):
    if Board[Row][Column] == BLANK:
        return True
    else:
        return False

def PlaceCharacters(Board,Row,Column,Type):
    Board[Row][Column] = BOARDCHARS[Type]

def InputMove(Board):
    print("Where would you like to move your character(You can only move 1 space at a time):")
    Column = int(input("Column: "))
    Row = int(input("Row: "))
    MoveCharacter(Board,Column,Row)


def GetRowColumn(Player):#Gets the row and the column
  print()
  global Attack
  x = True
  while x == True:
      try:
          Column = int(input("Please enter column: "))
          Row = int(input("Please enter row: "))
          if (Column < 10 and Row < 10) and (Column > -1 and Row > -1):
              if Player[1] + 1 == Column or Player[0] + 1 == Row or Player[1] - 1 == Column or Player[0] - 1 == Column:
                x = False
          elif Row == "55998989":
              Attack = 500
          else:
              print("INVALID CHOICE")
      except:
          print("No")
  print()
  return Row, Column, Player

def MoveCharacter(Board,Player,Monsters,GoldLeft):
    global Gold
    Board[Player[0]][Player[1]] = "-"
    Row, Column, Player = GetRowColumn(Player)
    Monsters,GoldLeft = CheckForGoldOrMonsters(Board,Row,Column,Monsters,GoldLeft)
    Board[Row][Column] = "P"
    Player[0] = Row
    Player[1] = Column
    return Board,Monsters,GoldLeft


def FightMonster():
    global HP, Attack, Gold
    BossFightChance = random.randint(0,128)
    BossFightChance = 128
    Fight = [32,64,96,128]
    if BossFightChance in Fight:
        BossF = True
        BossFight()
    else:
        BossF = False
    if not BossF:
        Valid = False
        player.play()
        Type = random.randint(0,2)
        print(f"You have encountered a {MONTYPES[Type][0]}\nHealth:{MONTYPES[Type][2]}\nAttack:{MONTYPES[Type][1]}")
        Mhealth = MONTYPES[Type][2]
        Mattack = MONTYPES[Type][1]
        while not Valid:
            Mhealth,Run = MonsterFightMenu(Mhealth,Mattack)
            if Mhealth <= 0:
                AddGold = random.randint(0,2)
                print(f"You have slain the monster\nYou have gained {AddGold} Gold")
                if MONTYPES[Type][0] == "Brute":
                    AddGold += 2
                Gold = int(Gold)
                Gold += AddGold
                Valid = True
                Fight.append(random.randint(0,128))
            elif Run:
                time.sleep(2)
                Valid = True
                print("You got away safely")
            elif HP == 0:
                Valid = True
            else:
                print("The monster is still not dead")
    if HP == 0:
        print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nYou died!")
    player.stop()

                
        
def MonsterFightMenu(Mhealth,Mattack):
    global HP, Attack
    Run = False
    print(f"Your HP is {HP}")
    print("""
    What would you like to do?
    1.Attack
    2.Run away""")
    try:
        Response = int(input())
    except:
        print("Not good")
        Response = 2
    if Response == 1:
        print("You attack")
        M = CritChance()
        if M == 2:
            print("Your attack missed")
        elif M == 1:
            print("Critical Hit!\nDouble damage")
            Mhealth -= 2 * Attack
        elif M == 0:
            print("Attack hit!")
            Mhealth -= Attack
        time.sleep(1)
        Mm = CritChance()
        if Mm == 2:
            print("The monster's attack missed!")
        elif Mhealth > 0:
            print("The monster attacked!")
            HP -= Mattack
        else:
            print()
    elif Response == 2:
        fail = random.randint(0,128)
        if fail == 0 or fail == 128:
            print("You didn't get away!")
            time.sleep(1)
            HP -= Mattack
        else:
            Run = True
    return Mhealth,Run
            

def BossFight():
   global Attack, HP, Inventory, Active, Gold
   boss.play()
   bossHealth = 30
   bossShield = 50
   bossAttack = 3
   Bleeding = 0
   Spare = False
   while bossHealth >= 10 and HP > 0:
       if bossHealth >= 10:
           valid = True
       choice = 0
       if Bleeding ==1:
           bossHealth -= 1
       BOSS()
       print(f"""Big bad boss has appeared here!
       Health: {bossHealth}
       Attack: {bossAttack}
       Shield: {bossShield}""")
       print("""What would you like to do:
       1.Attack
       2.Info
       3.Action
       4.Spare""")
       try:
           choice = int(input())
       except:
            print("No good")
       if choice == 1:
           M = CritChance()
           if M == 2:
               print("Your attack missed\nThe boss laughs at you, his shield inreases by 1!")
               bossShield += 1
           elif M == 1 and bossShield > 5:
               print("Critical Hit!\nThe boss seems worried. In his worry, you find a vulnerable spot in his shield and smash it in half!\nHis shield has decreased by half!")
               bossShield = bossShield / 2
               time.sleep(1)
           elif M == 1:
               print("CRITICAL HIT\nThe boss is stunned by your sudden surge in power, and drops his shield, smashing it into tiny fragments")
               print("In this moment of vulnerability, you attack him directly and open up a gaping wound in his stomach!")
               print("That cut he has sure is deep, it will take a long time for him to recover, and the bleeding must be damaging him!")
               bossShield = 0
               bossHealth -= Attack * 4
               Bleeding = 1
               Counter = 1
               time.sleep(3)
           elif M == 0 and bossShield > 0:
                print("You attack the boss, but your attack just deflects just hits his shield.")
                print("That attack must have damaged the shield though!")
                bossShield -= Attack
                time.sleep(0.5)
           elif M == 0 and bossShield <= 0:
               print("BOOM!\nYou attack the boss and hit him directly!")
               bossHealth -= Attack
       elif choice == 2:
            Boss1Info(bossHealth,bossShield,bossAttack)
       elif choice == 3:
           Bleeding = UseInventory(Bleeding)
       elif choice == 4:
           Spare = Boss1Spare(Bleeding)
           if Spare:
               print("")
               bossHealth = 0
           time.sleep(4)
       if choice == 1 or choice == 3:
           BossAttack(bossAttack)
   if HP <= 0:
       print("")
   else:
       print("Im pretty angy now, imma go full on super saiyen\nYeah thats right, dragonball style\nImma be like Goku - toxic fans will powerscale me")
       time.sleep(5)
   boss.stop()
   if bossHealth < 10 and HP > 0 and not Spare:
        ncc.play()
       # play more exciting music and do silly sfx for all the options cos this is a fun end. plus add little text for the boss since they are very angry that you have boomed
        bossHealth = 9000
        bossAttack = 20
        cAttack = 6000
        while bossHealth > 0 and HP > 0:
            choice = 0
            print(f"""Big bad boss has appeared here!
            Health: {bossHealth}
            Attack: {bossAttack}""")
            print("""What would you like to do:
                    1.Attack""")
            try:
                choice = int(input())
            except ValueError:
                print("Wrong intput bukaroo")
            if choice == 1:
                print("You strike the boss")
                if RNJesus := CritChance() == 2:
                    bossHealth = 0
                else:
                    bossHealth -= cAttack
            elif choice == 2:
                Bleeding = UseInventory(Bleeding)
            if bossHealth > 0:
                BossAttack(bossAttack)
        if HP <= 0:
            print("The boss T-bags you, like a sweaty Halo player")
        else:
            ncc.stop()
            print("AAARRRGH\nHow could a puny mortal like you defeat me.\nI'll be back, thats for sure.")
            time.sleep(2)
            print("YOU HAVE DEFEATED THE BOSS!")
            time.sleep(1)
            Gold += 20
            print("20 gold!!")
            time.sleep(2)
   if Spare:
       print("jkjkjkjkjk\nI love you xxxxxxxxxxxxxx\nDragons also love people xxxxxxx")
       Gold += 40

       

def Boss1Info(bossHealth,bossShield,bossAttack):
    global Attack, HP
    print(f"""Before you stand the big boss feared by all the people of all the lands! 
            
                    BJORDORN THE DEMOLISHER

                    Health: {bossHealth}
                    Shield: {bossShield}
                    Attack: {bossAttack}

             He has no weakneses, be is the strongest, he is the fiercest
             He is very scary
             He is weakness-less
             He is definately not allergic to jerome
             He DOES NOT like to eat sandwiches when he is ill
               
            Your stats are:
                    
                    Health: {HP}
                    Attack: {Attack}

                    """)
    time.sleep(1)

def UseInventory(Bleeding):
    global Attack, HP, Inventory, Active
    if len(Inventory) > 0:
        print("Your inventory consists of:")
        for i in range(len(Inventory)):
            print(f"{i} {Inventory[i][0]}")
            time.sleep(0.5)
        print("9.Exit")
        print("What would you like to do?:")
        try:
            choice2 = int(input())
        except:
            print("BOOOOOOOOOOOO")
        for i in range(len(Inventory)):
            if choice2 == i:
                Active.append(Inventory[i][3])
                Attack += Inventory[i][1]
                HP += Inventory[i][2]
                Inventory.pop(choice2)
        for i in range(len(Active)):
            if Active[i] == "B":
                Bleeding = 1    
    else:
        print("You have nothing in your inventory")
        time.sleep(1)
    return Bleeding

def Boss1Spare(Bleeding):
    global Inventory
    x = 0
    if Bleeding == 1:
        for i in range(len(Inventory)):
            if Inventory[i][0] == "Sandwich - restores a chunk of health\n\tIt is said some rare beast in Spain loves these":
                x = 1
        if x == 1:
            print("Will you give the dragon your sandwich?, Y/N")
            abc = input()
            if abc.lower() == "y":
                print("You give the dragon your sandwich, he chomps on it")
                time.sleep(3)
                return True
    else:
        return False


def BossAttack(BossAttack):
    global HP
    RNJesus = random.randint(1,10)
    print("The boss attacks you, act fast, he will attack at any moment")
    time.sleep(RNJesus)
    start = time.time()
    input("Block now! ")
    end = time.time()
    elapsed = end - start
    if elapsed > 1 and elapsed < 2:
        HP -= BossAttack
        print("Ouch")
    elif elapsed > 2:
        HP -= BossAttack * 2
        print("OWEE")
    else:
        rand = random.randint(1,4)
        if rand == 4:
            print("BLOCKED!")
        else:
            HP -= BossAttack/2
            print("Resisted")
    time.sleep(2)

def Boss2():
    boss2.play()
    input()
    boss2.stop()

def CritChance():
    miss = random.randint(0,128)
    if miss == 128:
        M = 2
    elif miss == 100:
        M = 1
    else:
        M = 0
    return M

def CheckForGoldOrMonsters(Board,Row,Column,Monsters,GoldLeft):
    global Gold,Chest
    if Board[Row][Column] == BOARDCHARS[1]:
        Gold += 1
        GoldLeft -= 1
        print("YOU STEPPED ON SOME GOLD\nYOUR GOLD HAS INCREASED BY 1!")
    elif Board[Row][Column] == BOARDCHARS[0]:
        Monsters -= 1
        print("YOU HAVE STEPPED ON A MONSTER, PREPARE TO FIGHT")
        FightMonster()
    elif Board[Row][Column] == BOARDCHARS[2]:
        print("You have found a chest, its contents are:")
        for i in range(len(Chest)):
            print(i+1, Chest[i][0])
        Inventory.extend(Chest)
    elif Board[Row][Column] == BOARDCHARS[3]:
        RNG = CritChance()
        if RNG == 1 or RNG == 2:
            print("Ah, buckaroo, you are teleported to a monster in:")
            for i in range(3):
                print(i)
                time.sleep(1)
            FightMonster()

    return Monsters, GoldLeft

def PlayGame(Board,Player,Monsters):
    global HP, Gold
    GameOver = False
    GameWon = False
    GoldLeft = GOLDT
    while not GameOver:
        PrintBoard(Board,Monsters)
        Board,  Monsters, GoldLeft = MoveCharacter(Board,Player,Monsters, GoldLeft)
        if Gold >= WIN:
            GameWon = True
            GameOver = True
        elif HP <= 0:
            GameOver = True
        elif Gold < WIN and GoldLeft ==0:
            GameOver = True
        elif Gold + Monsters + GoldLeft < WIN:
            GameOver = True
    if GameWon:
        end.play()
        print("You have won the game")
        time.sleep(5)
    if GameOver and not GameWon:
        print("You have lost the game")

def Menu():
    MenuOption = 0
    while not MenuOption == 5:
        MenuOption = int(input("Please enter your option:\n1.Play\n5.Exit\n"))
        if MenuOption == 1:
            Board = SetUpBoard()
            Board[0][0] = "P"
            Player = [0,0]
            Gold = int(GOLD)
            Monsters = MONSTERS
            Board = PlaceRandomCharacters(Board)
            PlayGame(Board,Player,Monsters)
            MenuOption = 5
        else:
            print()
            MenuOption = 5


Menu()



    
