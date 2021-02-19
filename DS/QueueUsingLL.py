# Queue using LinkedList

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def peek(self):
        return self.front.value
    
    def enqueue(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        self.length += 1
        

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.front == self.rear:
            self.rear = None
        else:
            self.front = self.front.next
            self.length -=1

if __name__ == "__main__":
    myq = Queue()
    #print(myq.peek().__str__())
    myq.enqueue("John")
    print(myq.peek().__str__())
    myq.enqueue("Jack")
    print(myq.peek().__str__())
    myq.enqueue("Jay")
    print(myq.peek().__str__())
    myq.dequeue()
    print(myq.peek().__str__())
