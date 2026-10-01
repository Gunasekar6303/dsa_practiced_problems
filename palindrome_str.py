# For txt
def is_palindrome(txt):
    reversed_str = ""
    for i in range(len(txt)-1,-1,-1):
        reversed_str += txt[i]
    return reversed_str == txt
txt = "Guna"
print(is_palindrome(txt))

# For number
def is_palindrome(number):
    if number < 0:
        return False
    original = number
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = (reversed_num * 10) + digit
        number = number // 10
    return reversed_num == original
number = 121
print(is_palindrome(number))