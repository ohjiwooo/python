

if __name__=='__main__':

    answer=0

    n,m=map(int,input().split())
    arr=[]
    arr=list(map(int,input().split()))

    s=0;e=0;sum=0;nn=0

    while(s<=e):
        if sum < m :
            if e+1 > n:
                break
            else : sum+=arr[e];e+=1;nn+=1

        else:
            if answer > nn or answer==0: answer = nn
            sum-=arr[s];s+=1;nn-=1

    print(answer)


