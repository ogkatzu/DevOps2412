# for i in range(5):
#     print(f"hello {i}")
#
# for i in range(10):
#     print(f"you are number {i}")
#

def my_printer(prefix, amount):
    for i in range(1, amount+1):
        print(f"{prefix} {i}")


my_printer("hello", 5)
my_printer("you are number", 10)