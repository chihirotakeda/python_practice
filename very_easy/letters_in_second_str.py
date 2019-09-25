
def letters_in_second_str(x):
    for char in x[1]:
        if char not in x[0].lower():
            return False
    return True


list_1 = ["trances", "nectar"]
list_3 = ["parses", "parsecs"]
list_4 = ["THE EYES", "they see"]


print(letters_in_second_str(list_1))
print (letters_in_second_str(list_3))
print (letters_in_second_str(list_4))