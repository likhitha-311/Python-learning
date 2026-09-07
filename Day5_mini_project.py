# Day 5 Mini Project - AI Learning Tracker

def show_dashboard():
    print("Likhitha's AI Learning Tracker")
    print("Name: Likhitha")
    print("Location: Nellore")
    print("Branch: CAI - AI and Data Science")
    print("Goal: GenAI Engineer")
    print("GitHub: github.com/likhitha-311/Python-learning")
    print("")

def track_topics():
    topics = ["Python Basics", "Loops", "Functions", "GitHub Push"]
    completed = 0

    print("My Learning Status:")
    for i, topic in enumerate(topics, 1):
        ans = input(f"{i}. {topic} - Done? (yes/no): ")
        if ans.lower() == "yes" or ans.lower() == "y":
            completed = completed + 1
    
    return completed, len(topics)

def calculate_progress(done, total):
    
    per = (done / total) * 100
    return per

if __name__ == "__main__":
    show_dashboard()

    done, total = track_topics()
    percent = calculate_progress(done, total)

    print("")
    print(f"Your Progress: {done}/{total} = {percent}%")
    
    if percent == 100:
        print("Streak: 5 Days! Amazing Likhitha, keep pushing!")
    else:
        print(f"Streak: {total} days started, {done} completed. Keep going!")
    
    print("\nMessage: I am becoming a GenAI Engineer - Day 5 Completed!")
    print("I push code daily, no AI shortcut.")
