temperature = int(input("What is the temperature today?:"))
if temperature <= 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today.")
    print("Wear a", outfit)   

is_raining = input("Is it raining today? (yes/no):")