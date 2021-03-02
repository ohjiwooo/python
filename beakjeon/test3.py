
s=0;e=0;now=0
def main(m):
    global s;global e;global now

    l=0
    for i in range(s,int(e/2)):
        if m[i]> l:l=m[i]
    
   
    r=0
    for i in range(int(e/2),e):
        if m[i]> r:r=m[i]
    if l > r :
        s=int(e/2);return l
    else : e=int(e/2);return r
    


if __name__=="__main__":

    e=int(input())
    m=list(map(int,input().split()))
    now=e
    answer=0 
    while(now > 1):

        answer+=main(m);now/=2

    print(answer)