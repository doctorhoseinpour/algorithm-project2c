import random


def generate_graph(v, e):
    adjacency_list = {}
    for i in range(1, v + 1):
        adjacency_list[i] = []

    edges = set()

    while len(edges) < e:
        v1 = random.randint(1, v)
        v2 = random.randint(1, v)
        if v1 != v2 and (v1, v2) not in edges:
            edges.add((v1, v2))
            adjacency_list[v1].append(v2)

    return adjacency_list