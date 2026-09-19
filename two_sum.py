def two_sum(numbers):
    target = 61
    left = 0
    right = len(numbers) -1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return left,right
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return None

numbers = [1,2,3,4,5]
print(two_sum(numbers))