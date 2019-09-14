def num_to_dashes(num):
    dash = []
    for i in range(num):
        dash.append("-")
    return ''.join(dash)


print(num_to_dashes(1))
print(num_to_dashes(5))
print(num_to_dashes(3))


def num_to_dashes_2(num):
    return "-" * num


print(num_to_dashes_2(1))
print(num_to_dashes_2(5))
print(num_to_dashes_2(3))