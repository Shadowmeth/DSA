# search a target value in an ordered array

step_count = 0

def linear_search(array, target):
    global step_count
    for index, element in enumerate(array):
        step_count += 1
        if element == target:
            return index
        elif element > target:
            break
    return None

def binary_search(array, target):
    global step_count
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        step_count += 1
        midpoint = (lower_bound + upper_bound) // 2
        value_at_midpoint = array[midpoint]

        if target == value_at_midpoint:
            return midpoint
        elif target < value_at_midpoint:
            upper_bound = midpoint - 1
        elif target > value_at_midpoint:
            lower_bound = midpoint + 1
    return None

linear_search([3, 17, 75, 80, 202], 22)
print(f'linear_search took {step_count} steps')
step_count = 0
binary_search([3, 17, 75, 80, 202], 22)
print(f'binary_search took {step_count} steps')

