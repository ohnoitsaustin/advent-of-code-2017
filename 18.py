import re


def read_line(line):
    tokens = line.split()
    return {
        'cmd': tokens[0],
        'register': tokens[1],
        'value': tokens[2] if len(tokens) > 2 else None,
    }


def read_puzzle(puzzle_input):
    return [read_line(line) for line in puzzle_input.split('\n')]


def initialize_memory(instructions):
    return {i: 0 for i in set([i['register'] for i in instructions])}


def pull(index, memory):
    return int(memory[index]) if re.match('[a-z]', index) else int(index)


def snd(i, memory, register, value):
    memory['snd'] = pull(register, memory)
    return i+1, memory


def set_(i, memory, register, value):
    memory[register] = pull(value, memory)
    return i+1, memory


def add(i, memory, register, value):
    memory[register] += pull(value, memory)
    return i+1, memory


def mul(i, memory, register, value):
    memory[register] *= pull(value, memory)
    return i+1, memory


def mod(i, memory, register, value):
    memory[register] %= pull(value, memory)
    return i+1, memory


def rcv(i, memory, register, value):
    if pull(register, memory) != 0:
        memory['rcv'] = memory['snd']
    return i+1, memory


def jgz(i, memory, register, value):
    if pull(register, memory):
        return i+pull(value, memory), memory
    return i+1, memory


def answer(puzzle_input):
    cmds = {
        'snd': snd,
        'set': set_,
        'add': add,
        'mul': mul,
        'mod': mod,
        'rcv': rcv,
        'jgz': jgz,
    }
    instructions = read_puzzle(puzzle_input)
    memory = initialize_memory(instructions)
    memory['snd'] = None
    memory['rcv'] = None
    i = 0
    print(memory)
    while memory['rcv'] is None and 0 <= i  < len(instructions):
        i, memory = cmds[instructions[i]['cmd']](i, memory, instructions[i]['register'], instructions[i]['value'])

    print(memory)


test = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''
puzzle_input = open('18-input.txt', 'r').read()

answer(test)
answer(puzzle_input)