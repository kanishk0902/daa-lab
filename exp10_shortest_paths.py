import minheap

INF = float('inf')


def dijkstra(n, adj, src):
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = minheap.pop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                minheap.push(heap, (nd, v))
    return dist


def max_profit(prices, fee):
    cash, hold = 0, -prices[0]
    for p in prices[1:]:
        cash = max(cash, hold + p - fee)
        hold = max(hold, cash - p)
    return cash


def max_bottleneck(n, adj, src, dst):
    best = [0] * n
    best[src] = INF
    heap = [(-INF, src)]
    while heap:
        b, u = minheap.pop(heap)
        b = -b
        if u == dst:
            return b
        if b < best[u]:
            continue
        for v, w in adj[u]:
            nb = b if b < w else w
            if nb > best[v]:
                best[v] = nb
                minheap.push(heap, (-nb, v))
    return 0


def build_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w)); adj[v].append((u, w))
    return adj

def run_benchmarks():
    from bench import measure, plot, make_graph, BIG, nothing
    times = measure(BIG, lambda n: (nothing, lambda _, adj=make_graph(n), n=n: dijkstra(n, adj, 0)))
    plot("Experiment 10 - Dijkstra's Algorithm", "Number of Vertices (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, p=[(i * 31) % 97 + 1 for i in range(n)]: max_profit(p, 2)))
    plot("Experiment 10 - Stock Buy/Sell with Transaction Fee", "Number of Days (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, adj=make_graph(n), n=n: max_bottleneck(n, adj, 0, n - 1)))
    plot("Experiment 10 - Maximum Bottleneck Path", "Number of Vertices (n)", BIG, [("", times)])


if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4),
             (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
    print("Dijkstra from 0 :", dijkstra(9, build_adj(9, edges), 0))
    print("Stock with fee  :", max_profit([1, 3, 2, 8, 4, 9], 2))
    print("Bottleneck 0->2 :", max_bottleneck(3, build_adj(3, [(0, 1, 10), (1, 2, 10), (0, 2, 4)]), 0, 2))
    run_benchmarks()
