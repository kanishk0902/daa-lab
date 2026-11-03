INF = float('inf')


def bellman_ford(n, edges, src):
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            return dist
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None
    return dist


def floyd_warshall(d):
    n = len(d)
    for k in range(n):
        dk = d[k]
        for i in range(n):
            dik = d[i][k]
            if dik == INF:
                continue
            d[i] = [a if a <= dik + b else dik + b for a, b in zip(d[i], dk)]
    return d


def find_city(n, edges, threshold):
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    floyd_warshall(d)
    best, city = INF, -1
    for i in range(n):
        cnt = 0
        for j in range(n):
            if j != i and d[i][j] <= threshold:
                cnt += 1
        if cnt <= best:
            best, city = cnt, i
    return city

def run_benchmarks():
    from bench import measure, plot, MID, SMALL, nothing

    def chain_edges(n, reverse):
        edges = [(i, i + 1, 1) for i in range(n - 1)] + [(i, i + 2, 3) for i in range(n - 2)]
        return edges[::-1] if reverse else edges

    good = measure(MID, lambda n: (nothing, lambda _, e=chain_edges(n, False), n=n: bellman_ford(n, e, 0)))
    bad = measure(MID, lambda n: (nothing, lambda _, e=chain_edges(n, True), n=n: bellman_ford(n, e, 0)))
    plot("Experiment 11 - Bellman-Ford Algorithm", "Number of Vertices (n)", MID,
         [("Favourable edge order", good), ("Reversed edge order", bad)])

    def floyd_input(n):
        base = [[INF] * n for _ in range(n)]
        for i in range(n):
            base[i][i] = 0
            base[i][(i + 1) % n] = i % 9 + 1
            base[i][(i + 3) % n] = i % 7 + 2
        return (lambda: [row[:] for row in base]), floyd_warshall

    plot("Experiment 11 - Floyd-Warshall Algorithm", "Number of Vertices (n)", SMALL, [("", measure(SMALL, floyd_input))])

    def city_input(n):
        edges = [(i, (i + 1) % n, i % 9 + 1) for i in range(n)] + [(i, (i + 3) % n, i % 7 + 2) for i in range(n)]
        return nothing, lambda _: find_city(n, edges, 50)

    plot("Experiment 11 - City with Fewest Reachable Neighbors", "Number of Cities (n)", SMALL, [("", measure(SMALL, city_input))])


if __name__ == "__main__":
    e = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
    print("Bellman-Ford          :", bellman_ford(5, e, 0))
    print("With negative cycle   :", bellman_ford(5, e + [(2, 0, -5)], 0))
    g = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
    print("Floyd-Warshall row 0  :", floyd_warshall([r[:] for r in g])[0])
    print("City (threshold 4)    :", find_city(4, [(0, 1, 3), (1, 2, 1), (1, 3, 4), (2, 3, 1)], 4))
    run_benchmarks()
