import sys

N = int(sys.stdin.readline().strip())
Nlist =[list(map(int,sys.stdin.readline().split())) for i in range (N)]
#print(Nlist)

#정렬 lambda 매개변수 : 표현식 #t시간순으로 정렬
# sort() 원본 수정
# sorted 원본 수정 x ,sorted(Nlist , key = lamda a : a[0])
Nlist = sorted(Nlist , key= lambda  a:a[0])
#print(Nlist)
Nlist = sorted(Nlist , key= lambda  a:a[1])
#print(Nlist)

count = 0
start =0
end =0

for a , b in Nlist:
    #print("",a ,"::", b )
    if(end <= a):
        #회의가 끝난 이후 , 다음 회의 시작 시간이 더 큰 경우 OK
        count+=1
       # print("count : %d , start : %d : end :%d" %(count , a, b))
        start = a
        end = b

print(count)