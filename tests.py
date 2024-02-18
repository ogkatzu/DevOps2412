from selenium import webdriver

firefox_driver = webdriver.Firefox()

def is_a_palindrome(x) -> bool:
    palindrome = str(x)
    for i in range(len(palindrome)):
        if i == 0:
            if palindrome[i] != palindrome[-1]:
                print("bad")
                return False
        else:
            if palindrome[i] != palindrome[-i-1]:
                return False
    return True


def is_a_palindrome_new(x) -> bool:
    pal = str(x)
    i = -1
    for num in pal:
        if num != pal[i]:
            return False
        i -= 1
    return True


print(is_a_palindrome(987789))
print(is_a_palindrome_new(987789))
