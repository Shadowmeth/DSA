from itertools import count


def sum(low, high):
    if high < low:
        return 0
    else:
        return high + sum(low, high - 1)


# print(sum(1, 10))

array = [
    1,
    2,
    3,
    [4, 5, 6],
    7,
    [8, [9, 10, 11, [12, 13, 14]]],
    [15, 16, 17, 18, 19, [20, 21, 22, [23, 24, 25, [26, 27, 29]], 30, 31], 32],
    33,
]


def print_array(array):
    for ele in array:
        if isinstance(ele, list):
            print_array(ele)
        else:
            print(ele)


# print_array(array)


def double_array(array, index=0):
    if index >= len(array):
        return

    array[index] *= 2
    double_array(array, index + 1)


def reverse(string):
    if not string:
        return ""

    return reverse(string[1:]) + string[0]


def count_x(string):
    if not string:
        return 0

    if string[0] == "x":
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])


def number_of_paths(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)


def anagrams_of(string):
    if len(string) == 1:
        return [string[0]]
    collection = []
    substring_anagrams = anagrams_of(string[1:])
    for substring_anagram in substring_anagrams:
        for index in range(len(substring_anagram) + 1):
            new_string = (
                substring_anagram[:index] + string[0] + substring_anagram[index:]
            )

            collection.append(new_string)
    return collection


# print(anagrams_of("abc"))


def count_total_len(array):
    if not array:
        return 0
    else:
        return len(array[0]) + count_total_len(array[1:])


# print(count_total_len(["ab", "c", "def", "ghij"]))


def only_evens(array, i=0):
    if i >= len(array):
        return []

    if array[i] % 2 == 0:
        return [array[i]] + only_evens(array, i + 1)
    else:
        return only_evens(array, i + 1)


# print(only_evens([1, 2, 3, 4, 5, 6,  7, 8, 9, 10]))


def triangular_nums(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return n + triangular_nums(n - 1)


# print(triangular_nums(7))


def first_x(string, i=0):
    if i >= len(string):
        return -1
    if string[i] == "x":
        return i
    return first_x(string, i + 1)


print(first_x("abcdefghijklmnopqrstuvwxyz"))



















