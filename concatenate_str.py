def concate_str(s1,s2):
    combined_str = []

    for char in s1 + s2:
        combined_str.append(char)
    return "".join(combined_str)
s1 = "Guna"
s2 = "Sekar"
print(concate_str(s1,s2))