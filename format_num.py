def format_num(n):
    formatted_n = "{:,}".format(n)
    return formatted_n


n1 = format_num(123000)
print(n1)

# print("{:,}".format(123000))
