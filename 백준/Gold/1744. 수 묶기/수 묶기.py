import sys
from collections import deque
n = int(sys.stdin.readline().strip())

# 음수 , 양수 나누고
# 1과 , 0 처리 하기 
#그 후에 print 
# 양수와 음수, 1,0 을 따로 저장
q = []
positive = []
negative = []
one = 0
zero = 0
result = 0
for _ in range(n) :
    num = int(sys.stdin.readline().strip())
    q.append(num)
    if num > 1 : # 1보다 커ㅂ
        positive.append(num)
    elif num == 1 : # 1일떄ㅇ
        one += 1 
    elif num == 0 : # 0일때ㄸ
        zero +=1
    elif num < 0 : # 음수일때 ㄸ
        negative.append(num)

# 음수는 큰수 부터 정렬 (작은수 부터 pop 하려고)
negative.sort(reverse = True)
# 양수는 작은수 부터 정렬 ( 큰수부터 pop 하려고)
positive.sort()
#print(negative)

# 음수부터 계산 
while len(negative)>1 :
    num1 = negative.pop()
    num2 = negative.pop()
    result += (num1 * num2)
if len(negative) == 1 :
    # 0  이있다면 ? 음수랑 곱해서 0으로 만듬
    if zero > 0:
        result += (negative.pop() * 0)
    else : 
        result += negative.pop() 
#print(result)


while len(positive)>1 :
    num1 = positive.pop()
    num2 = positive.pop()
    result += (num1 * num2)
if len(positive) == 1 :
    result +=  positive.pop() 
if one >= 1 :
    result += (one )




print(result)
