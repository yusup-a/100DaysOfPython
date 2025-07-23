import art
def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def print_operations():
    for operation in operationDictionary:
        print(operation)
my_favourite_calculation = add
my_favourite_calculation(3, 5)

operationDictionary = {
    "+" : add,
    "-" : minus,
    "*" : mult,
    "/" : divide
}


# print(operationDictionary["*"](4,8))

def calc():
    print(art.logo)
    firstNum = float(input("What's the first number?: "))
    print_operations()
    operation = input("Pick an operation: ")
    secondNum = float(input("What's the next number?: "))
    result = operationDictionary[operation](firstNum, secondNum)
    print(f"{firstNum} {operation} {secondNum} = {result}")
    inputStr = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    while inputStr == "y":
        print_operations()
        operation = input("Pick an operation: ")
        secondNum = float(input("What's the next number?: "))
        newResult = operationDictionary[operation](result, secondNum)
        print(f"{result} {operation} {secondNum} = {newResult}")
        inputStr = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        result = newResult

    calc()

calc()