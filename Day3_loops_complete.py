# My Day 3 Practice - Loops

# 1. even odd check
numbers = [1,2,3,4,5,10,15]
for num in numbers:
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

# 2. sum of list
list2 = [1,2,3,4,5]
total = 0
for i in list2:
    total = total + i
print("Sum is:", total)

# 3. table
n = int(input("Enter table number: "))
for i in range(1,11):
    print(n, "x", i, "=", n*i)

# 4. factorial
fact_num = 5
fact = 1
for i in range(1, fact_num+1):
    fact = fact * i
print("Factorial of", fact_num, "is", fact)

# 5. vowel count
my_name = "Likhitha"
my_name = my_name.lower()
vowel_count = 0
for c in my_name:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        vowel_count += 1
print("Vowels:", vowel_count)
