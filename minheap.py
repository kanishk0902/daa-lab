def push(h, x):
    h.append(x)
    i = len(h) - 1
    while i > 0:
        p = (i - 1) // 2
        if h[i] < h[p]:
            h[i], h[p] = h[p], h[i]
            i = p
        else:
            break


def pop(h):
    top = h[0]
    last = h.pop()
    if h:
        h[0] = last
        i, n = 0, len(h)
        while True:
            l, r, m = 2 * i + 1, 2 * i + 2, i
            if l < n and h[l] < h[m]: m = l
            if r < n and h[r] < h[m]: m = r
            if m == i:
                break
            h[i], h[m] = h[m], h[i]
            i = m
    return top
