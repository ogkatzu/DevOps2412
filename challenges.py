import math


def radianstoangles(rad) -> float:
    pi_value = math.pi
    result = rad * (180/pi_value)
    return result


def sortingList(unsort_list, sort_type) -> list:
    sort_type = str(sort_type)
    if sort_type == 'asc':
        return sorted(unsort_list)
    elif sort_type == 'desc':
        return sorted(unsort_list, reverse=True)
    return unsort_list


def dectobin(dec_num):
    bin_num = ''
    while dec_num > 0:
        bin_num = str(dec_num % 2) + bin_num
        dec_num //= 2
    return bin_num


def vowelcounter(word):
    counter = 0
    vowels = ['i', 'a', 'e', 'o', 'u']
    for letter in word:
        if letter in vowels:
            counter += 1
    return counter


def credit_card_hider(credit_number):
    credit_number = str(credit_number)
    cencored_card = '*' * (len(credit_number) - 4)
    cencored_card += credit_number[-4:]
    return cencored_card

# print(vowelcounter("omegalul"))


print(credit_card_hider("6343234234749090"))