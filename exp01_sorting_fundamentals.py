def insertion_sort_iter(a):
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def insertion_sort_rec(a, n=None):
    if n is None:
        n = len(a)
    if n <= 1:
        return a
    insertion_sort_rec(a, n - 1)
    key, j = a[n - 1], n - 2
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
    return a


def dutch_flag(a):
    low, mid, high = 0, 0, len(a) - 1
    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1; mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a


def majority_element(a):
    cand, count = None, 0
    for x in a:
        if count == 0:
            cand = x
        count += 1 if x == cand else -1
    total = 0
    for x in a:
        if x == cand:
            total += 1
    return cand if total > len(a) // 2 else None

def run_benchmarks():
    import random
    import sys
    from bench import measure, plot, BIG, nothing
    sys.setrecursionlimit(5000)
    small = list(range(100, 1501, 100))
    iterative = measure(small, lambda n: ((lambda a=[random.randint(0, n) for _ in range(n)]: a[:]), insertion_sort_iter))
    recursive = measure(small, lambda n: ((lambda a=[random.randint(0, n) for _ in range(n)]: a[:]), insertion_sort_rec))
    plot("Experiment 1 - Insertion Sort", "Array Size (n)", small, [("Iterative", iterative), ("Recursive", recursive)])
    times = measure(BIG, lambda n: ((lambda a=[random.randint(0, 2) for _ in range(n)]: a[:]), dutch_flag))
    plot("Experiment 1 - Dutch National Flag", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(0, 3) for _ in range(n)]: majority_element(a)))
    plot("Experiment 1 - Majority Element", "Array Size (n)", BIG, [("", times)])


if __name__ == "__main__":
    print("Insertion sort (iterative):", insertion_sort_iter([8, 4, 2, 9, 5]))
    print("Insertion sort (recursive):", insertion_sort_rec([8, 4, 2, 9, 5]))
    print("Dutch National Flag       :", dutch_flag([2, 0, 1, 2, 1, 0, 0]))
    print("Majority element          :", majority_element([2, 2, 1, 2, 3, 2, 2]))
    run_benchmarks()
