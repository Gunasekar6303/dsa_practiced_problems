def char_count(characters):
    result = {}

    for char in characters:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

characters = 'a','a','b'
print(char_count(characters))