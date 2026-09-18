def freq_count(numbers):
    result = {}

    for num in numbers:
        if num not in result:
            result[num] = 1
        else:
            result[num] = result[num] + 1
    return result

numbers = [1,1,2,2,2,3,4,5,5]
print(freq_count(numbers))