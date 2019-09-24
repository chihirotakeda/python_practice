def index_of_caps(word):
    lst = []
    for i in range(len(word)):
        if word[i].isupper():
            lst.append(i)
    return lst


print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))