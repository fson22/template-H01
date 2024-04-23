# dataframe.py

from index import Index
from series import Series

class DataFrame:
    def __init__(self, values, columns = None):
        if len(values) == 0:
            raise ValueError
        self._values = values
        if columns is None:
            columns = Index(labels = list(range(0, len(values))))
        else:
            if len(values) != len(columns.labels):
                raise ValueError
        self._columns = columns
        
    @property
    def columns(self):
        return self._columns
    
    def get(self, key):
        if key in self.columns.labels:
            columns_loc = self.columns.get_loc(key)
            return self.values[columns_loc]
        return None