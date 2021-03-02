import heapq


if __name__=='__main__':

    n=int(input())
    mm=[[] for i in range(n+1)]
    for i in range(1,n+1):
        mm[i]=list(map(int,input().split()))
    
    s=1
    vis=[False]*(n+1)
    vis[1]=True
    q=[];answer=0
    now=1
    while(s<n):
        for i in range(0,n):
            if vis[i+1]!=True:
                heapq.heappush(q,(mm[now][i],i+1))
        while(True):
            if vis[q[0][1]]==True:heapq.heappop(q)
            else :answer+=q[0][0];vis[q[0][1]]=True;now=q[0][1];heapq.heappop(q);s+=1;break

    print(answer)




        