def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def Multiplication(num1, num2):
    return num1 * num2


def Division(num1, num2):
    if num2 > 0:
        return num1 / num2
    elif num2 == 0:
        print("Can't divide by zero")


print("Please select operation -\n"
      "1. Add\n" "2. Subtract\n" "3. Multiply\n"  "4. Divide\n")

number1 = int(input("Enter the number: "))
number2 = int(input("Enter the number: "))
select = int(input("Select an operation from 1 2 3 4: "))
if select == 1:
    print(number1, '+', number2, '=', addition(number1, number2))

elif select == 2:
    print(number1, '-', number2, '=', subtraction(number1, number2))

elif select == 3:
    print(number1, '*', number2, '=', Multiplication(number1, number2))

elif select == 4:
    print(number1, '/', number2, '=', Division(number1, number2))