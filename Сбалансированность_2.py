from itertools import permutations

def is_cycle(vertex_sequence, graph):
    j = 0
    for i in range(len(vertex_sequence)):
        if graph[vertex_sequence[i-1]][vertex_sequence[i]] == 0:
            return False, 0
        j += 1
    return True, j

def is_positive_cycle(vertex_sequence, graph):
    sign = 1
    for i in range(len(vertex_sequence)):
        sign *= graph[vertex_sequence[i-1]][vertex_sequence[i]]
    return sign == 1

def get_cycles_number(graph):
    n = len(graph)
    length_all = [0] * (n + 1)
    length_pos = [0] * (n + 1)
    for mask in range(1 << n):
        vertexes = []
        for i in range(n):
            if mask & (1 << i):
                vertexes.append(i)
        if len(vertexes) <= 2:
            continue
        for vertex_sequence in permutations(vertexes):
            cycle = is_cycle(vertex_sequence, graph)
            if cycle[0]:
                length_all[cycle[1]] += 1
                if is_positive_cycle(vertex_sequence, graph):
                    length_pos[cycle[1]] += 1
        pos_m = 0
        all_m = 0
        for i in range(1, n+1):
          pos_m += length_pos[i]*1.0/(2*i**2)
          all_m += length_all[i]*1.0/(2*i**2)

    return pos_m/all_m

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u][v] = c
    graph[v][u] = c
    
res = get_cycles_number(graph)
print(f"Balance of the graph 2: {res[0]}")
