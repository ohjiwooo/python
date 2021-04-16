from collections import deque


def bfs(k,s,n,arr):
    qq=deque()
    vis=[0 for i in range(n+1)]
    answer=[ 9876543210 for i in range(n+1)]
    vis[s]=1
    qq.append(s)
    while(len(qq)>0):
        a=qq[0];qq.popleft()
        for i in range(len(arr[a])):
            if vis[arr[a][i][0]] == 0:
                answer[arr[a][i][0]]=min( arr[a][i][1], answer[a])
                qq.append(arr[a][i][0]);vis[arr[a][i][0]]=1
    ans=0
    for i in range(1,n+1):
        if answer[i] >= k and i !=s:
            ans+=1

    print(ans)


if __name__=='__main__':

    q=deque()
    n,qu=map(int,input().split())
    arr=[ [] for i in range(n+2)]
    for i in range(n-1):
        a,b,c=map(int,input().split())
        arr[a].append((b,c))
        arr[b].append((a,c))

    for i in range(qu):
        a,b=map(int,input().split())
        q.append((a,b))

    while(len(q)>0):
        k=q[0][0];s=q[0][1];q.popleft()
        bfs(k,s,n,arr)