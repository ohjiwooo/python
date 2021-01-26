from collections import deque

imap=[-1,-1,0,1,1,1,0,-1]
jmap=[0,1,1,1,0,-1,-1,-1]
answer=0
m=0;n=0;k=0
q=[[[] for i in range(55)]for j in range (55)]
     

def move():
    global n;global m;global k;global q
    temp=[[[] for i in range (55)] for j in range(55)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(len(q[i][j]) > 0) :
                for k in range(len(q[i][j])):
                    g=q[i][j][k][0];a=q[i][j][k][1];d=q[i][j][k][2]
                    newi = (imap[d] * a) % n
                    newi = (i+newi) % n
                    if newi == 0 : newi=n
                    newj = (jmap[d] * a) % n
                    newj = (j+newj) % n
                    if newj==0:newj=n
                    temp[newi][newj].append((g,a,d))
    q=temp

def over():
    global n;global m;global k;global answer;global q
    for i in range(1,n+1):   
        for j in range(1,n+1):
            if(len(q[i][j]) >= 2) :
                newg=0;newa=0;e=0;o=0;nn=0
                for k in range(len(q[i][j])):
                    newg+= q[i][j][0][0]; newa += q[i][j][0][1]
                    nn+=1;answer-=q[i][j][0][0]
                    if q[i][j][0][2] % 2 == 0 : e+=1
                    else : o+=1
                    del(q[i][j][0])
                newg=newg/5;newg=int(newg);newa=newa/nn;newa=int(newa)
                if o==0 or e==0 : d=0
                else : d=1
                if newg != 0 :
                    for k in range(4):
                        q[i][j].append((newg,newa,d));d+=2;answer+=newg
                


if __name__=='__main__':
    n,m,k=map(int,input().split()) #n:격자크기 m:볼갯수 k:명령수
    a=[]
    for i in range(m):
       a=list(map(int,input().split()))
       q[a[0]][a[1]].append((a[2],a[3],a[4]))
       answer+=a[2]

    for i in range(k):
        move();over()

    print(answer)
  
    
    
 
