prime = 101

def pattern_matching(text, pattern):
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(pattern, m - 1)
    text_hash = create_hash(text, m - 1)

    for i in range(1, n - m + 2):
        if pattern_hash == text_hash:
            return i - 1

        if i < n - m + 1:
            text_hash = recalculate_hash(text, text_hash, i, m)

    return -1


def recalculate_hash(text, old_hash, index, p_size):

    old_hash = (old_hash - ord(text[index - 1]))
    old_hash = old_hash/prime
    old_hash += ord(text[index + p_size - 1]) * pow(prime, p_size-1)
   # print (old_hash)

    return old_hash


def create_hash(arr, s):
    a_hash = 0
    for i in range(s + 1):
        a_hash = a_hash + ord(arr[i]) * pow(prime, i)
    print(a_hash)
    return a_hash


print(pattern_matching("Vijay Shanker", "er"))
