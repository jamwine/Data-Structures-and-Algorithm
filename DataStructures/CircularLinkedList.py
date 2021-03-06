class CircularLinkedListNode(object):
    def __init__(self,value):
        self.info=value
        self.link=None
        
class CircularLinkedList(object):
    def __init__(self):
        self.last=None
    
    def display_list(self):
        if self.last==None:
            print("List is empty")
            return
        
        p=self.last.link
        while True:
            print(p.info,' ',end='')
            p=p.link
            if p==self.last.link:
                break
        print()
        
    def insert_in_beginning(self,data):
        temp=CircularLinkedListNode(data)
        temp.link=self.last.link
        self.last.link=temp
        
    def insert_in_empty_list(self,data):
        temp=CircularLinkedListNode(data)
        self.last=temp
        self.last.link=self.last
        
    def insert_at_end(self,data):
        temp=CircularLinkedListNode(data)
        temp.link=self.last.link
        self.last.link=temp
        self.last=temp
        
    def create_list(self):
        n=int(input("Enter the number of nodes:"))
        if n==0:
            return
        data=int(input("Enter the element to be inserted:"))
        self.insert_in_empty_list(data)
        
        for i in range(n-1):
            data=int(input("Enter the element to be inserted:"))
            self.insert_at_end(data)
        
    def insert_after(self,data,x):
        p=self.last.link
        
        while True:
            if p.info==x:
                break
            p=p.link
            if p==self.last.link:
                break
        if p==self.last.link and p.info!=x:
            print(x,'not present in the list')
        else:
            temp=CircularLinkedListNode(data)
            temp.link=p.link
            p.link=temp
            if p==self.last:
                self.last=temp
                    
    def delete_first_node(self):
        if self.last is None:
            return
        if self.last.link==self.last:
            self.last=None
            return
        self.last.link=self.last.link.link
    
    def delete_last_node(self):
        if self.last is None:
            return
        if self.last.link==self.last:
            self.last=None
            return
        
        p=self.last.link
        while p.link!=self.last:
            p=p.link
        p.link=self.last.link
        self.last=p
        
    def delete_node(self,x):
        if self.last is None:
            return
        if self.last.link==self.last and self.last.info==x:
            self.last=None
            return
        
        p=self.last.link
        while p.link!=self.last.link:
            if p.link.info==x:
                break
            p=p.link
            
        if p.link==self.last.link:
            print(x,'Not found in the list')
        else:
            p.link=p.link.link
            if self.last.info==x:
                self.last=p
                