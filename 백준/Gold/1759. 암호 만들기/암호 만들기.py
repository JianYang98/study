import sys

l ,c = map(int , sys.stdin.readline().split())
cList = list(map(str , sys.stdin.readline().split()))
cList.sort()

voCnt = 0 # 모음 수
coCnt = 0 # 자음 수ㅅ

aeiouList = ['a','e','i','o','u']
visited = [False] * c
for x in cList :
    if x in aeiouList:
        voCnt+=1



coCnt = c - voCnt # 자음 수, 갯수 - 모음수 

currentVo = 0 # 현재 모음 수
currentCo = 0 # 현재 자음 수


result = []

def DFS(indexNum):
    check = '' 
    global currentVo
    global currentCo
    if len(result) == l :
        if currentVo >=1 and currentCo >=2 :
            print(''.join(result))
            return
        else:
            return
    #elif indexNum > c: # 인자값 제한             
    elif indexNum > c -(l-c) : # 인자값 제한 
        return         
    else:
        
        for x in range(indexNum , c) :
            if visited[x] == False and len(result) == 0 or max(result) <cList[x] : 
                if cList[x] in aeiouList: # 현재 문자열이 모음이면 모음 수 업ㅁ
                    currentVo+=1 # 
                else : # 자음이면 자음수 업
                    currentCo+=1
                check= cList[x]
                visited[x] = True
                result.append(cList[x])
                #print(" reulst: " , result)
                DFS(indexNum + 1)
                visited[x] = False
                
                result.pop()
                if cList[x] in aeiouList: 
                    currentVo-=1 # 
                else : # 자음이면 자음수 업
                    currentCo-=1
            

DFS(0)            
            
        

    







