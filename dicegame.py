from random import randint
import time


def betty():
    input("\nEnter any keyword to proceed:")
    print("It is Betty's turn now.")


def user():
    abc = input("Enter 'A' to roll the dice:")
    if abc != "A":
        print("Seems like you have entered the wrong input.Please try again.")
        user()
    else:
        dice()
        global user_roll
        user_roll = no


def replay():
    ch = input("\nDo you want to play more? Y/N:")
    if ch == "y" or ch == "Y":
        user()
        betty()
        dice()
        replay()
    elif ch == "N" or ch == "n":
        print("\nIt was a nice game,", name,"!")
        print("Looking forward to your next game with Betty.")
        exit()
    else:
        replay()


def dice():
    print("\nPlease wait.The dice is rolling.")
    time.sleep(2)
    global no
    no = randint(1, 6)
    print("\nThe dice shows:", no)


    if no == 6:
        print("Player gets an additional turn.")
        dice()



def result():
    if user_roll > no:
        print("WOW! Looks like you rolled a higher number!")
    else:
        print("Aww! Hard Luck.")


print("***************************PLAY THE DICE*********************")
print("\n\nHello player! Welcome to playing the dice with Betty!")
name = input("How should we address you as:")
user()
betty()
dice()
result()
replay()
