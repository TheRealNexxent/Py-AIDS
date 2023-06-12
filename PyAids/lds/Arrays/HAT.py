class HAT:
    """
    Creates a Hashed array tree of a given size
    """
    def __init__(self, size: int):
        """
        ----------
        Parameters
        ----------
        size : int
            number of keys to create
        """
        self.size = size
        self.hash = {}
        for i in range(self.size):
            self.hash[i] = [None] * self.size
            
    def __dict__(self):
        return self.hash
            
    def __str__(self):
        return str(self.__dict__())
    
    def keys(self):
        """
        Returns a list of keys
        """
        return list(self.hash.keys())
    
    def values(self):
        """
        Returns a 2D list of values
        """
        return list(self.hash.values())
    
    def size(self):
        """
        Returns the size of the
        """
        return self.size
    
    def capacity(self):
        """
        Returns the current capacity of the hashed array tree
        """
        if self.size != 0:
            cap = len(self.keys()) * len(self.hash[0])
            return cap
        else:
            return 0
    
    def is_epmty(self):
        """
        Returns true if the hashed array tree is empty or false if it is not
        """
        if self.hash == {}:
            return True
        else:
            return False
                    
    def insert(self, key, value):
        """
        Inserts a key-value pair into the hashed array tree at the next available slot
        if the key is already in the hashed array tree then the value is added to the next available slot
        otherwise a new key is inserted into the hashed array tree and the value is added
        ----------
        Parameters
        ----------
        key : any
            key to insert into the hashed array tree at
        value : any 
            value to insert into the hashed array tree for the given key
        """
        if key in self.keys():   # if the key already exists then add the value to the next available slot
            for i in range(self.size):
                if self.hash[key][i] == None:
                    self.hash[key][i] = value
                    return
            raise IndexError("No more space in the list for this key.")
        else:   # if the key does not exist then add the initial None key value pair for the key and recursively call insert
            self.hash[key] = [None] * self.size
            self.insert(key, value)
        
        
    
    def resize_all(self, newsize: int):
        """
        Resizes the keys and values for the hashed array tree to the given size
        eg:- adds new keys and values to the hashed array tree for the new given size
        ----------
        Parameters
        ----------
        newsize : int
            size to resize the keys and values
        """
        if newsize < self.size:
            raise ValueError("New size must be greater than current size.")

        for i in range(self.size):
            if self.hash[i]:
                for j in range(newsize - self.size):
                    self.hash[i].append(None)
                    
        for i in range(self.size, newsize):
            self.hash[i] = [None] * newsize
                
        self.size = newsize
        
        
    def resize_values(self, newsize: int):
        """
        resizes only the value arrays for each key in the hashed array tree to the given size
        ----------
        Parameters
        ----------
        newsize : int
            size to resize the values for each key
        """
        if newsize < self.size:
            raise ValueError("New size must be greater than current size.")
        
        for i in self.keys():
            for j in range(newsize - self.size):
                self.hash[i].append(None)
        
        
        
    def lookup(self, key: any):
        """
        Returns the values for the given key in the hashed array tree
        ----------
        Parameters
        ----------
        key : any
            key to lookup in the hashed array tree
        """
        if key in self.keys():
            return self.hash[key]
        else:
            raise KeyError("Key not found")
    
    
    # deletes the key and all its values
    def delete_key(self, key: any):
        """
        deletes the key and all its values
        ----------
        Parameters
        ----------
        key: any
            key to delete from the hashed array tree
        """
        if key in self.keys():
            del self.hash[key]
            
        else:
            raise KeyError("Key not found")
    
    # deletes the first occurence of the value for the given key append a None value to the end of the list
    def delete_value(self, key: any, value: any):
        """
        deletes the first instance of the value in hash of the given key and appends a None value at the end of the hash
        ----------
        Parameters
        ----------
        key: any
            key to delete the value from
        value: any
            value to delete from the given key
        """
        if key in self.keys() and value in self.hash[key]:
            del self.hash[key][self.hash[key].index(value)]
            self.hash[key].append(None)

        elif key not in self.keys():
            raise KeyError("Key not found")
        
        elif value not in self.hash[key]:
            raise ValueError("Value not found for the given key")
    
        
        
    def range_lookup(self, startKey: any, endKey: any):
        """
        returns the values for all the keys between startKey and endKey
        ----------
        Parameters
        ----------
        startKey: any
            key to start the range lookup from
        endKey: any
            key to end the range lookup at
        """
        if startKey in self.keys() and endKey in self.keys():
            if self.keys().index(startKey) < self.keys().index(endKey):
                lookupKeys = self.keys[self.keys().index(startKey): self.keys().index(endKey)]
                lookupValues = []
                for i in lookupKeys:
                    lookupValues.append(self.hash[i])
                return lookupValues
            else:
                raise KeyError("Start key must come before end key")
        else:
            raise KeyError("Key not found")