from symbol_table import SymbolTable

class Semantics:
    def __init__(self):
        self.global_vars = SymbolTable()
        self.local_vars = SymbolTable()
        self.global_scope = True

    def change_scope(self):
        self.global_scope = False
        self.local_vars = SymbolTable()
        print "AAAAAAAAA"
        return self.global_scope

    def insert_var(self, name, datatype, value):
        if self.global_scope:
            table = self.global_vars
        else:
            table = self.local_vars
        return table.insert(name, datatype, value)

    def find_var(self, name):
        local_table_search = self.local_vars.find(name)
        if local_table_search == None:
            global_table_search = self.global_vars.find(name)
            if global_table_search == None:
                return None
            else:
                return global_table_search
        else:
            return local_table_search
