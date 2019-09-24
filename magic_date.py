def magic(txt):
    lst = txt.split()
    if int(lst[0]) * int(lst[1]) == int(lst[2][-1]):
        return True
    elif int(lst[0]) * int(lst[1]) == int(lst[2][2:]):
        return True
    elif int(lst[0]) * int(lst[1]) == int(lst[2][3:]):
        return True
    else:
        return False


print(magic("1 1 2011"))
print(magic("4 1 2001"))
print(magic("5 2 2010"))
print(magic("9 2 2011"))


def magic_2(txt):
    lst = txt.split()
    day_month = int(lst[0]) * int(lst[1])
    last_1 = int(lst[2][-1])
    last_2 = int(lst[2][2:])
    last_3 = int(lst[2][3:])
    if day_month == (last_1 or last_2 or last_3):
        return True
    else:
        return False


print(magic_2("1 1 2011"))
print(magic_2("4 1 2001"))
print(magic_2("5 2 2010"))
print(magic_2("9 2 2011"))


def magic_3(txt):
    month, day, year = [int(txt[:2]), int(txt[2:4]), txt[4:]]
    return True if year.endswith(str(month * day)) else False


print(magic_3("1 1 2011"))
print(magic_3("4 1 2001"))
print(magic_3("5 2 2010"))
print(magic_3("9 2 2011"))
