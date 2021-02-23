import heapq

heap=[]

answer=0
if __name__=='__main__':

    iv,e=map(int,input().split())
    arr = [[] for i in range(iv+1)]
    vis = [False] * (iv+1)
    for i in range(e):
        a,b,c=map(int,input().split())
        arr[a].append((b,c))
        arr[b].append((a,c))

    n=0
    v=1
    vis[1]=True
    while(n<iv-1):
        for i in range(len(arr[v])):
            if vis[arr[v][i][0]] != True :
                heapq.heappush(heap,(arr[v][i][1],arr[v][i][0]))
        while(True):
            if vis[heap[0][1]]==True : heapq.heappop(heap)
            else : v=heap[0][1];answer += heap[0][0]
                   heapq.heappop(heap);vis[v]=True;n+=1;break

    print(answer)

