def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error: Divide by zero"

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Choose operation: ")
    if choice == '5':
        break
    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == '1': print("Result:", add(a, b))
        elif choice == '2': print("Result:", sub(a, b))
        elif choice == '3': print("Result:", mul(a, b))
        elif choice == '4': print("Result:", div(a, b))
    else:
        print("Invalid option.")

