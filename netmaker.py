
from collections import defaultdict
import pprint

_input = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"],
]
graph = {}

neighbors = {(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)}

# print(_input)

for i_y, y in enumerate(_input):
    for i_x, x in enumerate(y):
        tempset = []

        for neighbor in neighbors:
            new_y, new_x = i_y + neighbor[1], i_x + neighbor[0]
            if 0 <= new_y < 4 and 0 <= new_x < 4:
                try:
                    node = _input[new_y][new_x]
                    tempset.append(node)
                except Exception as e:
                    pass
                    # print(i_x, i_y, neighbor)


        graph[x] = set(tempset)


current = []

def dfs(value, adjacents, visited):
    if visited.get(value, False):
        return None
    else:
        visited[value] = True

    current.append(value)
    # print(''.join(current))

    for adjacent in adjacents[value]:
        dfs(adjacent, adjacents, visited)

    current.pop()
    visited[value] = False


# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(graph)
visited = defaultdict()

for y in _input:
    for x in y:
        dfs(x, graph, visited)
