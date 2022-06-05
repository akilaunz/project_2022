from itertools import permutations
def is_cycle(vertex_sequence, graph):
    for i in range(len(vertex_sequence)):
        if graph[vertex_sequence[i-1]][vertex_sequence[i]] == 0:
            return False
    return True
def is_positive_cycle(vertex_sequence, graph):
    sign = 1
    for i in range(len(vertex_sequence)):
        sign *= graph[vertex_sequence[i-1]][vertex_sequence[i]]
    return sign == 1
def get_cycles_number(graph):
    cycles_number = 0
    positive_cycles_number = 0
    n = len(graph)
    for mask in range(1 << n):
        vertexes = []
        for i in range(n):
            if mask & (1 << i):
                vertexes.append(i)
        if len(vertexes) <= 2:
            continue
        cur_cycles_number = 0
        cur_positive_number = 0
        for vertex_sequence in permutations(vertexes):
            if is_cycle(vertex_sequence, graph):
                cur_cycles_number += 1
                if is_positive_cycle(vertex_sequence, graph):
                    cur_positive_number += 1
        cur_cycles_number //= (2 * len(vertex_sequence))
        cur_positive_number //= (2 * len(vertex_sequence))
        cycles_number += cur_cycles_number
        positive_cycles_number += cur_positive_number
    return cycles_number, positive_cycles_number
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u][v] = c
    graph[v][u] = c
res = get_cycles_number(graph)
print(f"Cycles: {res[0]}")
print(f"Positive cycles {res[1]}")
print(f"Balance of the graph =  {res[1]/res[0]}")
