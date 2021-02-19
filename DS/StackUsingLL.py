#Stack using LinkedList

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def peek(self):
        return self.top.value


    def push(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
        else:
            temp = self.top
            self.top = newNode
            self.top.next = temp
        self.length += 1
    
    def pop(self):
        self.top = self.top.next
    
    def is_empty(self):
        #return True if self.length == 0 else False
        if self.length == 0:
            return True
        else:
            return False
        



if __name__ == "__main__":
    mystack = Stack()
    mystack.push("Google")
    mystack.push("youtube")
    mystack.pop()
    print(mystack.peek().__str__())
    mystack.push("facebook")
    print(mystack.peek().__str__())
    print(mystack.is_empty())

