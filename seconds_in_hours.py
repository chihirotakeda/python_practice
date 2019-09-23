def seconds_in_hours(hours):
    return hours * 60 * 60


print(seconds_in_hours(2))
print(seconds_in_hours(10))
print(seconds_in_hours(24))


def convert(hours, minutes):
    return hours * 3600 + minutes * 60


print(convert(1, 3))
print(convert(2, 0))
print(convert(0, 0))

