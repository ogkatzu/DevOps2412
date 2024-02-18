import random
# A
x = 5
y = 10

if x > y:
    print(f"BIG")
elif x < y:
    print(f"small")

# B

for i in range(1, 6):
    print(i)

# C

season_num = random.randint(1, 4)
if season_num == 1:
    print(f"this season is summer")
elif season_num == 2:
    print(f"this season is winter")
elif season_num == 3:
    print(f"this season is fall")
elif season_num == 4:
    print(f"this season is spring")


# D
count = 1
while count < 11:
    print(count)
    count += 1
# This loop will run 10 times

# E

my_dict = {"age": 28,
           "flettername": "s",
           "shekel_dollar_value": 0.28,
           "did_fly": True,
           "apart_num": 12
           }
for key, value in my_dict.items():
    print(f"{key} {value}")

print(f"{my_dict['age']+my_dict['shekel_dollar_value']}")

# F

# while True:
#     phone_number = input("Please enter you phone number, type exit to close the program")
#     if phone_number.lower() == "exit":
#         break
#     elif  phone_number.isdigit():
#         print(f"Phone number: {phone_number}")
#     else:
#         print("Please type a valid phone number")

# G


def printHello():
    print("hello")


def calculate():
    print(5+3.2)


# H

def namePrint(name):
    print(f"Your name is {name}")


def devideByTwo(num):
    print(num / 2)

# I

def addtwonums(num1, num2):
    result = num1 + num2
    return result


def addSpace(str1, str2):
    result = f"{str1} {str2}"
    return result


# K
base = "#"
for i in range(1, 6):
    print(base)
    base = base + "#"


# L


size = 7  # Adjust the size as needed

for i in range(size):
    for j in range(size):
        if i == j or j == (size - i - 1):
            print("#", end="")  # Print '#' if i equals j or j equals (size - i - 1)
        else:
            print(" ", end="")  # Print space otherwise
    print()


# M


def getnum():
    user_input = input("Please enter a number")
    return user_input


def sum_digits():
    user_input = getnum()
    digits = [int(digit) for digit in str(user_input)] # Creating a list for each digit by converting it to string
    result = 0
    for digit in digits:
        result = result + digit
    return result


print(sum_digits())
