def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

numbers = [20, 50, 90, 120]
maximum = find_max(numbers)
print(maximum)