from .Node import Node

class LinkedList:
    """
    Creates a linked list object with a head node.
    """
    
    def __init__(self, head=None):
        """
        ----------
        Parameters
        ----------
        head : any, optional
            The value of the head node. The default is None.
        """
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
        repr_str = f"LinkedList({self.__str__()})"
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
        """
        Inserts a node at the end of the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value of the node to be inserted.
        """
        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
            current.next_node = Node(value)
    
    def insert_begin(self, value):
        """
        Inserts a value at the beginning of the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value of the node to be inserted.
        """
        if self.head == None:
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
    
    
    def insert(self, value, index):
        """
        Inserts a value at any given index in the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value of the node to be inserted.
        index : int
            The index at which the node is to be inserted.
        """
        if index == 0:
            self.insert_begin(value)
        elif index == len(self):
            self.insert_end(value)
        else:
            current = self.head
            for i in range(index-1):
                current = current.next_node
            current.next_node = Node(value, current.next_node)
            
            
            
    def search(self, value):
        """
        Searches for the given value in the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value to be searched.
        -------
        Returns
        -------
        bool
            True if the value is present in the linked list, else False.
        """
        if self.head == None:
            return False
        else:
            current = self.head
            while current.next_node != None:
                if current.value == value:
                    return True
                current = current.next_node
            return False
    
    def index(self, value):
        """
        Returns the index of the given value in the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value whose index is to be returned.
        
        -------
        Returns
        -------
        int
            The index of the given value.
        """
        index = None
        if self.head == None:
            return index
        else:
            index = 0
            if self.head.value == value:
                return index
            else:
                current = self.head
                while current.next_node != None:
                    index += 1
                    if current.next_node.value == value:
                        return index
                    current = current.next_node
    
            
    def delete_begin(self):
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            current = self.head
            self.head = self.head.next_node
            del current
    
    def delete_end(self):
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            current = self.head
            while current.next_node.next_node != None:
                current = current.next_node
            current.next_node = None
            
    def delete_index(self, index):
        if self.__len__() == 0:
            raise IndexError("The linked list is empty.")
        else:
            if index == 0:
                self.delete_begin()
            elif index == len(self)-1:
                self.delete_end()
            else:
                current = self.head
                for i in range(index-1):
                    current = current.next_node
                current.next_node = current.next_node.next_node
    
    def delete_value(self, value):
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            if self.search(value):
                self.delete_index(self.index(value))
                
            else:
                raise ValueError("The value is not present in the linked list.")
            
    def update(self, index, value):
        if self.__len__() == 0:
            raise IndexError("The linked list is empty.")
        else:
            if index == 0:
                self.head.value = value
            else:
                current = self.head
                for i in range(index):
                    current = current.next_node
                current.value = value
        
    
    def reverse(self):
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            current = self.head
            prev = None
            while current != None:
                next_node = current.next_node
                current.next_node = prev
                prev = current
                current = next_node
            self.head = prev
    
    def concatenate(self, other):
        if self.__len__() == 0:
            self.head = other.head
        elif other.__len__() == 0:
            pass
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
                
            current.next_node = other.head
    
    def swap(self, index1, index2):
        if self.__len__() == 0:
            raise IndexError("The linked list is empty.")
        elif self.__len__() == 1:
            raise IndexError("The list has only one element.")
        else:
            if index1 == 0:
                current1 = self.head
            else:
                current1 = self.head
                for i in range(index1):
                    current1 = current1.next_node
            
            if index2 == 0:
                current2 = self.head
            else:
                current2 = self.head
                for i in range(index2):
                    current2 = current2.next_node
            
            temp = current1.value
            current1.value = current2.value
            current2.value = temp
    
            
    def sorted(self, ascending: bool = True):
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            if ascending == True:
                current = self.head
                while current.next_node != None:
                    if current.value > current.next_node.value:
                        return False
                    current = current.next_node
                return True
            else:
                current = self.head
                while current.next_node != None:
                    if current.value < current.next_node.value:
                        return False
                    current = current.next_node
                return True
    
    def sort(self, ascending=True):
        if self.__len__() == 0:
            return None
        else:
            if self.sorted(ascending=ascending):
                return
            else:
                # create a list of the linked list and sort them and convert back to linked list
                values = self.to_list()
                values.sort(reverse= not ascending)
                self.create_from_list(values)
        
    
    
    ###### Custom Methods for creation of linked lists ######
    
    
    # return a list of the values of the linked lists
    def to_list(self):
        if self.__len__() == 0:
            return []
        else:
            current = self.head
            values = []
            while current != None:
                values.append(current.value)
                current = current.next_node
            return values
    
    
    # create a linked list from a list
    def create_from_list(self, array: list):
        if len(array) == 0:
            self.head = None
        else:
            self.head = Node(array[0])
            current = self.head
            for i in range(1, len(array)):
                current.next_node = Node(array[i])
                current = current.next_node
    
    
    # create a linked list from a dictionary with the keys as the values of the nodes and the values as the next nodes
    def create_from_dict(self):
        pass            
                    