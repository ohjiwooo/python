if __name__=='__main__':
   
    n,m=map(int,input().split())
    arr=[[] for i in range(n+1)]
    for i in range(m):
        a,b,c=map(int,input().split())
        arr[a].append((b,c))
    inf=987654321
    d=[inf] * (n+1) #거리
    d[1]=0
    flag=0
    
    for  v in range(n): #v번 반복
        flag=0
        for k in range(1,n+1): 
            for i in range(len(arr[k])):
                if d[k] != inf and d[k] + arr[k][i][1] < d[arr[k][i][0]]:
                    d[arr[k][i][0]]= (d[k] + arr[k][i][1])
                    if v == n-1 :flag=1
    if flag==1 : print(-1)
    else:
        for i in range(n-1):
            if d[i+2] != inf:
                print(d[i+2])
            else : print(-1)

