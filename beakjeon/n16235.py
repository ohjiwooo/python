from collections import deque

map2=deque()
temp=deque()

def spring(map1):
    imap=[-1,-1,0,1,1,1,0,-1]
    jmap=[0,1,1,1,0,-1,-1,-1]
    global map2;global temp
    l=len(map2)
    index=0;i=0
    while i<l:
        ni=map2[index][0];nj=map2[index][1];age=map2[index][2]
        del(map2[index])
        if map1[ni][nj][0]>=age:
            map1[ni][nj][0]-=age
            map2.append((ni,nj,age+1))
            if (age+1)%5==0:
                for k in range(8):
                    if ni+imap[k] > 0 and ni+imap[k] <= n and nj+jmap[k] > 0 and nj+jmap[k] <=n:
                        map2.appendleft((ni+imap[k],nj+jmap[k],1));index+=1
        else : map1[ni][nj][2]+=int((age)/2)
        i+=1

def winter(map1,n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            map1[i][j][0]+=map1[i][j][1]+map1[i][j][2];map1[i][j][2]=0

if __name__=='__main__':

    n,m,k=map(int,input().split())
    map1=[ [[5,0,0] for i in range(n+1)] for j in range (n+1)] 
   
    for i in range(1,n+1):
        w=list(map(int,input().split()))
        for j in range(1,n+1):
            map1[i][j][1]=w[j-1]

    for i in range(m):
        a,b,c=map(int,input().split())
        map2.append((a,b,c))
    
 
    for i in range(k):
        spring(map1)
        winter(map1,n)

    print(len(map2))

    
