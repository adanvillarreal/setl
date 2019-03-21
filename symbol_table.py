from collections import namedtuple

class SymbolTable:
    def __init__(self):
        self.table = {}
        self.table_entry = namedtuple('table_entry', ['name', 'data_type', 'value'])

    def exists(self, name):
        return name in self.table

    def insert(self, name, data_type, value):
        if self.exists(name):
            return False
        else:
            self.table[name] = self.table_entry(name, data_type, value)
            return True

    def find(self, name):
        if self.exists(name):
            return self.table[name]
        else:
            return None
