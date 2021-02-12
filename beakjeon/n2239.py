from collections import deque

board=[ [0 for i in range(9)] for j in range(9) ]
q=deque()
r_check = [ [False for i in range(10)] for j in range(10) ]
c_check = [ [False for i in range(10)] for j in range(10) ]
s_check = [[[False for i in range(10)] for j in range(3)] for k in range(3)]

def insert():
    global q;global board;global r_check;global c_check;global s_check
    
    if len(q)==0:
        p(board);return True

    ni=q[0][0];nj=q[0][1];q.popleft()
    for i in range(1,10):
        board[ni][nj]=i
        k=int(ni/3);l=int(nj/3)
        if r_check[ni][i]==False and c_check[i][nj]==False and s_check[k][l][i]==False:
            r_check[ni][i]=True;c_check[i][nj]=True;s_check[k][l][i]=True
            if insert()==True : return True
            r_check[ni][i]=False;c_check[i][nj]=False;s_check[k][l][i]=False
    
    board[ni][nj]=0
    q.appendleft((ni,nj))
    return False

        
def p(arr):
    for i in range(9):
            for j in range(9):
                if j!=8:
                    print(arr[i][j],end='')
                else :print(arr[i][j])


if __name__=='__main__':

    
    for i in range(9):
        a=str(input())
        for j in range(9):
            board[i][j]=int(a[j])
        
    for i in range(9):
        for j in range(9):
            k=int(i/3);l=int(j/3)
            r_check[i][board[i][j]]=True
            c_check[board[i][j]][j]=True
            s_check[k][l][board[i][j]]=True
            if board[i][j]==0:
                q.append((i,j))
    
    insert()

    