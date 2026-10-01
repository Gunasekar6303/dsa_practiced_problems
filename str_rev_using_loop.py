def reverse_str(characters):
    reversed_word = []
    words = characters.split()

    for word in words:
        rev_word = ""
        for i in range(len(word)-1,-1,-1):
            rev_word += word[i]
        reversed_word.append(rev_word)
    return " ".join(reversed_word)

characters = "Hello Wordl"
print(reverse_str(characters))
