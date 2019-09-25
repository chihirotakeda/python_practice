def remove_dups(lst):
    return sorted(set(lst), key=lst.index)


print(remove_dups([1, 0, 1, 0]))
print(remove_dups(["The", "big", "cat"]))
print(remove_dups(["John", "Taylor", "John"]))