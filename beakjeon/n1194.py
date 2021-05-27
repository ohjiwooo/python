from itertools import permutations

def check(num,n):
   
    for i in range(len(n)):
        num+=n[i]
    num=int(num)
    for i in range(2,num):
        if num%i==0: return 0 #소수가 아니면 0
    return 1

def solution(numbers):
    answer = 0
    
    for i in range(1,len(numbers)):
        num=list(permutations(numbers,i))
        print(num)
        for j in range(len(num)):
            if num[j][0]!=0 and check(num[j],n)==1:
                answer+=1
    return answer

if __name__=="__main__":
    numbers="011"
    number=[]
    for i in range(len(numbers)):
        number.append(int(numbers[i]))
    print(number)
    print(solution(number))