from symbol_table import SymbolTable, ProcTable

# Quadruple class with 4 slots
class Quadruple:
    # Quadruple constructor
    def __init__(self, action, first, second, result):
        self.action = action
        self.first = first
        self.second = second
        self.result = result

    # Quadruple print for debugging
    def print_quad(self):
        print(str(self.action) + "~" + str(self.first) + "~" + str(self.second) + "~" + str(self.result))

# List of Quadruples class
class QuadrupleList:
    # List constructor
    def __init__(self):
        self.list = []
        self.temp_counter = 0

    # Returns next available temporary variable
    def next_temp(self):
        self.temp_counter = self.temp_counter + 1
        return 't' + str(self.temp_counter)

    # Returns newest temporary variable
    def current_temp(self):
        return 't' + str(self.temp_counter)

    # Returns id of next quad, same as length of List
    def current_quad_number(self):
        return len(self.list)

    # Adds a quadruple to Quadruple List
    def add(self, quadruple):
        #print("ASDASDASD")
        quadruple.print_quad()
        self.list.append(quadruple)

    # Prints all quadruples in list, calls print functin in Quadruple object
    def print_quads(self):
        idx = 0
        for x in self.list:
            print idx, x.print_quad()
            idx = idx + 1

    # Gets the quadruple at index
    def get(self, index):
        return self.list[index]


# A simple class stack that only allows pop and push operations
class Stack:
    def __init__(self):
        self.stack = []

    def top(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def pop(self):
        print "POP", self.stack
        if len(self.stack) < 1:
            print("EMPTY STACK")
            return None
        #print("POPING " + str(self.stack[-1]))
        return self.stack.pop()

    def push(self, item):
        print "PUSHING", self.stack
    #    print("PUSHING " + str(item))
        self.stack.append(item)
        print(self.stack)

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)

# Memory class that holds:
# - a map for each datatype, each with its initial address.
# - the size occupied in memory by each datatype
# - A map of variables for each datatype containing
class Memory:
    #Memory constructor, a delta value that indicates datatype ranges in memory
    def __init__(self, init_value, delta):
        self.delta = delta
        self.int_addr = init_value
        self.init_address = {'BOOL': init_value, 'FLOAT': init_value+delta, 'INT': init_value+delta*2, 'CHAR':init_value+delta*3, 'STRING':init_value+delta*4}
        self.size_occupied = {'BOOL': 0, 'FLOAT': 0, 'INT': 0, 'CHAR': 0, 'STRING': 0}
        self.maps = {'BOOL': {}, 'FLOAT': {}, 'INT': {}, 'CHAR': {}, 'STRING':{}}

    # Returns the next available address in memory for a given data type
    def next_address(self, data_type):
        print "NEXT ADDRESS LENGTH OF MAP",  data_type, self.maps[data_type]
        #return self.init_address[data_type] + len(self.maps[data_type])
        return self.init_address[data_type] + self.size_occupied[data_type]

    # Assigns memory to variable 'value' if enough space is available.
    # Updates size occupied by given data type
    def assign(self, data_type, value, size_needed):
        if value in self.maps[data_type]:
            return self.maps[data_type][value]
        if len(self.maps[data_type]) + size_needed > self.delta:
            return None
        next_address = self.next_address(data_type)
        self.size_occupied[data_type] += size_needed

        print "Size occupied ", self.size_occupied[data_type]
        self.maps[data_type][value] = next_address
        return next_address

    # Returns the map containing sizes occupied in memory for each data type
    def memory_length(self):
        return self.size_occupied

# Memory Manager class
class MemoryManager:
    # Memory Manager constructs a map of memories(init_value, delta)
    # for local, global, temporary and constant variables
    def __init__(self):
        self.memories = {'local':Memory(0, 1000), 'global': Memory(5000, 1000), 'temporary':Memory(10000, 1000), 'constant': Memory(15000, 1000)}

    # Local and temporary memories are reset
    def reset_memory(self):
        self.memories['local'] = Memory(0, 1000)
        self.memories['temporary'] = Memory(10000, 1000)

    # Calls memory_length from Memory class with a given memory_type {local, global, constant, temporary}
    def get_memory_size(self, memory_type):
        return self.memories[memory_type].memory_length()

    # Returns the address
    def find_constant(self, value, datatype):
        return self.memories['constant'].maps[datatype][value]

    #
    def find_global(self, value, datatype):
        return self.memories['global'].maps[datatype][value]

# Semantics class
class Semantics:
    # Semantic constructor:
    # builds symbol tables for global and local vars
    # build procedure table for functions
    # Sets vars global_scope, last_proc_name, current_proc, param_counter,
    # called_function, proc_has_return, has_return to default values
    # Declares a memory manager
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

    # Inserts a variable with a given name and datatype and value in memory
    def insert_var(self, name, datatype, value):

        size_needed = 1
        original_datatype = datatype

        # Sets need at least 10 cells of memory
        if datatype.startswith('SET'):
            is_set = True
            datatype = datatype[4: -1]
            size_needed = 10
            print "Incoming Set of datatype",
            value = True

        # Maps need at least 10 cells of memory
        if datatype.startswith('MAP'):
            og_datatype = datatype
            datatype = datatype[4: -1] # map <int,int> M;
            datatype = datatype.split(",")
            size_needed = 10
            print "Incoming Map"
            print datatype[0]
            print datatype[1]
            return self.insert_map_handler(name, og_datatype, datatype[0], datatype[1], True)

        # Insert var in global memory
        if self.global_scope:
            table = self.global_vars
            current_address = self.memory_manager.memories['global'].assign(datatype, name, size_needed)
            if current_address is None:
                print "ADDRESS NOT AVAILABLE"
                raise SyntaxError
            print("^^^^^^^^^^^^^^^GLOBAL MEMORY")
            print "Semantics: ", name, datatype, value, current_address

            return table.insert(name, original_datatype, value, current_address)
        else: # Insert var in local memory
            proc = self.functions.find(self.current_proc)
            table = proc[2]
            current_address = self.memory_manager.memories['local'].assign(datatype, name, size_needed)
            if current_address is None:
                print "ADDRESS NOT AVAILABLE"
                raise SyntaxError
            print("^^^^^^^^^^^^^ASSIGNING MEMORY")
            print name, datatype, value, current_address
            if table.insert(name, original_datatype, value, current_address):
                proc = proc._replace(vars_table=table)
                return True
            else:
                return False

    # Inserts map with a given name, and key and value datatypes in memory
    def insert_map_handler(self, name, og_datatype, datatype_key, datatype_value, value):
        value = True
        size_needed = 10
        if self.global_scope:
            table = self.global_vars
            current_address_key = self.memory_manager.memories['global'].assign(datatype_key, name + '.k', size_needed)
            current_address_val = self.memory_manager.memories['global'].assign(datatype_value, name + '.v', size_needed)

            current_address = [current_address_key, current_address_val]

            if None in current_address:
                print "ADDRESS NOT AVAILABLE"
                raise SyntaxError
            print("^^^^^^^^^^^^^^^GLOBAL MEMORY")
            print "Semantics: ", name, datatype_key, datatype_value, value, current_address
            print og_datatype

            return table.insert(name, og_datatype, value, current_address)
        else:
            proc = self.functions.find(self.current_proc)
            table = proc[2]
            current_address = [self.memory_manager.memories['global'].assign(datatype_key, name + '.k', size_needed),
                               self.memory_manager.memories['global'].assign(datatype_value, name + '.v', size_needed)]
            if None in current_address:
                print "ADDRESS NOT AVAILABLE"
                raise SyntaxError
            print("^^^^^^^^^^^^^ASSIGNING MEMORY")
            print "Semantics: ", name, datatype_key, datatype_value, value, current_address
            if table.insert(name, og_datatype, value, current_address):
                proc = proc._replace(vars_table=table)
                return True
            else:
                return False

    # Inserts a value of a datatype in the constant memory
    def insert_to_constants(self, value, datatype):
        current_address = self.memory_manager.memories['constant'].assign(datatype, value, 1)
        if current_address is None:
            raise SyntaxError

    # Inserts procedure table to
    def update_proc_var_table(self, table):
        proc = self.functions.find(self.current_proc)
        if proc != None:
            self.functions.insert(proc[0], proc[1], table)
            return True
        else:
            return False

    # Appends a parameter to the list of parameters of the current procedure
    def add_proc_param(self, param):
        proc = self.functions.find(self.current_proc)
        proc[3].append(param)
        new_list = proc[3]
        if proc != None:
            self.functions.update(proc[0], proc._replace(params = new_list))
            return True
        else:
            return False

    # Adds current quad counter to current procedure
    def add_quad_counter(self, quad):
        proc = self.functions.find(self.current_proc)
        if proc != None:
            self.functions.update(proc[0], proc._replace(quadruple = quad))
            return True
        else:
            return False

    # Updates the size occupied for each datatype in local and temporary memories
    def save_used_memory(self):
        old_proc = self.functions.find(self.current_proc)
        memory_size_map = {'local':self.memory_manager.get_memory_size('local'), 'temporary': self.memory_manager.get_memory_size('temporary')}
        print "SAVE USED MEMORY", memory_size_map
        self.functions.update(old_proc[0], old_proc._replace(memory_size = memory_size_map))
        print self.functions.find(old_proc[0])

    # Sets variable as an assigned one
    def set_variable_assigned(self, var_name):
        proc = self.functions.find(self.current_proc)
        table = proc[2] # current_proc vars table
        print "TABLE", table.find(var_name)
        local_table_search = table.find(var_name)
        if local_table_search == None:
            global_table_search = self.global_vars.find(var_name)
            if global_table_search == None:
                return None
            else:
                return global_table_search
        else: #local table
            new_record = local_table_search._replace(value = True)
            table.update(var_name, new_record)
            print "NEW TABLE", table
            self.functions.update(proc[0], proc._replace(vars_table = table))
            print self.functions.find(proc[0])

    # Inserts new procedure in local or global symbol table
    def new_proc(self, name, returntype):
        if not returntype is None:
            self.global_scope = True
            self.insert_var(name, returntype, True)

        self.global_scope = False

        self.memory_manager.reset_memory()
        if self.functions.find(name) != None:
            return False

        self.functions.insert(name, returntype, SymbolTable(), list(), None, 0)
        self.current_proc = name
        self.local_vars = SymbolTable()
        return True

    # Verifies that param_number doesnt exceed the number of parameters
    # in func_name and that its type matches a given current_type
    def verify_param(self, func_name, param_number, current_type):
        proc = self.functions.find(func_name)
        if (len(proc.params) > param_number):
            print str(proc.params) + " " + current_type
            return proc.params[param_number] == current_type
        else:
            return None

    # Verifies that the number of parameters given in a function macthes
    # its signature
    def verify_all_params_sent(self, func_name, counter):
        proc = self.functions.find(func_name)
        return len(proc.params) == counter + 1

    # Finds a variable. Looks in local table and then in global table
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

    # Validates that return type given matches the return type
    # of current procedure
    def check_return_type(self, return_type):
        print "CHECK RETURN TYPE"
        print return_type
        og_return_type =  self.functions.find(self.current_proc).return_type
        print og_return_type
        return og_return_type == None or return_type == og_return_type

    # has_return setter
    def set_has_return(self, has_return):
        print has_return
        self.has_return = has_return

    # has_return getter
    def get_has_return(self):
        return self.has_return

    # Returns procedure table given function name
    def find_proc(self, name):
        return self.functions.find(name)
