from collections import deque

def f(time,v,v2,arr,n,goal):

    vis=[ 0 for i in range(n+2)]
    ans=0
    q=deque()
    while(ans<n):
        for i in range(1,n+1):
            if vis[i]==0 and arr[i]==0:
                q.append(i);vis[i]=1;ans+=1
        
        while(len(q)>0):
            a=q[0];q.popleft()
            temp=0
            for i in range(0,len(v2[a])):
                temp=max(time[v2[a][i]],temp)
            time[a]+=temp
            for i in range(0,len(v[a])):
                arr[v[a][i]]-=1
    print(time[goal])


if __name__=='__main__':

    t=int(input())

    while(t>0):
        n,k=map(int,input().split())
        time=[ 0 for i in range(n+5)]
        v=[[] for i in range(n+5)]
        v2=[[] for i in range(n+5)]
        arr=[ 0 for i in range(n+5)]
        s = list(map(int,input().split()))
        for i in range(n):
            time[i+1]=s[i]
        for i in range(k):
            a,b=map(int,input().split())
            v[a].append(b);v2[b].append(a);arr[b]+=1

        goal=int(input())
        f(time,v,v2,arr,n,goal)

        t-=1