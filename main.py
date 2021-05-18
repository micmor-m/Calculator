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

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

# Print list of operation to user:
for operation in operations:
    print(operation)

operation_symbol = (input("Pick an operation from the line above: "))

function = operations[operation_symbol]
result = function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {result}")

