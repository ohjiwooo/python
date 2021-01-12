
def robotin(arr,arr2,k2): #로봇올리기
    if arr[0] >= 1 and arr2[0]==None : 
        arr[0] -=1
        arr2[0] = 1
        if arr[0] == 0 : k2+=1 
    return k2

def robotmove(arr,arr2,n,k2):
    for i in range(n-2,0,-1):
        if arr2[i+1] == None and arr[i+1] >= 1 and arr2[i]==1: #없고 내구도 가능
            arr2[i] = None #이동 
            arr2[i+1] = 1 #이동 
            arr[i+1] -=1 #내구도 감소
            if arr[i+1] == 0 : k2+=1
    return k2

def movebelt(arr,m):
    b=arr[m-1]

    for i in range(m-1,0,-1):
        arr[i] = arr[i-1]

    arr[0]=b
    

def p(arr):
    for i in range(0,len(arr)):
        print(arr[i])

if __name__=="__main__":
    ans=1
    k2=0
    n,k=map(int,input().split())
    m=n*2
    arr = [None] * m #내구도
    arr2 = [None] * m #로봇여부

    arr = list(map(int, input().split()))

    for i in range(0,m):
        if arr[i] == 0 : k2+=1  #내구도 0인곳의 개수

    while True:

        if arr2[n-1] == 1:
            arr2[n-1] = None #로봇내림
        
        movebelt(arr,m)
        movebelt(arr2,m) #벨트돌아감

        if arr2[n-1] == 1:
            arr2[n-1] = None #로봇내림
        

        k2 = robotmove(arr,arr2,n,k2) #로봇이동

        if arr2[n-1] == 1:
            arr2[n-1] = None #로봇내림
        

        k2 = robotin(arr,arr2,k2) #로봇올림

        if k2 >= k : break
        ans+=1

    print(ans)


    



