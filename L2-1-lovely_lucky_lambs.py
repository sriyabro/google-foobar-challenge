def solution(lambs):
    
    genList = []
    x = 0
    genTotal = 0
    
    while x <= lambs:
        genValue = 2**x
        genList.append(genValue)
        genTotal += genValue
        if genTotal > lambs:
            break
        x=x+1
        
    
    stingList = [1,1]
    stingTotal = 2
    y=2
    
    while y <= lambs:
        stingValue = stingList[y-1] + stingList[y-2]
        stingList.append(stingValue)
        stingTotal += int(stingList[y])
        if stingTotal > lambs:
            break
        y=y+1
        
    answer = len(stingList) - len(genList)
    

    #print(genList)
    #print(stingList)
    return answer

#print(solution(10000))
