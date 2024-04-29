import sys

t = int(sys.stdin.readline().strip())
atmList = list(map(int,sys.stdin.readline().split()))

atmList.sort()

cnt = 0
result = 0

for atm in atmList:
    cnt += atm
    result+=cnt
print(result)
