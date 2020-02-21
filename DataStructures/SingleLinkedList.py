class SingleLinkedListNode:
    def __init__(self,value):
        self.info=value
        self.link=None
        
class SingleLinkedList:
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
                p=p.link
            print()
    
    def count_nodes(self):
        p=self.start
        n=0
        while p is not None:
            n+=1
            p=p.link
        print("Number of nodes in the list:",n)
        
    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print(x,"is at position:",position)
                return True
            position+=1
            p=p.link
        else:
            print(x,"not found in the list.")
            return False
        
    def insert_in_beginning(self,data):
        temp=SingleLinkedListNode(data)
        temp.link=self.start
        self.start=temp
        
    def insert_at_end(self,data):
        temp=SingleLinkedListNode(data)
        if self.start is None:
            self.start=temp
            return
        
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp
        
        
    def create_list(self):
        n=int(input("Enter the number of nodes:"))
        if n==0:
            return
        for i in range(n):
            data=int(input("Enter the element to be inserted:"))
            self.insert_at_end(data)
            
    def insert_after(self,data,x):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
            
        if p is None:
            print(x,"not present in the list")
            return
        else:
            temp=SingleLinkedListNode(data)
            temp.link=p.link
            p.link=temp
            
    def insert_before(self,data,x):
        # if list is empty
        if self.start==None:
            print("List is empty.")
            return
        # x is in first node, new node is to be inserted before first node
        if x==self.start.info:
            temp=SingleLinkedListNode(data)
            temp.link=self.start
            self.start=temp
            return
        
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
            
        if p.link is None:
            print(x,"is not present in the list")
            return
        else:
            temp=SingleLinkedListNode(data)
            temp.link=p.link
            p.link=temp
            
    def insert_at_position(self,data,k):
        if k==1:
            temp=SingleLinkedListNode(data)
            temp.link=self.start
            self.start=temp
            return
        
        p=self.start
        i=1
        while i<k-1 and p is not None:
            p=p.link
            i+=1
        if p is None:
            print("Insertion is possible only upto position",i)
            return
        else:
            temp=SingleLinkedListNode(data)
            temp.link=p.link
            p.link=temp
            
    def delete_node(self,x):
        if self.start is None:
            print("List is empty.")
            
        if self.start.info==x:
            self.start=self.start.link
            return
        
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
            
        if p.link is None:
            print("Element",x,"is not in the list")
        else:
            p.link=p.link.link
    
    def delete_first_node(self):
        if self.start is None:
            return
        self.start=self.start.link
        
    def delete_last_node(self):
        if self.start is None:
            return
        
        if self.start.link is None:
            self.start=None
            return
        
        p=self.start
        while p.link.link is not None:
            p=p.link
        p.link=None
        
    def reverse_list(self):
        print("List is reversed")
        prev=None
        p=self.start
        while p is not None:
            next=p.link
            p.link=prev
            prev=p
            p=next
        self.start=prev
        
    def has_cycle(self):
        if self.find_cycle() is None:
            print('No Cycle Detected')
            return False
        else:
            print('Cycle Detected')
            return True
        
    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        
        slow=self.start
        fast=self.start
        
        while fast is not None and fast.link is not None:
            slow=slow.link
            fast=fast.link.link
            if slow==fast:
                print('Cycle is at position',slow.info)
                return slow
        return None
    
    def remove_cycle(self):
        c=self.find_cycle()
        if c is None:
            print('No Cycle available to remove')
            return
        print('Node at which cycle is detected is:',c.info)
    
        p=c
        q=c
        len_cycle=0

        while True:
            len_cycle+=1
            q=q.link
            if p==q:
                break
        print('Length of cycle is:',len_cycle)
        
        len_remaining_list=0
        p=self.start
        while p!=q:
            len_remaining_list+=1
            p=p.link
            q=q.link
            
        print('Number of nodes not included in the cycle are:',len_remaining_list)
        length_list=len_cycle+len_remaining_list
        print('Length of the list is:',length_list)
        
        p=self.start
        for i in range(length_list-1):
            p=p.link
        p.link=None
        
        
    def insert_cycle(self,x):
        if self.start is None:
            return
        
        p=self.start
        px=None
        prev=None
        
        while p is not None:
            if p.info==x:
                px=p
            prev=p
            p=p.link
            
        if px is not None:
            prev.link=px
        else:
            print(x,'is not present in the list')   
