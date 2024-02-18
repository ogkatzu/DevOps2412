#
a = 5
b = 14
my_name = "roee"

if my_name == "saar" and (b >= 10 or a < 10):
    print(f"you are {my_name}")
    # Every code that is within this indentation is in the scope of the IF statement

elif my_name == "roee":
    print(f"your name is {my_name}")
else:
    print(f"Not head to the wall")

print(a == 50)

my_list = []
if my_list:
    print("you have items")
else:
    print("you don't have items in the list")

my_other_list = ["or", "tohat", "adam", "moshe"]
my_other_name = "moshe"
if my_other_name in my_other_list:
    print(f"{my_other_name} is in the list")
else:
    print(f"{my_other_name} is not in the list")

tt = "saar"
rr = "saar"
print(tt is rr)
