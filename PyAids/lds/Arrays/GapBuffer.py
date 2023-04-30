class GBuffer:
    """
    Creates a gap buffer of a given size.
    """
    
    def __init__(self, size: int):
        """
        Parameters
        ----------
        size: int
            size of gap buffer
        """
        self.size = size
        self.buffer = [None] * size
        self.bufferStr = ""
        
    def toString(self):
        """
        returns the gap buffer as a string
        """
        for i in self.buffer:
            if i != None:
                self.bufferStr += i
                
        return self.bufferStr
        
    def __str__(self):
        return str(self.buffer)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        return self.buffer[index]
    
    
    def insert(self, value: any, index: int = None):
        """
        Inserts a value at the given index,
        If index is not given, the value is inserted at the start of the gap,
        If index is given in between a gap, the gap is shifted to the right to make room for the value,
        ----------
        Parameters
        ----------
        value: any
            value to insert
        index: int
            index to insert value at
            
        """
        if index == None:
            index = self.getGapIndex()
            
        if(index >= self.size or index < 0 ):
            raise IndexError("Index out of range")
        
        elif(self.getGapSize() == 0):
            self.growGap(index)
            self.insert(value, index)
        
        elif(self.buffer[index] != None):
            self.reduceGap(self.getGapSize())
            self.growGap(index)
            self.insert(value, index)
            
        elif(len(value) > self.getGapSize()):
            self.growGap(index)
            self.insert(value, index)
            
        elif(self.buffer[:index].count(None) > 0 and self.buffer[index:].count(None) > 0 and index != 0):
            index = self.getGapIndex()
            self.insert(value, index)
        else:
            for i in range(len(value)):
                self.buffer[index] = value[i]
                index += 1
    
    
    def reduceGap(self, size: int):
        """
        Reduces the gap by the given size
        ----------
        Parameters
        ----------
        size: int
            size to reduce gap by
        """
        self.buffer = self.buffer[:self.getGapIndex()] + self.buffer[self.getGapIndex()+size:]
    
    def reposeGap(self, index: int):
        """
        Reposition the gap to the given index
        ----------
        Parameters
        ----------
        index: int
            index to reposition gap to
        """
        if(index >= self.size or index < 0 ):
            raise IndexError("Index out of range")
        else:
            gapSize = self.getGapSize()
            self.reduceGap(gapSize)
            self.growGap(index, gapSize)
            
    
    def getGapSize(self):
        """
        Returns the size of the gap
        """
        return self.buffer.count(None)
        
    def getGapIndex(self):
        """
        Returns the index where gap starts
        """
        return self.buffer.index(None)
    
    
    def growGap(self, index: int, size: int = None):
        """
        Grows the gap by the given size at the given index, if the size is not given, the gap is grown by initial size defined in the constructor
        ----------
        Parameters
        ----------
        index: int
            index to grow gap at
        size: int
            size to grow gap by (defaults at contructor size)
        """
        if(size == None):
            size = self.size
        self.buffer = self.buffer[:index] + [None]*size + self.buffer[index:]
        
        
    def move_gap(self, distance: int):
        """
        moves the gap by the given distance
        ----------
        Parameters
        ----------
        distance: int
            distance to move gap by
        """
        if isinstance(distance, int):
            if distance > 0 and distance < len(self.buffer[self.getGapIndex() + self.getGapSize() + 1:]):
                self.reposeGap(self.getGapIndex() + distance)
            elif distance < 0 and distance < len(self.buffer[:self.getGapIndex()]):
                distance = abs(distance)
                self.reposeGap(self.getGapIndex() - distance)
            else:
                raise ValueError("Distance out of range")
        
    def get_text(self):
        """
        returns the text in the gap buffer with the gap replaced by spaces
        """
        res = ""
        for i in range(len(self.buffer)):
            if self.buffer[i] == None:
                res += " "
            else:
                res += self.buffer[i]
        
        return res
    