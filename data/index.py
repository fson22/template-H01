# index.py

class Index:
    """ Class for indexing sequences """
    
    def __init__(self, labels, name = ""):
        """
        Args:
            labels (list) - list of keys
            name (str) - name of the index, defaults to ""
        """
        
        """
        Raises:
            ValueError: If labels contain duplicates or have zero length
        """
        if len(labels) == 0:
            raise ValueError("Index lable must have at least one element.")
        if len(labels) != len(set(labels)):
            raise ValueError("Index labels cannot contain duplicates.")
        self._labels = labels
        self._name = name
        
    @property
    def labels(self):
        return self._labels
    
    @property
    def name(self):
        return self._name
    
    
    def get_loc(self, key):
        """
        
        Get the index of a key in labels.
        
        Args:
            key (str) - The key to locate in the index.
            
        Returns:
            Index location of the key.
            
        Raises:
            KeyError: If the key is not in labels. 
        
        """
        try:
            return self._labels.index(key)
        except ValueError:
            raise KeyError(f"Key '{key} is not in labels'")