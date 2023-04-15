class CircularBuffer:
    """
    Create a Circular Buffer of size 'size'
    """
    def __init__(self,size):
        """
        ----------
        Parameters
        ----------
        size: int
            size of buffer
        """
        self.size = size
        self.buffer = [None] * self.size
        self.tail = 0
        self.head = 0
        
    def __getitem__(self, index):
        if index > self.lastBufferIndex:
            index = index - self.lastBufferIndex - 1
            self.__getitem__(index)
        else:
            return self.buffer[index]
        
        
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return str(self.buffer)
    
    def append(self, obj):
        """
        Append an object to the buffer and increment the tail
        ----------
        Parameters
        ----------
        obj: any
            object to be appended to the buffer
        """
        self.buffer[self.tail] = obj
        self.tail = (self.tail + 1) % self.size
        if self.tail == self.head:
            self.head = (self.head + 1) % self.size
            
            
    def read(self):
        """
        Retruns the object at the head of the buffer and increments the head
        """
        read = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        return read
    
    def getHead(self):
        """
        Returns the current head of the buffer
        """
        return self.head
        
        
    def getTail(self):
        """
        Returns the current tail of the buffer
        """
        return self.tail
            
    def getBuffer(self):
        """
        Returns the buffer
        """
        return self.buffer
    
    
    
        
        
    
    
    
            
        