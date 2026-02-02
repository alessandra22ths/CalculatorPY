def menu():
    print("\nCalculator")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")


running = True

while running:
    menu()
    option = input("Option: ")

    if option == "5":
        print("Goodbye")
        running = False
        continue

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except:
        print("Invalid input")
        continue

    if option == "1":
        result = a + b
    elif option == "2":
        result = a - b
    elif option == "3":
        result = a * b
    elif option == "4":
        if b == 0:
            print("Cannot divide by zero")
            continue
        result = a / b
    else:
        print("Invalid option")
        continue

    print("Result:", result)