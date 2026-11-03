import time
import statistics
import matplotlib.pyplot as plt

BIG = list(range(100, 10001, 500))
MID = list(range(50, 1001, 50))
SMALL = list(range(10, 201, 10))
HASH = list(range(100, 5001, 250))


def nothing():
    return None


def measure(sizes, setup, runs=5):
    result = []
    for n in sizes:
        prep, fn = setup(n)
        times = []
        for _ in range(runs):
            x = prep()
            start = time.perf_counter_ns()
            fn(x)
            times.append(time.perf_counter_ns() - start)
        result.append(statistics.median(times))
    return result


def plot(title, xlabel, sizes, series):
    plt.figure(figsize=(10, 6))
    for (label, ys), marker in zip(series, "os^"):
        plt.plot(sizes, ys, marker=marker, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Median Execution Time (ns)")
    if len(series) > 1:
        plt.legend()
    plt.grid(True)
    plt.show()


def make_graph(n):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for d in (1, 7, 13):
            j = (i + d) % n
            if j != i:
                w = (i * 37 + d) % 100 + 1
                adj[i].append((j, w))
                adj[j].append((i, w))
    return adj
