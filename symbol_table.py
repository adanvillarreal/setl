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

class ProcTable:
    def __init__(self):
        self.table = {}
        self.table_entry = namedtuple('table_entry', ['name', 'return_type', 'vars_table', 'params', 'quadruple'])

    def exists(self, name):
        return name in self.table

    def update(self, name, entry):
        self.table[name] = entry
        print "UPDATETETETETETETETETE"
        print self.table[name]

    def insert(self, name, returntype, varstable, params, quad):
        if self.exists(name):
            return False
        else:
            self.table[name] = self.table_entry(name, returntype, varstable, params, quad)
            print("TABLE INSERT)))()()()()()()")
            print(self.table[name])
            return True

    def find(self, name):
        if self.exists(name):
            return self.table[name]
        else:
            return None
