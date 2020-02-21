class EmptyStackError(Exception):
    pass

class StackFullError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class Stack:
    
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, data): # adding new node at the end of linked list
        temp=Node(data)
        temp.link=self.top
        self.top=temp

    def pop(self): # removing first node at the beginning of linked list
        if self.is_empty():
            raise EmptyStackError("Stack is Empty")
        popped=self.top.info
        self.top=self.top.link
        return popped

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is Empty")
        return self.top.info

    def size(self):
        if self.is_empty():
            return 0
        count=0
        p=self.top
        while p is not None:
            count+=1
            p=p.link
        return count        
    
    def display_stack(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("\nStack is:\n-----")        
        p=self.top
        while p is not None:
            print(p.info)
            p=p.link
            print('-----')