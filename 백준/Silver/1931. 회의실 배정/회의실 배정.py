#https://www.acmicpc.net/problem/1931
# 한 회의실에 N개의 회의에 대한 회의실 사용포를 만들려고함
# 각 회의 I에 대해 시작시간 ,끝나느 시간이 주어져 있고, 각 회의가 겹치지 않으면서서 회의실을 사용 할수 있는 최대 개수를 찾아보기

#첫째 줄 N (회의 수)
# N+1줄까지의 각 회의 정보가 주어지는데 시작과 끝

# 최대 사용 할 수 있는 최대 개수를 출력하라
#(1,4), (5,7), (8,11), (12,14)  를 이용 하여 처음 값의 end 값 보다 ,
# #다음 값의 start가 더 크면 사용 가능
N = int(input())



#print(N)
list =[list(map(int,input().split())) for i in range (N)]

#정렬 lambda 매개변수 : 표현식 #t시간순으로 정렬
# sort() 원본 수정
# sorted 원본 수정 x ,sorted(list , key = lamda a : a[0])
list = sorted(list , key= lambda  a:a[0])
list = sorted(list , key= lambda  a:a[1])


#start =list[0][0]
#end = list[0][1]
count = 0
start =0
end =0

for a , b in list:
    #print("",a ,"::", b )
    if(end <= a):
        #회의가 끝난 이후 , 다음 회의 시작 시간이 더 큰 경우 OK
        count+=1
       # print("count : %d , start : %d : end :%d" %(count , a, b))
        start = a
        end = b

print(count)
