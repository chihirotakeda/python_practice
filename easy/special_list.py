def is_special_array(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 1 or lst[i + 1] % 2 == 0:
            return False
    return True


print(is_special_array([2, 7, 4, 9, 6, 1, 6, 3]))
print(is_special_array([2, 7, 9, 1, 6, 1, 6, 3]))
print(is_special_array([2, 7, 8, 8, 6, 1, 6, 3]))


def is_special_array_2(lst):
    return all(lst[i] % 2 == i % 2 for i in range(len(lst)))


print(is_special_array_2([2, 7, 4, 9, 6, 1, 6, 3]))
print(is_special_array_2([2, 7, 9, 1, 6, 1, 6, 3]))
print(is_special_array_2([2, 7, 8, 8, 6, 1, 6, 3]))