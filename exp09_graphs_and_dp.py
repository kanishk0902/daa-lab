import minheap
from exp08_binary_search_trees import Node


def prim(n, adj):
    visited, heap, total, count = [False] * n, [(0, 0)], 0, 0
    while heap and count < n:
        w, u = minheap.pop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        count += 1
        for v, wt in adj[u]:
            if not visited[v]:
                minheap.push(heap, (wt, v))
    return total


def count_nodes(root):
    if not root:
        return 0
    lh = rh = 0
    l = r = root
    while l: lh += 1; l = l.left
    while r: rh += 1; r = r.right
    if lh == rh:
        return (1 << lh) - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def lps(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n - 2, -1, -1):
        prev = 0
        for j in range(i + 1, n):
            tmp = dp[j]
            dp[j] = prev + 2 if s[i] == s[j] else (dp[j] if dp[j] > dp[j - 1] else dp[j - 1])
            prev = tmp
    return dp[n - 1]


def complete_tree(n):
    nodes = [Node(i + 1) for i in range(n)]
    for i in range(n):
        if 2 * i + 1 < n: nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n: nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None

def run_benchmarks():
    from bench import measure, plot, make_graph, BIG, MID, nothing

    def count_every_node(root):
        return 0 if not root else 1 + count_every_node(root.left) + count_every_node(root.right)

    times = measure(BIG, lambda n: (nothing, lambda _, adj=make_graph(n), n=n: prim(n, adj)))
    plot("Experiment 9 - Prim's MST", "Number of Vertices (n)", BIG, [("", times)])
    fast = measure(BIG, lambda n: (nothing, lambda _, t=complete_tree(n): count_nodes(t)), 21)
    slow = measure(BIG, lambda n: (nothing, lambda _, t=complete_tree(n): count_every_node(t)), 21)
    plot("Experiment 9 - Count Nodes in Complete Binary Tree", "Number of Nodes (n)", BIG,
         [("Height method", fast), ("Count every node", slow)])
    times = measure(MID, lambda n: (nothing, lambda _, s="".join(chr(97 + (i * 7) % 26) for i in range(n)): lps(s)))
    plot("Experiment 9 - Longest Palindromic Subsequence", "String Length (n)", MID, [("", times)])


if __name__ == "__main__":
    edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
    adj = [[] for _ in range(5)]
    for u, v, w in edges:
        adj[u].append((v, w)); adj[v].append((u, w))
    print("Prim MST cost         :", prim(5, adj))
    print("Nodes in complete tree:", count_nodes(complete_tree(15)))
    print("LPS('bbbab')          :", lps("bbbab"))
    run_benchmarks()
