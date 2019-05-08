# Semantic Cube Class
# defines valid operations between data types
# accepts or rejects a given operation between 2 operands
# Works as a 2D list of dictionaries, where first 2 dimensions are the data types
# the key, value in dictionaries represent Operation and data type returned
class SemanticCube:

    num_operators = 26
    num_datatypes = 8

    def init_names(self):
        self.datatypes = { "INT" : 0, "FLOAT": 1, "CHAR": 2,
        "BOOL": 3, "STRING": 4, "SET": 5, "MAP": 6, "NONE" : 7}

        self.operators = { "+" : 0, "-" : 1, "*" : 2, "/" : 3, "&&" : 4,
        "||" : 5, ">" : 6, ">=" : 7, "<" : 8, "<=" : 9, "==" : 10,
        "!=" : 11, "!" : 12, "=" : 13, "PRINT" : 14, "READ" : 15, "DOMAIN" : 16,
        "RANGE" : 17, "SIZE" : 18, "CLEAR" : 19, "INSERT" : 20, "REMOVE" : 21,
        "FIND" : 22, ".+" : 23, ".*" : 24, ".-" : 25 }

    # Initialize cube to an empty 2D list of dictionaries
    def init_cube(self):
        self.cube = []
        for i in range(0,self.num_datatypes):
            self.cube.append([])
            for j in range(0,self.num_datatypes):
                self.cube[i].append([])
                for k in range(0,self.num_operators):
                    self.cube[i][j].append({})

    def fill_cube(self):
        key_int = self.datatypes["INT"]
        key_float = self.datatypes["FLOAT"]
        key_bool = self.datatypes["BOOL"]
        key_char = self.datatypes["CHAR"]
        key_string = self.datatypes["STRING"]
        key_set = self.datatypes["SET"]
        key_map = self.datatypes["MAP"]
        key_none = self.datatypes["NONE"]

        key_add = self.operators["+"]
        key_sub = self.operators["-"]
        key_mult = self.operators["*"]
        key_div = self.operators["/"]
        key_gt= self.operators[">"]
        key_gqt = self.operators[">="]
        key_lt = self.operators["<"]
        key_lqt = self.operators["<="]
        key_equals = self.operators["=="]
        key_diff = self.operators["!="]
        key_log_and = self.operators["&&"]
        key_log_or = self.operators["||"]
        key_not = self.operators["!"]
        key_assign = self.operators["="]

        key_print = self.operators["PRINT"]
        key_read = self.operators["READ"]
        key_domain = self.operators["DOMAIN"]
        key_range = self.operators["RANGE"]
        key_size = self.operators["SIZE"]
        key_clear = self.operators["CLEAR"]
        key_insert = self.operators["INSERT"]
        key_remove = self.operators["REMOVE"]
        key_find = self.operators["FIND"]

        key_set_union = self.operators[".+"]
        key_set_difference = self.operators[".-"]
        key_set_intersection = self.operators[".*"]

        # Int versus everyone
        self.cube[key_int][key_int] = {"+": "INT" , "-": "INT", "*": "INT",
                                    "/": "INT", ">": "BOOL", ">=": "BOOL",
                                    "<": "BOOL", "<=": "BOOL", "==": "BOOL",
                                    "!=": "BOOL", "=": "INT"}

        #Float versus everyone
        self.cube[key_float][key_float] = {"+": "FLOAT" , "-": "FLOAT", "*": "FLOAT",
                                        "/": "FLOAT", ">": "BOOL", ">=": "BOOL",
                                        "<": "BOOL", "<=": "BOOL", "==": "BOOL",
                                        "!=": "BOOL", "=": "FLOAT"}
        # Char versus everyone
        self.cube[key_char][key_char] = {">": "BOOL", ">=": "BOOL", "<": "BOOL",
                                        "<=": "BOOL", "==": "BOOL","!=": "BOOL",
                                        "=": "CHAR"}
        # Bool versus everyone
        self.cube[key_bool][key_bool] = {"==": "BOOL", "!=": "BOOL",
                                        "&&": "BOOL", "||": "BOOL", "=": "BOOL"}

        self.cube[key_bool][key_none] = {"!": "BOOL"}

        # String versus everyone
        self.cube[key_string][key_string] = {"+": "STRING", ">": "BOOL",
                                            ">=": "BOOL", "<": "BOOL",
                                            "<=": "BOOL", "==": "BOOL",
                                            "!=": "BOOL", "=": "STRING"}

        #Set versus everyone
        self.cube[key_set][key_set] = {".+": "SET", ".-": "SET", ".*": "SET",
                                       "=": "SET"}
        self.cube[key_set][key_int] = {"INSERT": "NONE", "REMOVE": "NONE",
                                       "FIND": "BOOL"}
        self.cube[key_set][key_float] = {"INSERT": "NONE", "REMOVE": "NONE",
                                         "FIND": "BOOL"}
        self.cube[key_set][key_char] = {"INSERT": "NONE", "REMOVE": "NONE",
                                        "FIND": "BOOL"}
        self.cube[key_set][key_string] = {"INSERT": "NONE", "REMOVE": "NONE",
                                         "FIND": "BOOL"}
        self.cube[key_set][key_bool] = {"INSERT": "NONE", "REMOVE": "NONE",
                                        "FIND": "BOOL"}
        self.cube[key_set][key_none] = {"SIZE": "INT", "CLEAR": "NONE"}

        #Map
        self.cube[key_map][key_none] = {"DOMAIN": "SET", "RANGE": "SET",
                                        "SIZE": "INT", "CLEAR": "NONE"}


    def __init__(self):
        self.init_names()
        self.init_cube()
        self.fill_cube()

    # Returns the type returned by two operands and an operation
    # Or returns false if operation is not valid 
    def accepts(self, datatype1, datatype2, operator):
        datatype1 = str(datatype1).upper()
        datatype2 = str(datatype2).upper()

        #Fprint(str(datatype1) + " " + str(datatype2) + "***" + str(operator))

        key_param1 = self.datatypes[datatype1]
        key_param2 = self.datatypes[datatype2]

        if operator in self.cube[key_param1][key_param2]:
            return self.cube[key_param1][key_param2][operator]
        else:
            return False
