import operator
from functools import reduce


def to_ascii(string):
    return [ord(c) for c in string]


def knot(hash, start, end):
    hashhash = hash + hash
    subhash = hashhash[start:end]
    reverse_subhash = subhash[::-1]
    hashhash[start:end] = reverse_subhash
    hash[start:len(hash)] = hashhash[start:len(hash)]
    if end > len(hash):
        hash[0:end - len(hash)] = hashhash[len(hash):end]

    return hash


def knot_hash_lengths(string):
    lengths = to_ascii(string)
    lengths += [17, 31, 73, 47, 23]
    return lengths


def knot_hash(hash, lengths_str, length, i, skip_size):
    lengths = knot_hash_lengths(lengths_str)
    for length in lengths:
        start = i % len(hash)
        end = start + length

        knot(hash, start, end)
        i += length + skip_size
        skip_size += 1
    return hash, i, skip_size


def sparse_hash(lengths_str):
    length = 256
    i = 0
    skip_size = 0
    hash = [i for i in range(length)]
    for j in range(64):
        hash, i, skip_size = knot_hash(hash, lengths_str, length, i, skip_size)

    return hash


def dense_hash(sparse):
    return [reduce(operator.xor, sparse[i * 16:i * 16 + 16]) for i in range(int(len(sparse) / 16))]


def answer(lengths_str):
    sparse = sparse_hash(lengths_str)
    dense = dense_hash(sparse)
    knot_hash_str = ['{0:02x}'.format(h) for h in dense]
    return ''.join(knot_hash_str)


puzzle_input = '157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30'
print(answer(puzzle_input))


# tests from puzzle text
# print(to_ascii('1,2,3') == [49,44,50,44,51])
# print(knot_hash_lengths('1,2,3') == [49,44,50,44,51,17,31,73,47,23])
# print(dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == [64])
# print(answer('') == 'a2582a3a0e66e6e86e3812dcb672a272')
# print(answer('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d')
# print(answer('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e')
# print(answer('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd')
