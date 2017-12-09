def read_line(line):
    tokens = line.split()
    return {
        'register': tokens[0],
        'cmd': tokens[1],
        'amount': tokens[2],
        'left': tokens[4],
        'cond': tokens[5],
        'right': tokens[6]
    }

def read_puzzle(puzzle_input):
    return [read_line(line) for line in puzzle_input.split('\n')]


def initialize_memory(instructions):
    return {i: 0 for i in set([i['register'] for i in instructions])}


def answer(puzzle_input):
    conditions = {
        '>': lambda x, y: int(x) > int(y),
        '<': lambda x, y: int(x) < int(y),
        '==': lambda x, y: int(x) == int(y),
        '>=': lambda x, y: int(x) >= int(y),
        '<=': lambda x, y: int(x) <= int(y),
        '!=': lambda x, y: int(x) != int(y)
    }
    cmds = {
        'inc': lambda a, b: int(a) + int(b),
        'dec': lambda a, b: int(a) - int(b)
    }
    instructions = read_puzzle(puzzle_input)
    memory = initialize_memory(instructions)
    highest = 0
    for line in instructions:
        if conditions[line['cond']](memory[line['left']], line['right']):
            memory[line['register']] = cmds[line['cmd']](memory[line['register']], line['amount'])
            if memory[line['register']] > highest:
                highest = memory[line['register']]

    print(memory)
    print(max(memory.values()))
    print(highest)


test = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''
puzzle_input = open('08-input.txt', 'r').read()

answer(test)
answer(puzzle_input)