def contains_duplicates(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False

numbers = [1,2,3,4,5,1]
print(contains_duplicates(numbers))