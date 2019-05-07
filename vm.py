from config import *
from symbol_table import *
import copy

# Class that handles the memory in the vm. Receives:
# memory ranges, delta for data types, sizes for global vars, sizes for local vars, sizes for temp_sizes and constants
# The sizes are required to preallocate memory
class VMMemory:
    def __init__(self, virtual_memory_ranges, delta, global_sizes, local_sizes, temp_sizes, constants):
        # memory preallocation. sizes is a map of {data_type: slots}
        # transformed into {data_type: []}
        for k, v in global_sizes.items():
            global_sizes[k] = [None]*v

        for k, v in local_sizes.items():
            local_sizes[k] = [None]*v

        for k, v in temp_sizes.items():
            temp_sizes[k] = [None]*v

        # local and temp memory are stacks, which are pushed and popped when
        # calling functions
        initial_stack_1 = Stack()
        initial_stack_2 = Stack()
        initial_stack_1.push(local_sizes)
        initial_stack_2.push(temp_sizes)

        # datastructure that holds the memory addresses
        self.memories = {'local': initial_stack_1, 'global': global_sizes, 'temporary': initial_stack_2, 'constant': {'BOOL': [], 'FLOAT': [], 'INT': [], 'CHAR': [], 'STRING':[]}}

        self.virtual_memory_ranges = virtual_memory_ranges
        self.delta = delta

        # preallocate and popullate constants in self.memories
        for key, value in constants.items():
            inv_map = {v: k for k, v in value.items()}
            for k, v in inv_map.items():
                self.append(k, v)
        #print self.memories

    # adds a new level to the local and temp stacks in self.memories.
    # receives memory_size, which is a map that holds the sizes for local and
    # temporary memories {datatype: slots}
    def push_new_level(self, memory_size):
        # preallocate memory
        local_sizes = memory_size['local'].copy()
        for k, v in local_sizes.items():
            local_sizes[k] = [0]*v

        temp_sizes = memory_size['temporary'].copy()
        for k, v in temp_sizes.items():
            temp_sizes[k] = [0]*v

        # push to stacks
        self.memories['local'].push(local_sizes)
        self.memories['temporary'].push(temp_sizes)

    # pops a level from the local and temp stacks.
    def pop_level(self):
        self.memories['local'].pop()
        self.memories['temporary'].pop()

    # Translates a virtual memory address to a place in the memories map.
    # Receives an address
    # Returns [mem_type, data_type, index]
    def translate(self, address):
        idx = 0
        config_memories = ['local', 'global', 'temporary', 'constant']
        config = ['BOOL', 'FLOAT', 'INT', 'CHAR', 'STRING']
        # ranges for memory
        vm_ranges = [0, 5000, 10000, 15000, 20000, 25000]
        for lim in vm_ranges:
            if address < lim:
                address = address - vm_ranges[idx-1]
                return [config_memories[idx-1], config[address/self.delta], address % self.delta]
            idx = idx + 1
        return None

    # Assigns parameters to memory. Params are the first addresses assigned.
    # Receives [[value, address],...]
    def assign_parameters(self, params):
        offset = {'BOOL':0, 'FLOAT': 0, 'INT': 0, 'CHAR': 0, 'STRING': 0}
        for param in params:
            translation = self.translate(param[1])
            #print "ASSIGNING PARAM", param, translation
            self.memories['local'].top()[translation[1]][offset[translation[1]]] = param[0]
            offset[translation[1]] = offset[translation[1]] + 1

    # Appends a value to a given memory
    # Receives an address and a value
    def append(self, address, value):
        translation = self.translate(address)
        #print 'assigning ', translation, address, value
        if translation is None:
            raise RuntimeError("OUT OF MEMORY")
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]].append(value)
        else:
            self.memories[translation[0]][translation[1]].append(value)

    # Assigns a value to a given memory address
    # Receives an address and a value
    def assign(self, address, value):
        translation = self.translate(address)
        print 'assigning ', translation, address, value
        if translation is None:
            raise RuntimeError("OUT OF MEMORY")
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]][translation[2]] = value
        else:
            self.memories[translation[0]][translation[1]][translation[2]] = value

    # Assigns a value without an address (Similar to assign but without translating)
    # Receives translation [memory_type, data_type, index] and value
    def assign_explicit(self, translation, value):
        if translation is None:
            print self.memories['global']['INT']
            raise RuntimeError("OUT OF MEMORY")
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]][translation[2]] = value
        else:
            self.memories[translation[0]][translation[1]][translation[2]] = value

    # Appends 10 new cells to a memory with value None
    # Receives a translation [memory_type, data_type, index]
    def add_memory_chunk(self, translation):
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            self.memories[translation[0]].top()[translation[1]] = self.memories[translation[0]].top()[translation[1]] + [None] * 10
        else:
            self.memories[translation[0]][translation[1]] = self.memories[translation[0]][translation[1]] + [None] * 10

    # Returns the first available address after a given address
    # Receives an address
    # Returns [memory_type, data_type, address, abs_count], where abs_count is
    # the distance from address to first available address.
    def first_available_addr(self, address):
        mem_base_addr = {'local':0, 'global':5000, 'temporary': 10000, 'constant': 15000}
        data_type_base_addr = {'BOOL': 0, 'FLOAT': 1000, 'INT': 2000, 'CHAR': 3000, 'STRING': 4000}
        chunk_size = 10
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        abs_count = 0;
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        first_addr = idx

        # while address is not bigger than delta 1000
        while(idx + counter < 1000):
            print idx, counter
            # 10th cell has a pointer. Follow or add append a new chunk.
            if counter != 0 and counter % 9 == 0:
                # if more memory is needed
                if memory[idx + counter] is None:
                    memory[idx + counter] = len(memory)
                    idx = len(memory)
                    counter = 0
                    self.add_memory_chunk(translation)
                    if (translation[0] == 'local' or translation[0] == 'temporary'):
                        memory = self.memories[translation[0]].top()[translation[1]]
                    else:
                        memory = self.memories[translation[0]][translation[1]]
                # follow the pointer
                else:
                    idx = memory[idx + counter]
                    counter = 0
            # normal cell
            else:
                # if free
                if memory[idx + counter] is None:
                    first_addr = idx + counter
                    # print "FIND MEM IN", [translation[0], translation[1], first_addr]
                    return[translation[0], translation[1], first_addr, abs_count]
                counter = counter + 1
            abs_count = abs_count + 1
        # memory limit exceeded
        return None

    # counts distance from start address of container to it's end, without
    # counting None cells
    # Receives address
    # Returns abs_counter.
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
        # while not bigger than memory
        while(idx + counter < len(memory)):
            # if cell is a pointer, return if end or follow pointer.
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

    # find a value by traversing a container in memory.
    # receives a value and address
    # Returns [memory_type, data_type, address, abs_count], where abs_count is
    # distance to the value from address or None if not found
    def find_value_in_addr(self, value, address):
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        abs_count = 0
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        # while still in range of memory
        while(idx + counter < len(memory)):
            #print idx, counter, idx + counter
            # if cell is a pointer, return None if end or follow pointer.
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    return None
                else:
                    idx = memory[idx + counter]
                    counter = 0
            else:
                # if value found
                if (memory[idx+counter] == value):
                    return [translation[0], translation[1], idx+counter, abs_count]
                counter = counter + 1
            abs_count = abs_count + 1
        return None

    # set all the elements of a container to None
    # receives an address
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
            #print idx, counter
            # if cell is a pointer, return if end or follow pointer and cleanup.
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    return
                else:
                    old_idx = idx
                    idx = memory[idx + counter]
                    memory[old_idx + counter] = None
                    counter = 0
            else:
                # set value to None.
                memory[idx + counter] = None
                counter = counter + 1
        return

    # Returns a vector representation of a collection in memory (without
    # pointers or empty spaces)
    # Receives address
    # Returns new_vector
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
        # while still in range of memory
        while(idx + counter < len(memory)):
            #print idx, counter
            # if cell is a pointer, return vector if end or follow pointer.
            if counter != 0 and counter % 9 == 0:
                if memory[idx + counter] is None:
                    return new_vector
                else:
                    idx = memory[idx + counter]
                    counter = 0
            else:
                # if not None, append to vector
                if not memory[idx+counter] is None:
                    new_vector.append(memory[idx+counter])
                counter = counter + 1
        return new_vector

    # create a collection in memory from a vector
    # receives a vector l_set, and an address
    def assign_list_to_addr(self, l_set, address):
        # initial addresses and offsets by datatype
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
        # set idx to the collection's head
        first_addr = idx
        set_idx = 0
        # while in range of delta and the vector still has elements
        while(idx + counter < 1000 and set_idx < len(l_set)):
            # if cell is a pointer
            if counter != 0 and counter % 9 == 0:
                # if a new chunk is needed, add chunk and link
                if memory[idx + counter] is None:
                    memory[idx + counter] = len(memory)
                    idx = len(memory)
                    counter = 0
                    self.add_memory_chunk(translation)
                    if (translation[0] == 'local' or translation[0] == 'temporary'):
                        memory = self.memories[translation[0]].top()[translation[1]]
                    else:
                        memory = self.memories[translation[0]][translation[1]]
                # follow a pointer to next chunk. This else would be used for
                # future optimizations.
                else:
                    idx = memory[idx + counter]
                    counter = 0
            else:
                # if space is available, assign the vector's value
                if memory[idx + counter] is None:
                    first_addr = idx + counter
                    print"ASDASDASDASDASDASDADSDASDASDASD", set_idx, len(l_set)
                    self.assign_explicit([translation[0], translation[1], first_addr], l_set[set_idx])
                    set_idx = set_idx + 1
                # This else would be used for future optimizations.
                #else:
                counter = counter + 1

        # check if the while exited because memory ran out
        if idx + counter >= 1000:
            return None
        else:
            return True

    # given a translation [memory_type, data_type, address], returns an address.
    # receives translation
    # returns address
    def reverse_translate(self,translation):
        # base memory addresses
        mem_base_addr = {'local':0, 'global':5000, 'temporary': 10000, 'constant': 15000}
        data_type_base_addr = {'BOOL': 0, 'FLOAT': 1000, 'INT': 2000, 'CHAR': 3000, 'STRING': 4000}
        return mem_base_addr[translation[0]] + data_type_base_addr[translation[1]] + translation[2]

    # returns the address after an offset is applied. Used to get the address
    # corresponding to a key's value
    def map_value_address(self, address, offset):
        translation = self.translate(address)
        idx = translation[2]
        memory = []
        new_vector = []
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            memory = self.memories[translation[0]].top()[translation[1]]
        else:
            memory = self.memories[translation[0]][translation[1]]
        counter = 0
        # abs_counter keeps track of the traversal
        abs_counter = 0

        # while still in memory range.
        while(idx + counter < len(memory)):
            #print "MAP VALUE ACCESS", idx, counter, offset
            # if traversed count is same as offset, return the address
            if abs_counter == offset:
                return self.reverse_translate([translation[0], translation[1], idx + counter])
            # if pointer and more memory needed, add a chunk. Else, follow pointer
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
                    #print "AQUI"
                    idx = memory[idx + counter]
                    counter = 0
            # keep traversing
            else:
                counter = counter + 1
            abs_counter = abs_counter + 1

        # if ran out of memory, return none
        return None

    # returns the value for a given address
    # receives an address
    # returns a value
    def retrieve(self, address):
        translation = self.translate(address)
        #print 'retrieving', translation, address
        if translation is None:
            raise RuntimeError("OUT OF MEMORY")
        if (translation[0] == 'local' or translation[0] == 'temporary'):
            # check if it's required to cast value
            if translation[1] == 'INT':
                #print self.memories
                return int(self.memories[translation[0]].top()[translation[1]][translation[2]])
            elif translation[1] =='FLOAT':
                return float(self.memories[translation[0]].top()[translation[1]][translation[2]])
            else:
                return self.memories[translation[0]].top()[translation[1]][translation[2]]
        else:
            # check if it's required to cast value
            if translation[1] == 'INT':
                return int(self.memories[translation[0]][translation[1]][translation[2]])
            elif translation[1] =='FLOAT':
                return float(self.memories[translation[0]][translation[1]][translation[2]])
            else:
                return self.memories[translation[0]][translation[1]][translation[2]]

# Class that handles operations with the virtual machine.
# Receives the functions_table, constants map, memory for global vars, quadruples, ranges for memory, delta for datatypes in memory, and global vars
class VM:
    def __init__(self, functions, constants, global_vars_mem, quadruples, vm_ranges, delta, global_vars):
        self.functions_table = functions
        # set the main memory sizes using the functions table
        main_memory_info = functions.find('MAIN').memory_size
        self.quadruples = quadruples
        #print main_memory_info
        # initialize the memory with the info for MAIN, global vars and constants.
        self.memory = VMMemory(vm_ranges, delta, global_vars_mem, main_memory_info['local'], main_memory_info['temporary'], constants)

        # variables for the handling of function calls
        self.params_stack = Stack()
        self.pointer_stack = Stack()
        self.params_list = []
        # has the global addresses to save the returned value
        self.return_addr_stack = Stack()
        self.global_vars = global_vars

    # preprocess an address to check whether it's a pointer to an address or an
    # address
    # Receives an address
    # Returns an address
    def process_addr(self, address):
        #print "PROCESS ADDR", address
        if address is None:
            return None
        # if starts with (, it's a pointer to an address, retrieve the address
        if str(address).startswith('('):
            address = address[1:-1]
            #print "PROCESS RES", address, self.memory.retrieve(int(address))
            return int(self.memory.retrieve(int(address)))
        # return the address
        else:
            return address

    # Processes a quad at a given pointer.
    # Receives a pointer to a quad.
    def process_quad(self, pointer):
        while(True):
            # Retrieves the quad's information
            action = self.quadruples.get(pointer).action
            left = self.process_addr(self.quadruples.get(pointer).first)
            right = self.process_addr(self.quadruples.get(pointer).second)
            quad_result = self.process_addr(self.quadruples.get(pointer).result)
            #print self.memory.memories['global']
            #print "TEEEEEMP"
            #print self.memory.memories['temporary'].top()
            #print "QUUUUUUUUAD", action, left, right, quad_result

            # switch with operations start. Always add 1 to the pointer.
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
                if self.memory.retrieve(right) == 0:
                    raise RuntimeError("DIVISION BY ZERO")
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
                # save pointer to where execution will resume in this scope
                checkpoint_pointer = pointer + 1
                self.pointer_stack.push(checkpoint_pointer)

                #print "^^^^^^^^^^^^^GOSUB ", new_pointer, checkpoint_pointer
                #print self.functions_table.find(left).memory_size

                # push a new level to local and temporary memory
                self.memory.push_new_level(copy.copy(self.functions_table.find(left).memory_size))
                # assign parameters
                self.memory.assign_parameters(self.params_stack.top())
                pointer = new_pointer
            elif action == 'ERA':
                function = self.global_vars.find(left)
                #print function
                # push -1 to return address stack if void
                if function is None:
                    #print "PUSHING -1 because of void"
                    self.return_addr_stack.push(-1) #function is void
                # push the return address to the global var
                else:
                    self.return_addr_stack.push(function.address)
                # push a new vector to the params stack
                self.params_stack.push([])
                pointer = pointer + 1
            elif action == 'PARAMETER':
                # Add a param to the top of the params stack
                self.params_stack.top().append([self.memory.retrieve(left), left])
                #print "PARAMS", self.params_stack.top()
                pointer = pointer + 1
            elif action == 'RETURN':
                #print "RETURN"
                # get addr to save the result, pop from stack
                return_addr = self.return_addr_stack.pop()
                # if non-void functoin
                if return_addr != -1:
                    #print "RETURN STUFF", return_addr, self.memory.retrieve(left)
                    self.memory.assign(return_addr, self.memory.retrieve(left))
                # pop params stack, pointer_stack and memory level. Set pointer
                # to previous level
                self.params_stack.pop()
                pointer = self.pointer_stack.pop()
                self.memory.pop_level()
            elif action == 'ENDPROC':
                # pop params stack, pointer_stack and memory level. Set pointer
                # to previous level
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
                #print "RESULT ", result
                self.memory.assign(quad_result, str(result).lower())
                pointer = pointer + 1
            elif action == '==':
                result = self.memory.retrieve(left) == self.memory.retrieve(right)
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == '!=':
                result = self.memory.retrieve(left) != self.memory.retrieve(right)
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == '&&':
                result = self.memory.retrieve(left) == 'true' and self.memory.retrieve(right) == 'true'
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == '||':
                result = self.memory.retrieve(left) == 'true' or self.memory.retrieve(right) == 'true'
                self.memory.assign(quad_result,  str(result).lower())
                pointer = pointer + 1
            elif action == '!':
                result = self.memory.retrieve(left) == 'false'
                self.memory.assign(quad_result, str(result).lower)
                pointer = pointer + 1
            elif action == 'END':
                # this ends the while loop and the execution.
                return
            elif action == 'PRINT':
                if right == "SET":
                    new_vector = self.memory.to_vector(left)
                    print '>', new_vector
                else:
                    print '>', self.memory.retrieve(left)
                pointer = pointer + 1
            elif action == 'READ':
                translation = self.memory.translate(quad_result)
                user_input = raw_input(">")
                data_type = translation[1]
                # try and parse the given input. Fail if mismatch.
                try:
                    if (data_type == "INT"):
                        user_input = int(user_input)
                    elif (data_type == "STRING"):
                        user_input = str(user_input)
                    elif (data_type == "CHAR"):
                        if(len(user_input) == 1):
                            user_input = str(user_input)
                        else:
                            raise RuntimeError
                    elif (data_type == "BOOL"):
                        if user_input == "true":
                            user_input = True
                        elif user_input == "false":
                            user_input = False
                        else:
                            raise RuntimeError
                    self.memory.assign(quad_result, user_input)
                except:
                    raise RuntimeError("Data type mismatch in read")
                pointer = pointer + 1
            elif action == 'INSERT':
                # if value not found in set, assign in first_available addr
                if self.memory.find_value_in_addr(self.memory.retrieve(right), left) is None:
                    first_addr = self.memory.first_available_addr(left)
                    if first_addr is None:
                        raise RuntimeError("OUT OF MEMORY")
                    result = self.memory.assign_explicit(first_addr, self.memory.retrieve(right))
                pointer = pointer + 1
            elif action == 'REMOVE':
                addr = self.memory.find_value_in_addr(self.memory.retrieve(right), left)
                #print "REMOVE", addr
                # if found value, remove it
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
                # if map, then remove key and value collections
                if isinstance(left, list):
                    self.memory.remove_list(left[0])
                    self.memory.remove_list(left[1])
                else:
                    # remove set
                    self.memory.remove_list(left)
                pointer = pointer + 1
            elif action == 'SIZE':
                if isinstance(left, list):
                    result = self.memory.size_in_addr(left[0])
                    #print "RESULT ", result
                    self.memory.assign(quad_result, result)
                else:
                    result = self.memory.size_in_addr(left)
                    #print "RESULT ", result
                    self.memory.assign(quad_result, result)
                pointer = pointer + 1
            elif action == '.+':
                set_a = self.memory.to_vector(left)
                set_b = self.memory.to_vector(right)
                new_set = list(set((set_a + set_b)))
                #print "lklklk", new_set
                self.memory.assign_list_to_addr(new_set, quad_result)
                pointer = pointer + 1
            elif action == '.-':
                set_a = self.memory.to_vector(left)
                set_b = self.memory.to_vector(right)
                new_set = list(set(set_a) - set(set_b))
                #print "lklklk", new_set
                self.memory.assign_list_to_addr(new_set, quad_result)
                pointer = pointer + 1
            elif action == '.*':
                set_a = self.memory.to_vector(left)
                set_b = self.memory.to_vector(right)
                new_set = list(set(set_a) & set(set_b))
                #print "lklklk", new_set
                self.memory.assign_list_to_addr(new_set, quad_result)
                pointer = pointer + 1
            elif action == 'ACCESS':
                key_start = left[0]
                val_start = left[1]
                key_addr = self.memory.find_value_in_addr(self.memory.retrieve(right), key_start)
                #print "KEY_ADDR",key_addr
                # if key doesn't exist, reserve a space for the key and set
                # value to default value.
                if key_addr is None:
                    new_key_addr = self.memory.first_available_addr(key_start)
                    self.memory.assign_explicit(new_key_addr, self.memory.retrieve(right))
                    new_val_addr = self.memory.map_value_address(val_start, new_key_addr[3])

                    default_values = {'BOOL': 'false', 'INT': 0, 'FLOAT': 0.0, 'CHAR': ' ', 'STRING': " "}
                    translated_val = self.memory.translate(new_val_addr)

                    self.memory.assign(new_val_addr, default_values[translated_val[1]])
                    #print "ACCESSSSSSSSS", quad_result, new_val_addr
                    self.memory.assign(quad_result, new_val_addr)
                # key already exist, just update value
                else:
                    #print "OFFFSET ", key_addr
                    val_addr = self.memory.map_value_address(val_start, key_addr[3])
                    self.memory.assign(quad_result, val_addr)
                pointer = pointer + 1
            elif action == 'DOMAIN':
                key_start = left[0]
                val_start = left[1]
                result = self.memory.to_vector(key_start)
                #print "DOMAIN",result, quad_result
                self.memory.assign_list_to_addr(result, quad_result)
                pointer = pointer + 1
            elif action == 'RANGE':
                key_start = left[0]
                val_start = left[1]
                result = self.memory.to_vector(val_start)
                self.memory.assign_list_to_addr(list(set(result)), quad_result)
                pointer = pointer + 1
