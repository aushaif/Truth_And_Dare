from distutils.util import change_root
import random

import time

state = 1

count = 1





while(state == 1):

    if(count == 1):

        t = 1
        print("\n\n")
        print("#############################################")
        print("\tMADE BY AUSHAIF")
        print("#############################################")
        

        time.sleep(t)
        
        print("\n\n")
        print("#############################################")
        print("\tWELCOME TO TRUTH AND DARE GAME...")
        print("#############################################")

        time.sleep(t)

        print("\n\n")
        print("#############################################")
        print("\tGAME IS STARTING SOON")
        print("#############################################")
        print("\n\n")
        
        
        players = []
        print("----------------------------------------")
        player_num = int(input("\tEnter the number of player : ")) # 10
        print("----------------------------------------")

        for i in range(1, player_num + 1):
            print("\n")
            name = input("Enter Player {} Name : ".format(i))
            print("\n")
            players.append(name)


    count = 2    


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


    print("\t--------------------------------------------")
    print("\n")
    print("\tBALLI KA BAKRA [TARGET] : ", players[y - 1])
    print("\n")
    print("\t--------------------------------------------")
    

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
        time.sleep(1.5)

print("\n")
print("\t\tGAME OVER")
print("\n")