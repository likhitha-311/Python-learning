
def calculate_salary(basic_salary, bonus):
    total_salary = basic_salary + bonus
    return total_salary


name = input("Enter employee name: ")

basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus amount: "))

salary = calculate_salary(basic_salary, bonus)

print("\nEmployee Details:")
print("Employee Name:", name)
print("Basic Salary:", basic_salary)
print("Bonus:", bonus)
print("Total Salary:", salary)
