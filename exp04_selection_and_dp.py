import random


def max_product_subarray(arr):
    hi = lo = best = arr[0]
    for x in arr[1:]:
        if x < 0:
            hi, lo = lo, hi
        p = hi * x
        hi = p if p > x else x
        q = lo * x
        lo = q if q < x else x
        if hi > best:
            best = hi
    return best


def kth_largest(arr, k):
    arr = arr[:]
    target = len(arr) - k
    low, high = 0, len(arr) - 1
    while low < high:
        r = random.randint(low, high)
        arr[r], arr[high] = arr[high], arr[r]
        pivot, i = arr[high], low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        if i == target:
            return arr[i]
        if i < target: low = i + 1
        else: high = i - 1
    return arr[low]


def fibonacci(n):
    a, b = 0, 1
    for bit in bin(n)[2:]:
        c = a * (2 * b - a)
        d = a * a + b * b
        a, b = (d, c + d) if bit == '1' else (c, d)
    return a


def smallest_missing_positive(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        v = arr[i]
        while 1 <= v <= n and arr[v - 1] != v:
            arr[i], arr[v - 1] = arr[v - 1], v
            v = arr[i]
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1

def run_benchmarks():
    from bench import measure, plot, BIG, nothing
    pattern = [-2, 3, -1, 4, 0, 2, -3, 1]
    times = measure(BIG, lambda n: (nothing, lambda _, a=(pattern * (n // 8 + 1))[:n]: max_product_subarray(a)))
    plot("Experiment 4 - Maximum Product Subarray", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, a=[random.randint(0, n) for _ in range(n)]: kth_largest(a, n // 2)))
    plot("Experiment 4 - Kth Largest using Quick Select", "Array Size (n)", BIG, [("", times)])
    fib_sizes = list(range(1000, 100001, 5000))
    times = measure(fib_sizes, lambda n: (nothing, lambda _, n=n: fibonacci(n)))
    plot("Experiment 4 - Nth Fibonacci Number", "n (Fibonacci index)", fib_sizes, [("", times)])

    def missing_input(n):
        a = list(range(2, n + 2))
        a[n // 2] = 1
        return nothing, lambda _: smallest_missing_positive(a)

    plot("Experiment 4 - Smallest Missing Positive", "Array Size (n)", BIG, [("", measure(BIG, missing_input))])


if __name__ == "__main__":
    print("Max product subarray :", max_product_subarray([2, 3, -2, 4]))
    print("Kth largest (k=2)    :", kth_largest([3, 2, 1, 5, 6, 4], 2))
    print("Fibonacci(10)        :", fibonacci(10))
    print("Smallest missing +ve :", smallest_missing_positive([3, 4, -1, 1]))
    run_benchmarks()
