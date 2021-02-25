

def bellman(arr,n):
   flag=0 #갱신여부
   inf=987654321
   dis=[inf]*(n+1)
   
   
   for k in range(n):
       flag=0

       for i in range(1,n+1):  
            for j in range(len(arr[i])):
                if dis[arr[i][j][0]] > dis[i]+arr[i][j][1]:
                    dis[arr[i][j][0]]= dis[i]+arr[i][j][1]
                    if k==n-1:flag=1
        
       if flag==1:
           return True
       
   return False

        


if __name__=='__main__':

   cc=int(input())
   k=1
   while(k<=cc):
    n,m,w=map(int,input().split())
    arr=[ [] for i in range(n+1)]

    for i in range(m):
        a,b,c= map(int,input().split())
        arr[a].append((b,c))
        arr[b].append((a,c))
    
    for i in range(w):
        a,b,c=map(int,input().split())
        arr[a].append((b,-c))

    if bellman(arr,n)==True: print('YES')
    else : print('NO')
    k+=1

   
