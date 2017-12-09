def bang(string, i):
    return i+2


def group(string, i, depth):
    score = 0
    garbage_score = 0
    depth += 1
    i += 1
    while i < len(string):
        if string[i] == '}':
            i += 1
            break
        if string[i] in group_funcs.keys():
            i, func_score, func_garbage_score = group_funcs[string[i]](string, i, depth)
            garbage_score += func_garbage_score
            score += func_score
        else:
            i += 1
    return i, score+depth, garbage_score


def garbage(string, i, depth):
    i += 1
    score = 0
    while i < len(string):
        if string[i] == '>':
            i += 1
            break
        if string[i] in garbage_funcs.keys():
            i = garbage_funcs[string[i]](string, i)
        else:
            score += 1
            i += 1

    return i, 0, score


group_funcs = {
    '{': group,
    '<': garbage,
}

garbage_funcs = {
    '!': bang
}


def score(string):
    i, score, garbage_score = group(string, 0, 0)
    print(string)
    print(score)
    print(garbage_score)


def score_all(strings):
    for string in strings:
        score(string)


puzzle_input = open('09-input.txt', 'r').read()

garbage_tests = [
    '{<>}',
    '{<random characters>}',
    '{<<<<>}',
    '{<{!>}>}',
    '{<!!>}',
    '{<!!!>>}',
    '{<{o"i!a,<{i<a>}'
]

group_tests = [
    '{}',
    '{{{}}}',
    '{{},{}}',
    '{{{},{},{{}}}}',
    '{<a>,<a>,<a>,<a>}',
    '{{<ab>},{<ab>},{<ab>},{<ab>}}',
    '{{<a>},{<a>},{<a>},{<a>}}',
    '{{<!>},{<!>},{<!>},{<a>}}'
]

# score_all(garbage_tests)
# score_all(group_tests)
score(puzzle_input)