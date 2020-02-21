class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.prev=value
        self.next=None

class Deque:
    
    def __init__(self):
        self.front=None
        self.rear=None
        
    def is_empty(self):
        return self.rear == None

    def insert_rear(self, data): 
        temp=Node(data)
        if self.is_empty():
            self.rear=self.front=temp
        else:
            temp.next=self.rear
            self.rear.prev=temp
            self.rear=temp

    def insert_front(self, data): 
        temp=Node(data)
        if self.is_empty():
            self.rear=self.front=temp
        else:
            self.front.next=temp
            temp.prev=self.front
            self.front=temp

    def delete_rear(self): 
        if self.is_empty():
            raise EmptyQueueError("Deque is Empty")
        
        x=self.rear.info
        if self.rear.next is None:
            self.rear=self.front=None
        else:
            self.rear=self.rear.next
            self.rear.prev=None
        return x
    
    def delete_front(self): 
        if self.is_empty():
            raise EmptyQueueError("Deque is Empty")
        
        x=self.front.info
        if self.rear.next is None:
            self.front=self.rear=None
        else:
            self.front=self.front.prev
            self.front.next=None
        return x

    def size(self):
        if self.is_empty():
            return 0
        n=0
        p=self.rear
        while p is not None:
            n+=1
            p=p.next
        return n
        
    def display_deque(self):
        if self.is_empty():
            print("Deque is empty")
            return
        print('\nDeque:\n')
        p=self.rear
        deque='|'
        while p is not None:
            deque=deque+' '+str(p.info)+' |'
            p=p.next
        print(deque)