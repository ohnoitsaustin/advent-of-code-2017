def within_memory(i, memory):
    return len(memory) > i >= 0


def increase_by_one(amount):
    return amount + 1


def increase_by_one_if_below_three(amount):
    return amount - 1 if amount >= 3 else amount + 1


def count_jumps(puzzle_input, register_update):
    memory = [int(i) for i in puzzle_input.split('\n')]
    time = i = 0
    while within_memory(i, memory):
        jump_amount = memory[i]
        memory[i] = register_update(memory[i])
        i += jump_amount
        time += 1

    return time



test = '''0
3
0
1
-3'''
print(count_jumps(test, increase_by_one))
puzzle_input = open('05-input.txt', 'r').read()
print(count_jumps(puzzle_input, increase_by_one))

print(count_jumps(test, increase_by_one_if_below_three))
print(count_jumps(puzzle_input, increase_by_one_if_below_three))