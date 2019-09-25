import collections

def palindrome(word: str):
    c = collections.Counter(word)
    count = 0
    for c_val in c.values():
        if c_val % 2 == 0 and count < 2:
            count = count
        elif c_val % 2 != 0 and count < 2:
            count += 1
        else:
            return False
    return True
