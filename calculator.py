# ========== TASK 1: EASY ==========
print("--- TASK 1: Simple Addition ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum is: {a + b}")

# ========== TASK 2: MEDIUM ==========
print("\n--- TASK 2: All Operations ---")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

# ========== TASK 3: PRO ==========
print("\n--- TASK 3: Pro Calculator ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator!")
