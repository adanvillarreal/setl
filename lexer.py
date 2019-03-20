import ply.lex as lex
import ply.yacc as yacc
import sys
from collections import namedtuple
import logging

class SymbolTable:
    def __init__(self):
        self.table = {}

    def exists(self, name):
        return name in self.table

    def insert(self, name, symbol_type, data_type):
        if self.exists(name):
            return False
        else
            self.table[name] = namedtuple(name, symbol_type, data_type)
            return True

    def find(self, name):
        if self.exists(name):
            return self.table[name]
        else
            return None



tokens = [
    'CTE_FLOAT',
    'CTE_INT',
    'CTE_BOOL',
    'CTE_STRING',
    'CTE_CHAR',
    'ID',
    'ASSIGNATOR',
    'LEQ',
    'GEQ',
    'EQ',
    'NOT_EQ',
    'AND',
    'OPERATION',
    'OR',
]

t_ASSIGNATOR =  r':='
t_LEQ = r'<='
t_GEQ = r'>='
t_EQ = r'=='
t_NOT_EQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_OPERATION = r'(size|clear|insert|remove|find)'

literals = ['+', '-', '*', '/', '(', ')', '{', '}','.', ',', ':', ';', '=', '>', '<', '!']

reserved = {
  'bool': 'BOOL',
  'char': 'CHAR',
  'else' : 'ELSE',
  'float': 'FLOAT',
  'if' : 'IF',
  'int': 'INT',
  'main': 'MAIN',
  'map': 'MAP',
  'print': 'PRINT',
  'program' : 'PROGRAM',
  'read' : 'READ',
  'return': 'RETURN',
  'set': 'SET',
  'string': 'STRING',
  'void': 'VOID',
  'while': 'WHILE',
  'size' : 'OPERATION',
  'clear' : 'OPERATION',
  'insert' : 'OPERATION',
  'remove' : 'OPERATION',
  'find' : 'OPERATION',
  'true' : 'CTE_BOOL',
  'false' : 'CTE_BOOL'
}

def t_ID(t):
    r'([a-zA-Z][a-zA-Z0-9-_]*)'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_CTE_FLOAT(t):
    r'\d+\.\d+'
    return t

def t_CTE_INT(t):
    r'\d+'
    return t

def t_CTE_STRING(t):
    r'\"[a-zA-Z0-9]*\"'
    return t

def t_CTE_CHAR(t):
    r'\'[a-zA-Z0-9]\''
    return t

def t_CTE_BOOL(t):
    r'("true"|"false")'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t\n'

tokens = tokens + list(reserved.values())

# parser

start = "program"

def p_program(p):
    '''program : PROGRAM ID ';' program1'''

def p_program1(p):
    '''program1 : var program1
                | program2'''

def p_program2(p):
    '''program2 : proc program2
                | main'''

def p_procs(p):
    '''procs : proc
             | proc procs'''

def p_proc(p):
    '''proc : datatype procA
            | VOID procA
            | empty'''
def p_procA(p):
    '''procA : ID '(' proc1 ')' '{' proc3 '}' '''

def p_proc1(p):
    '''proc1 : datatype ID proc2
             | empty'''

def p_proc2(p):
    '''proc2 : ',' datatype ID proc2
             | empty'''

def p_proc3(p):
    '''proc3 : var proc3
             | proc4'''

def p_proc4(p):
    '''proc4 : statement proc4
             | empty'''

#
# def p_proc(p):
#     '''proc : datatype procA
#             | VOID procA
#             | empty'''
# def p_procA(p):
#     '''procA : ID '(' proc1 ')' '{' proc3 proc4 '}' '''
#
# def p_proc1(p):
#     '''proc1 : datatype ID proc2
#              | empty'''
#
# def p_proc2(p):
#     '''proc2 : ',' datatype ID proc2
#              | empty'''
#
# def p_proc3(p):
#     '''proc3 : vars
#              | empty'''
#
# def p_proc4(p):
#     '''proc4 : statement proc4
#              | empty'''

def p_vars(p):
    '''vars : var vars
            | var'''

def p_var(p):
    '''var : datatype var1 '''

def p_var1(p):
    '''var1 : ID ',' var1
             | ID var2'''

def p_var2(p):
    '''var2 : ';' '''

# def p_vars1(p):
#     '''vars2 : empty
#              | vars'''
#
#
# def p_vars(p):
#     '''vars : datatype vars1 ';' vars
#             | datatype vars1 ';' '''
#
# def p_vars1(p):
#     '''vars1 : ID ',' vars1
#              | ID'''
#
# def p_vars2(p):
#     '''vars2 : vars
#              | empty'''

def p_assignment(p):
    '''assignment : ID ASSIGNATOR expression'''

def p_condition(p):
    '''condition : IF '(' expression ')' block condition1'''

def p_condition1(p):
    '''condition1 : ELSE block
                  | empty'''

def p_input(p):
    '''input : READ '(' ID input1 ')' '''

def p_input1(p):
    '''input1 : ',' ID input1
              | empty'''

def p_output(p):
    '''output : PRINT '(' expression output1 ')' '''

def p_output1(p):
    '''output1 : ',' expression output1
               | empty'''

def p_function_call(p):
    '''function_call : ID '(' function_call1 ')' '''

def p_function_call1(p):
    '''function_call1 : empty
                      | function_call2'''

def p_function_call2(p):
    '''function_call2 : expression ',' function_call2
                      | expression'''

def p_return(p):
    '''return : RETURN expression'''

def p_set_operation(p):
    '''set_operation : ID '.' OPERATION '(' set_operation1 ')' '''

def p_set_operation1(p):
    '''set_operation1 : expression
                       | empty'''

def p_statement(p):
    '''statement : statement1 ';'
                 | statement2 '''

def p_statement1(p):
    '''statement1 : assignment
                  | input
                  | output
                  | set_operation
                  | map_definition
                  | return
                  | map_assignment
                  | map_operation
                  | function_call''' #aqui no falta set_asisignemtn?

def p_statement2(p):
    '''statement2 : condition
                  | while'''

def p_while(p):
    '''while : WHILE '(' expression ')' block'''

def p_relop(p):
    '''relop : '<'
             | '>'
             | NOT_EQ
             | EQ
             | LEQ
             | GEQ'''

def p_logop(p):
 '''logop : OR
          | AND'''

######## Segunda Parte

def p_expression(p):
  '''expression : exp0 expression2'''

def p_expression2(p):
  '''expression2 : logop exp0 expression2
                 | empty'''

def p_exp0(p):
  '''exp0 : exp exp02'''

def p_exp02(p):
  '''exp02 : relop exp0
           | empty'''

def p_exp(p):
  '''exp : term exp2'''

def p_addsub(p):
  '''addsub : '+'
            | '-' '''

def p_muldiv(p):
  '''muldiv : '*'
            | '/' '''

def p_exp2(p):
  '''exp2 : addsub term exp2
          | empty'''

def p_term(p):
  '''term : term_not factor term2'''

def p_term2(p):
  '''term2 : muldiv factor term2
           | empty'''

def p_term_not(p):
  '''term_not : '!'
              | empty'''

def p_factor(p):
  '''factor : '(' expression ')'
            | factor2'''

def p_factor2(p):
  '''factor2 : factor3 varcte'''

def p_factor3(p):
  '''factor3 : addsub
             | empty'''

def p_varcte(p):
  '''varcte : ID
            | CTE_INT
            | CTE_FLOAT
            | CTE_BOOL
            | CTE_STRING
            | CTE_CHAR
            | function_call
            | map_access
            | map_operation
            | set_operation '''

def p_functype(p):
  '''functype : datatype
               | VOID'''

def p_datatype(p):
  '''datatype : INT
               | FLOAT
               | BOOL
               | STRING
               | CHAR
               | set_definition
               | map_definition'''

def p_set_definition(p):
  '''set_definition : SET '<' datatype '>' '''

def p_block(p):
  '''block : '{' statement_aux '}' '''

def p_statement_aux(p):
  '''statement_aux : statement statement_aux
                   | empty'''

def p_main(p):
  '''main : MAIN '{' vars_aux statement_aux '}' '''

def p_vars_aux(p):
  '''vars_aux : vars
              | empty'''

def p_map_definition(p):
  '''map_definition : MAP '<' datatype ',' datatype '>' '''

def p_map_access(p):
  '''map_access : ID '(' exp ')' '''

def p_map_assignment(p):
  '''map_assignment : map_access ASSIGNATOR exp'''

def p_map_operation(p):
  '''map_operation : ID '.' OPERATION '(' ')' '''

def p_empty(p):
    '''empty :'''

def p_error( p ):
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

    print('Syntax error in input! Parser State:{} {} . {}'
      .format(parser.state,
              stack_state_str,
              p))


#----------------------------

#Build the lexer
lexer = lex.lex()

#Build the parser
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
parser = yacc.yacc()

f = open("test1.txt", "r")
s = ""

for x in f:
  s = s + x

print(s)
res = parser.parse(s, debug=log)
print(res)
lexer.input(s)
while True:
    tok = lexer.token()
    if not tok:
      break
    print(tok)
    print("~~~~~~~~~~~~~~")
