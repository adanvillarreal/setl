from config import *
from symbol_table import *

class VMMemory:
    def __init__(self, virtual_memory_ranges, delta, global_sizes, local_sizes, temp_sizes, constants):
        for k, v in global_sizes.items():
            global_sizes[k] = [0]*v

        for k, v in local_sizes.items():
            local_sizes[k] = [0]*v

        for k, v in temp_sizes.items():
            temp_sizes[k] = [0]*v

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

    def translate(self, address):
        idx = 0
        config_memories = ['local', 'global', 'temporary', 'constant']
        config = ['BOOL', 'FLOAT', 'INT', 'CHAR', 'STRING']
        for mem_addr in self.virtual_memory_ranges:
            #print address, mem_addr
            if address < mem_addr:
                address = address - mem_addr
                return [config_memories[idx], config[address/self.delta], address % self.delta]
            idx = idx + 1
        return None

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
    def __init__(self, functions, constants, global_vars_mem, quadruples, vm_ranges, delta):
        self.functions_table = functions
        main_memory_info = functions.find('MAIN').memory_size
        self.quadruples = quadruples
        print main_memory_info
        self.memory = VMMemory(vm_ranges, delta, global_vars_mem, main_memory_info['local'], main_memory_info['temporary'], constants)

    def process_quad(self, pointer):
        while(True):
            action = self.quadruples.get(pointer).action
            #print action
            left = self.quadruples.get(pointer).first
            right = self.quadruples.get(pointer).second
            quad_result = self.quadruples.get(pointer).result
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
                pointer = right
            elif action == 'ERA':
                a = 1
            elif action == 'PARAM':
                a = 1
            elif action == 'RETURN':
                a = 1
            elif action == 'ENDPROC':
                a = 1
            elif action == '>':
                result = self.memory.retrieve(left) > self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == '<':
                result = self.memory.retrieve(left) < self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == 'GEQ':
                result = self.memory.retrieve(left) >= self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == 'LEQ':
                result = self.memory.retrieve(left) <= self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == 'EQ':
                result = self.memory.retrieve(left) == self.memory.retrieve(right)
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == 'AND':
                result = self.memory.retrieve(left) == true and self.memory.retrieve(right) == true
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == 'OR':
                result = self.memory.retrieve(left) == true or self.memory.retrieve(right) == true
                self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == 'END':
                return
            elif action == 'PRINT':
                print '>', self.memory.retrieve(left)
                pointer = pointer + 1
            elif action == 'READ':
                a = 1
