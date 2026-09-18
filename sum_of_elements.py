def sum_of_elements(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
numbers = [1,2,3,4,5]
print(sum_of_elements(numbers))