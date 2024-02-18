
def get_user_age():
    try:
        user_age = int(input("Enter your age: "))

    except BaseException as e:
        print(e.args)
    if user_age < 0:
        raise ValueError("Age must be above zero")

    return user_age

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     result = a / b
#     print(result)
#
# except ValueError:
#     print("Enter a valid number")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except BaseException as e2:
#     print(e2.args)

