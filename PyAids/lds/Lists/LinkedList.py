from .Node import Node

class LinkedList:
    
    def __init__(self, head=None):
        if head == None:
            self.head = None
        else:
            self.head = Node(head)
    
    def __str__(self):
        if self.head == None:
            return "None"
        elif self.head.next_node == None:
            return f"{self.head.value}"
        else:
            str_str = ""
            current = self.head
            while current.next_node != None:
                str_str += f"{current.value} --> "
                current = current.next_node
            
            str_str += f"{current.value}"
            return str_str
        
    def __repr__(self):
        if self.head.next_node == None:
            repr_str = f"LinkedList(head=> data({self.head.value}) --> next_node(None))"
            return repr_str
        repr_str = f"LinkedList(head=> data({self.head.value}) --> next_node({self.head.next_node.value}))"
        return repr_str
        
    def __len__(self):
        if self.head == None:
            return 0
        else:
            count = 1
            current = self.head
            while current.next_node != None:
                count += 1
                current = current.next_node
            return count
    
    
    def insert_end(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
            current.next_node = Node(value)
    
    def insert_begin(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
    
    
    
    
    
    
    
    