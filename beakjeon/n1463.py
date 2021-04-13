
def f(n):

    arr=[ 0 for i in range(n+5)]
    for i in range(1,n+1):

        if i%3==0 :
            if arr[i]==0:
                arr[i]=arr[int(i/3)]+1
            else : arr[i]= min(arr[int(i/3)]+1,arr[i])
        if i%2==0 :
            if arr[i]==0:
                arr[i]=arr[int(i/2)]+1
            else : arr[i]= min(arr[int(i/2)]+1,arr[i])
        if i-1>0:
            if arr[i]==0:
                arr[i]=arr[i-1]+1
            else : arr[i]=min(arr[i-1]+1,arr[i])
    return arr[n]



if __name__=='__main__':

    n=int(input())
    print(f(n))
