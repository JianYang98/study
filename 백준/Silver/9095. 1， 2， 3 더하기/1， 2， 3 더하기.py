import sys

t = int(sys.stdin.readline().strip())


for _ in range(t) :
    n = int(sys.stdin.readline().strip())
    a = []

    # a[1] = 1 , a[2] = 2 , a[3] = 4 값세팅
    a.append(0)
    a.append(1)
    a.append(2)
    a.append(4)

    if n<=3 :
        print(a[n])
    else:
        # 점화식 ㄱㄱ ㄱ
        for x in range(4,n+1):
            a.append(a[x-1] + a[x-2] + a[x-3])
        print(a[n])
        
    