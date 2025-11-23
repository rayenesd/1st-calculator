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
if mode == "-":
    print(Subtraction)
if mode == "x" and "x":
    print(Multiplication)
if mode == "/":
    print(Division)