from collections import deque

inf=9876543210

def bfs(q,n,trans,e):
    vis=[ 0 for i in range(n+1)]
    qq=deque()
    while(len(q)>0):
        a=q[0];q.popleft();qq.append(a)
        vis[a]=1
        while(len(qq)>0):
            b=qq[0];qq.popleft()
            if b==e : return 1
            for i in range(len(trans[b])):
                if vis[trans[b][i][0]]==0:
                    qq.append(trans[b][i][0]);vis[trans[b][i][0]]=1
    return 0


def bel(n,s,e,money,trans):
    answer=[ inf for i in range(n+1)]
    answer[s]=-money[s]
    q=deque()
    for i in range(n): #마을 수 만큼 반복
        for j in range(n):
            if answer[j]==inf : continue
            for k in range(len(trans[j])):
                if answer[trans[j][k][0]]>answer[j] +trans[j][k][1]-money[trans[j][k][0]]:
                    if i==n-1:
                        q.append(trans[j][k][0])
                    else :answer[trans[j][k][0]]=answer[j]+trans[j][k][1]-money[trans[j][k][0]]
                

    if bfs(q,n,trans,e)==1 : print('Gee');return 0
    elif answer[e]==inf : print('gg');return 0
    else : print(-answer[e]); return 0


if __name__=='__main__':

    n,s,e,m=map(int,input().split())
    trans=[ [] for i in range(n+1)]
    money=[]
    for i in range(m):
        a,b,c=map(int,input().split())
        trans[a].append((b,c))

    money=list(map(int,input().split()))
    bel(n,s,e,money,trans)




    
