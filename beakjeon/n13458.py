


if __name__=='__main__':
    answer=0
    a=int(input())
    arr=[]
    arr=list(map(int,input().split()))
    c,d=map(int,input().split())

    for i in range(a):
        arr[i]-=c;answer+=1
        if arr[i]>0:
            if(arr[i]%d==0):answer+=int(arr[i]/d)
            else:answer+=int(arr[i]/d)+1
    print(answer)


            




