print("=== Bio Data ===")
student = {
  "name": "likhitha",
  "dob": "11 March 2008",
  "branch": "CAI"
}
for key, value in student.items():
  print(f"{key.upper()} : {value}")

print("\n=== Marks & Grade ===")
marks = [85, 90, 78]
total = sum(marks)
avg = total / len(marks)
grade = 'A' if avg >= 80 else 'B'
print(f"Total: {total} | Avg: {avg:.2f} | Grade: {grade}")

print("\n=== Swapping Numbers ===")
a, b = 2008, 11
a, b = b, a
print(f"Swapped: a={a}, b={b}")
