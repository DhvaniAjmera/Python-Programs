from random import randint
import time
print("Rock Paper Scissor Game")
print("------------------------")
print("1.Rock/Paper    -> Paper")
print("2.Rock/Scissor  -> Rock")
print("3.Scissor/Paper -> Scissor")
print("It is a 2 player game.")
while True:
    opt=int(input("Enter your choice- 1.Rock\n\t\t\t\t   2.Paper\n\t\t\t\t   3.Scissor : "))
    while opt==1 or opt==2 or opt==3:
        if opt==1:
            choice="Rock"
            print("You chose:",choice)
        elif opt==2:
            choice="Paper"
            print("You chose:", choice)
        elif opt==3:
            choice="Scissor"
            print("You chose:", choice)
        break
    if opt>3:
        print("Error")
        break
    time.sleep(2)

    print("Its computer's turn now")
    comp = randint(1, 3)
    if comp == 1:
        compname="Rock"
    elif comp == 2:
        compname = "Paper"
    else:
        compname="Scissor"
    print("The computer plays:", compname)


    if compname == choice:
        print("It is a tie.")
        comp=randint(1,3)
    elif ((opt == 1 and comp == 2) or (comp == 1 and opt == 2)):
        print("1.Rock/Paper -> Paper")
        result = "Paper"
    elif ((opt == 1 and comp == 3) or (comp == 3 and opt == 1)):
        print("1.Rock/Scissor -> Rock")
        result = "Rock"
    else:
        print("1.Scissor/Paper -> Scissor")
        result = "Scissor"

    '''elif compname=="Rock" and choice == "Scissor" or compname=="Scissor" and choice=="Rock" :
        print("Rock wins.")
    elif compname=="Rock" and choice=="Paper" or compname=="Paper" and choice=="Rock" :
        print("Paper wins.")
    elif compname=="Paper" and choice=="Scissor" or compname=="Scissor" and choice=="Paper" :
        print("Scissor wins.")
    else:
        print("Error")'''
    #The above code is the alternative
    if result==choice:
        print("You win!")
    else:
        print("You lost")

    ask=input("Do you wish to play again? Y/N :")
    if ask=="N" or ask=="n":
        break
print("Thank you for playing")