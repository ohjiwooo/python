import heapq


def dijk(n,arr):
    imap=[-1,0,1,0]
    jmap=[0,1,0,-1]
    inf=987654321
    minh=[]
    vis=[ [0 for i in range(n+1)] for j in range(n+1)]
    dis=[ [inf for i in range(n+1)] for j in range(n+1)]

    vis[0][0]=1 #true
    dis[0][0]=0
    heapq.heappush(minh,(0,0,0))

    while (len(minh)>0):
        noww=minh[0][0];nowi=minh[0][1];nowj=minh[0][2];heapq.heappop(minh)

        for i in range(4):
           
            if nowi+imap[i] >=0 and nowi+imap[i] <n and nowj+jmap[i] >=0 and nowj+jmap[i] <n and vis[nowi+imap[i]][nowj+jmap[i]]==0:
                dis[nowi+imap[i]][nowj+jmap[i]]=min(dis[nowi][nowj]+arr[nowi+imap[i]][nowj+jmap[i]],dis[nowi+imap[i]][nowj+jmap[i]])
                heapq.heappush(minh,(dis[nowi+imap[i]][nowj+jmap[i]],nowi+imap[i],nowj+jmap[i]))
                vis[nowi+imap[i]][nowj+jmap[i]]=1

    return dis[n-1][n-1]


if __name__=='__main__':

    n=int(input())
    arr= [[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(n):
        s=str(input())
        for j in range(n):
            arr[i][j]=int(s[j])
            if arr[i][j]==1:arr[i][j]=0
            else: arr[i][j]=1


    print(dijk(n,arr))
    