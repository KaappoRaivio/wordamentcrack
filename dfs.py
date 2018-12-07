"""

vector<pair<int,int>> adjacents[4][4];
bool visited[4][4];

void dfs(int x, int y) {
    if (visited[x][y]) return;
    visited[x][y] = 1;
    // handle the case
    for (auto adjacent : adjacents[x][y]) {
        dfs(adjacent.first, adjacent.second);
    }
    visited[x][y] = 0;
}

"""
from typing import List, Tuple


def dfs(x: int, y: int, visited: List[List[bool]], adjacents: List[List[List[Tuple[int ,int]]]]):
    if visited[x][y]:
        return
    else:
        visited[x][y] = True

    for adjacent in adjacents[x][y]:
        dfs(adjacent[0], adjacent[1], visited, adjacents)


