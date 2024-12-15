class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            self.tree[idx] = min(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        l += self.n
        r += self.n + 1
        res = float('inf')
        while l < r:
            if l % 2 == 1:
                res = min(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = min(res, self.tree[r])
            l //= 2
            r //= 2
        return res

n, q = map(int, input().split())
arr = list(map(int, input().split()))
seg_tree = SegmentTree(arr)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        k, u = query[1] - 1, query[2]
        seg_tree.update(k, u)
    elif query[0] == 2:
        a, b = query[1] - 1, query[2] - 1
        print(seg_tree.query(a, b))
