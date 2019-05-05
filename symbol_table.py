from collections import namedtuple

class SymbolTable:
    def __init__(self):
        self.table = {}
        self.table_entry = namedtuple('table_entry', ['name', 'data_type', 'value', 'address'])

    def exists(self, name):
        return name in self.table

    def insert(self, name, data_type, value, address):
        if self.exists(name):
            return False
        else:
            print "Symbol Table: Insert ", data_type , " in symbol table in address ", address
            self.table[name] = self.table_entry(name, data_type, value, address)
            return True

    def find(self, name):
        if self.exists(name):
            return self.table[name]
        else:
            return None
    def update(self, name, entry):
        print "UP SYMBOL TABLE", name, entry
        self.table[name] = entry
        print self.table[name]

    def print_table(self):
        print(self.table)

class ProcTable:
    def __init__(self):
        self.table = {}
        self.table_entry = namedtuple('table_entry', ['name', 'return_type', 'vars_table', 'params', 'quadruple', 'memory_size'])

    def exists(self, name):
        return name in self.table

    def update(self, name, entry):
        self.table[name] = entry
    #    print "UPDATETETETETETETETETE"
        print self.table[name]

    def insert(self, name, returntype, varstable, params, quad, memory_size):
        if self.exists(name):
            return False
        else:
            self.table[name] = self.table_entry(name, returntype, varstable, params, quad, memory_size)
            return True

    def find(self, name):
        if self.exists(name):
            return self.table[name]
        else:
            return None
