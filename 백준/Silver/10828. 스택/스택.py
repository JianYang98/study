import sys
#sys.stdin = open("input.txt" , "r")
n = int(sys.stdin.readline())

result = []
for _ in range(n):
    word = sys.stdin.readline().split()

    if word[0] == "push" :
        result.append(word[1])
    elif word[0] =="top":
        if  not result:
            print(-1)
        else:
            print(result[-1])

    elif word[0] == "size" :
            print(len(result))
    elif word[0] == "empty" :
        if not result:
            print(1)
        else :
            print(0)
    elif word[0] == "pop" :
        if  not result:
            print(-1)
        else :
            print(result.pop())



