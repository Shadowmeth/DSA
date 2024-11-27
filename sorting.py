from typing import List


def bubble_sort(array: List[int]) -> None:
    if not array:
        return

    unsorted_till_index = len(array) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_till_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        unsorted_till_index -= 1


def selection_sort(array):
    if not array:
        return

    for i in range(len(array) - 1):
        lowest_so_far = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_so_far]:
                lowest_so_far = j

        if lowest_so_far != i:
            array[i], array[lowest_so_far] = array[lowest_so_far], array[i]


def insertion_sort(array):
    if not array:
        return

    for i in range(1, len(array)):
        temp_value = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp_value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp_value
        print(f"PASS: {i}")
        print(f"array: {array}")


array = [4, 2, 7, 1, 3]
insertion_sort(array)
print(array)
