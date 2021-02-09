

if __name__=='__main__':
    
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        a=int(input())
        arr.append(a)

    arr.sort()

    e=1;s=0;answer=0;c=0

    while(s<e):
        if arr[e]-arr[s] >= m :
            if answer > arr[e]-arr[s] or (answer==0 and c==0): answer=arr[e]-arr[s];c=1
            s+=1
        else :e+=1
        if s == e : e+=1
        if e >= n :break

    print(answer)