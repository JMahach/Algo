def is_power(n):
    return (n & (n - 1)) == 0 and n != 0


test = [16, 1, 60, 64, 1024, 1026, 0]
print(list((is_power(n)) for n in test))
