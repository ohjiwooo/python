import heapq

imap=[-1,0,1,0]
jmap=[0,1,0,-1]


def dijk(arr,n,m):

    inf=999999999
    q=[]
    vis=[False]*(n*m+1)
    dis=[inf]*(n*m+1)
    dis[0]=0
    heapq.heappush(q,(0,0)) #비용,노드번호

    while(len(q) > 0):
        noww=q[0][0];nown=q[0][1];heapq.heappop(q)
        if vis[nown]==True : continue
        else : vis[nown]=True

        for i in range(len(arr[nown])):
            newn=arr[nown][i][0];neww=arr[nown][i][1]
            ans=min(dis[newn],dis[nown]+neww)
            dis[newn]=ans
            heapq.heappush(q,(ans,newn))

    print(dis[n*m-1])

if __name__=='__main__':

    n,m=map(int,input().split())
    map=[[0]*n for i in range(m)]

    
    for i in range(m):
        a=str(input())
        for j in range(n):
            map[i][j]=int(a[j])
    arr=[ [] for i in range(n*m+1)]
    for i in range(m):
        for j in range(n):
            for k in range(4):
                ni=i+imap[k];nj=j+jmap[k]
                if ni >= 0 and ni <m and nj >= 0 and nj < n:
                    arr[i*n+j].append((ni*n+nj,map[ni][nj]))

    dijk(arr,n,m)

    
    