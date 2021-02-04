import heapq

heap=[]
answer=0
ans=0
if __name__=='__main__':
    n,m=map(int,input().split())
    arr=[ [] for i in range(n+1)]
    vis=[False] * (n+1)
    for i in range(m):
        a,b,c=map(int,input().split())
        arr[a].append((b,c))
        arr[b].append((a,c))
    nn=0
    v=1
    vis[1]=True
    while(nn<n-1):
        for i in range(len(arr[v])):
            if vis[arr[v][i][0]] != True :
                heapq.heappush(heap,(arr[v][i][1],arr[v][i][0]))
        while(True):
            if vis[heap[0][1]] ==True : heapq.heappop(heap)
            else :
                if(ans < heap[0][0]) : ans = heap[0][0]
                answer+=heap[0][0];v=heap[0][1];heapq.heappop(heap);nn+=1;vis[v]=True;break
    answer-=ans
    print(answer)


