
arr2=[None]*(10005)
answer=0

def find(k):
    global arr2
    if k == arr2[k]: return k
    else : arr2[k] = find(arr2[k]);return arr2[k]

def union(x,y):
    global arr2
    if arr2[x] > arr2[y] :
        arr2[arr2[x]] = arr2[y]
    else : arr2[arr2[y]] = arr2[x]

if __name__=='__main__':

    v,e=map(int,input().split())
    arr = []*e
    for i in range(e):
        a,b,c=map(int,input().split())
        if a > b  : a,b = b,a
        arr.append((c,a,b))

    arr.sort()
    
    for i in range(v+1):
        arr2[i]=i

    arr2[arr[0][2]]=arr[0][1] #첫 엣지
    answer+=arr[0][0]
    for i in range(1,e):
        if find(arr[i][1]) != find(arr[i][2]) :
            union(arr[i][1],arr[i][2])
            answer+=arr[i][0]
    print(answer)

    