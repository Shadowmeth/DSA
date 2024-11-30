thesaurus = {}

thesaurus["bad"] = "evil"
thesaurus["cab"] = "taxi"
thesaurus["ace"] = "star"

# print(thesaurus.get("bad"))


def is_subset(array1, array2):
    hash_table = {}
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1

    for value in larger_array:
        hash_table[value] = True

    for value in smaller_array:
        if not hash_table.get(value):
            return False
    return True


def intersection(array1, array2):
    instersect = []
    hash_table = {}

    for num in array1:
        hash_table[num] = True

    for num in array2:
        if hash_table.get(num):
            instersect.append(num)
    return instersect

def first_duplicate(array):
    hash_table = {}
    for s in array:
        if hash_table.get(s) == 1:
            return s
        else:
            hash_table[s] = 1

def missing_character(string):
    hash_table = {}
    for c in string:
        hash_table[c] = True
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for alphabet in alphabets:
        if not hash_table.get(alphabet):
            return alphabet

def first_non_duplicate(string):
    hash_table = {}
    for c in string:
        if not hash_table.get(c):
            hash_table[c] = 1
        else:
            hash_table[c] += 1
    for c in string:
        if hash_table.get(c) == 1:
            return c

print(intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))
print(first_duplicate(["a", "b", "c", "d", "c", "e", "f"]))
print(missing_character("the quick brown box jumps over a lazy dog"))
print(first_non_duplicate("minimum"))
