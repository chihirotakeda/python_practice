import re


def find_zip(txt):
    m = list(re.finditer('zip', txt))
    if len(m) >= 2:
        new_tuple = m[1].span()
        return new_tuple[0]
    else:
        return -1


txt1 = "all zip files are zipped"
txt2 = "all zip files are compressed"
print(find_zip(txt1))
print(find_zip(txt2))


def find_zip_2(txt):
    return txt.find('zip', txt.find('zip') + 1)


print(find_zip_2(txt1))
print(find_zip_2(txt2))

# Test.assert_equals(find_zip("all zip files are zipped"), 18)
# Test.assert_equals(find_zip("all zip files are compressed"), -1)
# Test.assert_equals(find_zip("We believe university-level zip education can be both high quality and low cost. Using the economics of the Internet, we've connected some of the greatest teachers to hundreds of thousands of students all over the world."), -1)
# Test.assert_equals(find_zip("Zip is a file format used for data compression and archiving. A zip file contains one or more files that have been compressed, to reduce file size, or stored as is. The zip file format permits a number of compression algorithms."), 169)