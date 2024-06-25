import sys

s= str(sys.stdin.readline().strip())
t = list(str(sys.stdin.readline().strip())) # 리스트에 하나하나 쪼개기


while len(s) < len(t) :
    if t[-1] == 'A' :
        t.pop()
    elif t[-1] == 'B' :
        t.pop()
        t.reverse()

if s == ''.join(t) :
    print(1)
else:
    print(0)