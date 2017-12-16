def generator(a, b, divisor):
    while True:
        product = a*b
        a = product % 2147483647
        if a % divisor == 0:
            yield "{:032b}".format(a)


def answer(iterations=40000000, a_seed=516, b_seed=190):
    a = generator(a_seed, 16807, 4)
    b = generator(b_seed, 48271, 8)
    matches = [i for i in range(iterations) if next(a)[16:] == next(b)[16:]]
    return len(matches)


# print(answer())
# print(answer(1056, 65, 8921) == 1)
print(answer(5000000))
