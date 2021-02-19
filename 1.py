# Binary Search Tree

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        newnode = Node(value)
        if self.root == None:
            self.root = newnode
        else:
            currentnode = self.root
            
            while(True):
                if value < currentnode.value:
                    if currentnode.left == None:
                        currentnode.left = newnode
                        break
                    else:
                        currentnode = currentnode.left
                else:
                    if currentnode.right == None:
                        currentnode.right = newnode
                        break
                    else:
                        currentnode = currentnode.right
    
    def inorder(self,root):
        if root: 
            self.inorder(root.left)
            print(root.value) 
            self.inorder(root.right) 
    
    def preorder(self,root):
        if root:
            print(self.root.value)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(self.root.value)

        
            

if __name__ == "__main__":
    mytree = BST()
    mytree.insert(5)
    mytree.insert(3)
    mytree.insert(1)
    print("Printing Inorder:")
    mytree.inorder(mytree.root)
    print("Printing PreOrder:")
    mytree.preorder(mytree.root)
    print("Printing PostOrder:")
    mytree.postorder(mytree.root)
    