import random, itertools, heapq
from exp01_sorting_fundamentals import *
from exp02_divide_and_conquer import *
from exp03_matrices_and_selection import *
from exp04_selection_and_dp import *
from exp05_heap_applications import *
from exp06_linear_time_sorting import *
from assessment1 import *
from exp07_hashing import *
from exp08_binary_search_trees import *
from exp09_graphs_and_dp import *
from exp10_shortest_paths import *
from exp11_advanced_graphs import *

R = random.Random(7)
rl = lambda n, lo, hi: [R.randint(lo, hi) for _ in range(n)]
INFV = float('inf')

for _ in range(1500):
    a = rl(R.randint(0, 12), -9, 9)
    assert insertion_sort_iter(a[:]) == insertion_sort_rec(a[:]) == merge_sort(a) == heap_sort(a[:]) == sorted(a)
    assert count_inversions(a) == sum(a[i] > a[j] for i in range(len(a)) for j in range(i + 1, len(a)))
    d = rl(R.randint(0, 12), 0, 2)
    assert dutch_flag(d[:]) == sorted(d)
    m = majority_element(a)
    assert m == next((x for x in set(a) if a.count(x) > len(a) // 2), None)
    A, B = sorted(set(rl(6, 0, 9))), sorted(set(rl(6, 0, 9)))
    assert union_intersection(A, B) == (sorted(set(A) | set(B)), sorted(set(A) & set(B)))
    s = sorted(set(rl(8, -20, 20))); r = R.randint(0, len(s) - 1); rot = s[r:] + s[:r]
    t = R.randint(-20, 20)
    assert search_rotated(rot, t) == (rot.index(t) if t in rot else -1)
print("exp 1-2 ok")

for _ in range(300):
    n = R.randint(1, 6)
    A = [rl(n, -5, 5) for _ in range(n)]; B = [rl(n, -5, 5) for _ in range(n)]
    assert strassen(A, B) == mat_mul(A, B)
    books = rl(R.randint(1, 7), 1, 30); st = R.randint(1, len(books))
    best = min(max(sum(books[i:j]) for i, j in zip((0,) + c, c + (len(books),)))
               for c in itertools.combinations(range(1, len(books)), st - 1))
    assert allocate_pages(books, st) == best
    X, Y = sorted(rl(R.randint(0, 6), -9, 9)), sorted(rl(R.randint(1, 6), -9, 9))
    z = sorted(X + Y); h = len(z) // 2
    assert median_two_sorted(X, Y) == (z[h] if len(z) % 2 else (z[h - 1] + z[h]) / 2)
print("exp 3 ok")

def brute_prod(a):
    best = a[0]
    for i in range(len(a)):
        p = 1
        for j in range(i, len(a)):
            p *= a[j]; best = max(best, p)
    return best
for _ in range(1500):
    a = rl(R.randint(1, 9), -4, 4)
    assert max_product_subarray(a) == brute_prod(a)
    k = R.randint(1, len(a)); assert kth_largest(a, k) == sorted(a, reverse=True)[k - 1]
    assert median_of_medians(a, k) == sorted(a)[k - 1]
    pos = rl(R.randint(1, 10), -3, 12); mm = 1
    while mm in pos: mm += 1
    assert smallest_missing_positive(pos) == mm
for n in range(200):
    x, y = 0, 1
    for _ in range(n): x, y = y, x + y
    assert fibonacci(n) == x
print("exp 4 ok")

for _ in range(1500):
    s = "".join(R.choice("abc") for _ in range(R.randint(1, 8)))
    out = rearrange_string(s)
    cnt = {c: s.count(c) for c in s}
    feasible = max(cnt.values()) <= (len(s) + 1) // 2
    assert (out != "") == feasible
    if out: assert sorted(out) == sorted(s) and all(out[i] != out[i + 1] for i in range(len(out) - 1))
    arrs = [sorted(rl(R.randint(0, 5), 0, 20)) for _ in range(R.randint(1, 5))]
    assert merge_k_sorted(arrs) == sorted(sum(arrs, []))
print("exp 5 ok")

def brute_halve(a, k):
    a = a[:]
    for _ in range(k):
        i = a.index(max(a)); a[i] = (a[i] + 1) // 2
    return sum(a)
for _ in range(1500):
    a = rl(R.randint(1, 10), 0, 30)
    assert counting_sort(a) == sorted(a)
    f = [R.random() for _ in range(R.randint(1, 10))]; assert bucket_sort(f) == sorted(f)
    b = rl(R.randint(1, 9), 1, 4); k = R.randint(1, 4)
    assert subarrays_with_k_distinct(b, k) == sum(len(set(b[i:j])) == k for i in range(len(b)) for j in range(i + 1, len(b) + 1))
    c = rl(R.randint(1, 6), 1, 40); kk = R.randint(0, 8)
    assert min_sum_after_k_ops(c, kk) == brute_halve(c, kk)
print("exp 6 ok")

for _ in range(1500):
    coins = sorted(set(rl(3, 1, 7))); amt = R.randint(0, 20)
    best = min((n for n in range(amt + 1) for c in itertools.combinations_with_replacement(coins, n) if sum(c) == amt), default=-1) if amt <= 12 else coin_change(coins, amt)
    assert coin_change(coins, amt) == best
    u = list(set(rl(R.randint(1, 4), 1, 9))); arr = u + u + [R.randint(10, 20)]; R.shuffle(arr)
    assert single_number(arr) == [x for x in arr if arr.count(x) == 1][0]
    pts = sorted(set(rl(R.randint(2, 7), 0, 30)))
    if len(pts) < 2: continue
    k = R.randint(2, len(pts))
    assert max_min_diff(pts, k) == max(min(b - a for a, b in zip(c, c[1:])) for c in itertools.combinations(pts, k))
print("assessment 1 ok")

for _ in range(1500):
    A = rl(R.randint(0, 12), 0, 9); B = list(set(rl(R.randint(0, 5), 0, 9)))
    exp = [x for b in B for x in [b] * A.count(b)] + sorted(x for x in A if x not in B)
    assert relative_sort(A, B) == exp
    s = "".join(R.choice("abc") for _ in range(R.randint(0, 9))); t = "".join(R.choice("abc") for _ in range(R.randint(1, 3)))
    cand = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)
            if all(s[i:j].count(c) >= t.count(c) for c in t)]
    got = min_window(s, t)
    assert (got == "" and not cand) or len(got) == min(map(len, cand))
    keys = rl(R.randint(1, 8), 0, 40)
    for H in (ChainingHashTable(11), LinearProbingHashTable(11)):
        for k in keys: H.insert(k)
        assert all(H.search(k) for k in keys) and all(H.search(q) == (q in keys) for q in range(45))
print("exp 7 ok")

def is_bst(n, lo=-INFV, hi=INFV):
    return n is None or (lo < n.val < hi and is_bst(n.left, lo, n.val) and is_bst(n.right, n.val, hi))
def size(n): return 0 if n is None else 1 + size(n.left) + size(n.right)
def brute_lbst(n):
    if n is None: return 0
    return size(n) if is_bst(n) else max(brute_lbst(n.left), brute_lbst(n.right))
def rand_tree(depth):
    if depth == 0 or R.random() < 0.2: return None
    n = Node(R.randint(0, 30)); n.left = rand_tree(depth - 1); n.right = rand_tree(depth - 1); return n
for _ in range(1500):
    root = None; vals = rl(R.randint(1, 12), 0, 40)
    for v in vals: root = insert(root, v)
    assert inorder(root) == sorted(set(vals)) and is_bst(root)
    u = sorted(set(vals)); p, q = R.choice(u), R.choice(u)
    lo, hi = min(p, q), max(p, q)
    assert lca(root, p, q).val in [x for x in u if lo <= x <= hi]
    tr = rand_tree(5); assert largest_bst(tr) == brute_lbst(tr)
print("exp 8 ok")

def rand_graph(n):
    edges = {}
    for i in range(1, n): edges[(R.randint(0, i - 1), i)] = R.randint(1, 20)
    for _ in range(R.randint(0, n)):
        u, v = R.sample(range(n), 2)
        if (min(u, v), max(u, v)) not in edges: edges[(min(u, v), max(u, v))] = R.randint(1, 20)
    return [(u, v, w) for (u, v), w in edges.items()]
def apsp(n, edges):
    d = [[INFV] * n for _ in range(n)]
    for i in range(n): d[i][i] = 0
    for u, v, w in edges: d[u][v] = d[v][u] = w
    for k in range(n):
        for i in range(n):
            for j in range(n): d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
for _ in range(600):
    n = R.randint(1, 8)
    ed = rand_graph(n) if n > 1 else []
    adj = build_adj(n, ed)
    par = list(range(n))
    def f(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    mst = 0
    for u, v, w in sorted(ed, key=lambda e: e[2]):
        if f(u) != f(v): par[f(u)] = f(v); mst += w
    assert prim(n, adj) == mst
    d = apsp(n, ed)
    assert dijkstra(n, adj, 0) == d[0]
    assert bellman_ford(n, [(u, v, w) for u, v, w in ed] + [(v, u, w) for u, v, w in ed], 0) == d[0]
    assert floyd_warshall([[0 if i == j else INFV for j in range(n)] for i in range(n)]) is not None
    th = R.randint(1, 30)
    cnts = [sum(1 for j in range(n) if j != i and d[i][j] <= th) for i in range(n)]
    assert find_city(n, ed, th) == max(i for i in range(n) if cnts[i] == min(cnts))
    if n > 1:
        t = R.randint(1, n - 1)
        bb = 0
        for thr in sorted({w for _, _, w in ed}):
            seen, st = {0}, [0]
            while st:
                x = st.pop()
                for y, w in adj[x]:
                    if w >= thr and y not in seen: seen.add(y); st.append(y)
            if t in seen: bb = thr
        assert max_bottleneck(n, adj, 0, t) == bb
    m = [[0 if i == j else INFV for j in range(n)] for i in range(n)]
    for u, v, w in ed: m[u][v] = m[v][u] = w
    assert floyd_warshall(m) == d
for _ in range(1500):
    p = rl(R.randint(1, 9), 1, 30); fee = R.randint(0, 6)
    best = 0
    hold, cash = -INFV, 0
    for x in p:
        cash, hold = max(cash, hold + x - fee), max(hold, cash - x)
    assert max_profit(p, fee) == cash
    s = "".join(R.choice("abc") for _ in range(R.randint(1, 9)))
    sub = lambda s: max((len(c) for L in range(len(s) + 1) for c in map(lambda ix: [s[i] for i in ix], itertools.combinations(range(len(s)), L)) if c == c[::-1]), default=0)
    assert lps(s) == sub(s)
    n = R.randint(0, 40); assert count_nodes(complete_tree(n)) == n
print("exp 9-11 ok")
print("ALL TESTS PASSED")
