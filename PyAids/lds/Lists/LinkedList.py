from .Node import Node

class LinkedList:
    
    def __init__(self, head=None):
        if head == None:
            self.head = None
        else:
            self.head = Node(head)
    
    def __str__(self):
        return f"{self.head.value} --> {self.head.next_node.value}"
        
    def __repr__(self):
        repr_str = f"LinkedList(head=> data({self.head.value}) --> next_node({self.head.next_node.value}))"
        return repr_str
        
    def __len__(self):
        pass
    
    
    
    
    
    
    
    
    