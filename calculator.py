def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def main():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (1/2/3/4): ")

        if operation == "1":
            result = add(num1, num2)
        elif operation == "2":
            result = subtract(num1, num2)
        elif operation == "3":
            result = multiply(num1, num2)
        elif operation == "4":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
