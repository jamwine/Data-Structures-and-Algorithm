class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class Queue:
    
    def __init__(self):
        self.front = None
        self.rear=None
        self.size_queue=0        
        
    def is_empty(self):
        return self.front == None

    def enqueue(self, data): # adding new node at the end of linked list
        temp=Node(data)
        if self.front==None:
            self.front=temp
        else:
            self.rear.link=temp
        self.rear=temp
        self.size_queue+=1

    def dequeue(self): # removing first node at the beginning of linked list
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        x=self.front.info
        self.front=self.front.link
        self.size_queue-=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.front.info

    def size(self):
        return self.size_queue    
        
    def display_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print('\nQueue: (--->)\n')
        queue=''
        
        p=self.front
        while p is not None:
            queue='| '+str(p.info)+' '+queue
            p=p.link
        print(queue+'|')
            