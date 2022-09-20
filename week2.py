myDict = {
    1: "Python",
    2: "Javascript",
    3: "C++",
    4: "C#",
    5: "Ruby",
    6: ""
}
myDict[6]=input("pls enter next prog language")
print(myDict)
for k,v in myDict.items():
    print (v)
    
newDict = {}
mykey=input("pls enter key")
newDict[mykey] = input("pls enter details")
print(newDict)

player_list = []
addPlayer = True 

while addPlayer:
    pName = input("player name: ")
    pPass= input("player pass: ")
    pScore= int(input("current score: "))
    pHscore= int(input("highest pass: "))
    playerProfile = {"playerTag": pName, "pass" : pPass, 
                     "score": pScore, "hscore": pHscore}
    player_list.append(playerProfile)
    
    anotherplayer = input ("add another player y/n?")
    if anotherplayer == "n":
        addPlayer = False
    
print(f"list of players: \n{player_list}")

import time


uName = input("Enter user name: ")

fName = input("Enter full name: ")

age = int(input("Enter age: "))


with open("/Users/olehpysmenko/Desktop/Projects/Python-practices2/userData1.txt", "a") as dataFile:



    # method 1  

    wContent = dataFile.write("\n"+  uName +" " + " " + fName + " " + str(age) )