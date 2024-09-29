def solution(s):
    answer = []
    result = {}
    ss = s.replace('}','').rstrip().split('{')
    
    for x in ss:
        if x != '':
            xList = x.split(',')
            for ele in xList:
                if ele in result:
                    result[ele] +=1
                elif ele!= '' :
                    result[ele] = 1
    result = sorted(result.items() ,key=lambda x:int(x[1]), reverse=True) 
    #print(result)
    resultList = [int(key) for key , _ in result ]
    #print(resultList)
    return resultList