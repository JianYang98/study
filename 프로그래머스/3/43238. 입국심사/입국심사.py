def solution(n, times):
    timeMin = 0 
    timeMax = max(times) * n
    
    while timeMin <= timeMax :
        timeMid = (timeMin + timeMax) // 2
        cnt = 0
        
        for time in times:
            cnt+= timeMid // time
        if cnt >= n :
            timeMax= timeMid -1
        else :
            timeMin = timeMid +1
        
    answer = 0
    return timeMin