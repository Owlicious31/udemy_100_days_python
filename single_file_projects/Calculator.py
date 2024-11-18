import art

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
    "/": divide,
}

print(art.logo3)

first_number = float(input("What is the first number: "))
while True:
    print("/\n*\n-\n+")
    operation = input("Which operation do you wish to perform: ")
    second_number = float(input("What is the second number: "))

    def calculate(n1,n2):
        for symbol in operations:
            if symbol == operation:
                answer = float(operations[symbol](n1, n2))
                return answer

    result = calculate(first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    print(f"The result is: {result}")

    continue_with_answer = input(f"Type 'y' to continue with {result} or 'n' to start over: ").lower()
    if continue_with_answer == "y":
        first_number = result
    elif continue_with_answer == "n":
        print("\n" * 20)
        print(art.logo3)
        first_number = float(input("What is the first number: "))
