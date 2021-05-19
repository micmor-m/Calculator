# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
    running = "y"
    is_first_loop = True
    while running == "y":
        num1 = int(input("What is the first number?: "))
        # Print list of operation to user:
        for operation in operations:
            print(operation)
        operation_symbol = (input("Pick an operation from the line above: "))
        function = operations[operation_symbol]

        if is_first_loop:
            num2 = int(input("What is the second number?: "))
        else:
            num2 = result

        result = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        running = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
        is_first_loop = False
        if running == "n":
            calculator()


calculator()
