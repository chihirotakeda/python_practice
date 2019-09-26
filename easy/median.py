import numpy


def median(lst):
    sorted_lst = sorted(lst)
    l = len(lst)
    if l % 2 == 1:
        return sorted_lst[int((l - 1) / 2)]
    elif l % 2 == 0:
        return int((sorted_lst[int(l/2 - 1)] + sorted_lst[int(l/2)]) / 2)


print(median([2, 5, 6, 2, 6, 3, 4]))
print(median([21.4323, 432.54, 432.3, 542.4567]))
print(median([-23, -43, -29, -53, -67]))
print((median([342, 98, 5456, 32, 786, 432, 890, 321])))


def median_2(lst):
    lst.sort()
    n = len(lst)
    m = n // 2
    if n % 2 == 0:
        return (lst[m - 1] + lst(m)) / 2
    else:
        return lst[m]


def median_3(lst):
    return numpy.median(lst)

