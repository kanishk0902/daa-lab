def union_intersection(A, B):
    i = j = 0
    union, inter = [], []
    while i < len(A) or j < len(B):
        if j == len(B) or (i < len(A) and A[i] < B[j]):
            v = A[i]; i += 1
        elif i == len(A) or B[j] < A[i]:
            v = B[j]; j += 1
        else:
            v = A[i]; i += 1; j += 1
            if not inter or inter[-1] != v:
                inter.append(v)
        if not union or union[-1] != v:
            union.append(v)
    return union, inter


def search_rotated(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[lo] <= a[mid]:
            if a[lo] <= target < a[mid]: hi = mid - 1
            else: lo = mid + 1
        else:
            if a[mid] < target <= a[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1


def merge_sort(a):
    return _sort_count(a)[0]


def count_inversions(a):
    return _sort_count(a)[1]


def _sort_count(a):
    if len(a) <= 1:
        return a[:], 0
    mid = len(a) // 2
    left, x = _sort_count(a[:mid])
    right, y = _sort_count(a[mid:])
    merged, inv, i, j = [], x + y, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            inv += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, inv

def run_benchmarks():
    import random
    from bench import measure, plot, BIG, nothing
    times = measure(BIG, lambda n: (nothing, lambda _, A=list(range(0, 2 * n, 2)), B=list(range(0, 3 * n, 3)): union_intersection(A, B)))
    plot("Experiment 2 - Union and Intersection of Sorted Arrays", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=list(range(n // 3, n)) + list(range(n // 3)): [search_rotated(a, 5) for _ in range(500)]))
    plot("Experiment 2 - Search in Rotated Sorted Array (500 searches)", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(0, n) for _ in range(n)]: merge_sort(a)))
    plot("Experiment 2 - Merge Sort", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(0, n) for _ in range(n)]: count_inversions(a)))
    plot("Experiment 2 - Count Inversions", "Array Size (n)", BIG, [("", times)])


if __name__ == "__main__":
    u, i = union_intersection([1, 2, 4, 5], [2, 4, 6])
    print("Union =", u, " Intersection =", i)
    print("Rotated search index :", search_rotated([6, 7, 8, 1, 2, 3, 4], 2))
    print("Merge sort           :", merge_sort([9, 3, 7, 1, 6]))
    print("Inversions           :", count_inversions([8, 4, 2, 1]), "inversions")
    run_benchmarks()
