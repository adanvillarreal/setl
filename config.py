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

    def current_temp(self):
        return 't' + str(self.temp_counter)

    def current_quad_number(self):
        return len(self.list)

    def add(self, quadruple):
        #print("ASDASDASD")
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
        print("PUSHING " + str(item))
        self.stack.append(item)
        print(self.stack)

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)

class Memory:
    def __init__(self, init_value, delta):
        self.delta = delta
        self.int_addr = init_value
        self.init_address = {'BOOL': init_value, 'FLOAT': init_value+ delta, 'INT': init_value+delta*2, 'CHAR':init_value+delta*3, 'STRING':init_value+delta*4}
        self.maps = {'BOOL': {}, 'FLOAT': {}, 'INT': {}, 'CHAR': {}, 'STRING':{}}

    def next_address(self, data_type):
        print "NEXT ADDRESS LENGTH OF MAP", self.maps[data_type]
        return self.init_address[data_type]+ len(self.maps[data_type])

    def assign(self, data_type, value):
        if len(self.maps[data_type]) == self.delta:
            return None
        next_address = self.next_address(data_type)
        self.maps[data_type][value] = next_address
        return next_address

class MemoryManager:
    def __init__(self):
        self.memories = {'local':Memory(0, 1000), 'global': Memory(5000, 1000), 'temporary':Memory(10000, 1000), 'constant': Memory(15000, 1000)}

class Semantics:
    def __init__(self):
        self.global_vars = SymbolTable()
        self.local_vars = SymbolTable()
        self.global_scope = True
        self.functions = ProcTable()
        self.last_proc_name = ""
        self.current_proc = ""
        self.param_counter = 0
        self.called_function = ""
        self.proc_has_return = False
        self.has_return = False
        self.memory_manager = MemoryManager()


    def change_scope(self):
        self.global_scope = False
        self.has_return = False
        self.local_vars = SymbolTable()
        print "AAAAAAAAA"
        return self.global_scope

    def insert_var(self, name, datatype, value):
        if self.global_scope:
            table = self.global_vars
            current_address = self.memory_manager.memories['global'].assign(datatype, name)
            if current_address is None:
                print "ADDRESS NOT AVAILABLE"
                return SyntaxError
            print("^^^^^^^^^^^^^^^ASSIGNING MEMORY")
            print name, datatype, value, current_address

            return table.insert(name, datatype, value, current_address)
        else:
            proc = self.functions.find(self.current_proc)
            table = proc[2]
            current_address = self.memory_manager.memories['local'].assign(datatype, name)
            if current_address is None:
                print "ADDRESS NOT AVAILABLE"
                return SyntaxError
            print("^^^^^^^^^^^^^ASSIGNING MEMORY")
            print name, datatype, value, current_address
            if table.insert(name, datatype, value, current_address):
                proc = proc._replace(vars_table=table)
                return True
            else:
                return False

    def insert_to_constants(self, value, datatype):
        current_address = self.memory_manager.memories['constant'].assign(datatype, value)
        if current_address is None:
            raise SyntaxError


    def update_proc_var_table(self, table):
        proc = self.functions.find(self.current_proc)
        if proc != None:
            self.functions.insert(proc[0], proc[1], table)
            return True
        else:
            return False

    def add_proc_param(self, param):
        proc = self.functions.find(self.current_proc)
        proc[3].append(param)
        new_list = proc[3]
        if proc != None:
            self.functions.update(proc[0], proc._replace(params = new_list))
            return True
        else:
            return False

    def add_quad_counter(self, quad):
        proc = self.functions.find(self.current_proc)
        if proc != None:
            self.functions.update(proc[0], proc._replace(quadruple = quad))
            return True
        else:
            return False

    def new_proc(self, name, returntype):
        self.global_scope = False
        if self.functions.find(name) != None:
            return False

        self.functions.insert(name, returntype, SymbolTable(), list(), None)
        self.current_proc = name
        self.local_vars = SymbolTable()
        return True

    def verify_param(self, func_name, param_number, current_type):
        proc = self.functions.find(func_name)
        if (len(proc.params) > param_number):
            print str(proc.params) + " " + current_type
            return proc.params[param_number] == current_type
        else:
            return None

    def verify_all_params_sent(self, func_name, counter):
        proc = self.functions.find(func_name)
        return len(proc.params) == counter + 1

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

    def check_return_type(self, return_type):
        print "CHECK RETURN TYPE"
        print return_type
        og_return_type =  self.functions.find(self.current_proc).return_type
        print og_return_type
        return og_return_type == None or return_type == og_return_type

    def set_has_return(self, has_return):
        print has_return
        self.has_return = has_return

    def get_has_return(self):
        return self.has_return

    def find_proc(self, name):
        return self.functions.find(name)
