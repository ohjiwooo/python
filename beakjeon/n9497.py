
def union(arr2,x,y):
    if arr2[x] > arr2[y] :
        arr2[arr2[x]] = arr2[y]
    else : arr2[arr2[y]] =arr2[x]

def find(arr2,x):
    if arr2[x]!=x:
        arr2[x]= find(arr2,arr2[x]);return arr2[x]
    else : return x

if __name__=='__main__':
    ans=[]
    while(True):
        m,n=map(int,input().split())
        total=0
        if m==0 and n==0 : break
        arr=[]*n

        arr2=[None]*m
        for i in range(m):
            arr2[i]=i

        for i in range(n):
            a,b,c=map(int,input().split())
            arr.append((c,a,b))
            total+=c
        answer=0
        arr.sort()
        
        for i in range(0,n):
            if find(arr2,arr[i][1]) != find(arr2,arr[i][2]):
                union(arr2,arr[i][1],arr[i][2])
                answer+=arr[i][0]
        ans.append(total-answer)
    
    for i in range(len(ans)):
        print(ans[i])
        
        

        

        

