def reverse_str(characters):
    reversed_word = ""

    for i in range(len(characters)-1,-1,-1):
        reversed_word += characters[i]
    return reversed_word
characters = "Hello"
print(reverse_str(characters))