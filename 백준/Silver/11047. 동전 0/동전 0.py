import sys

n , k = map(int,sys.stdin.readline().split())
coins = []
cnt = 0
for __ in range(n):
    coins.append(int(sys.stdin.readline().strip()))
#print(coins)

for x in range(n-1,-1,-1):
    if coins[x] <= k :
        cnt+= k//coins[x] # 몫ㅁ
        #print(" coins[x] :", coins[x] ," coins[x]//k  :: ",k//coins[x]," K:", k," coins[x] % k:", k% coins[x])

        k =k% coins[x]  # 나머지머



print(cnt)





