print("Welcome To Rayane's Calculator")
mode = input("chose mode: + or - or X or / : ")
num_1 = float(input("first number: "))
num_2 = float(input("second number: "))
Addition = num_1 + num_2
Subtraction = num_1 - num_2
Multiplication = num_1 * num_2
Division = num_1 / num_2
if mode == "+":
    print(Addition)
elif mode == "-":
    print(Subtraction)
elif mode == "x" and "x":
    print(Multiplication)
elif mode == "/":
    if num_2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(Division)

else :
    print("Invalid mode selected.")    