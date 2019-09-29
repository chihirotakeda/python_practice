def total_volume(*boxes):
    r = 0
    for box in boxes:
        r += box[0] * box[1] * box[2]
    return r


# total_volume([1, 2, 3])
print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
print(total_volume([2, 2, 2], [2, 1, 1]))
print(total_volume([1, 1, 1]))

