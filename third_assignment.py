from PIL import Image

def print_names(file_name):
    with open(file_name, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            print(line.strip())


def create_canvas(width=200, height=200, dcolor='white'):
    try:
        new_image = Image.new('RGB', (width, height), color=dcolor)
        new_image.save('test_image.png')
        print("Image was created sucssefully")
    except BaseException as e:
        print(e.args)


def add_words_to_file(file_name, word):
    with open(file_name, 'a', encoding='utf-8') as my_file:
        my_file.write(word+"\n")

# try:
#     a = 1 / 0
# except ZeroDivisionError:
#
# try:
#     x = 10
# finally:
#     print("finally")
# It's legal. The finally block will run no matter what.

# 4. When leaving the Except keyword empty it will catch any error that will accure.
# However, using a generic except block without specifying the exception type isn't considered a good
# practice in most scenarios.
# It might make it harder to debug issues because you're not handling specific exceptions differently.

# except IOError will catch different kinds of Input/Output errors (writing to read only file, etc.)
# except ZeroDivisionError This handler catches exceptions raised when attempting to divide by zero.


add_words_to_file(file_name="words.txt", word="סער")

print_names("words.txt")

create_canvas(width=500, height=500, dcolor='black')
