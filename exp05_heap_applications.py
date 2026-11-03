import minheap
from exp01_sorting_fundamentals import insertion_sort_iter


def heap_sort(a):
    n = len(a)

    def sift_down(i, size):
        while True:
            l, r, m = 2 * i + 1, 2 * i + 2, i
            if l < size and a[l] > a[m]: m = l
            if r < size and a[r] > a[m]: m = r
            if m == i:
                return
            a[i], a[m] = a[m], a[i]
            i = m

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(0, end)
    return a


def rearrange_string(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    heap = []
    for ch in count:
        minheap.push(heap, (-count[ch], ch))
    out, prev = [], None
    while heap:
        c, ch = minheap.pop(heap)
        out.append(ch)
        if prev:
            minheap.push(heap, prev)
        prev = (c + 1, ch) if c + 1 < 0 else None
    return "".join(out) if len(out) == len(s) else ""


def merge_k_sorted(arrays):
    heap, out = [], []
    for i, arr in enumerate(arrays):
        if arr:
            minheap.push(heap, (arr[0], i, 0))
    while heap:
        v, i, j = minheap.pop(heap)
        out.append(v)
        if j + 1 < len(arrays[i]):
            minheap.push(heap, (arrays[i][j + 1], i, j + 1))
    return out


def _select(a, k):
    if len(a) <= 5:
        return insertion_sort_iter(a[:])[k]
    medians = []
    for i in range(0, len(a), 5):
        g = insertion_sort_iter(a[i:i + 5])
        medians.append(g[len(g) // 2])
    pivot = _select(medians, len(medians) // 2)
    lows = [x for x in a if x < pivot]
    equal = len([x for x in a if x == pivot])
    if k < len(lows):
        return _select(lows, k)
    if k < len(lows) + equal:
        return pivot
    highs = [x for x in a if x > pivot]
    return _select(highs, k - len(lows) - equal)


def median_of_medians(a, k):
    return _select(a, k - 1)

def run_benchmarks():
    import random
    from bench import measure, plot, BIG, nothing
    times = measure(BIG, lambda n: ((lambda a=[random.randint(0, n) for _ in range(n)]: a[:]), heap_sort))
    plot("Experiment 5 - Heap Sort", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, s="".join(chr(97 + i % 26) for i in range(n)): rearrange_string(s)))
    plot("Experiment 5 - Rearrange String", "String Length (n)", BIG, [("", times)])

    def merge_input(n):
        k = 10
        arrays = [list(range(i, n, k)) for i in range(k)]
        return nothing, lambda _: merge_k_sorted(arrays)

    plot("Experiment 5 - Merge K Sorted Arrays (k = 10)", "Total Elements (n)", BIG, [("", measure(BIG, merge_input))])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(0, n) for _ in range(n)]: median_of_medians(a, n // 2)))
    plot("Experiment 5 - Median of Medians", "Array Size (n)", BIG, [("", times)])


if __name__ == "__main__":
    print("Heap sort        :", heap_sort([12, 11, 13, 5, 6]))
    print("Rearrange string :", rearrange_string("aaabbc"))
    print("Merge K arrays   :", merge_k_sorted([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
    print("Median of medians:", median_of_medians([7, 10, 4, 3, 20, 15], 3))
    run_benchmarks()
