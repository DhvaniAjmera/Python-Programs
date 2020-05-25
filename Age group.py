age = int(input("Enter the age of a person: "))
if age<4:
    print("The person is a baby.\nPlay the most with him.")
elif age < 13:
    print("The person is a child.")
elif age <= 19:
    print("The person is a teenager.")
elif age <= 59:
    print("The person is an adult.")
elif age > 59:
    print("The person is a senior citizen.\nTake good care of their health.")