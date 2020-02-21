class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class Queue:
    
    def __init__(self):
        self.rear=None
        
    def is_empty(self):
        return self.rear == None

    def enqueue(self, data): 
        temp=Node(data)
        if self.is_empty():
            self.rear=temp
            self.rear.link=self.rear
        else:
            temp.link=self.rear.link
            self.rear.link=temp
            self.rear=temp

    def dequeue(self): 
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        
        if self.rear.link==self.rear:
            temp=self.rear
            self.rear=None
        else:
            temp=self.rear.link
            self.rear.link=self.rear.link.link
        return temp.info

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.rear.link.info

    def size(self):
        if self.is_empty():
            return 0
        n=0
        p=self.rear.link
        while True:
            n+=1
            p=p.link
            if p==self.rear.link:
                break
        return n
        
    def display_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print('\nQueue: (--->)\n')
        queue=''
        p=self.rear.link
        while True:
            value=p.info
            p=p.link
            queue='| '+str(value)+' '+queue
            if p==self.rear.link:
                break
        print(queue+'|')
            