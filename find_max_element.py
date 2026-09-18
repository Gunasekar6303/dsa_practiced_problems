def find_max(numbers):
    max_element = numbers[0]

    for num in numbers:
        if num > max_element:
            max_element = num
    return max_element
numbers = [1,2,3,4,5]
print(find_max(numbers))