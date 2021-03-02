def main():
    x = input()
    
    print(x)

if __name__=="__main__":
    s=str(input())
    arr=[]
    for i in range(len(s)):
        if(s[i]!=' '):
            arr.append(s[i])

    nn=int(input())
    arr2=[]
    for i in range(nn):
        a=str(input())
        arr2.append((a[0],a[2]))
    print(arr2)