def highest(memory):
    return memory.index(max(memory))


def redistribute(memory, which):
    i = which(memory)
    v = memory[i]
    memory[i] = 0
    for steps in range(v):
        i = i + 1 if i < len(memory)-1 else 0
        memory[i] += 1
    return memory


def snapshot(memory):
    return ''.join([str(m) for m in memory])


def answer(puzzle_input):
    memory = [int(n) for n in puzzle_input.split()]
    snapshots = [snapshot(memory)]
    while len(snapshots) == len(set(snapshots)):
        memory = redistribute(memory, highest)
        snapshots.append(snapshot(memory))

    start_of_loop = snapshots.index(snapshots[-1])
    print(len(snapshots) - start_of_loop - 1)
    return len(snapshots)


puzzle_input = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"
test = "0   2   7   0"
print(answer(test))     # 5
print(answer(puzzle_input))
