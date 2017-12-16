def load_lines(file):
    raw_lines = file.split('\n')
    lines = [[] for i in range(len(raw_lines))]
    for line in raw_lines:
        parts = line.split(" <-> ")
        line_in = int(parts[0])
        line_out = [int(n) for n in parts[1].split(", ")]
        lines[line_in] = line_out
    return lines


def load_nodes(file):
    return [i for i in range(len(file.split('\n')))]


def connected(nodes, comm_lines, reachable=None):
    if reachable is None:
        reachable = []

    if len(reachable) == len(set(reachable + nodes)):
        return reachable

    reachable = list(set(reachable + nodes))

    for node in nodes:
        if len(reachable) != len(set(reachable + comm_lines[node])):
            reachable = list(set(reachable + connected(comm_lines[node], comm_lines, reachable)))

    return reachable


def answer(puzzle_input):
    comm_lines = load_lines(puzzle_input)
    nodes = load_nodes(puzzle_input)
    connected_to_root = connected(comm_lines[0], comm_lines)
    groups = [connected_to_root]
    unreachable = [node for node in nodes if node not in connected_to_root]
    while len(unreachable) > 0:
        group = connected([unreachable[0]], comm_lines)
        groups.append(group)
        unreachable = [node for node in unreachable if node not in group]

    print(len(groups))






test = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''
puzzle_input = open('12-input.txt', 'r').read()

answer(test)
answer(puzzle_input)