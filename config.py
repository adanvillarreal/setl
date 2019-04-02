from symbol_table import SymbolTable, ProcTable
class Quadruple:
    def __init__(self, action, first, second, result):
        self.action = action
        self.first = first
        self.second = second
        self.result = result

class Semantics:
    def __init__(self):
        self.global_vars = SymbolTable()
        self.local_vars = SymbolTable()
        self.global_scope = True
        self.functions = ProcTable()
        self.last_proc_name = ""
        self.current_proc = ""

    def change_scope(self):
        self.global_scope = False
        self.local_vars = SymbolTable()
        print "AAAAAAAAA"
        return self.global_scope

    def insert_var(self, name, datatype, value):
        if self.global_scope:
            table = self.global_vars
            return table.insert(name, datatype, value)
        else:
            proc = self.functions.find(self.current_proc)
            table = proc[2]
            if table.insert(name, datatype, value):
                proc = proc._replace(vars_table=table)
                return True
            else:
                return False

    def update_proc_var_table(self, name, table):
        proc = self.functions.find(name)
        if proc != None:
            self.functions.insert(proc[0], proc[1], table)
            return True
        else:
            return False


    def new_proc(self, name, returntype):
        self.global_scope = False
        if self.functions.find(name) != None:
            return False

        self.functions.insert(name, returntype, SymbolTable())
        self.current_proc = name
        self.local_vars = SymbolTable()
        return True

    def find_var(self, name):
        proc = self.functions.find(self.current_proc)
        table = proc[2]
        local_table_search = table.find(name)
        if local_table_search == None:
            global_table_search = self.global_vars.find(name)
            if global_table_search == None:
                return None
            else:
                return global_table_search
        else:
            return local_table_search

    def find_proc(self, name):
        return self.functions.find(name)
