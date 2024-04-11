import sys

N = int(sys.stdin.readline())
for x in range(N):
    qeueList =[]
    tmpWord = list(sys.stdin.readline().strip())
    for a in tmpWord: # a 지금 요소값
        last = ''    # last 현재 큐에 마지막 값
        if(len(qeueList)>0):
            last= qeueList[-1]
        qeueList.append(a)
        if last =='(' and a == ')': # 큐 안에서 순서 ( ) 맞는지 보는 조건
            qeueList.pop()
            qeueList.pop()
            
    print("YES" if len(qeueList) == 0 else "NO"  )