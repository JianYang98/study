import sys
   
#입력된 숫자들을 자른다. 
#숫자들의 조합을 DFS 로 만든다.
# 만들어진 숫자가 제시된 숫자보다 클때 list에 넣는다.
# 마지막 list의 min을 출력한다. 

n = int(sys.stdin.readline().strip())

nList =list(map(int,(str(n))))
res =[False] * len(nList)
tmp = []
result = []

def DFS():
    check = 0 #pop하기 전 값을 세팅하기 위한 값

    if len(tmp) == len(nList):
        # 숫자가 들어있는 리스트를 str로 변경해서 한줄로 만들고 int 
        currentValue = int(''.join(map(str, tmp)))
        if currentValue > n :
            result.append(currentValue)

            
        return
    else : 
        for x in range(len(nList)):
            if res[x] == False and check != nList[x] :
                tmp.append(nList[x])
                check = nList[x]
                res[x] = True
                DFS()
                tmp.pop()
                res[x] = False
                

DFS()
if len(result) == 0 :
    print(0)
else:
    print(min(result))