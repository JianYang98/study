n, s = map(int,input().split())
nlist = list(map(int,input().split()))

cnt = 0

def dfs(num,sum):
	global cnt
	if num >= n:
		return

	if sum + nlist[num] == s:
		cnt += 1


	dfs(num+1,sum+nlist[num])
	dfs(num+1,sum)

dfs(0,0)
print(cnt)