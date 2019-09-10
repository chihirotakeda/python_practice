import re

def remove_vowels(txt):
    new_txt = txt.lower()
    vowels = "aiueo" #('a', 'i', 'u', 'e', 'o')
    for char in new_txt:
        if char in vowels:
            new_txt = new_txt.replace(char, '')
    return new_txt

def remove_vowels_regex(txt):
    new_txt_regex = re.sub('[aiueoAIUEO]', '', txt)
    return new_txt_regex


test_txt1 = "If Obama resigns from office NOW,\
 thereby doing a great service to the country - \
I will give him free lifetime golf at any one of my courses!"

test_txt2 = "This election is a total sham and a travesty. We are not a democracy!"


removed_txt1 = remove_vowels(test_txt1)
print(removed_txt1)

removed_txt2 = remove_vowels(test_txt2)
print (removed_txt2)

removed_text_regex1 = remove_vowels_regex(test_txt1)
print(removed_text_regex1)

removed_text_regex2 = remove_vowels_regex(test_txt2)
print(removed_text_regex2)
