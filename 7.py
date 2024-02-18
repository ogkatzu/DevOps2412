my_nums = list(range(1, 101))

for num in my_nums:
    if num % 7 != 0 and '7' not in str(num):
        print(num)
    else:
        print("boom boom boom in my room")
