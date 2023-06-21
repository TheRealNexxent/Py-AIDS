from .Node import Node

class DoublyLinkedList:
    
    def __init__(self, head=None) -> None:
        if head is None:
            self.head = None
        else:
            self.head = Node(head)
        
        
    def __str__(self) -> str:
        if self.head == None:
            return "None"
        elif self.head.next_node == None:
            return f"None <-- {self.head.value} --> None"
        else:
            current = self.head
            string = "None <-- "
            while current.next_node != None:
                string += f"{current.value} <--> "
                current = current.next_node
            string += f"{current.value} --> None"
            
            return string
        
    def __repr__(self) -> str:
        repr_str = f"DoublyLinkedList({self.__str__()})"
        return repr_str
    
    def __len__(self) -> int:
        if self.head == None:
            return 0
        else:
            current = self.head
            count = 1
            while current.next_node != None:
                count += 1
                current = current.next_node
            return count
        
        
    def __getitem__(self, index: int):
        if index >= self.__len__() or index < 0:
            raise IndexError("Index out of range.")
        else:
            current = self.head
            for i in range(index):
                current = current.next_node
            return current.value
        
    def insert_end(self, value):
        if self.head == None:
            self.head = Node(value)
        elif(self.head.next_node == None):
            self.head.next_node = Node(value)
            self.head.next_node.prev_node = self.head
        else:
            current = self.head
            prev = self.head.prev_node
            while current.next_node != None:
                prev = current
                current = current.next_node
            current.next_node = Node(value)
            current.next_node.prev_node = prev
    
    def insert_begin(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            self.head.prev_node = Node(value, next_node=self.head)
            self.head = self.head.prev_node
            
    def insert(self, value: any, index: int):
        if index == 0:
            self.insert_begin(value)
        elif index == self.__len__():
            self.insert_end(value)
        else:
            if index > self.__len__() or index < 0:
                raise IndexError("Index out of range.")
            else:
                current = self.head
                prev = self.head.prev_node
                for i in range(index):
                    prev = current
                    current = current.next_node
                
                current = Node(value, next_node=current, prev_node=prev)
                current.next_node.prev_node = current
                current.prev_node.next_node = current
    
    def search(self, value):
        if self.head == None:
            return False
        else:
            current = self.head
            while current.next_node != None:
                if current.value == value:
                    return True
            
            return False
        
    def index(self, value):
        if self.head == None:
            return None
        elif self.head.value == value:
            return 0
        else:
            current = self.head
            index = 0
            while current.next_node != None:
                if current.value == value:
                    return index
                index += 1
                current = current.next_node
            return None
    
    def delete_begin(self):
        if self.__len__() == 0:
            raise ValueError("Cannot delete from empty list.")
        elif self.__len__() == 1:
            self.head = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
    
    def delete_end(self):
        if self.__len__() == 0:
            raise ValueError("Cannot delete from empty list.")
        elif self.__len__() == 1:
            self.head = None
        else:
            current = self.head
            prev = self.head.prev_node
            while current.next_node != None:
                prev = current
                current = current.next_node
            prev.next_node = None
        
    def delete_index(self, index: int):
        if self.__len__() == 0:
            raise IndexError("Index out of range.")
        else:
            if index > self.__len__():
                raise IndexError("Index out of range.")
            elif index < 0:
                raise IndexError("Index out of range.")
    
    def delete_value(self, value: any):
        if self.__len__() == 0:
            raise ValueError("Cannot delete from empty list.")
        elif self.__len__() == 1:
            if self.head.value == value:
                self.head = None
        else:
            current = self.head
            prev = self.head.prev_node
            while current.next_node != None:
                if current.value == value:
                    prev.next_node = current.next_node
                    current.next_node.prev_node = prev
                    return
                prev = current
                current = current.next_node
            if current.value == value:
                prev.next_node = None
                return
            raise ValueError("Value not found in list.")