# Day 4 Problem 3 - My Profile Card
# This file proves I am coding daily
# Name: Likhitha

def show_my_profile():
    print("My Profile Card:")
    print("Name: Likhitha")
    print("Location: Kavali, Andhra Pradesh")
    print("Branch: CAI - AI and Data Science")
    print("Current Learning: Python Functions - Day 4")
    print("Goal: GenAI Engineer")
    
    print("\nMy Learning Journey:")
    skills = ["Python Basics", "Loops", "Functions"]
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill} - Done")

    print("\nI am pushing code daily on GitHub.")

if __name__ == "__main__":
    show_my_profile()
