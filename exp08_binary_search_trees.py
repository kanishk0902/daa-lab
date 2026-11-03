class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def insert(root, val):
    if root is None:
        return Node(val)
    cur = root
    while True:
        if val < cur.val:
            if cur.left is None:
                cur.left = Node(val); return root
            cur = cur.left
        elif val > cur.val:
            if cur.right is None:
                cur.right = Node(val); return root
            cur = cur.right
        else:
            return root


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def lca(root, p, q):
    while root:
        if p < root.val and q < root.val: root = root.left
        elif p > root.val and q > root.val: root = root.right
        else: return root
    return None


def largest_bst(root):
    best = 0

    def post(node):
        nonlocal best
        if node is None:
            return 0, float('inf'), float('-inf')
        ls, llo, lhi = post(node.left)
        rs, rlo, rhi = post(node.right)
        if ls >= 0 and rs >= 0 and lhi < node.val < rlo:
            size = ls + rs + 1
            best = max(best, size)
            return size, min(llo, node.val), max(rhi, node.val)
        return -1, 0, 0

    post(root)
    return best

def run_benchmarks():
    import random
    from bench import measure, plot, BIG, nothing

    def balanced(vals, lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = Node(vals[mid])
        node.left = balanced(vals, lo, mid - 1)
        node.right = balanced(vals, mid + 1, hi)
        return node

    def build_input(n):
        keys = [random.randint(0, 10 * n) for _ in range(n)]

        def run(_):
            root = None
            for k in keys:
                root = insert(root, k)

        return nothing, run

    plot("Experiment 8 - BST Construction", "Number of Keys (n)", BIG, [("", measure(BIG, build_input))])
    times = measure(BIG, lambda n: (nothing, lambda _, t=balanced(list(range(n)), 0, n - 1), n=n: [lca(t, 0, n - 1) for _ in range(500)]))
    plot("Experiment 8 - Lowest Common Ancestor (500 queries)", "Number of Nodes (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, t=balanced(list(range(n)), 0, n - 1): largest_bst(t)))
    plot("Experiment 8 - Largest BST in a Binary Tree", "Number of Nodes (n)", BIG, [("", times)])


if __name__ == "__main__":
    root = None
    for v in (50, 30, 70, 20, 40):
        root = insert(root, v)
    print("Inorder       :", inorder(root))
    print("LCA(20, 40)   :", lca(root, 20, 40).val)

    left = None
    for v in (30, 20, 40, 10, 25):
        left = insert(left, v)
    tree = Node(50); tree.left = left; tree.right = Node(5)
    print("Largest BST   :", largest_bst(tree))
    run_benchmarks()
