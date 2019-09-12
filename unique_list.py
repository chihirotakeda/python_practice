def unique_lst(lst):
    new_lst = sorted(set(lst), key=lst.index)
    unique_list = []
    for i in new_lst:
        if i > 0:
            unique_list.append(i)
    return unique_list


list1 =[-5, 1, -7, -5, -2, 3, 3, -5, -1, -1]
list2 = [3, -3, -3, 5, 5, -6, -2, -4, -1, 3]
list3 = [10, 6, -12, 13, 5, 5, 13, 6, 5]

# print(unique_lst(list1))
# print(unique_lst(list2))
# print(unique_lst(list3))

def unique_lst_loop(lst):
    new_lst_loop = []
    for i in lst:
        if i > 0 and i not in new_lst_loop:
            new_lst_loop.append(i)
    return new_lst_loop


print(unique_lst_loop(list1))
print(unique_lst_loop(list2))
print(unique_lst_loop(list3))