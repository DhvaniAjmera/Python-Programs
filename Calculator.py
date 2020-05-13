print(" ******************* WELCOME TO MY CALCULATOR ******************** \n\n")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number: "))

task = int(
    input("Select the operation you want to perform from-  1.Addition 2.Subtraction 3.Multiplication 4. Division "
          "5. All of the above 6. Exit: "))
if task > 6:
    print("Invalid Operation!")
# print("Task is : ",task)
if task == 1:
    ans = num1 + num2
    print("The addition of {} and {} is: ".format(num1, num2, ans))

elif task == 2:
    ans = num1 - num2
    print("The subtraction of {} and {} is: ".format(num1, num2), ans)

elif task == 3:
    ans = num1 * num2
    print("The multiplication of {} and {} is: ".format(num1, num2), ans)

elif task == 4:
    ans = num1 / num2
    print("The division of {} and {} is: ".format(num1, num2), round(ans, 2))

elif task == 5:
    ans = num1 + num2
    print("The addition       of {} and {} is: ".format(num1, num2), ans)
    ans = num1 - num2
    print("The subtraction    of {} and {} is: ".format(num1, num2), ans)
    ans = num1 * num2
    print("The multiplication of {} and {} is: ".format(num1, num2), ans)
    ans = num1 / num2
    print("The division       of {} and {} is: ".format(num1, num2), round(ans,2))
elif task == 6:
    print("Thank You!")
exit()
