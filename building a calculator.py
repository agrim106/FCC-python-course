num1 = float(input("enter first number: "))
op = input("enter operator: ")
num2 = float(input("enter first number: "))

if op == "+":
    print(num1 + num2)
elif op == "*":
    print(num1*num2)
elif op == "-":
    print(num2-num1)
elif op == "/":
    print(num2/num1) 
else:
    print("Invalid Operator")     

