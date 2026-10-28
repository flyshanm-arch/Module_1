username = input("Please enter your name")
userage = input("Please enter your age")
usergender = input("please tell me your gender")
if int(userage) >= 18:
    print("You can vote")
else: 
    print("You cannot vote")
number = int(input("Is this a even number or odd number?"))
if number %2 != 0:
    print("Correct! Your age is a odd number!")
else:
    print("Correct! your age is a even number!")