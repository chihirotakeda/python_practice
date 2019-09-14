def difference_max_min(lst):
    min_nun = min(lst)
    max_num = max(lst)
    difference = (max_num - min_nun)
    return difference


list1 = [10,4,1,2,8,91]
list2 = [-70,43,34,54,22]

print(difference_max_min(list1))
print(difference_max_min(list2))

# simpler code


def difference_max_min_2(lst):
    return max(lst) - min(lst)


print(difference_max_min_2(list1))
print(difference_max_min_2(list2))