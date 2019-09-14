def calculate_exponent(num, exp):
    result = num
    for i in range(exp - 1):
        result = result * num
    return result


print(calculate_exponent(3, 3))
print(calculate_exponent(10, 10))
print(calculate_exponent(5, 5))

def calculate_exponent_2(num, exp):
    return num ** exp


print(calculate_exponent_2(3, 3))
print(calculate_exponent_2(10, 10))
print(calculate_exponent_2(5, 5))

