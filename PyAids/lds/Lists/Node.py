class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node
            
        def __repr__(self):
            return f"Node({self.value})"
        
        def __str__(self):
            return f"Node({self.value})"
        
        
        def next(self):
            return self.next_node
        
        def set_next(self, node):
            self.next_node = node
            
        def get_value(self):
            return self.value
        
        def set_value(self, value):
            self.value = value