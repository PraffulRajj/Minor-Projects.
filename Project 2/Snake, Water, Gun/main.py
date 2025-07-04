'''
1 for snake
-1 for water
0 for gun
'''
computer = -1
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youdict[youstr]

print(f"You choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}")

if(computer == you):
    print("Draw!")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you ==0):
        print("You Loose!")

    elif(computer == 1 and you == -1):
        print("You Loose!")


    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you ==-1):
        print("You Win!")

    elif(computer ==0 and you ==1):
        print("You Loose!")

    else:
        print("Something went wrong!")    