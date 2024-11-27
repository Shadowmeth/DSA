from typing import List


def bubble_sort(array: List[int]) -> None:
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


array = [65, 55, 45, 35, 25, 15, 10]
selection_sort(array)
print(array)
