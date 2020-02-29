class DoublyLinkedListNode:
    def __init__(self,value):
        self.info=value
        self.prev=None
        self.next=None
        
class DoubleLinkedList:
    def __init__(self):
        self.start=None
        
    def display_list(self):
        if self.start is None:
            print("List is empty.")
            return
        else:
            print("List is:")
            p=self.start
            while p is not None:
                print(p.info," ",end="")
                p=p.next
            print()
    
    def count_nodes(self):
        p=self.start
        n=0
        while p is not None:
            n+=1
            p=p.next
        print("Number of nodes in the list:",n)
        return n
        
    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print(x,"is at position:",position)
                return True
            position+=1
            p=p.next
        else:
            print(x,"not found in the list.")
            return False
        
    def insert_in_beginning(self,data):
        temp=DoublyLinkedListNode(data)
        temp.next=self.start
        self.start.prev=temp
        self.start=temp
    
    def insert_in_empty_list(self,data):
        temp=DoublyLinkedListNode(data)
        self.start=temp
    
    def insert_at_end(self,data):
        temp=DoublyLinkedListNode(data)
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p
        
    def create_list(self):
        n=int(input("Enter the number of nodes:"))
        if n==0:
            return
        data=int(input("Enter the first element to be inserted:"))
        self.insert_in_empty_list(data)
            
        for i in range(n-1):
            data=int(input("Enter the next element to be inserted:"))           
            self.insert_at_end(data)
            
    def insert_after(self,data,x):
        temp=DoublyLinkedListNode(data)
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.next
            
        if p is None:
            print(x," not present in the list")
        else:
            temp.prev=p
            temp.next=p.next
            if p.next is not None:
                p.next.prev=temp
            p.next=temp
            
    def insert_before(self,data,x):
        if self.start is None:
            print("List is empty")
            return

        if x==self.start.info:
            temp=DoublyLinkedListNode(data)
            temp.next=self.start
            self.start.prev=temp
            self.start=temp
            return
        
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.next
            
        if p is None:
            print(x,"is not present in the list")
        else:
            temp=DoublyLinkedListNode(data)
            temp.prev=p.prev
            temp.next=p               
            p.prev.next=temp
            p.prev=temp
            
    def delete_node(self,x):
        if self.start is None:
            print("List is empty")
            
        if self.start.next is None:
            if self.start.info==x:
                self.start=None
            else:
                print(x,'not found')
                return
        
        if self.start.info==x:
            self.start=self.start.next
            self.start.prev=None
            return
        
        p=self.start.next
        while p.next is not None:
            if p.info==x:
                break
            p=p.next
            
        if p.next is not None:
            p.prev.next=p.next
            p.next.prev=p.prev
        else:
            if p.info==x:
                p.prev.next=None
            else:
                print("Element",x,"is not in the list")
        
    def delete_first_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start=None
            return
        self.start=self.start.next
        self.start.prev=None
        
    def delete_last_node(self):
        if self.start is None:
            return
        
        if self.start.next is None:
            self.start=None
            return
        
        p=self.start
        while p.next is not None:
            p=p.next
        p.prev.next=None
        
    def reverse_list(self):
        if self.start is None:
            return
        p1=self.start
        p2=p1.next
        p1.next=None
        p1.prev=p2
        
        while p2 is not None:
            p2.prev=p2.next
            p2.next=p1
            p1=p2
            p2=p2.prev
        self.start=p1
        print("List is reversed")
        