
# Single Linked List - Insertion and deletion (at the end of then node)

class Node:
    def __init__(self,key):
        self.data = key
        self.next = None
    
    
class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.next = None
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
    
    def delete(self):
        new_head = self.head
        while new_head:
            if new_head.next == None:
                self.head = None
            elif new_head.next.next == None:
                new_head.next = None
                break
            else:
                new_head = new_head.next



            

        
    def printNode(self):
        cur_head = self.head
        while cur_head:
            print(cur_head.data, end="")
            cur_head = cur_head.next



if __name__=='__main__': 
    
    myLinkedList = LinkedList()
    myLinkedList.insert(2)
    myLinkedList.insert(3)
    myLinkedList.insert(6)
    myLinkedList.insert(9)
    print("After Insertion:")
    myLinkedList.printNode()
    myLinkedList.delete()
    print("\nAfter Deletion:")
    myLinkedList.printNode()
    
   
    
    
    





