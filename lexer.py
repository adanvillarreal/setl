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
