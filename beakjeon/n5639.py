import sys
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self,key):
        self.l_child=None
        self.r_child=None
        self.key=key

class Tree:

    def __init__(self):
        self.root=None

    def create(self,key):
        newnode=Node(key)
        if self.root==None:
            self.root=newnode
        else : self.insert(self.root,newnode)

    def insert(self,root,newnode):
        now=root
        while(True):
            if now.key > newnode.key and now.l_child==None:
                now.l_child=newnode;break
            elif now.key < newnode.key and now.r_child==None:
                now.r_child=newnode;break
            elif now.key < newnode.key and now.r_child!=None:
                now=now.r_child
            elif now.key > newnode.key and now.l_child!=None:
                now=now.l_child

    def pre(self,root):

        print(root.key)
        if root.l_child != None :
            self.pre(root.l_child)
        if root.r_child != None :
            self.pre(root.r_child)
        
    def post(self,root):

        if root.l_child != None :
            self.post(root.l_child)
        if root.r_child != None :
            self.post(root.r_child)
        print(root.key)


if __name__=='__main__':
    arr=[]
    while (True):
        try:
            a=int(input());arr.append(a)
        except:
            break
    
    tree=Tree()
    while(len(arr)>0):
        tree.create(arr[0])
        del(arr[0])
    
    tree.post(tree.root)
    

    

