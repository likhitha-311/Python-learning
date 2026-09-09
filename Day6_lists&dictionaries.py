# Day 6 - Lists & Dictionaries

# Part 1 - List of AI Tools
ai_tools = ["Python", "GitHub", "ChatGPT", "VS Code"]
print("My AI Tools:", ai_tools)
print("First Tool:", ai_tools[0])
print("Total Tools:", len(ai_tools))
# Add new tool
ai_tools.append("Hugging Face")
print("After learning new tool:", ai_tools)

# Part 2 - Dictionary - My Profile
my_profile = {
    "name": "Likhitha",
    "branch": "CAI",
    "college": "SVCN",
    "goal": "GenAI Engineer"
}
print("\nMy Profile:")
for key, value in my_profile.items():
    print(f"{key} : {value}")

# Part 3 - Loop through list
print("\nMy Learning Journey:")
for tool in ai_tools:
    print(f"I know {tool}")
print("Day 6 Completed - Lists and Dict mastered!")
print("I push code daily, no AI shortcut.")
