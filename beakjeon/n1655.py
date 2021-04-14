import heapq
import sys



if __name__=='__main__':

    n=int(sys.stdin.readline())
    minh=[];maxh=[]

    for i in range(n):
        a=int(sys.stdin.readline())
        if i%2==0:
            heapq.heappush(maxh,-a)
        else:
            heapq.heappush(minh,a)
        
        if len(minh) > 0 and -maxh[0] > minh[0]:
            b=maxh[0]
            c=minh[0]
            heapq.heappop(maxh)
            heapq.heappop(minh)
            heapq.heappush(maxh,-c)
            heapq.heappush(minh,-b)
            


        print(-maxh[0])
            
