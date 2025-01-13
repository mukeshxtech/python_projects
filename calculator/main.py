import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    should_accumulate = True
    num1 = float(input("What's the first number?\n"))
    operation_symbol = []
    while should_accumulate:
        for symbol in operations:
            operation_symbol.append(symbol)
            print(symbol)
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?\n"))

        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            num1 = result
        elif choice == 'n':
            should_accumulate = False
            print("\n" * 30)
            print(art.logo)
            calculator()
        else:
            exit()


calculator()
