class EmptyQueueError:
    pass

class Node:
    def __init__(self,value,pr):
        self.info=value
        self.priority=pr
        self.link=None
        
class PriorityQueue:
    def __init__(self):
        self.start=None
    
    def is_empty(self):
        return self.start==None
    
    def size(self):
        n=0
        p=self.start
        while p is not None:
            n+=1
            p=p.link
        return n
    
    def enqueue(self,data,data_priority):
        temp=Node(data,data_priority)
        if self.is_empty() or data_priority< self.start.priority:
            temp.link=self.start
            self.start=temp
        else:
            p=self.start
            while p.link!=None and p.link.priority <=data_priority:
                p=p.link
            temp.link=p.link
            p.link=temp
            
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x=self.start.info
        self.start=self.start.link
        return x
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print('\nQueue:\n')
        p=self.start
        queue='|'
        while p is not None:
            queue=queue+' '+str(p.info)+'('+str(p.priority)+') |'
            p=p.link
        print(queue)