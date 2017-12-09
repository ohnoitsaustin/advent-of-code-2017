def forking_nodes(list_of_nodes):
    nodes_with_forks = [line for line in list_of_nodes if "->" in line]
    return nodes_with_forks


def fork_relationships(list_of_forks):
    return {forks.split()[0]: forks.split("-> ")[1].split(", ") for forks in list_of_forks}


def root_of_tree(list_of_nodes):
    list_of_forks = forking_nodes(list_of_nodes)
    forks = fork_relationships(list_of_forks)
    all_children = [child for children in forks.values() for child in children]
    root = [parent for parent in forks.keys() if parent not in all_children][0]
    return root


def node_weights(list_of_nodes):
    nodes = {}
    for node in list_of_nodes:
        if("->" in node):
            node_parts = node.split(" ->")[0].split()
        else:
            node_parts = node.split()
        nodes[node_parts[0]] = int(node_parts[1][1:-1])

    return nodes


def has_children(fork, forks):
    return fork in forks.keys()


def weight_of(root, forks, weights):
    node_weights = [0 for i in range(len(forks[root]))]
    for i, node in enumerate(forks[root]):
        if has_children(node, forks):
            node_weights[i] = weights[node] + weight_of(node, forks, weights)
        else:
            node_weights[i] = weights[node]

    if len(set(node_weights)) != 1:
        print(root, 'result:', weights[root], forks[root], node_weights, weights[root] + sum(node_weights))

    return sum(node_weights)



def answer(puzzle_input):
    list_of_nodes = puzzle_input.split("\n")
    root = root_of_tree(list_of_nodes)
    weights = node_weights(list_of_nodes)
    forks = fork_relationships(forking_nodes(list_of_nodes))
    fork_weights = weight_of(root, forks, weights)

    print(fork_weights)

    return root


puzzle_input = open('07-input.txt', 'r').read()
test = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''


# answer(test)
answer(puzzle_input)