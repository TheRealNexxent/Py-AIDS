class GBuffer:
    
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        
        
    def __str__(self):
        return str(self.buffer)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        return self.buffer[index]
    
    def __setitem__(self, index, value):
        if isinstance(value, str):
            if index > 0:
                if self.buffer[index: index + len(value)] == [None]*len(value) and self._getGapSize() >= len(value):
                    self._setValue(index, value)
                    return
                else:
                    self._growGap(index)
                    self.__setitem__(index, value)
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("Value must be a string")
    
    
    
    def _getGapSize(self):
        return self.buffer.count(None)
    
    
    def _growGap(self, index):
        self.buffer = self.buffer[:index] + [None]*self.size + self.buffer[index:]
        
    def shrinkGap(self, shrinkSize):
        if self._getGapSize() < shrinkSize:
            raise ValueError("Shrink size is too large")
        else:
            for i in range(shrinkSize):
                self.buffer.remove(None)
        
        
    def _setValue(self, index, value):
        if index >= len(self.buffer) or index < 0:
            raise IndexError("Index out of range")
        for i in range(len(value)):
            self.buffer[index + i] = value[i]
    
        
    
        
        
        