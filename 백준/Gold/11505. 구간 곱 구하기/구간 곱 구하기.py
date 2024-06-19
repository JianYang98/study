import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.read
data = input().split()
MOD = 1000000007

n = int(data[0])
m = int(data[1])
k = int(data[2])

tree = [1] * (4 * n)
tList = list(map(int, data[3:3 + n]))

# 기초 공사 build
def build(node, start, end):
    if start == end:
        tree[node] = tList[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

def query(node, start, end, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_product = query(node * 2, start, mid, left, right)
    right_product = query(node * 2 + 1, mid + 1, end, left, right)
    return (left_product * right_product) % MOD

def update(node, start, end, index, val):
    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= index <= mid:
            update(node * 2, start, mid, index, val)
        else:
            update(node * 2 + 1, mid + 1, end, index, val)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

build(1, 0, n - 1)

idx = 3 + n
for _ in range(m + k):
    a = int(data[idx])
    b = int(data[idx + 1])
    c = int(data[idx + 2])
    if a == 1:
        update(1, 0, n - 1, b - 1, c)
    else:
        print(query(1, 0, n - 1, b - 1, c - 1) % MOD)
    idx += 3