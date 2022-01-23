from distutils.util import change_root
import random

import time

state = 1

while(state == 1):

    t = 1
    print("\n\n")
    print("#############################################")
    time.sleep(t)
    print("\tMADE BY AUSHAIF")
    time.sleep(t)
    print("#############################################")
    time.sleep(t)
    print("\n\n")
    print("#############################################")
    time.sleep(t)
    print("\tWELCOME TO TRUTH AND DARE GAME...")
    time.sleep(t)
    print("#############################################")
    time.sleep(t)
    print("\n\n")
    print("#############################################")
    time.sleep(t)
    print("\tGAME IS STARTING SOON")
    time.sleep(t)
    print("#############################################")
    print("\n\n")
    
    
    players = []
    print("----------------------------------------")
    player_num = int(input("\tEnter the number of player : ")) # 10
    print("----------------------------------------")

    for i in range(1, player_num + 1):
        print("*********************************")
        name = input("Enter Player {} Name : ".format(i))
        print("*********************************")
        players.append(name)


    def bottle():
        x = random.randrange(1, player_num + 1)
        return x
    
    print("\n")    
    print("-----------------------------------------------------")
    print("\tBOTTLE IS SPINNING STAY BACK AND CHILL!!!")
    print("-----------------------------------------------------")
    print("\n")
    time.sleep(5)

    y = bottle()

    print("\n")
    print("\t--------------------------------------------")
    print("\n")
    print("\t\t\tTARGET : ", players[y - 1])
    print("\n")
    print("\t--------------------------------------------")
    print("\n")

    print("\n")
    print("------------------------------------------------------")
    print("\n")
    option = input(" \tPress t for TRUTH Or d for DARE (t/d): ")
    print("\n")
    print("------------------------------------------------------")
    print("\n")

    if(option == "t"):
            
        with open('./truth.txt',"r") as file:
            data = file.read()
            data = data.splitlines()

            print(random.choice(data))
        
    else:
        with open('dare.txt',"r") as f:
            data = f.read()
            data = data.splitlines()

            print(random.choice(data))


    print("\n")        
    print("------------------------------------------------------------------------")
    print("\n")        
    choice = input("press 'e' for exit ----- press 'r' for replay (e/r) : ")
    print("\n")
    print("------------------------------------------------------------------------")
    print("\n")


    if(choice == 'e'):
        state = 0
    elif(choice == 'r'):
        print("GAME RESTARTING...")
        time.sleep(3)


print("GAME OVER")