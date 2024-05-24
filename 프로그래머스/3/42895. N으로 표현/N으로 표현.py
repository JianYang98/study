def solution(N, number):
    answer = -1
    if N == number :
        return 1
    num = []
    for i in range(1, 9): # i = 숫자 N을 사용하는 횟수
        
        # NN값 세팅 
        case = {int(str(N)*i)} 
             
        #print("case",case)
        # 숫자 조합끼리의 사칙연산
        for j in range(0, i-1):  
            #print("num" , num)
            
            # num의 있는 값을 하나하나 꺼내서 (num)?N 수행
            # num 에서 숫자 조합을 하나씩 꺼내서 
            for x in num[j]:
                for y in num[-j-1]:
                    case.add(x+y)
                    case.add(x-y)
                    case.add(x*y)
                    if y != 0:
                        case.add(x//y)
         # 숫자 조합에 N 가 있는 경우
        if number in case:
            return i
        
        # 숫자 조합에 N 가 없으면 리스트에 추가
        #F(1) = N 세팅 
        num.append(case)
        #print("num" , num)
    return answer