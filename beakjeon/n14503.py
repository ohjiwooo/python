answer=1;n=0;m=0;r=0;c=0;d=0;f=0


def clean(borad,vis):
    global answer,n,m,r,c,d,f
    imap=[0,-1,0,1]
    jmap=[-1,0,1,0]
 
    newr=r+imap[d];newc=c+jmap[d]
    if vis[newr][newc]==0 and borad[newr][newc]==0:
        vis[newr][newc]=1;r=newr;c=newc;answer+=1;f=0
    else:f+=1
    d=(d+3)%4

    
        
       
def find(borad,vis):
    global answer,n,m,r,c,d,f
    imap=[1,0,-1,0]
    jmap=[0,-1,0,1]
    while(1):
        if f==4:
            if borad[r+imap[d]][c+jmap[d]]==0:
                r=r+imap[d];c=c+jmap[d];f=0
            else:print(answer);return 0
        clean(borad,vis)
    return 0
        


if __name__=='__main__':
    
    n,m=map(int,input().split())
    r,c,d=map(int,input().split())
    board=[[] for i in range(n)]
    vis=[  [0 for i in range(m)] for j in range(n)]
    vis[r][c]=1
    for i in range(n):
        board[i]=list(map(int,input().split()))
    
    find(board,vis)
    
        
