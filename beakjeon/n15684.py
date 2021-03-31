
def check(board,n,h):   #자기 자신으로 도착한 수
    answer=0
    for j in range(1,n+1):
        here=j
        for i in range(1,h+1):
            if board[i][here]==1:
                here=here+1
            elif board[i][here-1]==1:
                here=here-1

        if here==j:answer+=1
    return answer

def make(board,n,h,now,goal):
    if now==goal:
        if check(board,n,h)==n:print(goal);return 1
    for j in range(1,n+1):
        for i in range(1,h+1):
            if board[i][j] != 1 and board[i][j-1]!=1 and j+1<n+1 and board[i][j+1] !=1:
                board[i][j]=1
                if make(board,n,h,now+1,goal)==1:return 1
                board[i][j]=0   
    return 0


if __name__=='__main__':

    n,m,h=map(int,input().split())
    board=[[0 for i in range(n+1)]for i in range(h+1)]

    for i in range(m):
        a,b=map(int,input().split())
        board[a][b]=1

    if check(board,n,h)==n:print(0)
    elif make(board,n,h,0,1)==1 : exit
    elif make(board,n,h,0,2)==1 : exit
    elif make(board,n,h,0,3)==1 : exit
    else : print(-1); 



    

    

    
