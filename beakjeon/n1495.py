
def f(n,s,m,arr):
    vol=[ [0 for i in range(m+1)] for j in range(n+1) ]
    vis=[ [0 for i in range(m+1)] for j in range(n+1) ]
    for i in range(0,m+1):
    
        vol[n][i]=i
        vis[n][i]=1
    
    for i in range(n,0,-1):
        for j in range(0,m+1):
            if j+arr[i-1] >=0 and j+arr[i-1] <=m and vis[i][j]==1:
                vol[i-1][j+arr[i-1]]=max(vol[i-1][j+arr[i-1]],vol[i][j])
                vis[i-1][j+arr[i-1]]=1
            if j-arr[i-1] >=0 and j-arr[i-1] <=m and vis[i][j]==1:
                vol[i-1][j-arr[i-1]]=max(vol[i-1][j-arr[i-1]],vol[i][j])
                vis[i-1][j-arr[i-1]]=1

    if vis[0][s]==0:
        return -1
    else : return vol[0][s]
            

    

if __name__=='__main__':

    n,s,m=map(int,input().split())

    arr=list(map(int,input().split()))
    print(f(n,s,m,arr))
    
    
    
    