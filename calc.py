calculate = True

def addition(num0, num1):
    return num0 + num1

def multiply(num0, num1):
    return num0 * num1

def subtraction(num0, num1):
    return num0 - num1

def division(num0, num1):
    return num0 / num1


while calculate:
    print("+ = Addition, * = multiply, - = subtract, / = divide")

    fNum = float(input("Please enter first number: "))
    o = input("enter operator: ")
    sNum = float(input("Please enter second number: "))
    print(fNum, o, sNum)
    if o == "+":
        print(addition(fNum, sNum))

    elif o == "*":
        print(multiply(fNum, sNum))

    elif o == "-":
        print(subtraction(fNum, sNum))

    elif o == "/":
        print(division(fNum, sNum))

    else:
        print("Wrong operator")

    try_again = input("do you want to try again y/n: ")

    if try_again == "yes" or try_again == "y":
        calculate = True
    else:
        calculate = False

