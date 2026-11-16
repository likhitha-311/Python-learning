
student_name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = float(input("Enter student marks: "))

is_adult = age >= 18
is_passed = marks >= 35
is_distinction = marks >= 75

print("\nStudent Details")
print("Name:", student_name)
print("Age:", age)
print("Marks:", marks)

print("Adult:", is_adult)
print("Passed:", is_passed)
print("Distinction:", is_distinction)
