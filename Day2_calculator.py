# 1.EASY
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a+b)

# 2.MEDIUM
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

# 3.PRO
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a+b)
elif op == "-":
    print("Result:", a-b)
elif op == "*":
    print("Result:", a*b)
elif op == "/":
    if b != 0:
        print("Result:", a/b)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator!")
