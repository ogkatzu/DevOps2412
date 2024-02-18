
#
# for name in my_file.readlines():
#     print(f"Hello {name.strip()}")

def add_names(names):
    # First option
    # with open("names.txt", "a+") as file:
    #     file.write(f"\n{name1}\n{name2}\n{name3}")
    my_file = open("names.txt", "a")
    for name in names:
        my_file.write(name + "\n")


def print_names(file_name):
    my_files = open("names.txt", "r")
    names = my_files.readlines()
    for name in names:
        print(name + "\n")


add_names(names=["saar", "oded", "ronen"])
print_names(file_name="names.txt")
