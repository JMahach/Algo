# первое подходящее значение
def left_s(left, right, check, *par):
    while left < right:
        m = (left + right) // 2
        if check(m, *par):
            right = m
        else:
            left = m + 1
    return left


# последнее подходящее значение
def right_s(left, right, check, *par):
    while left < right:
        m = (left + right + 1) // 2
        if check(m, *par):
            left = m
        else:
            right = m - 1
    return left


def check_parents(m, *params):
    n, k = params
    return (k + m) * 3 >= n + m


def check_ex(m, *params):
    n, k = params
    return (k*m + m**2) / 2 >= n


def check_stickers(m, *params):
    n, w, h = params
    return ((w // m) * (h // m)) >= n


def check_number(m, *params):
    x = params[0]
    return x  # n[m] >= x


# print(left_s(0, len(n)-1, check_number, x))
