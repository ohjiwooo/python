from collections import deque

q=deque()
answer=[]
ans=0
if __name__=='__main__':

    n,m=map(int,input().split())
    arr=[[] for i in range(n+1)]
    arr2=[0] * (n+1)
    vis=[False] * (n+1)
    for i in range(m):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr2[b]+=1
    
    while(ans<n):
        for i in range(1,n+1):
            if arr2[i]==0 and vis[i]==False:
                answer.append(i);ans+=1;vis[i]=True
                for j in range(len(arr[i])):
                    arr2[arr[i][j]]-=1
                break

    for i in range(n):
        print(answer[i],end=' ')
        
    
    

    