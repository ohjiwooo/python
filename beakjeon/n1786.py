

def getpi(arr,pi):
    j=0
    for i in range(1,len(arr)):
        while(arr[i]!=arr[j] and j>0):
            j=pi[j-1]
        if arr[i]==arr[j]:
            pi[i]=(j+1);j+=1

def kmp(arr,text,pi,answer):
    ans=0
    j=0
    m=len(arr)
    for i in range(len(text)):
        while(text[i]!=arr[j] and j>0):
            j=pi[j-1]
        if arr[j]==text[i]:
            if j==(m-1) : ans+=1;answer.append(i-m+2);j=pi[j]
            else : j+=1

    return ans

if __name__=='__main__':

    
    text=str(input())
    arr=str(input())
    answer=[]
    pi=[0]*(len(arr)+1)
    getpi(arr,pi)   
    ans=kmp(arr,text,pi,answer)

    print(ans)
    for i in range(len(answer)):
        print(answer[i],end=' ')