import json
from datetime import datetime

with open("tips.json", "r") as file:
    data = json.load(file)

name = input("Enter your name: ")

print(f"Hello {name}! Welcome to Smart Student Assistant")

print("1. Generate Study Tips")
print("2. Generate Motivation Quote")
print("3. Display Current Date & Time")

choice = input("\nEnter your choice (1-3): ")

output = ""

if choice == "1":
    print("Study Tips:")
    
    for tip in data["study_tips"]:
        print("-", tip)
        output += tip + "\n"

elif choice == "2":
    print("Motivation Quotes:")
    
    for quote in data["motivation_quotes"]:
        print("-", quote)
        output += quote + "\n"

elif choice == "3":
    current = datetime.now()
    result = current.strftime("%d-%m-%Y %H:%M:%S")
    
    print("Current Date & Time:")
    print(result)
    
    output = result

else:
    print("Invalid Choice")
    output = "Invalid Choice"

with open("output.txt", "w") as file:
    file.write(output)

print("\nOutput saved in output.txt")
