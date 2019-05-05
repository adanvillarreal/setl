import ply.lex as lex
import ply.yacc as yacc
import sys
from collections import namedtuple
import logging
from symbol_table import SymbolTable
from semantic_cube import SemanticCube
from config import *
from vm import *
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
    'OP',
    'OP_ARGS',
    'OR',
    'SET_MATH_ADDSUB',
    'SET_MATH_MULDIV'
]

t_ASSIGNATOR =  r':='
t_LEQ = r'<='
t_GEQ = r'>='
t_EQ = r'=='
t_NOT_EQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_OP_ARGS = r'(insert|remove|find)'
t_OP = r'(size|clear|domain|range)'
t_SET_MATH_ADDSUB = r'(\.\+|\.\-)'
t_SET_MATH_MULDIV = r'(\.\*)'


literals = ['+', '-', '*', '/', '(', ')', '[', ']', '{', '}','.', ',', ':', ';', '=', '>', '<', '!']

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
  'size' : 'OP',
  'clear' : 'OP',
  'insert' : 'OP_ARGS',
  'remove' : 'OP_ARGS',
  'find' : 'OP_ARGS',
  'domain': 'OP',
  'range': 'OP',
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
    semantic_tool.insert_to_constants(t.value, 'FLOAT')
    operand_stack.push(semantic_tool.memory_manager.find_constant(t.value, 'FLOAT'))
    type_stack.push("FLOAT")
    return t

def t_CTE_INT(t):
    r'\d+'
    semantic_tool.insert_to_constants(t.value, 'INT')
    operand_stack.push(semantic_tool.memory_manager.find_constant(t.value, 'INT'))
    type_stack.push("INT")
    return t

def t_CTE_STRING(t):
    r'\"[a-zA-Z0-9]*\"'
    semantic_tool.insert_to_constants(t.value, 'STRING')
    operand_stack.push(semantic_tool.memory_manager.find_constant(t.value, 'STRING'))
    type_stack.push("STRING")
    return t

def t_CTE_CHAR(t):
    r'\'[a-zA-Z0-9]\''
    semantic_tool.insert_to_constants(t.value, 'CHAR')
    operand_stack.push(semantic_tool.memory_manager.find_constant(t.value, 'CHAR'))
    type_stack.push("CHAR")
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t\n'

tokens = tokens + list(reserved.values())

# parser

start = "program"

def p_program(p):
    '''program : PROGRAM ID ';' n_main_quad program1'''

def p_n_main_quad(p):
    '''n_main_quad : '''
    gen_quad('GOTO', None, None, None)

def p_program1(p):
    '''program1 : var program1
                | program2'''

def p_program2(p):
    '''program2 : proc program2
                | main'''

def p_proc(p):
    '''proc : proca1 procA n_check_has_return
            | VOID proca2 procA
            | empty'''
    print ":function" + p[1]

def p_n_check_has_return(p):
    '''n_check_has_return : '''
    print "CHECK HAS RETURN RULE *********************************************"
    if not semantic_tool.get_has_return():
        print "No return statement in non-void function"
        raise ValueError
    operand = operand_stack.top()
    result_type = type_stack.top()
    result = quadruples_list.next_temp()
    glob_addr = semantic_tool.memory_manager.find_global(semantic_tool.current_proc, result_type)
    #gen_quad('===', operand, None, glob_addr) esta es la parte donde se guarda el valor de retorno en la var global,
    # no se si se genera un cuadruplo para esto o se hace en la maquina virtual cuando ve el return.

def p_proca2(p): #void function
    '''proca2 : ID '(' '''
    if not semantic_tool.new_proc(p[1], None):
        print "Function " + p[1] + " already declared"
        raise ValueError

def p_proca1(p): #non void function
    '''proca1 :  datatype ID '(' '''
    if not semantic_tool.new_proc(p[2], str(p[1]).upper()):
        print "Function " + p[2] + " already declared"
        raise ValueError

    p[0] = p[1] + p[2]

def p_procA(p):
    '''procA : proc1 ')' '{' proc3 '}' '''
    gen_quad('ENDPROC', None, None, None)
    semantic_tool.save_used_memory()


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
        raise ValueError
    else:
        if not semantic_tool.add_proc_param(p[1].upper()):
            raise ValueError
        print "Added " + str(p[2]) + str(p[1])

def p_proc3(p):
    '''proc3 : var proc3
             | n_quad_counter proc4'''

def p_n_quad_counter(p):
    '''n_quad_counter : '''
    semantic_tool.add_quad_counter(quadruples_list.current_quad_number())

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
            raise ValueError
        else:
            print "Lexer: Added " + str(i) + " " + p[1]

def p_var1(p):
    '''var1 : ID ',' var1
             | ID var2'''
    if p[2] == ',':
        p[0] = p[1] + " " + p[3]
    else:
        p[0] = p[1]

def p_var2(p):
    '''var2 : ';' '''

def p_assignment(p):
    '''assignment : assignment2 ASSIGNATOR n_quad_assign expression'''
    print("assignation for " + str(p[1]))
    quad_process_assign(["="])

def p_assignment2(p):
    '''assignment2 : ID'''
    search_result = semantic_tool.find_var(p[1])
    if search_result == None: # checks if var has been declared
        print "Undeclared variable " + p[1]
        raise ValueError
    else:
        operand_stack.push(search_result.address)
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
        raise ValueError
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
    gen_quad('GOTO', None, None, 'TO BE DEFINED')
    goto_f = jump_stack.pop()
    fill_quad(goto_f, len(quadruples_list.list))

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
    operand = operand_stack.pop()
    operand_type = type_stack.pop()
    if operand_type.startswith('SET'):
        operand_type = 'SET'
    gen_quad('PRINT', operand, operand_type, None)

def p_function_call(p):
    '''function_call : n_era_size function_call1 ')' '''
    function_called = semantic_tool.find_proc(semantic_tool.function_called)
    proc_quad = function_called.quadruple
    gen_quad('GOSUB', semantic_tool.function_called, proc_quad, None)
    if not function_called.return_type is None:
        result = quadruples_list.next_temp()
        temp_addr = semantic_tool.memory_manager.memories['temporary'].assign(function_called.return_type, result, 1)
        gen_quad('=', semantic_tool.memory_manager.find_global(function_called.name, function_called.return_type), None, temp_addr)
        operand_stack.push(temp_addr)
        type_stack.push(function_called.return_type)

def p_n_era_size(p):
    '''n_era_size : ID '(' '''
    if semantic_tool.find_proc(p[1]) == None:
        print "Undeclared function " + p[1]
        raise ValueError
    gen_quad('ERA', p[1], None, None)
    semantic_tool.function_called = p[1]
    semantic_tool.param_counter = 0

def p_function_call1(p):
    '''function_call1 : empty
                      | function_call2'''

def p_function_call2(p):
    '''function_call2 : n_verify_argument ',' n_add_one_to_counter function_call2
                      | n_verify_argument'''
    if not semantic_tool.verify_all_params_sent(semantic_tool.function_called, semantic_tool.param_counter):
        print "Missing arguments for " + semantic_tool.function_called
        raise ValueError

def p_n_add_one_to_counter(p):
    '''n_add_one_to_counter : '''
    semantic_tool.param_counter = semantic_tool.param_counter + 1

def p_n_verify_argument(p):
    '''n_verify_argument : expression'''
    operand = operand_stack.pop()
    operand_type = type_stack.pop()
    result = semantic_tool.verify_param(semantic_tool.function_called, semantic_tool.param_counter, operand_type)
    if result == None:
        print "*************&&&" + str(semantic_tool.param_counter)
        print "Wrong number of arguments for " + semantic_tool.function_called
        raise ValueError
    if not result:
        print "Parameter type mismatch for " + semantic_tool.function_called
        raise ValueError
    gen_quad("PARAMETER", operand, semantic_tool.param_counter, None)

def p_return(p):
    '''return : RETURN expression'''
    if(not semantic_tool.check_return_type(type_stack.top())): #este no funciona con top, no se porque.
        print "Wrong return type."
        raise ValueError
    else:
        semantic_tool.set_has_return(True)
        gen_quad("RETURN", operand_stack.top(), None, None )

def p_container_operation_arg(p):
    '''container_operation : ID '.' OP_ARGS '(' expression ')' '''
    print("CONTAINER OPERATION WITH ARGUMENT ", p[3])

    var = semantic_tool.find_var(p[1])
    if var == None: #checks variable is declared
      print "Undeclared variable " + p[1]
      raise ValueError
    elif '<' not in var.data_type:
      print "Var is not of type map or set"
      raise ValueError
    else:
      datatype = var.data_type
      operation = str(p[3]).upper()
      print "Operacion ", operation,  " en la variable ", var, " de tipo " , datatype

      operand_stack.push(var.address)
      operator_stack.push(operation) # push SIZE, DOMAIN or RANGE
      type_stack.push(datatype[0:3]) #set<xxx> map<xxx>
      quad_process_container_with_arg(['INSERT', 'FIND', 'REMOVE'], datatype)

def p_container_operation(p):
    '''container_operation : ID '.' OP '('  ')' '''
    print("CONTAINER OPERATION WITHOUT ARGUMENT ", p[3])

    var = semantic_tool.find_var(p[1])
    print var.data_type
    if var == None: #checks variable is declared
      print "Undeclared variable " + p[1]
      raise ValueError
    elif '<' not in var.data_type:
      print "Var is not of type map or set"
      raise ValueError
    else:
      datatype = var.data_type
      operation = str(p[3]).upper()
      print "Operacion ", operation,  " en la variable ", var, " de tipo " , datatype

      operand_stack.push(var.address)
      operator_stack.push(operation) # push SIZE, DOMAIN or RANGE
      type_stack.push(datatype[0:3]) #set<xxx> map<xxx>
      quad_process_container_without_arg(['SIZE', 'CLEAR', 'DOMAIN', 'RANGE'], datatype)

def p_statement(p):
    '''statement : statement1 ';'
                 | statement2 '''

def p_statement1(p):
    '''statement1 : assignment
                  | input
                  | output
                  | container_operation
                  | map_definition
                  | return
                  | map_assignment
                  | function_call'''

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
    print "eeeeeentraaa ", result_type
    if result_type == False:
        print("Incompatible type " + right_type + " " + operator)
        raise ValueError
    else:
        result = quadruples_list.next_temp()
        temp_addr = semantic_tool.memory_manager.memories['temporary'].assign(result_type, result, 1)
        gen_quad(operator, right_operand, None, temp_addr)
        operand_stack.push(temp_addr)
        type_stack.push(result_type)

def quad_process_container_without_arg(operator_list, datatype):
    operator = operator_stack.top()
    if not operator in operator_list:
        return

    operator_stack.pop()
    right_operand = operand_stack.pop() #set, map
    right_type = type_stack.pop()
    result_type = semantic_cube.accepts(right_type, None, operator)

    print "eeeeeentraaa a without argument", result_type
    if result_type == False:
        print("Incompatible type " + right_type + " " + operator)
        raise ValueError
    else:
        if result_type != "NONE": # aqui cae Size, Domain, Range
            print result_type + "***"
            result = quadruples_list.next_temp()
            temp_addr = semantic_tool.memory_manager.memories['temporary'].assign(result_type, result, 1)
            gen_quad(operator, right_operand, None, temp_addr)
            operand_stack.push(temp_addr)
            type_stack.push(result_type)
        else: # aqui cae Clear
            gen_quad(operator, right_operand, None, None)

def quad_process_container_with_arg(operator_list, datatype):
    operator = operator_stack.top()
    if not operator in operator_list:
        return

    operator_stack.pop()
    left_operand = operand_stack.pop() #set, map
    left_type = type_stack.pop()
    right_operand = operand_stack.pop() # operation argument
    right_type = type_stack.pop()
    result_type = semantic_cube.accepts(left_type, right_type, operator)

    if datatype.startswith('SET'):
        if datatype[4: -1] != right_type:
            print "Invalid argument type in set operation"
            print right_type + " argument in " + datatype[4: -1] + " container"
            raise ValueError

    print "eeeeeentraaa a with argument", result_type
    if result_type == False:
        print("Incompatible type " + left_type + " " + right_type + " " + operator)
        raise ValueError
    else:
        if result_type != "NONE": #aqui cae Find
            print result_type + "***"
            result = quadruples_list.next_temp()
            temp_addr = semantic_tool.memory_manager.memories['temporary'].assign(result_type, result, 1)
            gen_quad(operator, right_operand, left_operand, temp_addr)
            operand_stack.push(temp_addr)
            type_stack.push(result_type)
        else: #aqui cae Insert y Remove
            gen_quad(operator, left_operand, right_operand, None)

def quad_process(operator_list):
    operator = operator_stack.top()
    print operator , "quad process********************************************************"
    if not operator in operator_list:
        print("Operator NOT IN list")
        print(operator)
        print(operator_list)
        return

    operator_stack.pop()
    right_operand = operand_stack.pop()
    right_type = type_stack.pop()
    left_operand = operand_stack.pop()
    left_type = type_stack.pop()

    original_right_type = right_type
    original_left_type = left_type

    if right_type.startswith('SET'):
        right_type = 'SET'

    if left_type.startswith('SET'):
        left_type = 'SET'

    result_type = semantic_cube.accepts(right_type, left_type, operator)

    original_result_type = result_type

    if result_type == 'SET':
        result_type = original_left_type[4:-1]
        print result_type, "AAA"

    if result_type == False:
        print("Incompatible type " + right_type + " " + operator + " " + left_type)
        raise ValueError
    elif original_left_type != original_right_type:
        print("Incompatible type " + original_left_type + " " + operator + " " + original_right_type)
        raise ValueError
    else:
        result = quadruples_list.next_temp()
        size_needed = 1
        if original_result_type == 'SET':
            size_needed = 10
        temp_addr = semantic_tool.memory_manager.memories['temporary'].assign(result_type, result, size_needed)
        gen_quad(operator, left_operand, right_operand, temp_addr)
        operand_stack.push(temp_addr)
        type_stack.push(original_left_type)

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

    original_right_type = right_type
    original_left_type = left_type

    if right_type.startswith('SET'):
        right_type = 'SET'

    if left_type.startswith('SET'):
        left_type = 'SET'

    result_type = semantic_cube.accepts(right_type, left_type, operator)
    if result_type == False:
        print("Incompatible type " + right_type + " " + operator + " " + left_type)
        raise ValueError
    elif original_left_type != original_right_type:
        print("Incompatible type " + original_left_type + " " + operator + " " + original_right_type)
        raise ValueError
    else:
        gen_quad(operator, right_operand, left_type, left_operand)

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
            | '-'
            | SET_MATH_ADDSUB '''
  operator_stack.push(p[1])

def p_muldiv(p):
  '''muldiv : '*'
            | '/'
            | SET_MATH_MULDIV'''
  operator_stack.push(p[1])

def p_exp2(p):
  '''exp2 : addsub term n_quad_addsub exp2
          | empty'''

def p_term(p):
  '''term : term_not factor n_quad_muldiv term2'''

def p_n_quad_muldiv(p):
  '''n_quad_muldiv : '''
  quad_process( ['*','/', '.*'] )

def p_n_quad_addsub(p):
  '''n_quad_addsub : '''
  quad_process( ['+','-', '.+', '.-'] )

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
        raise ValueError
      else:
        print "puttingaskdnfasjdkfwiaeunf ", var
        operand_stack.push(var.address)
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
               | container_operation'''
    #ultimos 4 pendientes
    if p[1] in ["true", "false"]:
        semantic_tool.insert_to_constants(p[1], 'BOOL')
        operand_stack.push(semantic_tool.memory_manager.find_constant(p[1], 'BOOL'))
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
  '''main : MAIN n_clear_scope n_main_quad2 '{' vars_aux statement_aux '}' '''
  gen_quad('END', None, None, None)
  semantic_tool.save_used_memory()

def p_n_main_quad2(p):
    '''n_main_quad2 : '''
    fill_quad(0, len(quadruples_list.list))

def p_n_clear_scope(p):
  ''' n_clear_scope : '''
  if not semantic_tool.new_proc("MAIN", None):
      print "Function " + "MAIN" + " already declared"
      raise ValueError

def p_vars_aux(p):
  '''vars_aux : vars
              | empty'''

def p_map_definition(p):
  '''map_definition : MAP '<' datatype ',' datatype '>' '''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_map_access(p):
  '''map_access : ID '[' exp ']' '''

def p_map_assignment(p):
  '''map_assignment : map_access ASSIGNATOR exp'''

def p_empty(p):
    '''empty :'''

def p_error( p ):
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

    print('Syntax error in input! Parser State:{} {} . {}'
      .format(parser.state,
              stack_state_str,
              p))
    raise ValueError


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

f = open("test2.txt", "r")
s = ""

for x in f:
  s = s + x

print(s)
try:
    res = parser.parse(s, debug=log)
    print(res)
    print("END RES")

    print("Operand stack")
    operand_stack.print_stack()
    print("Type stack")
    type_stack.print_stack()
    print("Quadruples list")
    quadruples_list.print_quads()

    print("Jump Stack")
    jump_stack.print_stack()

    vm = VM(semantic_tool.functions, semantic_tool.memory_manager.memories['constant'].maps, semantic_tool.memory_manager.get_memory_size('global'), quadruples_list, [5000, 10000, 15000, 20000], 1000, semantic_tool.global_vars)
    vm.process_quad(0)
except:
    print("Something went wrong :(")
