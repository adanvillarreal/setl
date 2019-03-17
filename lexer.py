import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'CTE_FLOAT',
    'CTE_INT',
    'CTE_STRING',
    'CTE_BOOL',
    'CTE_CHAR',
    'ID',
    'ASSIGNATOR',
    'LEQ',
    'GEQ',
    'EQ',
    'NOT_EQ',
    'AND',
    'OR',
    'OPERATION'
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
  'clear': 'CLEAR',
  'else' : 'ELSE',
  'find': 'FIND',
  'float': 'FLOAT',
  'if' : 'IF',
  'insert': 'INSERT',
  'int': 'INT',
  'main': 'MAIN',
  'map': 'MAP',
  'print': 'PRINT',
  'program' : 'PROGRAM',
  'read' : 'READ',
  'remove': 'REMOVE',
  'return': 'RETURN',
  'set': 'SET',
  'size': 'SIZE',
  'string': 'STRING',
  'var': 'VAR',
  'void': 'VOID',
  'while': 'WHILE'
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
    r'(true|false)'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t\n'

tokens = tokens + list(reserved.values())

lex.lex()

# parser

start = "program"

def p_program(p):
    '''program : PROGRAM ID ';' program1'''

def p_program1(p):
    '''program1 : program2 program3 main'''

def p_program2(p):
    '''program2 : vars
                | empty'''

def p_program3(p):
    '''program3 : proc program3
                | empty'''

def p_vars(p):
    '''vars : dataype vars1 ';' vars2'''

def p_vars1(p):
    '''vars1 : ID ',' vars1 | ID'''

def p_vars2(p):
    '''vars2 : vars | empty'''


def p_proc(p):
    '''proc : functype ID '(' proc1 ')' '{' proc3 proc4 '}'''

def p_proc1(p):
    '''proc1 : datatype ID proc2'''

def p_proc2(p):
    '''proc2 : ',' proc1 | empty'''

def p_proc3(p):
    '''proc3 : vars | empty'''

def p_proc4(p):
    '''proc4 : statement proc4 | empty'''

def p_assignment(p):
    '''assignment : ID ASSIGNATOR expression'''

def p_condition(p):
    '''condition : IF '(' expression ')' block condition1'''

def p_condition1(p):
    '''condition1 : ELSE block | empty'''

def p_input(p):
    '''input : READ '(' ID input1 ')' '''

def p_input1(p):
    '''input1 : ',' ID input1 | empty'''

def p_output(p):
    '''output : PRINT '(' expression output1 ')' '''

def p_output1(p):
    '''output1 : ',' expression output1 | empty'''

def p_function_call(p):
    '''function_call : ID '(' function_call1 ')' '''

def p_function_call1(p):
    '''function_call1 : function_call2 | empty'''

def p_function_call2(p):
    '''function_call2 : expression ',' function_call2 | empty'''

def p_return(p):
    '''return : RETURN expression'''

def p_set_operations(p):
    '''set_operations : ID '.' OPERATION '(' set_operations1 ')' '''

def p_set_operations1(p):
    '''set_operations1 : expression | empty'''

def p_statement(p):
    '''statement : statement1 ';' | statement2 '''

def p_statement1(p):
    '''statement1 : assignment
                  | input
                  | output
                  | set_operations
                  | map_definition
                  | map_assignment
                  | map_operation''' #aqui no falta set_asisignemtn?

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
