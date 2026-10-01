def average(scores):
    total = 0
    for s in scores:
        total = total + s

    if len(scores) == 0:
        return 0

    return total / len(scores)


print(average([90, 85, 77]))
print(average([]))