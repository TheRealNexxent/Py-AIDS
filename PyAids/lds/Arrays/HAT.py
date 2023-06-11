class HAT:
    
    def __init__(self, n):
        self.n = n
        self.hash = {}
        for i in range(self.n):
            self.hash[i] = [None] * self.n
            
    def __dict__(self):
        return self.hash
            
    def __str__(self):
        return str(self.__dict__())
    
    def keys(self):
        return list(self.hash.keys())
    
    def values(self):
        return list(self.hash.values())
    
    
    def insert(self, key, value):
        if key in self.keys():   # if the key already exists then add the value to the next available slot
            for i in range(self.n):
                if self.hash[key][i] == None:
                    self.hash[key][i] = value
                    return
            raise IndexError("No more space in the list for this key.")
        else:   # if the key does not exist then add the initial None key value pair for the key and recursively call insert
            self.hash[key] = [None] * self.n
            self.insert(key, value)
        
        
    
    def resize(self, newsize: int):
        if newsize < self.n:
            print("New size must be greater than current size.")
            return
        
        for i in range(self.n):
            if self.hash[i]:
                for j in range(newsize - self.n):
                    self.hash[i].append(None)
                    
        for i in range(self.n, newsize):
            self.hash[i] = [None] * newsize
                
        self.n = newsize