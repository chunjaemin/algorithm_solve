
friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
def solution(friends, gifts):
    N = len(friends)
    mapt = {v : i for i, v in enumerate(friends)}
        
    cgifts =[[0]* N for _ in range(N)]
    gift_index = [0]*N
    
    for x in gifts:
        sender, receiver = x.split()
        cgifts[mapt[sender]][mapt[receiver]] += 1 
    
    for i in range(N):
        gift_index[i] = sum(cgifts[i][x] for x in range(N)) - sum(cgifts[x][i] for x in range(N))
    
    nget_gifts = [0]*N
    for i in range(N):
        for j in range(N):
            if cgifts[i][j] > cgifts[j][i]:
                nget_gifts[i] += 1 
            if cgifts[i][j] == cgifts[j][i]:
                if gift_index[i] > gift_index[j]:
                    nget_gifts[i] += 1 
     
    return max(nget_gifts) 

print(solution(friends, gifts))