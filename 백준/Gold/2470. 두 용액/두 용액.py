import sys

# n , nList 입력 받는다.ㅂ
# 첫값과 , 마지막 값을 더한값의 절대값을 첫값으로 넣어준다.ㄷ
#result 값에 첫값과 , 끝값을 넣어준다.
# 투 포인터가 만나기전까지 반복문 괄괄괄 돌림
# 현재의 값이 num에 저장된 값보다 작으면 업뎃(작으면 0에 가까움 )
# sum이 음수면 lt 오르쪽 당기고, 양수면 rt 왼쪽으로 당겨줌


n = int(sys.stdin.readline().rstrip())
nList = list(map(int , sys.stdin.readline().split()))
nList.sort()


lt = 0
rt = n-1

answer = abs(nList[lt] + nList[rt])
#print(answer)

result = [nList[lt],nList[rt] ] 
#print(result)

while lt < rt : 
    leftNum = nList[lt]
    rightNum = nList[rt]
    sum =  leftNum+ rightNum
    if abs(sum) < answer :
        #print("answer:", answer , "abs(sum) : " ,abs(sum))
        # 값 교체 ㄱㄱㄱ
        answer = abs(sum)
        result=[leftNum,rightNum]
        if answer == 0 :
            break # 끝 끝 집에 가자
    if sum < 0 :
        lt +=1
    else :
        rt -=1
print(result[0],result[1])

