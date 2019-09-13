import itertools


def cumulative_sum(lst):
    return list(itertools.accumulate(lst))


list1 = [1, 2, 3]
list2 = [1, -2, 3]
list3 = [3, 3, -2, 408, 3, 3]
print(cumulative_sum(list1))
print(cumulative_sum(list2))
print(cumulative_sum(list3))


# リスト内包表記 reference (shorturl.at/uBMW7)
# sum() could take a list as an argument and returns sum of all values (https://pycarnival.com/sum/)

def cumulative_sum_list(lst):
    return [sum(lst[:i+1]) for i in range(len(lst)) ]


print(cumulative_sum_list(list1))
print(cumulative_sum_list(list2))
print(cumulative_sum_list(list3))