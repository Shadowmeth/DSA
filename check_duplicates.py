def has_duplicate_value_quadratic(array):
    steps = 0
    for i in range(len(array)):
        for j in range(len(array)):
            steps += 1
            if (i != j) and (array[i] == array[j]):
                return True
    print(steps)
    return False


def has_duplicate_value_linear(array):
    steps = 0
    existing_numbers = [0] * 11
    for i in range(len(array)):
        steps += 1
        if existing_numbers[array[i]] == 1:
            return True
        else:
            existing_numbers[array[i]] = 1

    print(steps)
    return False

def greatest_number(array):
    if not array:
        return None
    greatest = array[0]
    for i in range(1, len(array)):
        if array[i] > greatest:
            greatest = array[i]
    return greatest


