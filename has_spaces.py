def has_spaces(txt):
    for i in txt:
        if i == " ":
            return True
    return False


print(has_spaces("hello"))
print(has_spaces("hello, world"))
print(has_spaces(" "))
print(has_spaces(""))
print(has_spaces(",./!@#"))


def has_spaces_2(txt):
    return " " in txt


print(has_spaces_2("hello"))
print(has_spaces_2("hello, world"))
print(has_spaces_2(" "))
print(has_spaces_2(""))
print(has_spaces_2(",./!@#"))