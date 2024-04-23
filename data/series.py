# series.py

from index import Index

class Series:
    """ !!!!!!!!!!!!!!!!! """
    def __init__(self, values, index = None):
        if len(values) == 0:
            raise ValueError
        self._values = values
        if index is None:
            index = Index(labels = list(range(0, len(values))))
        else:
            if len(values) != len(index.labels):
                raise ValueError
        self._index = index
        
    @property
    def values(self):
        return self._values
    
    @property
    def index(self):
        return self._index
    
    
    
    def get(self, key):
        if key in self.index.labels:
            index_loc = self.index.get_loc(key)
            return self.values[index_loc]
        return None
    
    def sum(self):
        return sum(self.values)
    
    def max(self):
        return max(self.values)
    
    def min(self):
        return min(self.values)
    
    def mean(self):
        return sum(self.values / len(self.values))
    
    def apply(self, func):
        new_values = [func(value) for value in self.values]
        return Series(new_values, self.index)
    
    def abs(self):
        new_values = [abs(value) for value in self.values]
        return Series(new_values, index = self.index)