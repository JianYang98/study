import sys

n= int(sys.stdin.readline().strip()) 
numberList = list(map(int,sys.stdin.readline().split()))

sortSetList = sorted(list(set(numberList)))
result = []
sortSetListDict = { number:idx for idx , number in enumerate(sortSetList)}
for x in range(n):
    result.append(sortSetListDict[numberList[x]])
print(' '.join(map(str,result)))