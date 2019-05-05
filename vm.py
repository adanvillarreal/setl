from config import *
from symbol_table import *
import copy
class VMMemory:
    def __init__(self, virtual_memory_ranges, delta, global_sizes, local_sizes, temp_sizes, constants):
        for k, v in global_sizes.items():
            global_sizes[k] = [None]*v

        for k, v in local_sizes.items():
            local_sizes[k] = [None]*v

        for k, v in temp_sizes.items():
            temp_sizes[k] = [None]*v

        initial_stack_1 = Stack()
        initial_stack_2 = Stack()
        initial_stack_1.push(local_sizes)
        initial_stack_2.push(temp_sizes)

        self.memories = {'local': initial_stack_1, 'global': global_sizes, 'temporary': initial_stack_2, 'constant': {'BOOL': [], 'FLOAT': [], 'INT': [], 'CHAR': [], 'STRING':[]}}
        self.virtual_memory_ranges = virtual_memory_ranges
        self.delta = delta
        for key, value in constants.items():
            inv_map = {v: k for k, v in value.items()}
            for k, v in inv_map.items():
                self.append(k, v)
        print self.memories
    def push_new_level(self, memory_size):
        local_sizes = memory_size['local'].copy()
        for k, v in local_sizes.items():
            local_sizes[k] = [0]*v

        temp_sizes = memory_size['temporary'].copy()
        for k, v in temp_sizes.items():
            temp_sizes[k] = [0]*v

        self.memories['local'].push(local_sizes)
        self.memories['temporary'].push(temp_sizes)

    def pop_level(self):
        self.memories['local'].pop()
        self.memories['temporary'].pop()

    def translate(self, address):
        idx = 0
        config_memories = ['local', 'global', 'temporary', 'constant']
        config = ['BOOL', 'FLOAT', 'INT', 'CHAR', 'STRING']
        vm_ranges = [0, 5000, 10000, 15000, 20000, 25000]
        for lim in vm_ranges:
            if address < lim:
                address = address - vm_ranges[idx-1]
                return [config_memories[idx-1], config[address/self.delta], address % self.delta]
            idx = idx + 1
        return None

    def assign_parameters(self, params):
        offset = {'BOOL':0, 'FLOAT': 0, 'INT': 0, 'CHAR': 0, 'STRING': 0}
        for param in params:
            translation = self.translate(param[1])
            print "ASSIGNING PARAM", param, translation
            self.memories['local'].top()[translation[1]][offset[translation[1]]] = param[0]
            offset[translation[1]] = offset[translation[1]] + 1

    def append(self, address, value):
        translation = self.translate(address)
        print 'assigning ', translation, address, value
        if translation is None:
            print "MEMORY ERROR, COULDNT FIND TRANSLATE MEMORY ADDRESS"
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]].append(value)
        else:
            self.memories[translation[0]][translation[1]].append(value)

    def assign(self, address, value):
        translation = self.translate(address)
        print 'assigning ', translation, address, value
        if translation is None:
            print "MEMORY ERROR, COULDNT FIND TRANSLATE MEMORY ADDRESS"
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]][translation[2]] = value
        else:
            self.memories[translation[0]][translation[1]][translation[2]] = value

    def assign_explicit(self, translation, value):
        if translation is None:
            print "MEMORY ERROR, COULDNT FIND TRANSLATE MEMORY ADDRESS"
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]][translation[2]] = value
        else:
            self.memories[translation[0]][translation[1]][translation[2]] = value

    def add_memory_chunk(self, translation):
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]] = self.memories[translation[0]].top()[translation[1]] + [None] * 10
        else:
            self.memories[translation[0]][translation[1]] = self.memories[translation[0]][translation[1]] + [None] * 10
    def first_available_addr(self, address):
        mem_base_addr = {'local':0, 'global':5000, 'temporary': 10000, 'constant': 15000}
        data_type_base_addr = {'BOOL': 0, 'FLOAT': 1000, 'INT': 2000, 'CHAR': 3000, 'STRING': 4000}
        chunk_size = 10
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        first_addr = idx
        while(idx + counter < 1000):
            print idx, counter
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    memory[idx + counter] = len(memory)
                    idx = len(memory)
                    counter = 0
                    self.add_memory_chunk(translation)
                    if (translation[0] == 'local' or translation[0] == 'temporary'):
                        memory = self.memories[translation[0]].top()[translation[1]]
                    else:
                        memory = self.memories[translation[0]][translation[1]]
                else:
                    idx = memory[idx + counter]
                    counter = 0
            else:
                if memory[idx + counter] is None:
                    first_addr = idx + counter
                    print "FIND MEM IN", [translation[0], translation[1], first_addr]
                    return[translation[0], translation[1], first_addr]
                counter = counter + 1

        return None

    def size_in_addr(self, address):
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        abs_counter = 0
        while(idx + counter < len(memory)):
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    return abs_counter
                else:
                    idx = memory[idx + counter]
                    counter = 0
            if not memory[idx + counter] is None:
                abs_counter = abs_counter + 1
            counter = counter + 1
        return abs_counter

    def find_value_in_addr(self, value, address):
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        while(idx + counter < len(memory)):
            print idx, counter
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    return None
                else:
                    idx = memory[idx + counter]
                    counter = 0
            elif (memory[idx+counter] == value):
                return [translation[0], translation[1], idx+counter]
            counter = counter + 1
        return None

    def remove_list(self, address):
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        while(idx + counter < len(memory)):
            print idx, counter
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    return
                else:
                    old_idx = idx
                    idx = memory[idx + counter]
                    memory[old_idx + counter] = None
                    counter = 0
            else:
                memory[idx + counter] = None
                counter = counter + 1
        return

    def to_vector(self, address):
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        new_vector = []
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        while(idx + counter < len(memory)):
            print idx, counter
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    return new_vector
                else:
                    old_idx = idx
                    idx = memory[idx + counter]
                    memory[old_idx + counter] = None
                    counter = 0
            else:
                if not memory[idx+counter] is None:
                    new_vector.append(memory[idx+counter])
                counter = counter + 1
        return new_vector

    def assign_list_to_addr(self, l_set, address):
        mem_base_addr = {'local':0, 'global':5000, 'temporary': 10000, 'constant': 15000}
        data_type_base_addr = {'BOOL': 0, 'FLOAT': 1000, 'INT': 2000, 'CHAR': 3000, 'STRING': 4000}
        chunk_size = 10
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        first_addr = idx
        set_idx = 0
        while(idx + counter < 1000 and set_idx < len(l_set)):
            print idx, counter, memory
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    memory[idx + counter] = len(memory)
                    idx = len(memory)
                    counter = 0
                    self.add_memory_chunk(translation)
                    if (translation[0] == 'local' or translation[0] == 'temporary'):
                        memory = self.memories[translation[0]].top()[translation[1]]
                    else:
                        memory = self.memories[translation[0]][translation[1]]
                else:
                    print "AQUI"
                    idx = memory[idx + counter]
                    counter = 0
            else:
                if memory[idx + counter] is None:
                    first_addr = idx + counter
                    print"ASDASDASDASDASDASDADSDASDASDASD", set_idx, len(l_set)
                    self.assign_explicit([translation[0], translation[1], first_addr], l_set[set_idx])
                    set_idx = set_idx + 1
                counter = counter + 1

        if idx + counter >= 1000:
            return None
        else:
            return True

    def retrieve(self, address):
        translation = self.translate(address)
        #print 'retrieving', translation, address
        if translation is None:
            print "MEMORY ERROR, COULDNT FIND TRANSLATE MEMORY ADDRESS"
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            if translation[1] == 'INT':
                #print self.memories
                return int(self.memories[translation[0]].top()[translation[1]][translation[2]])
            elif translation[1] =='FLOAT':
                return float(self.memories[translation[0]].top()[translation[1]][translation[2]])
            else:
                return self.memories[translation[0]].top()[translation[1]][translation[2]]
        else:
            if translation[1] == 'INT':
                return int(self.memories[translation[0]][translation[1]][translation[2]])
            elif translation[1] =='FLOAT':
                return float(self.memories[translation[0]][translation[1]][translation[2]])
            else:
                return self.memories[translation[0]][translation[1]][translation[2]]

class VM:
    def __init__(self, functions, constants, global_vars_mem, quadruples, vm_ranges, delta, global_vars):
        self.functions_table = functions
        main_memory_info = functions.find('MAIN').memory_size
        self.quadruples = quadruples
        print main_memory_info
        self.memory = VMMemory(vm_ranges, delta, global_vars_mem, main_memory_info['local'], main_memory_info['temporary'], constants)
        self.params_stack = Stack()
        self.pointer_stack = Stack()
        self.params_list = []
        self.return_addr_stack = Stack()
        self.global_vars = global_vars

    def process_quad(self, pointer):
        while(True):
            action = self.quadruples.get(pointer).action
            left = self.quadruples.get(pointer).first
            right = self.quadruples.get(pointer).second
            quad_result = self.quadruples.get(pointer).result
            print self.memory.memories['global']
            print "TEEEEEMP"
            print self.memory.memories['temporary'].top()
            print "QUUUUUUUUAD", action, left, right
            if action == '+':
                result = self.memory.retrieve(left) + self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == '-':
                result = self.memory.retrieve(left) - self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == '*':
                #print  'MULTIPLICATION'
                #print self.memory.retrieve(left), self.memory.retrieve(right)
                #print "RES",quad_result
                result = self.memory.retrieve(left) * self.memory.retrieve(right)
                #print "RESULT ", result
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == '/':
                result = self.memory.retrieve(left) / self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == '=':
            #    print 'ASSIGNATION', quad_result, left
                if(right == "SET"):
                    self.memory.remove_list(quad_result)
                    new_vector = self.memory.to_vector(left)
                    self.memory.assign_list_to_addr(new_vector, quad_result)
                else:
                    self.memory.assign(quad_result, self.memory.retrieve(left))
                pointer = pointer + 1
            elif action == 'GOTO':
                pointer = quad_result
            elif action == 'GOTOF':
                if self.memory.retrieve(left) == 'false':
                    pointer = quad_result
                else:
                    pointer = pointer + 1
            elif action == 'GOSUB':
                new_pointer = int(right)
                checkpoint_pointer = pointer + 1
                self.pointer_stack.push(checkpoint_pointer)
                print "^^^^^^^^^^^^^GOSUB ", new_pointer, checkpoint_pointer
                print self.functions_table.find(left).memory_size
                self.memory.push_new_level(copy.copy(self.functions_table.find(left).memory_size))
                self.memory.assign_parameters(self.params_stack.top())
                pointer = new_pointer
            elif action == 'ERA':
                function = self.global_vars.find(left)
                print function
                if function is None:
                    print "PUSHING -1 because of void"
                    self.return_addr_stack.push(-1) #function is void
                else:
                    self.return_addr_stack.push(function.address)
                self.params_stack.push([])
                pointer = pointer + 1
            elif action == 'PARAMETER':
                self.params_stack.top().append([self.memory.retrieve(left), left])
                print "PARAMS", self.params_stack.top()
                pointer = pointer + 1
            elif action == 'RETURN':
                print "RETURN"
                return_addr = self.return_addr_stack.pop()
                if return_addr != -1:
                    print "RETURN STUFF", return_addr, self.memory.retrieve(left)
                    self.memory.assign(return_addr, self.memory.retrieve(left))
                self.params_stack.pop()
                pointer = self.pointer_stack.pop()
                self.memory.pop_level()
            elif action == 'ENDPROC':
                self.params_stack.pop()
                pointer = self.pointer_stack.pop()
                self.memory.pop_level()
            elif action == '>':
                result = self.memory.retrieve(left) > self.memory.retrieve(right)
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == '<':
                result = self.memory.retrieve(left) < self.memory.retrieve(right)
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == '>=':
                result = self.memory.retrieve(left) >= self.memory.retrieve(right)
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == '<=':
                result = self.memory.retrieve(left) <= self.memory.retrieve(right)
                print "RESULT ", result
                self.memory.assign(quad_result, str(result).lower())
                pointer = pointer + 1
            elif action == '==':
                result = self.memory.retrieve(left) == self.memory.retrieve(right)
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == 'AND':
                result = self.memory.retrieve(left) == true and self.memory.retrieve(right) == true
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == 'OR':
                result = self.memory.retrieve(left) == true or self.memory.retrieve(right) == true
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == 'END':
                return
            elif action == 'PRINT':
                if right == "SET":
                    new_vector = self.memory.to_vector(left)
                    print '>', new_vector
                else:
                    print '>', self.memory.retrieve(left)
                pointer = pointer + 1
            elif action == 'READ':
                a = 1
            elif action == 'INSERT':
                if self.memory.find_value_in_addr(self.memory.retrieve(right), left) is None:
                    first_addr = self.memory.first_available_addr(left)
                    if first_addr is None:
                        print "OUT OF MEMORY"
                        raise ValueError
                    result = self.memory.assign_explicit(first_addr, self.memory.retrieve(right))
                pointer = pointer + 1
            elif action == 'REMOVE':
                addr = self.memory.find_value_in_addr(self.memory.retrieve(right), left)
                print "REMOVE", addr
                if not addr is None:
                    self.memory.assign_explicit(addr, None)
                pointer = pointer + 1
            elif action == 'FIND':
                addr = self.memory.find_value_in_addr(self.memory.retrieve(right), left)
                if addr is None:
                    self.memory.assign(quad_result, 'false')
                else:
                    self.memory.assign(quad_result,'true')
                pointer = pointer + 1
            elif action == 'CLEAR':
                self.memory.remove_list(left)
                pointer = pointer + 1
            elif action == 'SIZE':
                result = self.memory.size_in_addr(left)
                print "RESULT ", result
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == '.+':
                set_a = self.memory.to_vector(left)
                set_b = self.memory.to_vector(right)
                new_set = list(set((set_a + set_b)))
                print "lklklk", new_set
                self.memory.assign_list_to_addr(new_set, quad_result)
                pointer = pointer + 1
            elif action == '.-':
                set_a = self.memory.to_vector(left)
                set_b = self.memory.to_vector(right)
                new_set = list(set(set_a) - set(set_b))
                print "lklklk", new_set
                self.memory.assign_list_to_addr(new_set, quad_result)
                pointer = pointer + 1
            elif action == '.*':
                set_a = self.memory.to_vector(left)
                set_b = self.memory.to_vector(right)
                new_set = list(set(set_a) & set(set_b))
                print "lklklk", new_set
                self.memory.assign_list_to_addr(new_set, quad_result)
                pointer = pointer + 1
