

def dp(n,k,arr,dpmap):

    for i in range(1,n+1):
        for j in range(1,k+1):
            if j-arr[i][0] >=0 :
                dpmap[i][j] = max(dpmap[i-1][j], dpmap[i-1][j-arr[i][0]]+arr[i][1])
            else:dpmap[i][j]=dpmap[i-1][j]

    return dpmap[n][k]

if __name__=='__main__':
    n,k=map(int,input().split())
    arr=[[]for i in range(n+1)]
    dpmap=[ [0 for i in range(k+1)] for j in range(n+1)]
    for i in range(1,n+1):
        a,b=map(int,input().split())
        arr[i].append(a)
        arr[i].append(b)

    print(dp(n,k,arr,dpmap))
    

    
        