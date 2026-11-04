
def calculate_total(m1, m2, m3):
    total = m1 + m2 + m3
    return total


def calculate_average(total):
    average = total / 3
    return average


name = input("Enter student name: ")

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

total = calculate_total(m1, m2, m3)
average = calculate_average(total)

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))

if average >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
