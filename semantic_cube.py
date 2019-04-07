
class SemanticCube:

    num_operators = 12 # sin contar unarios
    num_datatypes = 8 # int float bool char string set map

    def init_names(self):
        self.datatypes = { "INT" : 0, "FLOAT": 1, "CHAR": 2,
        "BOOL": 3, "STRING": 4, "SET": 5, "MAP": 6, "NONE" : 7}

        self.operators = { "+" : 0, "-" : 1, "*" : 2, "/" : 3, "&&" : 4,
        "||" : 5, ">" : 6, ">=" : 7, "<" : 8, "<=" : 9, "==" : 10,
        "!=" : 11, "!" : 12 }

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

        # Most repeated group
        # {"+" , "-", "*", "/", ">", ">=", "<=", "==", "!="}

        # Int versus everyone
        self.cube[key_int][key_int] = {"+": "INT" , "-": "INT", "*": "INT",
                                    "/": "INT", ">": "BOOL", ">=": "BOOL",
                                    "<": "BOOL", "<=": "BOOL", "==": "BOOL",
                                    "!=": "BOOL"}
        self.cube[key_int][key_float] = {"+": "FLOAT" , "-": "FLOAT", "*": "FLOAT",
                                        "/": "FLOAT", ">": "BOOL", ">=": "BOOL",
                                        "<": "BOOL", "<=": "BOOL", "==": "BOOL",
                                        "!=": "BOOL"}
        #Float versus everyone
        self.cube[key_float][key_int] = {"+": "FLOAT" , "-": "FLOAT", "*": "FLOAT",
                                        "/": "FLOAT", ">": "BOOL", ">=": "BOOL",
                                        "<": "BOOL", "<=": "BOOL", "==": "BOOL",
                                        "!=": "BOOL"}
        self.cube[key_float][key_float] = {"+": "FLOAT" , "-": "FLOAT", "*": "FLOAT",
                                        "/": "FLOAT", ">": "BOOL", ">=": "BOOL",
                                        "<": "BOOL", "<=": "BOOL", "==": "BOOL",
                                        "!=": "BOOL"}
        # Char versus everyone
        self.cube[key_char][key_char] = {">": "BOOL", ">=": "BOOL", "<": "BOOL",
                                        "<=": "BOOL", "==": "BOOL","!=": "BOOL"}
        # Bool versus everyone
        self.cube[key_bool][key_bool] = {"==": "BOOL", "!=": "BOOL",
                                        "&&": "BOOL", "||": "BOOL"}

        self.cube[key_bool][key_none] = {"!"}

        # String versus everyone
        self.cube[key_string][key_string] = {"+": "STRING", ">": "BOOL",
                                            ">=": "BOOL", "<": "BOOL",
                                            "<=": "BOOL", "==": "BOOL",
                                            "!=": "BOOL"}


    def __init__(self):
        self.init_names()
        self.init_cube()
        self.fill_cube()

    def accepts(self, datatype1, datatype2, operator):

        print(str(datatype1) + "" + str(datatype2) + "***" + str(operator))

        key_param1 = self.datatypes[datatype1]
        key_param2 = self.datatypes[datatype2]



        if operator in self.cube[key_param1][key_param2]:
            return self.cube[key_param1][key_param2][operator]
        else:
            return False

x = SemanticCube()
#print (x.cube)
#query = {TRUE,FALSE}
query = x.accepts("BOOL","BOOL","==") # este da NO
print(query)
#query = x.accepts("BOOL","BOOL","!=") # este da SI



'''
    def sum(p1, p2):
        return p1 + p2

    def sub(p1, p2):
        return p1 - p2

    def mult(p1, p2):
        return p1 * p2

    def div(p1, p2):
        return p1 / p2

    def gt(p1, p2):
        return p1 > p2

    def gqt(p1, p2):
        return p1 >= p2

    def lt(p1, p2):
        return p1 < p2

    def lqt(p1, p2):
        return p1 <= p2

    def equals(p1, p2):
        return p1 == p2

    def diff(p1, p2):
        return p1 != p2

    def log_and(p1, p2):
        return p1 and p2

    def log_or(p1, p2):
        return p1 or p2
'''
