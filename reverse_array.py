def reverse_array(numbers):
    reversed_list = []
    for i in range(len(numbers)-1,-1,-1):
        reversed_list.append(numbers[i])
    return reversed_list

numbers = [1,2,3,4,5]
print(reverse_array(numbers))