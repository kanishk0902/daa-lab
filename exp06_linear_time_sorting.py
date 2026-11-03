import minheap
from exp01_sorting_fundamentals import insertion_sort_iter


def counting_sort(a):
    if not a:
        return []
    count = [0] * (max(a) + 1)
    for x in a:
        count[x] += 1
    out = []
    for v, c in enumerate(count):
        out += [v] * c
    return out


def bucket_sort(a):
    n = len(a)
    buckets = [[] for _ in range(n)]
    for x in a:
        buckets[int(x * n)].append(x)
    out = []
    for b in buckets:
        out += insertion_sort_iter(b)
    return out


def _at_most(a, k):
    if k == 0:
        return 0
    freq, left, total = {}, 0, 0
    for right, x in enumerate(a):
        freq[x] = freq.get(x, 0) + 1
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        total += right - left + 1
    return total


def subarrays_with_k_distinct(a, k):
    return _at_most(a, k) - _at_most(a, k - 1)


def min_sum_after_k_ops(a, k):
    heap = []
    for x in a:
        minheap.push(heap, -x)
    for _ in range(k):
        x = -minheap.pop(heap)
        if x == 1:
            minheap.push(heap, -x)
            break
        minheap.push(heap, -((x + 1) // 2))
    return -sum(heap)

def run_benchmarks():
    import random
    from bench import measure, plot, BIG, nothing
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(0, n) for _ in range(n)]: counting_sort(a)))
    plot("Experiment 6 - Counting Sort", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.random() for _ in range(n)]: bucket_sort(a)))
    plot("Experiment 6 - Bucket Sort", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(1, 5) for _ in range(n)]: subarrays_with_k_distinct(a, 3)))
    plot("Experiment 6 - Subarrays with Exactly K Distinct (k = 3)", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(1, 1000) for _ in range(n)]: min_sum_after_k_ops(a, n)))
    plot("Experiment 6 - Minimize Array Sum after K Operations", "Array Size (n)", BIG, [("", times)])


if __name__ == "__main__":
    print("Counting sort :", counting_sort([4, 2, 2, 8, 3, 3, 1]))
    print("Bucket sort   :", bucket_sort([0.42, 0.32, 0.23, 0.52]))
    print("Exactly K=2   :", subarrays_with_k_distinct([1, 2, 1, 2, 3], 2))
    print("Min sum (k=4) :", min_sum_after_k_ops([10, 20, 7], 4))
    run_benchmarks()
