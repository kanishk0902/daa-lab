def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = A[i][k]
            for j in range(p):
                C[i][j] += aik * B[k][j]
    return C


def _add(A, B): return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]
def _sub(A, B): return [[a - b for a, b in zip(r, s)] for r, s in zip(A, B)]


def _strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    h = n // 2
    a11 = [r[:h] for r in A[:h]]; a12 = [r[h:] for r in A[:h]]
    a21 = [r[:h] for r in A[h:]]; a22 = [r[h:] for r in A[h:]]
    b11 = [r[:h] for r in B[:h]]; b12 = [r[h:] for r in B[:h]]
    b21 = [r[:h] for r in B[h:]]; b22 = [r[h:] for r in B[h:]]
    m1 = _strassen(_add(a11, a22), _add(b11, b22))
    m2 = _strassen(_add(a21, a22), b11)
    m3 = _strassen(a11, _sub(b12, b22))
    m4 = _strassen(a22, _sub(b21, b11))
    m5 = _strassen(_add(a11, a12), b22)
    m6 = _strassen(_sub(a21, a11), _add(b11, b12))
    m7 = _strassen(_sub(a12, a22), _add(b21, b22))
    c11 = _add(_sub(_add(m1, m4), m5), m7)
    c12 = _add(m3, m5)
    c21 = _add(m2, m4)
    c22 = _add(_sub(_add(m1, m3), m2), m6)
    return [r1 + r2 for r1, r2 in zip(c11, c12)] + [r1 + r2 for r1, r2 in zip(c21, c22)]


def strassen(A, B):
    n = len(A)
    size = 1
    while size < n:
        size *= 2
    pad = lambda M: [r + [0] * (size - n) for r in M] + [[0] * size for _ in range(size - n)]
    C = _strassen(pad(A), pad(B))
    return [r[:n] for r in C[:n]]


def allocate_pages(books, students):
    if students > len(books):
        return -1
    lo, hi = max(books), sum(books)
    while lo < hi:
        mid = (lo + hi) // 2
        need, load = 1, 0
        for p in books:
            if load + p > mid:
                need += 1; load = p
            else:
                load += p
        if need <= students: hi = mid
        else: lo = mid + 1
    return lo


def median_two_sorted(A, B):
    if len(A) > len(B):
        A, B = B, A
    m, n = len(A), len(B)
    lo, hi, half = 0, m, (m + n + 1) // 2
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        aL = A[i - 1] if i > 0 else float('-inf')
        aR = A[i] if i < m else float('inf')
        bL = B[j - 1] if j > 0 else float('-inf')
        bR = B[j] if j < n else float('inf')
        if aL <= bR and bL <= aR:
            left = aL if aL > bL else bL
            if (m + n) % 2: return left
            right = aR if aR < bR else bR
            return (left + right) / 2
        if aL > bR: hi = i - 1
        else: lo = i + 1

def run_benchmarks():
    import random
    from bench import measure, plot, BIG, nothing

    def matrix(n):
        return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]

    sizes = [4, 8, 16, 32, 64]
    brute = measure(sizes, lambda n: (nothing, lambda _, A=matrix(n), B=matrix(n): mat_mul(A, B)))
    fast = measure(sizes, lambda n: (nothing, lambda _, A=matrix(n), B=matrix(n): strassen(A, B)))
    plot("Experiment 3 - Matrix Multiplication", "Matrix Size (n x n)", sizes, [("Brute force", brute), ("Strassen", fast)])
    times = measure(BIG, lambda n: (nothing, lambda _, b=[random.randint(1, 100) for _ in range(n)]: allocate_pages(b, 10)))
    plot("Experiment 3 - Allocate Minimum Pages (10 students)", "Number of Books (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, A=sorted(random.randint(0, 10 * n) for _ in range(n)), B=sorted(random.randint(0, 10 * n) for _ in range(n)): [median_two_sorted(A, B) for _ in range(500)]))
    plot("Experiment 3 - Median of Two Sorted Arrays (500 queries)", "Size of Each Array (n)", BIG, [("", times)])


if __name__ == "__main__":
    A, B = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
    print("Matrix multiplication:", mat_mul(A, B))
    print("Strassen             :", strassen(A, B))
    print("Allocate pages       :", allocate_pages([12, 34, 67, 90], 2))
    print("Median of two arrays :", median_two_sorted([1, 3], [2]))
    run_benchmarks()
