# Queue using Stacks(2)

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enq(self,value):
        self.s1.append(value)
    
    def deq(self):
        
        if len(self.s1) ==0 and len(self.s2) == 0:
            print("Q is Empty")
        elif len(self.s2) > 0:
            self.s2.pop()
        else:
            while len(self.s1)-1 >= 0:
                self.s2.append(self.s1.pop())
            self.s2.pop()

    def printval(self):
        for i in self.s1:
            print(f"printing s1 {i}")
        for i in self.s2:
            print(f"printing s2 {i}")

if __name__ == "__main__":
    q = Queue()
    q.enq(5)
    q.enq(6)
    q.enq(7)
    q.printval()
    q.deq()
    q.enq(9)
    q.printval()
    q.deq()
    q.printval()
            
            

            