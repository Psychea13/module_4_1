from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return int(first/second)


# print(divide(4, 0))
# print(divide(4, 2))