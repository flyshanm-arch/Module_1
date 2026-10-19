print("=== Smart School Day Planner ===")
print("Answer 3 questions and I will plan your day! \n")

day     = input("What day is it? (Monday to Sunday):").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy):").strip().lower()
homework = input("Is your homework done? (yes / no):").strip().lower()

print()
print(f"=== Yout plan for {day} ===")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Day type  : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type  : First day of the week. Pak your weekly planner.")
elif day == "Friday":
    print("Day type  : Last school day. Return library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type   : Regular school day. Stay focused!")
else:
    print("Day type   : Day not recognized!")
if weather == "sunny" and homework == "yes":
    print("After school: Head to the park!")
if weather == "rainy" or weather == "cloudy":
    print("Pack your umbrella!")
if not (homework == "yes"):
    print("Homework not done yet!")
if weather == "rainy" and not (homework == "yes"):
    print("Finish homework!")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("All set for a great school day!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Play outside and have fun!")
else:
    print("Take one step at a time!")

print()
print("Plan complete! goodbye!")