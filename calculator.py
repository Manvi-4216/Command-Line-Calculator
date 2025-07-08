logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(a, b):
    """Adding two numbers"""
    return a + b


def subtract(a, b):
    """Subtracting two numbers"""
    return a - b


def multiply(a, b):
    """Multiplying two numbers"""
    return a * b


def divide(a, b):
    """Dividing two numbers"""
    return a / b


d = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    to_continue = True
    a = int(input("What's the first number? :"))
    for symbol in d:
        print(symbol)
    while to_continue:
        b = int(input("What's the next number? :"))

        operator = input("Pick an operation :")

        operation = d[operator]
        result = operation(a, b)

        print(f"{a} {operator} {b} = {result}")

        task = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.")

        if task == 'y':
            to_continue = True
            a = result
        elif task == 'n':
            to_continue = False
            calculator()


calculator()

