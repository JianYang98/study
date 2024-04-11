import sys
    
N = int(sys.stdin.readline())
for x in range(N):
    reversedList =[]
    tmpList =  list(map(str,sys.stdin.readline().split()))
    for word in tmpList:
        reversedList.append(''.join(reversed(word)) )
    print(' '.join(map(str,reversedList)))
