
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programAND ASSIGNATOR BOOL CHAR CTE_BOOL CTE_BOOL CTE_BOOL CTE_CHAR CTE_FLOAT CTE_INT CTE_STRING ELSE EQ FLOAT GEQ ID IF INT LEQ MAIN MAP NOT_EQ OP OP OP OP OP OP_ARGS OP_ARGS OP_ARGS OP_ARGS OR PRINT PROGRAM READ RETURN SET SET_MATH_ADDSUB SET_MATH_MULDIV STRING VOID WHILEprogram : PROGRAM ID ';' n_main_quad program1n_main_quad : program1 : var program1\n                | program2program2 : proc program2\n                | mainproc : proca1 procA n_check_has_return\n            | VOID proca2 procA\n            | emptyn_check_has_return : proca2 : ID '(' proca1 :  datatype ID '(' procA : proc1 ')' '{' proc3 '}' proc1 : n_push_variable proc2\n             | emptyproc2 : ',' n_push_variable proc2\n             | emptyn_push_variable :  datatype IDproc3 : var proc3\n             | n_quad_counter proc4n_quad_counter : proc4 : statement proc4\n             | emptyvars : var vars\n            | varvar : datatype var1 var1 : ID ',' var1\n             | ID var2var2 : ';' assignment : assignment2 ASSIGNATOR n_quad_assign expressionassignment2 : IDn_quad_assign : condition : IF '(' expression n_while_2 ')' block condition1condition1 : ELSE n_if_2 block n_if_3\n                  | n_if_3n_if_2 : n_if_3 : while : WHILE n_while_1 '(' expression ')' n_while_2 block n_while_3n_while_1 : n_while_2 : n_while_3 : input : READ '(' n_process_read input1 ')' input1 : ',' n_process_read input1\n              | emptyn_process_read : IDoutput : PRINT '(' n_output_quad output1 ')' output1 : ',' n_output_quad output1\n               | emptyn_output_quad : expressionfunction_call : n_era_size function_call1 ')' n_era_size : ID '(' function_call1 : empty\n                      | function_call2function_call2 : n_verify_argument ',' n_add_one_to_counter function_call2\n                      | n_verify_argumentn_add_one_to_counter : n_verify_argument : expressionreturn : RETURN expressioncontainer_operation : ID '.' OP_ARGS '(' expression ')' container_operation : ID '.' OP '('  ')' statement : statement1 ';'\n                 | statement2 statement1 : assignment\n                  | input\n                  | output\n                  | container_operation\n                  | map_definition\n                  | return\n                  | map_assignment\n                  | function_callstatement2 : condition\n                  | whilerelop : '<'\n             | '>'\n             | NOT_EQ\n             | EQ\n             | LEQ\n             | GEQlogop : OR\n           | ANDexpression : exp0 expression2expression2 : logop exp0 n_quad_logop expression2\n                 | emptyn_quad_logop : exp0 : exp exp02exp02 : relop exp\n           | emptyexp : term exp2addsub : '+'\n            | '-'\n            | SET_MATH_ADDSUB muldiv : '*'\n            | '/'\n            | SET_MATH_MULDIVexp2 : addsub term n_quad_addsub exp2\n          | emptyterm : term_not factor n_quad_muldiv term2n_quad_muldiv : n_quad_addsub : term2 : muldiv factor n_quad_muldiv term2\n           | n_quad_notn_quad_not : term_not : '!'\n              | emptyfactor : '(' n_push_false_bottom expression ')' n_pop_false_bottom\n            | varcten_push_false_bottom : n_pop_false_bottom : varcte : ID empty\n            | varcte1varcte1 : CTE_INT\n               | CTE_FLOAT\n               | CTE_BOOL\n               | CTE_STRING\n               | CTE_CHAR\n               | function_call\n               | map_access\n               | container_operationfunctype : datatype\n               | VOIDdatatype : INT\n               | FLOAT\n               | BOOL\n               | STRING\n               | CHAR\n               | set_definition\n               | map_definitionset_definition : SET '<' datatype '>' block : '{' statement_aux '}' statement_aux : statement statement_aux\n                   | emptymain : MAIN n_clear_scope n_main_quad2 '{' vars_aux statement_aux '}' n_main_quad2 :  n_clear_scope : vars_aux : vars\n              | emptymap_definition : MAP '<' datatype ',' datatype '>' map_access : ID '[' exp ']' map_assignment : map_access ASSIGNATOR expempty :"
    
_lr_action_items = {'$end':([1,10,11,14,33,34,127,],[0,-1,-4,-6,-3,-5,-132,]),'OP_ARGS':([124,],[171,]),'RETURN':([37,51,54,57,60,62,64,65,69,70,71,72,83,87,93,96,101,103,117,220,221,224,226,228,230,231,233,234,],[-26,-28,-29,-21,-27,-140,74,-21,-135,74,-25,-136,74,-62,-71,-72,74,-24,-61,74,-37,-41,-35,-33,-38,-129,-37,-34,]),'READ':([37,51,54,57,60,62,64,65,69,70,71,72,83,87,93,96,101,103,117,220,221,224,226,228,230,231,233,234,],[-26,-28,-29,-21,-27,-140,75,-21,-135,75,-25,-136,75,-62,-71,-72,75,-24,-61,75,-37,-41,-35,-33,-38,-129,-37,-34,]),'VOID':([4,5,13,15,16,32,37,41,48,51,54,60,73,],[-2,6,6,6,-9,-10,-26,-8,-7,-28,-29,-27,-13,]),'CHAR':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,52,54,57,59,60,62,65,71,73,],[-2,8,8,8,8,-9,8,8,-10,8,-26,-11,-8,8,-7,-28,-12,-29,8,8,-27,8,8,8,-13,]),'ASSIGNATOR':([81,82,92,192,],[114,115,-31,-138,]),'WHILE':([37,51,54,57,60,62,64,65,69,70,71,72,83,87,93,96,101,103,117,220,221,224,226,228,230,231,233,234,],[-26,-28,-29,-21,-27,-140,78,-21,-135,78,-25,-136,78,-62,-71,-72,78,-24,-61,78,-37,-41,-35,-33,-38,-129,-37,-34,]),'PROGRAM':([0,],[2,]),'PRINT':([37,51,54,57,60,62,64,65,69,70,71,72,83,87,93,96,101,103,117,220,221,224,226,228,230,231,233,234,],[-26,-28,-29,-21,-27,-140,79,-21,-135,79,-25,-136,79,-62,-71,-72,79,-24,-61,79,-37,-41,-35,-33,-38,-129,-37,-34,]),'SET_MATH_MULDIV':([129,130,131,132,134,135,136,137,138,139,140,141,169,176,177,192,210,212,213,219,222,223,],[-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-50,195,-109,-138,-60,-108,-98,-59,-105,195,]),'!':([74,89,113,114,115,123,125,126,133,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,175,186,189,190,],[107,107,107,107,-32,-51,107,107,-107,-89,-90,107,-91,-80,107,-79,-78,107,-75,-77,-76,-73,-74,107,107,-56,107,107,107,107,]),'GEQ':([105,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,169,176,177,178,192,196,198,201,210,212,213,214,219,222,223,229,],[-140,153,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-50,-102,-109,-99,-138,-97,-101,-140,-60,-108,-98,-95,-59,-105,-102,-100,]),'SET':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,52,54,57,59,60,62,65,71,73,],[-2,9,9,9,9,-9,9,9,-10,9,-26,-11,-8,9,-7,-28,-12,-29,9,9,-27,9,9,9,-13,]),')':([12,26,28,29,30,40,45,46,47,52,58,67,89,105,106,108,118,119,120,121,122,123,129,130,131,132,134,135,136,137,138,139,140,141,142,147,150,152,157,160,162,163,165,166,169,174,176,177,178,179,180,181,183,184,185,187,191,192,193,194,196,198,201,202,204,207,208,209,210,212,213,214,215,216,218,219,222,223,229,],[-140,-140,43,-15,-140,-11,-17,-14,-18,-12,-140,-16,-140,-140,-140,-140,-53,169,-57,-55,-52,-51,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-81,-83,-85,-87,-140,-45,-140,-49,-50,-40,-102,-109,-99,-84,-86,203,-44,205,206,-48,210,-138,211,212,-97,-101,-140,-140,-140,-140,-54,219,-60,-108,-98,-95,-82,-43,-47,-59,-105,-102,-100,]),'(':([25,38,49,74,75,78,79,89,92,94,104,107,110,112,113,114,115,122,123,125,126,133,138,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,171,172,175,186,189,190,195,197,199,200,],[40,52,52,-140,111,-39,113,-140,123,126,133,-103,-104,164,-140,-140,-32,-104,-51,-140,-140,-107,123,-89,-90,-140,-91,-80,-140,-79,-78,-140,-75,-77,-76,-73,-74,-140,-140,-56,190,191,-140,-140,-140,-140,-94,-92,-93,133,]),'+':([105,129,130,131,132,134,135,136,137,138,139,140,141,169,176,177,178,192,196,198,201,210,212,213,219,222,223,229,],[143,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-50,-102,-109,-99,-138,-97,-101,143,-60,-108,-98,-59,-105,-102,-100,]),'*':([129,130,131,132,134,135,136,137,138,139,140,141,169,176,177,192,210,212,213,219,222,223,],[-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-50,197,-109,-138,-60,-108,-98,-59,-105,197,]),'-':([105,129,130,131,132,134,135,136,137,138,139,140,141,169,176,177,178,192,196,198,201,210,212,213,219,222,223,229,],[144,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-50,-102,-109,-99,-138,-97,-101,144,-60,-108,-98,-59,-105,-102,-100,]),',':([7,8,17,19,21,22,23,30,38,47,50,56,58,61,99,105,106,108,120,121,129,130,131,132,134,135,136,137,138,139,140,141,142,147,150,152,157,160,162,163,165,166,169,176,177,178,179,180,192,196,198,201,202,204,207,210,212,213,214,215,219,222,223,229,],[-127,-125,-124,-126,-122,-121,-123,44,53,-18,59,-128,44,53,-137,-140,-140,-140,-57,170,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-81,-83,-85,-87,182,-45,186,-49,-50,-102,-109,-99,-84,-86,-138,-97,-101,-140,-140,182,186,-60,-108,-98,-95,-82,-59,-105,-102,-100,]),'/':([129,130,131,132,134,135,136,137,138,139,140,141,169,176,177,192,210,212,213,219,222,223,],[-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-50,199,-109,-138,-60,-108,-98,-59,-105,199,]),'.':([92,138,],[124,124,]),'CTE_CHAR':([74,89,104,107,110,113,114,115,122,123,125,126,133,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,175,186,189,190,195,197,199,200,],[-140,-140,135,-103,-104,-140,-140,-32,-104,-51,-140,-140,-107,-89,-90,-140,-91,-80,-140,-79,-78,-140,-75,-77,-76,-73,-74,-140,-140,-56,-140,-140,-140,-140,-94,-92,-93,135,]),';':([3,38,61,76,77,84,86,88,90,91,95,97,99,105,106,108,109,129,130,131,132,134,135,136,137,138,139,140,141,142,147,150,152,157,160,167,169,176,177,178,179,180,188,192,196,198,201,202,203,206,210,212,213,214,215,219,222,223,229,],[4,54,54,-67,-70,-64,-68,117,-66,-63,-69,-65,-137,-140,-140,-140,-58,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-81,-83,-85,-87,-139,-50,-102,-109,-99,-84,-86,-30,-138,-97,-101,-140,-140,-42,-46,-60,-108,-98,-95,-82,-59,-105,-102,-100,]),'<':([9,18,105,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,169,176,177,178,192,196,198,201,210,212,213,214,219,222,223,229,],[27,36,-140,159,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-50,-102,-109,-99,-138,-97,-101,-140,-60,-108,-98,-95,-59,-105,-102,-100,]),'>':([7,8,17,19,21,22,23,42,56,68,99,105,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,169,176,177,178,192,196,198,201,210,212,213,214,219,222,223,229,],[-127,-125,-124,-126,-122,-121,-123,56,-128,99,-137,-140,161,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-50,-102,-109,-99,-138,-97,-101,-140,-60,-108,-98,-95,-59,-105,-102,-100,]),'CTE_STRING':([74,89,104,107,110,113,114,115,122,123,125,126,133,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,175,186,189,190,195,197,199,200,],[-140,-140,141,-103,-104,-140,-140,-32,-104,-51,-140,-140,-107,-89,-90,-140,-91,-80,-140,-79,-78,-140,-75,-77,-76,-73,-74,-140,-140,-56,-140,-140,-140,-140,-94,-92,-93,141,]),'STRING':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,52,54,57,59,60,62,65,71,73,],[-2,17,17,17,17,-9,17,17,-10,17,-26,-11,-8,17,-7,-28,-12,-29,17,17,-27,17,17,17,-13,]),'NOT_EQ':([105,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,169,176,177,178,192,196,198,201,210,212,213,214,219,222,223,229,],[-140,155,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-50,-102,-109,-99,-138,-97,-101,-140,-60,-108,-98,-95,-59,-105,-102,-100,]),'ELSE':([221,231,],[227,-129,]),'[':([92,138,],[125,125,]),'CTE_INT':([74,89,104,107,110,113,114,115,122,123,125,126,133,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,175,186,189,190,195,197,199,200,],[-140,-140,137,-103,-104,-140,-140,-32,-104,-51,-140,-140,-107,-89,-90,-140,-91,-80,-140,-79,-78,-140,-75,-77,-76,-73,-74,-140,-140,-56,-140,-140,-140,-140,-94,-92,-93,137,]),']':([105,129,130,131,132,134,135,136,137,138,139,140,141,142,147,169,173,176,177,178,192,196,198,201,210,212,213,214,219,222,223,229,],[-140,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-50,192,-102,-109,-99,-138,-97,-101,-140,-60,-108,-98,-95,-59,-105,-102,-100,]),'ID':([2,6,7,8,17,19,20,21,22,23,31,35,37,51,53,54,56,57,60,62,64,65,66,69,70,71,72,74,83,87,89,93,96,99,101,103,104,107,110,111,113,114,115,117,122,123,125,126,133,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,175,182,186,189,190,195,197,199,200,220,221,224,226,228,230,231,233,234,],[3,25,-127,-125,-124,-126,38,-122,-121,-123,47,49,-26,-28,61,-29,-128,-21,-27,-140,92,-21,61,-135,92,-25,-136,-140,92,-62,-140,-71,-72,-137,92,-24,138,-103,-104,163,-140,-140,-32,-61,-104,-51,-140,-140,-107,-89,-90,-140,-91,-80,-140,-79,-78,-140,-75,-77,-76,-73,-74,-140,-140,-56,-140,163,-140,-140,-140,-94,-92,-93,138,92,-37,-41,-35,-33,-38,-129,-37,-34,]),'IF':([37,51,54,57,60,62,64,65,69,70,71,72,83,87,93,96,101,103,117,220,221,224,226,228,230,231,233,234,],[-26,-28,-29,-21,-27,-140,94,-21,-135,94,-25,-136,94,-62,-71,-72,94,-24,-61,94,-37,-41,-35,-33,-38,-129,-37,-34,]),'AND':([105,106,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,157,160,169,176,177,178,179,180,192,196,198,201,202,210,212,213,214,219,222,223,229,],[-140,148,-140,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-85,-87,-50,-102,-109,-99,-84,-86,-138,-97,-101,-140,148,-60,-108,-98,-95,-59,-105,-102,-100,]),'MAP':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,52,54,57,59,60,62,64,65,69,70,71,72,73,83,87,93,96,101,103,117,220,221,224,226,228,230,231,233,234,],[-2,18,18,18,18,-9,18,18,-10,18,-26,-11,-8,18,-7,-28,-12,-29,18,18,-27,18,18,18,-135,18,18,-136,-13,18,-62,-71,-72,18,-24,-61,18,-37,-41,-35,-33,-38,-129,-37,-34,]),'EQ':([105,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,169,176,177,178,192,196,198,201,210,212,213,214,219,222,223,229,],[-140,158,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-50,-102,-109,-99,-138,-97,-101,-140,-60,-108,-98,-95,-59,-105,-102,-100,]),'INT':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,52,54,57,59,60,62,65,71,73,],[-2,22,22,22,22,-9,22,22,-10,22,-26,-11,-8,22,-7,-28,-12,-29,22,22,-27,22,22,22,-13,]),'SET_MATH_ADDSUB':([105,129,130,131,132,134,135,136,137,138,139,140,141,169,176,177,178,192,196,198,201,210,212,213,219,222,223,229,],[146,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-50,-102,-109,-99,-138,-97,-101,146,-60,-108,-98,-59,-105,-102,-100,]),'FLOAT':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,52,54,57,59,60,62,65,71,73,],[-2,21,21,21,21,-9,21,21,-10,21,-26,-11,-8,21,-7,-28,-12,-29,21,21,-27,21,21,21,-13,]),'CTE_FLOAT':([74,89,104,107,110,113,114,115,122,123,125,126,133,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,175,186,189,190,195,197,199,200,],[-140,-140,139,-103,-104,-140,-140,-32,-104,-51,-140,-140,-107,-89,-90,-140,-91,-80,-140,-79,-78,-140,-75,-77,-76,-73,-74,-140,-140,-56,-140,-140,-140,-140,-94,-92,-93,139,]),'CTE_BOOL':([74,89,104,107,110,113,114,115,122,123,125,126,133,143,144,145,146,148,149,151,153,154,155,156,158,159,161,164,168,170,175,186,189,190,195,197,199,200,],[-140,-140,140,-103,-104,-140,-140,-32,-104,-51,-140,-140,-107,-89,-90,-140,-91,-80,-140,-79,-78,-140,-75,-77,-76,-73,-74,-140,-140,-56,-140,-140,-140,-140,-94,-92,-93,140,]),'LEQ':([105,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,169,176,177,178,192,196,198,201,210,212,213,214,219,222,223,229,],[-140,156,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-50,-102,-109,-99,-138,-97,-101,-140,-60,-108,-98,-95,-59,-105,-102,-100,]),'BOOL':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,52,54,57,59,60,62,65,71,73,],[-2,23,23,23,23,-9,23,23,-10,23,-26,-11,-8,23,-7,-28,-12,-29,23,23,-27,23,23,23,-13,]),'{':([24,39,43,55,205,211,217,227,232,],[-134,-133,57,62,-40,220,220,-36,220,]),'MAIN':([4,5,13,15,16,32,37,41,48,51,54,60,73,],[-2,24,24,24,-9,-10,-26,-8,-7,-28,-29,-27,-13,]),'}':([37,51,54,57,60,62,63,64,65,69,70,71,72,80,83,85,87,93,96,98,100,101,102,103,116,117,128,220,221,224,225,226,228,230,231,233,234,],[-26,-28,-29,-21,-27,-140,73,-140,-21,-135,-140,-25,-136,-20,-140,-23,-62,-71,-72,-19,127,-140,-131,-24,-22,-61,-130,-140,-37,-41,231,-35,-33,-38,-129,-37,-34,]),'OR':([105,106,108,129,130,131,132,134,135,136,137,138,139,140,141,142,147,157,160,169,176,177,178,179,180,192,196,198,201,202,210,212,213,214,219,222,223,229,],[-140,151,-140,-116,-110,-106,-117,-98,-115,-118,-111,-140,-112,-113,-114,-88,-96,-85,-87,-50,-102,-109,-99,-84,-86,-138,-97,-101,-140,151,-60,-108,-98,-95,-59,-105,-102,-100,]),'OP':([124,],[172,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'n_quad_muldiv':([134,213,],[176,223,]),'input1':([162,204,],[181,216,]),'n_add_one_to_counter':([170,],[189,]),'term2':([176,223,],[196,229,]),'vars':([62,71,],[69,103,]),'n_clear_scope':([24,],[39,]),'output1':([165,207,],[185,218,]),'map_definition':([5,12,13,15,26,27,36,44,57,59,62,64,65,70,71,83,101,220,],[7,7,7,7,7,7,7,7,7,7,7,76,7,76,7,76,76,76,]),'n_process_read':([111,182,],[162,204,]),'function_call':([64,70,83,101,104,200,220,],[77,77,77,77,129,129,77,]),'n_if_2':([227,],[232,]),'n_while_1':([78,],[112,]),'vars_aux':([62,],[70,]),'n_check_has_return':([32,],[48,]),'n_while_2':([174,205,],[193,217,]),'proc4':([64,83,],[80,116,]),'return':([64,70,83,101,220,],[86,86,86,86,86,]),'addsub':([105,201,],[145,145,]),'proc1':([12,26,],[28,28,]),'proc3':([57,65,],[63,98,]),'proc2':([30,58,],[46,67,]),'n_while_3':([224,],[230,]),'program1':([5,13,],[10,33,]),'program2':([5,13,15,],[11,11,34,]),'n_era_size':([64,70,83,101,104,200,220,],[89,89,89,89,89,89,89,]),'muldiv':([176,223,],[200,200,]),'exp2':([105,201,],[142,214,]),'n_main_quad2':([39,],[55,]),'exp0':([74,89,113,126,149,164,168,175,186,189,190,],[106,106,106,106,179,106,106,106,106,106,106,]),'proca1':([5,13,15,],[12,12,12,]),'n_pop_false_bottom':([212,],[222,]),'proca2':([6,],[26,]),'assignment2':([64,70,83,101,220,],[82,82,82,82,82,]),'program':([0,],[1,]),'n_output_quad':([113,186,],[165,207,]),'statement':([64,70,83,101,220,],[83,101,83,101,101,]),'n_quad_counter':([57,65,],[64,64,]),'var':([5,13,57,62,65,71,],[13,13,65,71,65,71,]),'input':([64,70,83,101,220,],[84,84,84,84,84,]),'main':([5,13,15,],[14,14,14,]),'proc':([5,13,15,],[15,15,15,]),'n_verify_argument':([89,189,],[121,121,]),'empty':([5,12,13,15,26,30,58,62,64,70,74,83,89,101,105,106,108,113,114,125,126,138,145,149,154,162,164,165,168,175,186,189,190,201,202,204,207,220,],[16,29,16,16,29,45,45,72,85,102,110,85,122,102,147,152,160,110,110,110,110,177,110,110,110,183,110,187,110,110,110,110,110,147,152,183,187,102,]),'condition1':([221,],[228,]),'term_not':([74,89,113,114,125,126,145,149,154,164,168,175,186,189,190,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'var1':([20,53,66,],[37,60,37,]),'statement2':([64,70,83,101,220,],[87,87,87,87,87,]),'statement1':([64,70,83,101,220,],[88,88,88,88,88,]),'var2':([38,61,],[51,51,]),'container_operation':([64,70,83,101,104,200,220,],[90,90,90,90,136,136,90,]),'assignment':([64,70,83,101,220,],[91,91,91,91,91,]),'factor':([104,200,],[134,213,]),'logop':([106,202,],[149,149,]),'n_quad_assign':([115,],[168,]),'n_push_false_bottom':([133,],[175,]),'map_access':([64,70,83,101,104,200,220,],[81,81,81,81,132,132,81,]),'n_quad_logop':([179,],[202,]),'n_main_quad':([4,],[5,]),'expression2':([106,202,],[150,215,]),'n_if_3':([221,233,],[226,234,]),'condition':([64,70,83,101,220,],[93,93,93,93,93,]),'varcte':([104,200,],[131,131,]),'term':([74,89,113,114,125,126,145,149,154,164,168,175,186,189,190,],[105,105,105,105,105,105,178,105,105,105,105,105,105,105,105,]),'n_push_variable':([12,26,44,],[30,30,58,]),'set_definition':([5,12,13,15,26,27,36,44,57,59,62,65,71,],[19,19,19,19,19,19,19,19,19,19,19,19,19,]),'datatype':([5,12,13,15,26,27,36,44,57,59,62,65,71,],[20,31,20,35,31,42,50,31,66,68,66,66,66,]),'varcte1':([104,200,],[130,130,]),'relop':([108,],[154,]),'procA':([12,26,],[32,41,]),'function_call1':([89,],[119,]),'map_assignment':([64,70,83,101,220,],[95,95,95,95,95,]),'while':([64,70,83,101,220,],[96,96,96,96,96,]),'function_call2':([89,189,],[118,208,]),'exp':([74,89,113,114,125,126,149,154,164,168,175,186,189,190,],[108,108,108,167,173,108,108,180,108,108,108,108,108,108,]),'n_quad_addsub':([178,],[201,]),'output':([64,70,83,101,220,],[97,97,97,97,97,]),'exp02':([108,],[157,]),'n_quad_not':([176,223,],[198,198,]),'expression':([74,89,113,126,164,168,175,186,189,190,],[109,120,166,174,184,188,194,166,120,209,]),'block':([211,217,232,],[221,224,233,]),'statement_aux':([70,101,220,],[100,128,225,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID ; n_main_quad program1','program',5,'p_program','lexer.py',137),
  ('n_main_quad -> <empty>','n_main_quad',0,'p_n_main_quad','lexer.py',141),
  ('program1 -> var program1','program1',2,'p_program1','lexer.py',145),
  ('program1 -> program2','program1',1,'p_program1','lexer.py',146),
  ('program2 -> proc program2','program2',2,'p_program2','lexer.py',149),
  ('program2 -> main','program2',1,'p_program2','lexer.py',150),
  ('proc -> proca1 procA n_check_has_return','proc',3,'p_proc','lexer.py',153),
  ('proc -> VOID proca2 procA','proc',3,'p_proc','lexer.py',154),
  ('proc -> empty','proc',1,'p_proc','lexer.py',155),
  ('n_check_has_return -> <empty>','n_check_has_return',0,'p_n_check_has_return','lexer.py',159),
  ('proca2 -> ID (','proca2',2,'p_proca2','lexer.py',172),
  ('proca1 -> datatype ID (','proca1',3,'p_proca1','lexer.py',178),
  ('procA -> proc1 ) { proc3 }','procA',5,'p_procA','lexer.py',186),
  ('proc1 -> n_push_variable proc2','proc1',2,'p_proc1','lexer.py',191),
  ('proc1 -> empty','proc1',1,'p_proc1','lexer.py',192),
  ('proc2 -> , n_push_variable proc2','proc2',3,'p_proc2','lexer.py',195),
  ('proc2 -> empty','proc2',1,'p_proc2','lexer.py',196),
  ('n_push_variable -> datatype ID','n_push_variable',2,'p_n_push_variable','lexer.py',199),
  ('proc3 -> var proc3','proc3',2,'p_proc3','lexer.py',209),
  ('proc3 -> n_quad_counter proc4','proc3',2,'p_proc3','lexer.py',210),
  ('n_quad_counter -> <empty>','n_quad_counter',0,'p_n_quad_counter','lexer.py',213),
  ('proc4 -> statement proc4','proc4',2,'p_proc4','lexer.py',217),
  ('proc4 -> empty','proc4',1,'p_proc4','lexer.py',218),
  ('vars -> var vars','vars',2,'p_vars','lexer.py',221),
  ('vars -> var','vars',1,'p_vars','lexer.py',222),
  ('var -> datatype var1','var',2,'p_var','lexer.py',225),
  ('var1 -> ID , var1','var1',3,'p_var1','lexer.py',235),
  ('var1 -> ID var2','var1',2,'p_var1','lexer.py',236),
  ('var2 -> ;','var2',1,'p_var2','lexer.py',243),
  ('assignment -> assignment2 ASSIGNATOR n_quad_assign expression','assignment',4,'p_assignment','lexer.py',246),
  ('assignment2 -> ID','assignment2',1,'p_assignment2','lexer.py',251),
  ('n_quad_assign -> <empty>','n_quad_assign',0,'p_n_quad_assign','lexer.py',263),
  ('condition -> IF ( expression n_while_2 ) block condition1','condition',7,'p_condition','lexer.py',280),
  ('condition1 -> ELSE n_if_2 block n_if_3','condition1',4,'p_condition1','lexer.py',283),
  ('condition1 -> n_if_3','condition1',1,'p_condition1','lexer.py',284),
  ('n_if_2 -> <empty>','n_if_2',0,'p_n_if_2','lexer.py',287),
  ('n_if_3 -> <empty>','n_if_3',0,'p_n_if_3','lexer.py',295),
  ('while -> WHILE n_while_1 ( expression ) n_while_2 block n_while_3','while',8,'p_while','lexer.py',300),
  ('n_while_1 -> <empty>','n_while_1',0,'p_n_while_1','lexer.py',303),
  ('n_while_2 -> <empty>','n_while_2',0,'p_n_while_2','lexer.py',307),
  ('n_while_3 -> <empty>','n_while_3',0,'p_n_while_3','lexer.py',311),
  ('input -> READ ( n_process_read input1 )','input',5,'p_input','lexer.py',326),
  ('input1 -> , n_process_read input1','input1',3,'p_input1','lexer.py',329),
  ('input1 -> empty','input1',1,'p_input1','lexer.py',330),
  ('n_process_read -> ID','n_process_read',1,'p_n_process_read','lexer.py',333),
  ('output -> PRINT ( n_output_quad output1 )','output',5,'p_output','lexer.py',336),
  ('output1 -> , n_output_quad output1','output1',3,'p_output1','lexer.py',339),
  ('output1 -> empty','output1',1,'p_output1','lexer.py',340),
  ('n_output_quad -> expression','n_output_quad',1,'p_n_output_quad','lexer.py',343),
  ('function_call -> n_era_size function_call1 )','function_call',3,'p_function_call','lexer.py',349),
  ('n_era_size -> ID (','n_era_size',2,'p_n_era_size','lexer.py',361),
  ('function_call1 -> empty','function_call1',1,'p_function_call1','lexer.py',370),
  ('function_call1 -> function_call2','function_call1',1,'p_function_call1','lexer.py',371),
  ('function_call2 -> n_verify_argument , n_add_one_to_counter function_call2','function_call2',4,'p_function_call2','lexer.py',374),
  ('function_call2 -> n_verify_argument','function_call2',1,'p_function_call2','lexer.py',375),
  ('n_add_one_to_counter -> <empty>','n_add_one_to_counter',0,'p_n_add_one_to_counter','lexer.py',381),
  ('n_verify_argument -> expression','n_verify_argument',1,'p_n_verify_argument','lexer.py',385),
  ('return -> RETURN expression','return',2,'p_return','lexer.py',399),
  ('container_operation -> ID . OP_ARGS ( expression )','container_operation',6,'p_container_operation_arg','lexer.py',408),
  ('container_operation -> ID . OP ( )','container_operation',5,'p_container_operation','lexer.py',429),
  ('statement -> statement1 ;','statement',2,'p_statement','lexer.py',451),
  ('statement -> statement2','statement',1,'p_statement','lexer.py',452),
  ('statement1 -> assignment','statement1',1,'p_statement1','lexer.py',455),
  ('statement1 -> input','statement1',1,'p_statement1','lexer.py',456),
  ('statement1 -> output','statement1',1,'p_statement1','lexer.py',457),
  ('statement1 -> container_operation','statement1',1,'p_statement1','lexer.py',458),
  ('statement1 -> map_definition','statement1',1,'p_statement1','lexer.py',459),
  ('statement1 -> return','statement1',1,'p_statement1','lexer.py',460),
  ('statement1 -> map_assignment','statement1',1,'p_statement1','lexer.py',461),
  ('statement1 -> function_call','statement1',1,'p_statement1','lexer.py',462),
  ('statement2 -> condition','statement2',1,'p_statement2','lexer.py',465),
  ('statement2 -> while','statement2',1,'p_statement2','lexer.py',466),
  ('relop -> <','relop',1,'p_relop','lexer.py',469),
  ('relop -> >','relop',1,'p_relop','lexer.py',470),
  ('relop -> NOT_EQ','relop',1,'p_relop','lexer.py',471),
  ('relop -> EQ','relop',1,'p_relop','lexer.py',472),
  ('relop -> LEQ','relop',1,'p_relop','lexer.py',473),
  ('relop -> GEQ','relop',1,'p_relop','lexer.py',474),
  ('logop -> OR','logop',1,'p_logop','lexer.py',478),
  ('logop -> AND','logop',1,'p_logop','lexer.py',479),
  ('expression -> exp0 expression2','expression',2,'p_expression','lexer.py',658),
  ('expression2 -> logop exp0 n_quad_logop expression2','expression2',4,'p_expression2','lexer.py',661),
  ('expression2 -> empty','expression2',1,'p_expression2','lexer.py',662),
  ('n_quad_logop -> <empty>','n_quad_logop',0,'p_n_quad_logop','lexer.py',665),
  ('exp0 -> exp exp02','exp0',2,'p_exp0','lexer.py',669),
  ('exp02 -> relop exp','exp02',2,'p_exp02','lexer.py',672),
  ('exp02 -> empty','exp02',1,'p_exp02','lexer.py',673),
  ('exp -> term exp2','exp',2,'p_exp','lexer.py',678),
  ('addsub -> +','addsub',1,'p_addsub','lexer.py',681),
  ('addsub -> -','addsub',1,'p_addsub','lexer.py',682),
  ('addsub -> SET_MATH_ADDSUB','addsub',1,'p_addsub','lexer.py',683),
  ('muldiv -> *','muldiv',1,'p_muldiv','lexer.py',687),
  ('muldiv -> /','muldiv',1,'p_muldiv','lexer.py',688),
  ('muldiv -> SET_MATH_MULDIV','muldiv',1,'p_muldiv','lexer.py',689),
  ('exp2 -> addsub term n_quad_addsub exp2','exp2',4,'p_exp2','lexer.py',693),
  ('exp2 -> empty','exp2',1,'p_exp2','lexer.py',694),
  ('term -> term_not factor n_quad_muldiv term2','term',4,'p_term','lexer.py',697),
  ('n_quad_muldiv -> <empty>','n_quad_muldiv',0,'p_n_quad_muldiv','lexer.py',700),
  ('n_quad_addsub -> <empty>','n_quad_addsub',0,'p_n_quad_addsub','lexer.py',704),
  ('term2 -> muldiv factor n_quad_muldiv term2','term2',4,'p_term2','lexer.py',708),
  ('term2 -> n_quad_not','term2',1,'p_term2','lexer.py',709),
  ('n_quad_not -> <empty>','n_quad_not',0,'p_n_quad_not','lexer.py',712),
  ('term_not -> !','term_not',1,'p_term_not','lexer.py',717),
  ('term_not -> empty','term_not',1,'p_term_not','lexer.py',718),
  ('factor -> ( n_push_false_bottom expression ) n_pop_false_bottom','factor',5,'p_factor','lexer.py',723),
  ('factor -> varcte','factor',1,'p_factor','lexer.py',724),
  ('n_push_false_bottom -> <empty>','n_push_false_bottom',0,'p_n_push_false_bottom','lexer.py',727),
  ('n_pop_false_bottom -> <empty>','n_pop_false_bottom',0,'p_n_pop_false_bottom','lexer.py',731),
  ('varcte -> ID empty','varcte',2,'p_varcte','lexer.py',735),
  ('varcte -> varcte1','varcte',1,'p_varcte','lexer.py',736),
  ('varcte1 -> CTE_INT','varcte1',1,'p_varcte1','lexer.py',751),
  ('varcte1 -> CTE_FLOAT','varcte1',1,'p_varcte1','lexer.py',752),
  ('varcte1 -> CTE_BOOL','varcte1',1,'p_varcte1','lexer.py',753),
  ('varcte1 -> CTE_STRING','varcte1',1,'p_varcte1','lexer.py',754),
  ('varcte1 -> CTE_CHAR','varcte1',1,'p_varcte1','lexer.py',755),
  ('varcte1 -> function_call','varcte1',1,'p_varcte1','lexer.py',756),
  ('varcte1 -> map_access','varcte1',1,'p_varcte1','lexer.py',757),
  ('varcte1 -> container_operation','varcte1',1,'p_varcte1','lexer.py',758),
  ('functype -> datatype','functype',1,'p_functype','lexer.py',767),
  ('functype -> VOID','functype',1,'p_functype','lexer.py',768),
  ('datatype -> INT','datatype',1,'p_datatype','lexer.py',771),
  ('datatype -> FLOAT','datatype',1,'p_datatype','lexer.py',772),
  ('datatype -> BOOL','datatype',1,'p_datatype','lexer.py',773),
  ('datatype -> STRING','datatype',1,'p_datatype','lexer.py',774),
  ('datatype -> CHAR','datatype',1,'p_datatype','lexer.py',775),
  ('datatype -> set_definition','datatype',1,'p_datatype','lexer.py',776),
  ('datatype -> map_definition','datatype',1,'p_datatype','lexer.py',777),
  ('set_definition -> SET < datatype >','set_definition',4,'p_set_definition','lexer.py',781),
  ('block -> { statement_aux }','block',3,'p_block','lexer.py',785),
  ('statement_aux -> statement statement_aux','statement_aux',2,'p_statement_aux','lexer.py',788),
  ('statement_aux -> empty','statement_aux',1,'p_statement_aux','lexer.py',789),
  ('main -> MAIN n_clear_scope n_main_quad2 { vars_aux statement_aux }','main',7,'p_main','lexer.py',792),
  ('n_main_quad2 -> <empty>','n_main_quad2',0,'p_n_main_quad2','lexer.py',795),
  ('n_clear_scope -> <empty>','n_clear_scope',0,'p_n_clear_scope','lexer.py',799),
  ('vars_aux -> vars','vars_aux',1,'p_vars_aux','lexer.py',805),
  ('vars_aux -> empty','vars_aux',1,'p_vars_aux','lexer.py',806),
  ('map_definition -> MAP < datatype , datatype >','map_definition',6,'p_map_definition','lexer.py',809),
  ('map_access -> ID [ exp ]','map_access',4,'p_map_access','lexer.py',813),
  ('map_assignment -> map_access ASSIGNATOR exp','map_assignment',3,'p_map_assignment','lexer.py',816),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',819),
]
