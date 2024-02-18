my_list = ["saar", "katz", 28, True]
my_dict = {"fname": "aviel",
           "lname": "buskila",
           "age": 34,
           "is_married:": True}
my_second_list = [
    {"fname": "or", "lname": "shemesh"},
    {"fname": "maxim", "lname": "maxim"}
]

for student in my_second_list:
    print(f"{student['lname']}")
print(my_dict.keys())
print(my_dict.values())
