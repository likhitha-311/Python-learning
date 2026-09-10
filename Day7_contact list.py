# Day 7 Mini Project

contacts = {}

print("Welcome to Likhitha's Contact list!")

# Add 3 contacts
contacts["mummy"] = "9876543210"
contacts["Daddy"] = "9123456780"
contacts["SVCN Friend"] = "9912324354"

print("\nMy Contacts:")
for name, number in contacts.items():
    print(f"{name} : {number}")

print("\nTotal contacts:", len(contacts))
print("Day 7 Project Completed!")
