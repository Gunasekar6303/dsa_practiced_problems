def is_palindrome(txt):
    reversed_str = ""
    for i in range(len(txt)-1,-1,-1):
        reversed_str += txt[i]
    return reversed_str == txt
txt = "Guna"
print(is_palindrome(txt))