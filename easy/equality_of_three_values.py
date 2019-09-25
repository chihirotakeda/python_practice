def equal(a, b, c):
    lst = [a, b, c]
    if len(set(lst)) == len(lst):
        return 0
    else:
        r = 0
        for i in range(len(lst)):
            if lst[i] in lst[i + 1:]:
                r += 1
        return r + 1


print(equal(3, 4, 3))
print(equal(1, 1, 1))
print(equal(3, 4, 1))


def equal_2(a, b, c):
    unique = set([a, b, c])
    if len(unique) == 3:
        return 0
    else:
        return 4 - len(unique)

