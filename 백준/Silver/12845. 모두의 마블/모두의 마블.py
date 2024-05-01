import sys


n = int(sys.stdin.readline().strip())
levelList = list(map(int, sys.stdin.readline().split()))
newlevelList= sorted(levelList, reverse = True)

max  = newlevelList[0]
reuslt = 0
for x in range(1,len(levelList)) :
    reuslt += max  + newlevelList[x]
print(reuslt)
    
