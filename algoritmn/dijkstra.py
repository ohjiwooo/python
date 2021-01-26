import heapq

heap=[]

def dijk(v,e,s,graph):
    check=[False]*(v+1) #방문체크
    inf=987654321
    d=[inf]*(v+1)
    d[s]=0 #시작점

    heapq.heappush(heap,(0,s))
    while(len(heap)>0):
        nowv=heap[0][1]
        w=heap[0][0]
        heapq.heappop(heap)
        if check[nowv] == True : continue
        check[nowv]=True

        for i in range(len(graph[nowv])):
            newv=graph[nowv][i][0];neww=graph[nowv][i][1]
            ans=min(w+neww,d[newv])
            d[newv]=ans
            heapq.heappush(heap,(ans,newv))

    for k in range(1,v+1):
        if d[k]==inf : print("INF")
        else : print(d[k])

            
if __name__=='__main__':   
    v,e=map(int,input().split())
    graph = [[]for i in range(v+1)]
    s=int(input())
    for i in range(e):
        f,t,w=map(int,input().split())
        graph[f].append((t,w))  #인접리스트 생성

    dijk(v,e,s,graph)

   


