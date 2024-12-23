def lst_divisors(n):
    ''' Возвращает список делителей числа'''
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)

    return res


def prime_number(n):
    '''Проверяет число на простоту'''
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def lst_divisors_prime(n):
    ''' возвращает список простых делителей числа'''
    res = []
    N = lst_divisors(n)

    for i in N:
        if prime_number(i) is True:
            res.append(i)
    return res


print(prime_number(8))
print(lst_divisors(8))
print(lst_divisors_prime(4))
