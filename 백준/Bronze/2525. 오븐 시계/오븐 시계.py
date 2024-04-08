 
h,m = map(int,input().split())  # 시간, 분
u=(int(input()))                # 사용 시간

if (m+u <60):
    print(h,m+u)
else:
    r = int((m+u)/60)  # 몫
    n = (m+u)%60 # 나머지
     
    if(h+r >23):
        print( (h+r)%24,n)
    else:
        print(h+r,n)
