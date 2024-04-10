from collections import deque
def solution(bridge_length, weight, truck_weights):
    currentWeigth = 0 
    deque_truck_weights = deque(truck_weights)
    truckList =[0] * bridge_length  
    answer = 0
    while deque_truck_weights : # 트럭에 없을때까지 돌아돌아 돌아라 
        # 빠져나가 
        if len(truckList) >= bridge_length :
            tmp = truckList.pop()
            if tmp != 0 :
                currentWeigth = currentWeigth - tmp
        # 들어와 
        if weight >= currentWeigth + deque_truck_weights[0]:
            currentWeigth = currentWeigth + deque_truck_weights[0]            
            truckList.insert(0,deque_truck_weights.popleft()) 
            
        else :# 읍읍 
            truckList.insert(0,0) 
        answer+=1  # 시간 up up

        
        
    return answer + bridge_length