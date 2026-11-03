# Design and Analysis of Algorithms Lab (CCE3130)

Lab programs for **Experiments 1–11 and Assessment I**, B.Tech CCE, Manipal University Jaipur
(Aug'26 – Nov'26) — by Kanishk Satyajit Das.


## Run

```bash
pip install matplotlib       # only needed for the timing graphs
python exp07_hashing.py      # sample output, then the timing graphs of that experiment
python run_all.py            # every experiment, one after the other
python test_all.py           # randomised tests against brute-force answers
```

Each experiment file contains the complete programs, the handout sample run, and the timing code
(median of 5 runs with `time.perf_counter_ns()`) that draws the graph for every program.
`bench.py` holds the shared timing/plot helpers.

## Contents

| File | Programs | Time complexity | Space |
|---|---|---|---|
| `exp01_sorting_fundamentals.py` | Insertion Sort (iterative & recursive), Dutch National Flag, Majority Element | O(n²) / O(n) / O(n) | O(1) |
| `exp02_divide_and_conquer.py` | Union & Intersection, Rotated Array Search, Merge Sort, Count Inversions | O(m+n) / O(log n) / O(n log n) | O(n) |
| `exp03_matrices_and_selection.py` | Matrix Multiplication, Strassen, Allocate Minimum Pages, Median of Two Sorted Arrays | O(n³) / O(n^2.81) / O(n log S) / O(log min(m,n)) | O(n²) |
| `exp04_selection_and_dp.py` | Max Product Subarray, Kth Largest (Quick Select), Nth Fibonacci, Smallest Missing Positive | O(n) / O(n) avg / O(log n) / O(n) | O(1) |
| `exp05_heap_applications.py` | Heap Sort, Rearrange String, Merge K Sorted Arrays, Median of Medians | O(n log n) / O(n log k) / O(N log k) / O(n) | O(1)–O(n) |
| `exp06_linear_time_sorting.py` | Counting Sort, Bucket Sort, Subarrays with Exactly K Distinct, Minimize Array Sum | O(n+m) / O(n) avg / O(n) / O((n+k) log n) | O(n) |
| `assessment1.py` | Coin Change, Single Non-Repeating Element, Maximize Minimum Difference | O(n·amt) / O(n) / O(n log n + n log D) | O(n) |
| `exp07_hashing.py` | Hash Table (chaining & linear probing), Relative Sorting, Minimum Window Substring | O(1) avg / O(n log n) / O(n+m) | O(n) |
| `exp08_binary_search_trees.py` | BST construction, Lowest Common Ancestor, Largest BST in a Binary Tree | O(log n) avg / O(log n) / O(n) | O(h) |
| `exp09_graphs_and_dp.py` | Prim's MST, Count Nodes in a Complete Binary Tree, Longest Palindromic Subsequence | O(E log V) / O(log² n) / O(n²) | O(V+E) / O(log n) / O(n) |
| `exp10_shortest_paths.py` | Dijkstra, Stock Buy/Sell with Fee, Maximum Bottleneck Path | O((V+E) log V) / O(n) / O(E log V) | O(V+E) / O(1) |
| `exp11_advanced_graphs.py` | Bellman-Ford, Floyd-Warshall, City with Fewest Reachable Neighbors | O(VE) / O(V³) / O(V³) | O(V) / O(V²) |

## Sample outputs (from the handout)

| Program | Output |
|---|---|
| Insertion sort `[8,4,2,9,5]` | `[2,4,5,8,9]` |
| Dutch flag `[2,0,1,2,1,0,0]` | `[0,0,0,1,1,2,2]` |
| Majority `[2,2,1,2,3,2,2]` | `2` |
| Inversions `[8,4,2,1]` | `6` |
| Allocate pages `[12,34,67,90]`, 2 students | `113` |
| Max product `[2,3,-2,4]` | `6` |
| Rearrange `aaabbc` | `ababac` |
| Exactly 2 distinct `[1,2,1,2,3]` | `7` |
| Min window `ADOBECODEBANC`, `ABC` | `BANC` |
| Prim MST | `16` |
| Stock `[1,3,2,8,4,9]`, fee 2 | `8` |
| Bellman-Ford | `[0,-1,2,-2,1]` |
| City, threshold 4 | `3` |
