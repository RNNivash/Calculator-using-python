def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "Zero not allowed!"
    else:
        return x / y
def mod(x,y):
    return x % y

def calculator():
    print("Select operation: ")
    print("1 : Add")
    print("2 : Sub")
    print("3 : Mul")
    print("4 : Div")
    print("5 : Mod")

    while True:
        choice = input("Enter choices (1/2/3/4/5): ")
        if choice in ["1","2","3","4","5"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1,num2)}")

            if choice == "2":
                print(f"{num1} - {num2} = {sub(num1,num2)}")

            if choice == "3":
                print(f"{num1} * {num2} = {mul(num1,num2)}")

            if choice == "4":
                print(f"{num1} / {num2} = {div(num1,num2)}")

            if choice == "5":
                print(f"{num1} % {num2} = {mod(num1,num2)}")
        else:
            print("Not a valid operation!")

        next_cal = input("Do you want to perform another calculation? (yes/no): ")
        if next_cal.lower() != "yes":
            break

    print("Exiting from calculator..., Goodbye!")

calculator()

