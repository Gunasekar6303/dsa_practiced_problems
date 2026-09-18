def find_min(numbers):
    min_element = numbers[0]

    for num in numbers:
        if num < min_element:
            min_element = num
    return min_element
numbers = [1,2,3,4,5]
print(find_min(numbers))