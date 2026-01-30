run = ""
while run != "turn off":
    run = input("turn on or turn off: ")
    if run == "turn on":
        operation = input("write the operation: ")
        if "+" in operation:
            # Addition
            num_1, num_2 = operation.split("+")
            num_1 = float(num_1)
            num_2 = float(num_2)
            print(operation)
        elif "-" in operation :
            num_1, num_2 = operation.split("-")
            num_1 = float(num_1)
            num_2 = float(num_2)
            print(operation)
        elif "*" in operation:
            num_1, num_2 = operation.split("*")
            num_1 = float(num_1)
            num_2 = float(num_2)
            print(operation)
        elif "/" in operation:
            num_1, num_2 = operation.split("/")
            num_1 = float(num_1)
            num_2 = float(num_2)
            print(operation)
        else : 
            print("invalid operation")
    elif run == "turn off":
        print("Goodbye!")
        break

    else:
        print("Invalid command, try again.")
