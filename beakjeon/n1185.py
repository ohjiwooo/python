
def uni(a,b,arr):
    if arr[a]>arr[b]:
        arr[arr[a]]=arr[b]
    else:
        arr[arr[b]]=arr[a]

def find(a,arr):
    if arr[a]==a : return a
    else : arr[a]=find(arr[a],arr);return arr[a]

if __name__=='__main__':

    n,p=map(int,input().split())
    arr=[ 0 for i in range(n+2)]
    arr2=[ 0 for i in range(n+2)]
    for i in range(n+2):
        arr2[i]=i
    cost=[]
    temp=999999
    for i in range(1,n+1):
        arr[i]=int(input())
        if arr[i]<temp: temp=arr[i]
    for i in range(p):
        a,b,c=map(int,input().split())
        c= c*2+arr[a]+arr[b]
        cost.append((c,a,b))
    cost.sort()
    answer=0
    for k in range(p):
        w=cost[k][0];i=cost[k][1];j=cost[k][2]
        if find(i,arr2)!=find(j,arr2):
            uni(i,j,arr2);answer+=w
    answer+=temp
    print(answer)