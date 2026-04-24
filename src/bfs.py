def bfs(g, s, t):
    info = {}
    for v in g.keys():
        info[v] = {"color": "white", "d": float("inf"), "p": None}
    info[s] = {"color": "gray", "d": 0, "p": None}
    Q = [s]
    while Q:
        u = Q.pop(0)
        for v in g[u]:
            if info[v]["color"] == "white":
                info[v]["color"] = "gray"
                info[v]["d"] = info[u]["d"] + 1
                info[v]["p"] = u
                Q.append(v)
        if u == t:
             break
        info[u]["color"] = "black"
    return info


def print_path(info, s, t):
    if info[t]["p"] is None and s != t:
        return None

    path = ""
    current = t
    while current is not None:
        if path == "":
            path = str(current)
        else:
            path = str(current) + "-" + path
        current = info[current]["p"]

    return path

