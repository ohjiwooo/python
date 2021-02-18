from collections import deque

def bfs(arr,n,k):

    answer=[];vis=[False] * (n+1);q=deque()
    q.append(k);vis[k]=True;answer.append(k)

    while( len(q) > 0):
        now=q[0];q.popleft()
        arr[now].sort()
        for i in range(len(arr[now])):
            if vis[arr[now][i]] == False :
                q.append(arr[now][i]); vis[arr[now][i]]=True;answer.append(arr[now][i])

    for i in range(len(answer)):
        print(answer[i],end=' ')


def dfs(arr,vis,now,answer):
    arr[now].sort()
    for i in range(len(arr[now])):
        if len(arr[now]) > 0 and vis[arr[now][i]] != True:
            nn=arr[now][i]
            vis[nn]=True
            answer.append(nn)
            dfs(arr,vis,nn,answer)

def search(arr,n,k):
    vis=[False] * (n+1)
    answer=[]
    answer.append(k)
    vis[k]=True
    dfs(arr,vis,k,answer)
    for i in range(len(answer)):
        if(i==len(answer)-1):
            print(answer[i],end='\n')
        else:print(answer[i],end=' ')
    


            


if __name__=='__main__':

    n,m,k=map(int,input().split())
    arr=[ [] for i in range(n+1)]
    for i in range(m):
        a,b= map(int,input().split())
        arr[a].append(b); arr[b].append(a)

    search(arr,n,k)
    bfs(arr,n,k)
    