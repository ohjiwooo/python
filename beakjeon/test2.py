


def main(arr,h,p):
    answer=[0]*(p+1)
    for i in range(len(arr)):
        if len(arr[i])>0:
            a=sum(arr[i],h)
    answer[i]=a
    return answer

def sum(arr2,t):
    sum=[]
    for i in range(len(arr2)):
        ans=0
        while(ans<=t and i < len(arr2)):
            ans+=arr2[i];i+=1
        sum.append(ans)
    sum.sort(reverse=True)
    return sum[0]



if __name__=="__main__":
    p,n,h=map(int,input().split())
    arr=[ [] for i in range(p+1)]
    for i in range(n):
        a,b=map(int,input().split())
        if b>h : continue
        arr[a].append(b)


    answer=main(arr,h,p)
    for i in range(1,len(answer)):
        print(i,end=' ')
        print(answer[i]*1000)