from symbol_table import SymbolTable, ProcTable
class Quadruple:
    def __init__(self, action, first, second, result):
        self.action = action
        self.first = first
        self.second = second
        self.result = result

    def print_quad(self):
        print(str(self.action) + "~" + str(self.first) + "~" + str(self.second) + "~" + str(self.result))

class QuadrupleList:
    def __init__(self):
        self.list = []
        self.temp_counter = 0

    def next_temp(self):
        self.temp_counter = self.temp_counter + 1
        return 't' + str(self.temp_counter)

    def add(self, quadruple):
        print("ASDASDASD")
        quadruple.print_quad()
        self.list.append(quadruple)

    def print_quads(self):
        for x in self.list:
            x.print_quad()

# A simple class stack that only allows pop and push operations
class Stack:

    def __init__(self):
        self.stack = []

    def top(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]


    def pop(self):
        if len(self.stack) < 1:
            print("EMPTY STACK")
            return None
        print("POPING " + str(self.stack[-1]))
        return self.stack.pop()

    def push(self, item):
        print("PUSHinG " + str(item))
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)


# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

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
