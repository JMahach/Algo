M = 10**9 + 7
P = 31


def hash(string):
    m = len(string)
    return sum(ord(string[i]) * pow(P, m-i-1) for i in range(m)) % M


def list_polinoms(strint):
    m = len(strint)
    list_hash = [hash(strint[0:1])]
    for i in range(m-1):
        list_hash.append((list_hash[i]*P + ord(strint[i+1])) % M)
    return list_hash


def rabin_karp(pattern, text):
    result = []
    n = len(text)
    m = len(pattern)

    pattern_hash = hash(pattern)
    window_hash = hash(text[0:m])
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i + m]:
                result.append(i)
        if i < n - m:
            window_hash = (window_hash*P
                           + ord(text[i+m])
                           - ord(text[i])*(P**m)) % M
    return result


def rabin_karp_polinoms_list(pattern, text):
    result = []
    n = len(text)
    m = len(pattern)

    pattern_hash = hash(pattern)
    text_polinoms_list = list_polinoms(text)
    window_hash = text_polinoms_list[m-1]
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i + m]:
                result.append(i)
        if i < n - m:
            window_hash = (text_polinoms_list[i+m]
                           - text_polinoms_list[i]*P**(m)) % M
    return result


text = 'abcabcabc'
pattern = 'abc'
indices = rabin_karp_polinoms_list(pattern, text)
print(f'Подстрока {pattern} найдена в '
      f'тексте {text} по индексам: {indices}')
