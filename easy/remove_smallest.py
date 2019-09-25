import numpy as np


def remove_smallest(lst):
    if not lst:
        return lst
    elif lst:
        min_index = np.argmin(lst)
        lst.pop(min_index)
        return lst


print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))
print(remove_smallest([3]))
print(remove_smallest([]))


def remove_smallest_1(lst):
    if lst:
        lst.remove(min(lst))
    return lst


print(remove_smallest_1([1, 2, 3, 4, 5]))
print(remove_smallest_1([5, 3, 2, 1, 4]))
print(remove_smallest_1([2, 2, 1, 2, 1]))
print(remove_smallest_1([3]))
print(remove_smallest_1([]))