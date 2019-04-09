import ply.lex as lex
import ply.yacc as yacc
import sys
from collections import namedtuple
import logging
from symbol_table import SymbolTable
from semantic_cube import SemanticCube
from config import *

global_vars_table = SymbolTable()
local_vars_table = SymbolTable()
procs_table = SymbolTable()
semantic_cube = SemanticCube()
current_table = global_vars_table
semantic_tool = Semantics()

#Expression-quads
operator_stack = Stack()
operand_stack = Stack()
type_stack = Stack()
quadruples_list = QuadrupleList()

#non-linear-quads
jump_stack = Stack()


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
    operand_stack.push(t.value)
    type_stack.push("FLOAT")
    return t

def t_CTE_INT(t):
    r'\d+'
    operand_stack.push(t.value)
    type_stack.push("INT")
    return t

def t_CTE_STRING(t):
    r'\"[a-zA-Z0-9]*\"'
    operand_stack.push(t.value)
    type_stack.push("STRING")
    return t

def t_CTE_CHAR(t):
    r'\'[a-zA-Z0-9]\''
    operand_stack.push(t.value)
    type_stack.push("CHAR")
    return t

# def t_CTE_BOOL(t):
#     r'("true"|"false")'
#     print("")
#     return t

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
    '''proc : proca1 procA
            | VOID procA
            | empty'''
    print ":function" + p[1]


def p_proca1(p):
    '''proca1 :  datatype ID '(' '''
    if not semantic_tool.new_proc(p[2], p[1]):
        print "Function " + p[2] + " already declared"
        raise SyntaxError

    p[0] = p[1] + p[2]

def p_procA(p):
    '''procA : proc1 ')' '{' proc3 '}' '''

def p_proc1(p): # cleans previous local vars table
    '''proc1 : n_push_variable proc2
             | empty'''

def p_proc2(p):
    '''proc2 : ',' n_push_variable proc2
             | empty'''

def p_n_push_variable(p):
    '''n_push_variable :  datatype ID'''
    if not semantic_tool.insert_var(p[2], p[1].upper(), None): #adds new variable to table
        print "Variable " + p[2] + " already declared"
        raise SyntaxError
    else:
        print "Added " + str(p[2]) + str(p[1])

def p_proc3(p):
    '''proc3 : var proc3
             | proc4'''

def p_proc4(p):
    '''proc4 : statement proc4
             | empty'''

def p_vars(p):
    '''vars : var vars
            | var'''

def p_var(p):
    '''var : datatype var1 '''
    p[0] = p[1] + " " + str(p[2])
    for i in p[2].split():
        if not semantic_tool.insert_var(i, p[1].upper(), None): #adds new variable to table
            print "Variable " + i + " already declared"
            raise SyntaxError
        else:
            print "Added " + str(i) + p[1]

def p_var1(p):
    '''var1 : ID ',' var1
             | ID var2'''
    if p[2] == ',':
        p[0] = p[1] + " " + p[3]
    else:
        p[0] = p[1]

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
    '''assignment : assignment2 ASSIGNATOR n_quad_assign expression'''
    print("assignation for " + str(p[1]))
    quad_process_assign(["="])

def p_assignment2(p):
    '''assignment2 : ID'''
    search_result = semantic_tool.find_var(p[1])
    if search_result == None: # checks if var has been declared
        print "Undeclared variable " + p[1]
        raise SyntaxError
    else:
        operand_stack.push(search_result.name)
        type_stack.push(search_result.data_type)
        p[0] = p[1]
        return p[0]

def p_n_quad_assign(p):
    '''n_quad_assign : '''
    operator_stack.push('=')

#paso 1 del if-else, 2 del while
def exp_eval():
    exp_type = type_stack.pop()
    if(exp_type != 'BOOL'):
        print "Type mismatch"
        raise SyntaxError
    else:
        result = operand_stack.pop()

        #tener cuidado con cambiar el orden
        gen_quad('GOTOF', result, None, 'TO BE DEFINED')
        jump_stack.push( len(quadruples_list.list) - 1 )

def p_condition(p):
    '''condition : IF '(' expression n_while_2 ')' block condition1'''

def p_condition1(p):
    '''condition1 : ELSE n_if_2 block n_if_3
                  | n_if_3'''

def p_n_if_2(p):
    '''n_if_2 : '''
    goto_f = jump_stack.pop()
    fill_quad(goto_f, len(quadruples_list.list))

    gen_quad('GOTO', None, None, 'TO BE DEFINED')
    jump_stack.push(len(quadruples_list.list) - 1)

def p_n_if_3(p):
    '''n_if_3 : '''
    goto_f = jump_stack.pop()
    fill_quad(goto_f, len(quadruples_list.list))

def p_while(p):
    '''while : WHILE n_while_1 '(' expression ')' n_while_2 block n_while_3'''

def p_n_while_1(p):
    '''n_while_1 : '''
    jump_stack.push( len(quadruples_list.list) );

def p_n_while_2(p):
    '''n_while_2 : '''
    exp_eval()

def p_n_while_3(p):
    '''n_while_3 : '''
    end = jump_stack.pop()
    returns = jump_stack.pop()
    print("RRRRRRRRRRRRRRRR")
    print(end)
    print(returns)
    gen_quad('GOTO', None, None, returns)
    print("se llenara el " + str(end) )

    # revisar si esto esta bien
    # quadruples_list.list [ len(quadruples_list.list) ]
    # es la posicion que sigue (esta vacia)
    fill_quad(end, len(quadruples_list.list))

def p_input(p):
    '''input : READ '(' n_process_read input1 ')' '''

def p_input1(p):
    '''input1 : ',' n_process_read input1
              | empty'''

def p_n_process_read(p):
    '''n_process_read : ID'''


def p_output(p):
    '''output : PRINT '(' n_output_quad output1 ')' '''

def p_output1(p):
    '''output1 : ',' n_output_quad output1
               | empty'''

def p_n_output_quad(p):
    '''n_output_quad : expression'''
    gen_quad('PRINT', quadruples_list.current_temp(), None, None)


def p_function_call(p):
    '''function_call : ID '(' function_call1 ')' '''
    if semantic_tool.find_proc(p[1]) == None:
        print "Undeclared function " + p[1]
        raise SyntaxError

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

def p_relop(p):
    '''relop : '<'
             | '>'
             | NOT_EQ
             | EQ
             | LEQ
             | GEQ'''
    operator_stack.push(p[1])

def p_logop(p):
  '''logop : OR
           | AND'''
  print("LOGOP read")
  print(p[1])
  operator_stack.push(p[1])


######## Segunda Parte

def gen_quad(first, second, third, fourth):
    quadruple = Quadruple(first, second, third, fourth)
    quadruples_list.add(quadruple)

#receives index of quad and 4th argument of quadruple
def fill_quad(position, value):
    print("PPPPPPPPPPPPP")
    print(position)
    print(value)
    quadruples_list.list[position].result = value
    quadruples_list.list[position].print_quad()


def quad_process_unary(operator_list):
    operator = operator_stack.top()
    if not operator in operator_list:
        return

    operator_stack.pop()
    right_operand = operand_stack.pop()
    right_type = type_stack.pop()
    result_type = semantic_cube.accepts(right_type, None, operator)
    if result_type == False:
        print("Incompatible type " + right_type + " " + operator)
        raise SyntaxError
    else:
        result = quadruples_list.next_temp()
        gen_quad(operator, right_operand, None, result)
        operand_stack.push(result)
        type_stack.push(result_type)

def quad_process(operator_list):
    operator = operator_stack.top()
    if not operator in operator_list:
        print("Operator IN list")
        print(operator)
        print(operator_list)
        return

    operator_stack.pop()
    right_operand = operand_stack.pop()
    right_type = type_stack.pop()
    left_operand = operand_stack.pop()
    left_type = type_stack.pop()
    result_type = semantic_cube.accepts(right_type, left_type, operator)
    if result_type == False:
        print("Incompatible type " + right_type + " " + operator + " " + left_type)
        raise SyntaxError
    else:
        result = quadruples_list.next_temp()
        gen_quad(operator, left_operand, right_operand, result)
        operand_stack.push(result)
        type_stack.push(result_type)

def quad_process_assign(operator_list):
    operator = operator_stack.top()
    if not operator in operator_list:
        print("sale")
        print(operator)
        print(operator_list)
        return

    operator_stack.pop()
    right_operand = operand_stack.pop()
    right_type = type_stack.pop()
    left_operand = operand_stack.pop()
    left_type = type_stack.pop()
    result_type = semantic_cube.accepts(right_type, left_type, operator)
    if result_type == False:
        print("Incompatible type " + right_type + " " + operator + " " + left_type)
        raise SyntaxError
    else:
        gen_quad(operator, right_operand, None, left_operand)

def p_expression(p):
  '''expression : exp0 expression2'''

def p_expression2(p):
  '''expression2 : logop exp0 n_quad_logop expression2
                 | empty'''

def p_n_quad_logop(p):
    '''n_quad_logop : '''
    quad_process( ['&&', '||'] )

def p_exp0(p):
  '''exp0 : exp exp02'''

def p_exp02(p):
  '''exp02 : relop exp
           | empty'''
  if(len(p) == 3):
      quad_process( ['<', '>', ">=",  '<=', '==', '!=' ] )

def p_exp(p):
  '''exp : term exp2'''

def p_addsub(p):
  '''addsub : '+'
            | '-' '''
  operator_stack.push(p[1])

def p_muldiv(p):
  '''muldiv : '*'
            | '/' '''
  operator_stack.push(p[1])

def p_exp2(p):
  '''exp2 : addsub term n_quad_addsub exp2
          | empty'''

def p_term(p):
  '''term : term_not factor n_quad_muldiv term2'''

def p_n_quad_muldiv(p):
  '''n_quad_muldiv : '''
  quad_process( ['*','/'] )

def p_n_quad_addsub(p):
  '''n_quad_addsub : '''
  quad_process( ['+','-'] )

def p_term2(p):
  '''term2 : muldiv factor n_quad_muldiv term2
           | n_quad_not'''

def p_n_quad_not(p):
    '''n_quad_not : '''
    if operator_stack.top() != None:
        quad_process_unary(["!"])


def p_term_not(p):
  '''term_not : '!'
              | empty'''
  if(p[1] == '!'):
      operator_stack.push('!')

def p_factor(p):
  '''factor : '(' n_push_false_bottom expression ')' n_pop_false_bottom
            | varcte'''

def p_n_push_false_bottom(p):
    '''n_push_false_bottom : '''
    operator_stack.push('(')

def p_n_pop_false_bottom(p):
    '''n_pop_false_bottom : '''
    operator_stack.pop() #pending

def p_varcte(p):
  '''varcte : ID empty
            | varcte1'''
  print("LEnGTH " + str(len(p)) + " " + str(p[1]))
  if len(p) == 3:
      var = semantic_tool.find_var(p[1])
      if var == None: #checks variable is declared
        print "Undeclared variable " + p[1]
        raise SyntaxError
      else:
        operand_stack.push(var.value)
        type_stack.push(var.data_type)
  if p[1] != None:
      p[0] = p[1]

def p_varcte1(p):
    '''varcte1 : CTE_INT
               | CTE_FLOAT
               | CTE_BOOL
               | CTE_STRING
               | CTE_CHAR
               | function_call
               | map_access
               | map_operation
               | set_operation'''
    #ultimos 4 pendientes
    if p[1] in ["true", "false"]:
        operand_stack.push(p[1])
        type_stack.push("BOOL")


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
  p[0] = p[1]

def p_set_definition(p):
  '''set_definition : SET '<' datatype '>' '''
  p[0] = p[1] + p[2] + p[3] + p[4]

def p_block(p):
  '''block : '{' statement_aux '}' '''

def p_statement_aux(p):
  '''statement_aux : statement statement_aux
                   | empty'''

def p_main(p):
  '''main : MAIN n_clear_scope '{' vars_aux statement_aux '}' '''

def p_n_clear_scope(p):
  ''' n_clear_scope : '''
  if not semantic_tool.new_proc("MAIN", None):
      print "Function " + "MAIN" + " already declared"
      raise SyntaxError

def p_vars_aux(p):
  '''vars_aux : vars
              | empty'''

def p_map_definition(p):
  '''map_definition : MAP '<' datatype ',' datatype '>' '''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

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

f = open("test.txt", "r")
s = ""

for x in f:
  s = s + x

print(s)
res = parser.parse(s, debug=log)
print(res)

print("Operand stack")
operand_stack.print_stack()
print("Type stack")
type_stack.print_stack()
print("Quadruples list")
quadruples_list.print_quads()

print("Jump Stack")
jump_stack.print_stack()
