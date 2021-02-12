import copy

def a(arr):
    arr2=[]
    arr2=copy.deepcopy(arr)
    arr2[1]=1


if __name__=='__main__':
    arr=[0]*5
    print(arr)
    a(arr)
    print(arr)
  