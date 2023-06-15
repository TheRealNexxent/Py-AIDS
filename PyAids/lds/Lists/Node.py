class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node
            
        def __repr__(self):
            return f"Node({self.value})"
        
        def __str__(self):
            return f"Node({self.value})"
        
        def __eq__(self, other):
            return self.value == other.value
        
        def __lt__(self, other):
            return self.value < other.value
        
        def __gt__(self, other):
            return self.value > other.value
        
        def __le__(self, other):
            return self.value <= other.value
        
        def __ge__(self, other):
            return self.value >= other.value
        
        def __ne__(self, other):
            return self.value != other.value
        
        def __add__(self, other):
            return self.value + other.value
        
        def __sub__(self, other):
            return self.value - other.value
        
        def __mul__(self, other):
            return self.value * other.value
        
        def __truediv__(self, other):
            return self.value / other.value
        
        def __floordiv__(self, other):
            return self.value // other.value
        
        def __mod__(self, other):
            return self.value % other.value
        
        def __pow__(self, other):
            return self.value ** other.value
        
        def next(self):
            return self.next_node
        
        def set_next(self, node):
            self.next_node = node
            
        def get_value(self):
            return self.value
        
        def set_value(self, value):
            self.value = value