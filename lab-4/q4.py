import datetime


current_hour = datetime.datetime.now().hour


user_name = input("Enter your name: ")


if 5 <= current_hour < 12:
    greeting = "Good morning"
elif 12 <= current_hour < 17:
    greeting = "Good afternoon"
elif 17 <= current_hour < 20:
    greeting = "Good evening"
else:
    greeting = "Good night"


print(f"{greeting}, {user_name} !!")
