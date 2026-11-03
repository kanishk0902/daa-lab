from exp02_divide_and_conquer import merge_sort


class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        bucket = self.table[key % self.size]
        if key not in bucket:
            bucket.append(key)

    def search(self, key):
        return key in self.table[key % self.size]


class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        i = key % self.size
        for _ in range(self.size):
            if self.table[i] is None or self.table[i] == key:
                self.table[i] = key
                return
            i = (i + 1) % self.size
        raise OverflowError("Hash table is full")

    def search(self, key):
        i = key % self.size
        for _ in range(self.size):
            if self.table[i] is None: return False
            if self.table[i] == key: return True
            i = (i + 1) % self.size
        return False


def relative_sort(A, B):
    freq = {}
    for x in A:
        freq[x] = freq.get(x, 0) + 1
    out = []
    for v in B:
        if v in freq:
            out += [v] * freq.pop(v)
    rest = []
    for v, c in freq.items():
        rest += [v] * c
    return out + merge_sort(rest)


def min_window(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing, left, best_left, best_len = len(t), 0, 0, len(s) + 1
    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if right - left + 1 < best_len:
                best_len, best_left = right - left + 1, left
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[best_left:best_left + best_len] if best_len <= len(s) else ""

def run_benchmarks():
    import random
    from bench import measure, plot, BIG, HASH, nothing

    def hash_times(table_class, factor):
        def setup(n):
            keys = [random.randint(0, 10 * n) for _ in range(n)]

            def run(_):
                table = table_class(factor * n)
                for k in keys:
                    table.insert(k)
                for k in keys:
                    table.search(k)

            return nothing, run

        return measure(HASH, setup)

    plot("Experiment 7 - Hash Table (insert and search n keys)", "Number of Keys (n)", HASH,
         [("Chaining", hash_times(ChainingHashTable, 1)), ("Linear probing", hash_times(LinearProbingHashTable, 2))])
    times = measure(BIG, lambda n: (nothing, lambda _, A=[random.randint(0, n // 2) for _ in range(n)], B=list(range(0, 100, 2)): relative_sort(A, B)))
    plot("Experiment 7 - Relative Sorting", "Array Size (n)", BIG, [("", times)])
    times = measure(BIG, lambda n: (nothing, lambda _, s="".join(random.choice("ABCDEFGH") for _ in range(n)): min_window(s, "ABC")))
    plot("Experiment 7 - Minimum Window Substring", "String Length (n)", BIG, [("", times)])


if __name__ == "__main__":
    for name, H in (("Chaining", ChainingHashTable(10)), ("Linear probing", LinearProbingHashTable(10))):
        for k in (15, 25, 35):
            H.insert(k)
        print(f"{name:15s}: search 25 ->", H.search(25), "| search 99 ->", H.search(99))
    print("Relative sort :", relative_sort([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8], [2, 1, 8, 3]))
    print("Min window    :", min_window("ADOBECODEBANC", "ABC"))
    run_benchmarks()
