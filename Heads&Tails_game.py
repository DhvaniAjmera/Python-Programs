import random
import time
print("********************* Welcome to the game of Heads & Tails! *************************\n")
a = ["Heads", "Tails"]
abc = int(input("Choose from the following: 0.Heads 1.Tails : "))
if abc == 0:
    print("You chose Heads")
    print("Bot is Tails\n")
    abc = "Heads"
else:
    print("You chose Tails")
    print("Bot is Heads\n")
    abc = "Tails"
toss = random.choice(a)
print("The coin is being tossed.Please Wait for a moment....")
time.sleep(2)
print("The toss is:", toss)
if toss == abc:
    print("Yay!You Won.")
else:
    print("Opps... looks like you lost and Bot Won!")