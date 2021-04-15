
class Stackk:
    
    class Node:
        def __init__(self,ele,next):
            self.ele = ele
            self.next = next
    
    def __init__(self):
        self.head=None
        self.size = 0

    def len(self):
        print("size of the stack is",self.size)

    def is_empty(self):
        return self.size == 0


    def push(self,ele):
        self.head=self.Node(ele,self.head)
        self.size += 1


    def pop (self):
        if self.is_empty():
            print("Stack is Empty")
        value = self.head.ele
        self.head = self.head.next
        self.size -= 1
        return value

    def top(self):
        if self.is_empty():
            print("Empty Stack")
        print(self.head.ele)

    def display(self):
        temp = self.head
        while temp:
            print(temp.ele)
            temp=temp.next
        print()

    