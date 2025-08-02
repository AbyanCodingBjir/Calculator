print("===Calculator===")

x = int(input("Insert the first number: "))
y = int(input("Insert the second number: "))

print("ther's a few operation you can choose: ")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

operation = int(input("Choose an option (1-4): "))

if operation == 1:
    result = x + y
    print(f"The result of {x} + {y} is: {result}")
elif operation == 2:
    result = x - y
    print(f"The result of {x} - {y} is: {result}")
elif operation == 3:
    result = x * y
    print(f"The result of {x} * {y} is: {result}")
elif operation == 4:
    if y != 0:
        result = x / y
        print(f"The result of {x} / {y} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose a number between 1 and 4.")
# End of the calculator code
# This code is a simple calculator that performs basic arithmetic operations
# based on user input. It includes error handling for division by zero