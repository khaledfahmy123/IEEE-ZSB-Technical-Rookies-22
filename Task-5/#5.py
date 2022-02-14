class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

    ## insertion implementation :)

    def insert(self, val):
        cur = self.root
        if not cur: 
            self.root = Node(val)
            return self.root
        
        while cur:
            if cur.info > val: 
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    break
            else: 
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    break
        
        return self.root

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None



