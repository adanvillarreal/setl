
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programAND ASSIGNATOR BOOL CHAR CTE_BOOL CTE_BOOL CTE_BOOL CTE_CHAR CTE_FLOAT CTE_INT CTE_STRING ELSE EQ FLOAT GEQ ID IF INT LEQ MAIN MAP NOT_EQ OP OP OP OP OP OP_ARGS OP_ARGS OP_ARGS OP_ARGS OR PRINT PROGRAM READ RETURN SET SET_MATH_ADDSUB SET_MATH_MULDIV STRING VOID WHILEprogram : PROGRAM ID ';' n_main_quad program1n_main_quad : program1 : var program1\n                | program2program2 : proc program2\n                | mainproc : proca1 procA n_check_has_return\n            | VOID proca2 procA\n            | emptyn_check_has_return : proca2 : ID '(' proca1 :  datatype ID '(' procA : proc1 ')' '{' proc3 '}' proc1 : n_push_variable proc2\n             | emptyproc2 : ',' n_push_variable proc2\n             | emptyn_push_variable :  datatype IDproc3 : var proc3\n             | n_quad_counter proc4n_quad_counter : proc4 : statement proc4\n             | emptyvars : var vars\n            | varvar : datatype var1 var1 : ID ',' var1\n             | ID ';' assignment : assignment2 ASSIGNATOR n_quad_assign expressionassignment2 : IDn_quad_assign : condition : IF '(' expression n_while_2 ')' block condition1condition1 : ELSE n_if_2 block n_if_3\n                  | n_if_3n_if_2 : n_if_3 : while : WHILE n_while_1 '(' expression ')' n_while_2 block n_while_3n_while_1 : n_while_2 : n_while_3 : input : READ '(' n_process_read input1 ')' input1 : ',' n_process_read input1\n              | emptyn_process_read : IDoutput : PRINT '(' n_output_quad output1 ')' output1 : ',' n_output_quad output1\n               | emptyn_output_quad : expressionfunction_call : n_era_size function_call1 ')' n_era_size : ID '(' function_call1 : empty\n                      | function_call2function_call2 : n_verify_argument ',' n_add_one_to_counter function_call2\n                      | n_verify_argumentn_add_one_to_counter : n_verify_argument : expressionreturn : RETURN expressioncontainer_operation : ID '.' OP_ARGS '(' expression ')' container_operation : ID '.' OP '('  ')' statement : statement1 ';'\n                 | statement2 statement1 : assignment\n                  | input\n                  | output\n                  | container_operation\n                  | map_definition\n                  | return\n                  | map_assignment\n                  | function_callstatement2 : condition\n                  | whilerelop : '<'\n             | '>'\n             | NOT_EQ\n             | EQ\n             | LEQ\n             | GEQlogop : OR\n           | ANDexpression : exp0 expression2expression2 : logop exp0 n_quad_logop expression2\n                 | emptyn_quad_logop : exp0 : exp exp02exp02 : relop exp\n           | emptyexp : term exp2addsub : '+'\n            | '-'\n            | SET_MATH_ADDSUB muldiv : '*'\n            | '/'\n            | SET_MATH_MULDIVexp2 : addsub term n_quad_addsub exp2\n          | emptyterm : term_not factor n_quad_muldiv term2n_quad_muldiv : n_quad_addsub : term2 : muldiv factor n_quad_muldiv term2\n           | n_quad_notn_quad_not : term_not : '!'\n              | emptyfactor : '(' n_push_false_bottom expression ')' n_pop_false_bottom\n            | varcten_push_false_bottom : n_pop_false_bottom : varcte : ID empty\n            | varcte1varcte1 : CTE_INT\n               | CTE_FLOAT\n               | CTE_BOOL\n               | CTE_STRING\n               | CTE_CHAR\n               | function_call\n               | map_access\n               | container_operationfunctype : datatype\n               | VOIDdatatype : INT\n               | FLOAT\n               | BOOL\n               | STRING\n               | CHAR\n               | set_definition\n               | map_definitionset_definition : SET '<' datatype '>' block : '{' statement_aux '}' statement_aux : statement statement_aux\n                   | emptymain : MAIN n_clear_scope n_main_quad2 '{' vars_aux statement_aux '}' n_main_quad2 :  n_clear_scope : vars_aux : vars\n              | emptymap_definition : MAP '<' datatype ',' datatype '>' map_access : ID '[' expression ']' map_assignment : map_access ASSIGNATOR n_quad_assign expempty :"
    
_lr_action_items = {'$end':([1,10,11,14,33,34,126,],[0,-1,-4,-6,-3,-5,-131,]),'OP_ARGS':([123,],[170,]),'RETURN':([37,53,56,59,61,63,64,68,69,70,71,82,86,92,95,100,102,116,220,221,224,226,228,230,231,233,234,],[-26,-28,-21,-27,-139,73,-21,-134,73,-25,-135,73,-61,-70,-71,73,-24,-60,73,-36,-40,-34,-32,-37,-128,-36,-33,]),'READ':([37,53,56,59,61,63,64,68,69,70,71,82,86,92,95,100,102,116,220,221,224,226,228,230,231,233,234,],[-26,-28,-21,-27,-139,74,-21,-134,74,-25,-135,74,-61,-70,-71,74,-24,-60,74,-36,-40,-34,-32,-37,-128,-36,-33,]),'VOID':([4,5,13,15,16,32,37,41,48,53,59,72,],[-2,6,6,6,-9,-10,-26,-8,-7,-28,-27,-13,]),'CHAR':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,53,56,58,59,61,64,70,72,],[-2,8,8,8,8,-9,8,8,-10,8,-26,-11,-8,8,-7,-12,-28,8,8,-27,8,8,8,-13,]),'ASSIGNATOR':([80,81,91,192,],[113,114,-30,-137,]),'WHILE':([37,53,56,59,61,63,64,68,69,70,71,82,86,92,95,100,102,116,220,221,224,226,228,230,231,233,234,],[-26,-28,-21,-27,-139,77,-21,-134,77,-25,-135,77,-61,-70,-71,77,-24,-60,77,-36,-40,-34,-32,-37,-128,-36,-33,]),'PROGRAM':([0,],[2,]),'PRINT':([37,53,56,59,61,63,64,68,69,70,71,82,86,92,95,100,102,116,220,221,224,226,228,230,231,233,234,],[-26,-28,-21,-27,-139,78,-21,-134,78,-25,-135,78,-61,-70,-71,78,-24,-60,78,-36,-40,-34,-32,-37,-128,-36,-33,]),'SET_MATH_MULDIV':([128,129,130,131,133,134,135,136,137,138,139,140,168,175,176,192,210,212,213,219,222,223,],[-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-49,195,-108,-137,-59,-107,-97,-58,-104,195,]),'!':([73,88,112,113,114,122,124,125,132,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,174,185,189,190,],[106,106,106,-31,-31,-50,106,106,-106,-88,-89,106,-90,-79,106,-78,-77,106,-74,-76,-75,-72,-73,106,106,106,-55,106,106,106,106,]),'GEQ':([104,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,168,175,176,177,192,196,198,201,210,212,213,214,219,222,223,229,],[-139,152,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-49,-101,-108,-98,-137,-96,-100,-139,-59,-107,-97,-94,-58,-104,-101,-99,]),'SET':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,53,56,58,59,61,64,70,72,],[-2,9,9,9,9,-9,9,9,-10,9,-26,-11,-8,9,-7,-12,-28,9,9,-27,9,9,9,-13,]),')':([12,26,28,29,30,40,45,46,47,51,57,66,88,104,105,107,117,118,119,120,121,122,128,129,130,131,133,134,135,136,137,138,139,140,141,146,149,151,156,159,161,162,164,165,168,173,175,176,177,178,179,180,182,183,184,186,191,192,193,194,196,198,201,202,204,207,208,209,210,212,213,214,215,216,218,219,222,223,229,],[-139,-139,43,-15,-139,-11,-17,-14,-18,-12,-139,-16,-139,-139,-139,-139,-52,168,-56,-54,-51,-50,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-80,-82,-84,-86,-139,-44,-139,-48,-49,-39,-101,-108,-98,-83,-85,203,-43,205,206,-47,210,-137,211,212,-96,-100,-139,-139,-139,-139,-53,219,-59,-107,-97,-94,-81,-42,-46,-58,-104,-101,-99,]),'(':([25,38,49,73,74,77,78,88,91,93,103,106,109,111,112,113,114,121,122,124,125,132,137,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,170,171,174,185,189,190,195,197,199,200,],[40,51,51,-139,110,-38,112,-139,122,125,132,-102,-103,163,-139,-31,-31,-103,-50,-139,-139,-106,122,-88,-89,-139,-90,-79,-139,-78,-77,-139,-74,-76,-75,-72,-73,-139,-139,-139,-55,190,191,-139,-139,-139,-139,-93,-91,-92,132,]),'+':([104,128,129,130,131,133,134,135,136,137,138,139,140,168,175,176,177,192,196,198,201,210,212,213,219,222,223,229,],[142,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-49,-101,-108,-98,-137,-96,-100,142,-59,-107,-97,-58,-104,-101,-99,]),'*':([128,129,130,131,133,134,135,136,137,138,139,140,168,175,176,192,210,212,213,219,222,223,],[-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-49,197,-108,-137,-59,-107,-97,-58,-104,197,]),'-':([104,128,129,130,131,133,134,135,136,137,138,139,140,168,175,176,177,192,196,198,201,210,212,213,219,222,223,229,],[143,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-49,-101,-108,-98,-137,-96,-100,143,-59,-107,-97,-58,-104,-101,-99,]),',':([7,8,17,19,21,22,23,30,38,47,50,55,57,60,98,104,105,107,119,120,128,129,130,131,133,134,135,136,137,138,139,140,141,146,149,151,156,159,161,162,164,165,168,175,176,177,178,179,192,196,198,201,202,204,207,210,212,213,214,215,219,222,223,229,],[-126,-124,-123,-125,-121,-120,-122,44,52,-18,58,-127,44,52,-136,-139,-139,-139,-56,169,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-80,-82,-84,-86,181,-44,185,-48,-49,-101,-108,-98,-83,-85,-137,-96,-100,-139,-139,181,185,-59,-107,-97,-94,-81,-58,-104,-101,-99,]),'/':([128,129,130,131,133,134,135,136,137,138,139,140,168,175,176,192,210,212,213,219,222,223,],[-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-49,199,-108,-137,-59,-107,-97,-58,-104,199,]),'.':([91,137,],[123,123,]),'CTE_CHAR':([73,88,103,106,109,112,113,114,121,122,124,125,132,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,174,185,189,190,195,197,199,200,],[-139,-139,134,-102,-103,-139,-31,-31,-103,-50,-139,-139,-106,-88,-89,-139,-90,-79,-139,-78,-77,-139,-74,-76,-75,-72,-73,-139,-139,-139,-55,-139,-139,-139,-139,-93,-91,-92,134,]),';':([3,38,60,75,76,83,85,87,89,90,94,96,98,104,105,107,108,128,129,130,131,133,134,135,136,137,138,139,140,141,146,149,151,156,159,168,175,176,177,178,179,187,188,192,196,198,201,202,203,206,210,212,213,214,215,219,222,223,229,],[4,53,53,-66,-69,-63,-67,116,-65,-62,-68,-64,-136,-139,-139,-139,-57,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-80,-82,-84,-86,-49,-101,-108,-98,-83,-85,-138,-29,-137,-96,-100,-139,-139,-41,-45,-59,-107,-97,-94,-81,-58,-104,-101,-99,]),'<':([9,18,104,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,168,175,176,177,192,196,198,201,210,212,213,214,219,222,223,229,],[27,36,-139,158,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-49,-101,-108,-98,-137,-96,-100,-139,-59,-107,-97,-94,-58,-104,-101,-99,]),'>':([7,8,17,19,21,22,23,42,55,67,98,104,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,168,175,176,177,192,196,198,201,210,212,213,214,219,222,223,229,],[-126,-124,-123,-125,-121,-120,-122,55,-127,98,-136,-139,160,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-49,-101,-108,-98,-137,-96,-100,-139,-59,-107,-97,-94,-58,-104,-101,-99,]),'CTE_STRING':([73,88,103,106,109,112,113,114,121,122,124,125,132,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,174,185,189,190,195,197,199,200,],[-139,-139,140,-102,-103,-139,-31,-31,-103,-50,-139,-139,-106,-88,-89,-139,-90,-79,-139,-78,-77,-139,-74,-76,-75,-72,-73,-139,-139,-139,-55,-139,-139,-139,-139,-93,-91,-92,140,]),'STRING':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,53,56,58,59,61,64,70,72,],[-2,17,17,17,17,-9,17,17,-10,17,-26,-11,-8,17,-7,-12,-28,17,17,-27,17,17,17,-13,]),'NOT_EQ':([104,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,168,175,176,177,192,196,198,201,210,212,213,214,219,222,223,229,],[-139,154,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-49,-101,-108,-98,-137,-96,-100,-139,-59,-107,-97,-94,-58,-104,-101,-99,]),'ELSE':([221,231,],[227,-128,]),'[':([91,137,],[124,124,]),'CTE_INT':([73,88,103,106,109,112,113,114,121,122,124,125,132,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,174,185,189,190,195,197,199,200,],[-139,-139,136,-102,-103,-139,-31,-31,-103,-50,-139,-139,-106,-88,-89,-139,-90,-79,-139,-78,-77,-139,-74,-76,-75,-72,-73,-139,-139,-139,-55,-139,-139,-139,-139,-93,-91,-92,136,]),']':([104,105,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,149,151,156,159,168,172,175,176,177,178,179,192,196,198,201,202,210,212,213,214,215,219,222,223,229,],[-139,-139,-139,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-80,-82,-84,-86,-49,192,-101,-108,-98,-83,-85,-137,-96,-100,-139,-139,-59,-107,-97,-94,-81,-58,-104,-101,-99,]),'ID':([2,6,7,8,17,19,20,21,22,23,31,35,37,52,53,55,56,59,61,63,64,65,68,69,70,71,73,82,86,88,92,95,98,100,102,103,106,109,110,112,113,114,116,121,122,124,125,132,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,174,181,185,189,190,195,197,199,200,220,221,224,226,228,230,231,233,234,],[3,25,-126,-124,-123,-125,38,-121,-120,-122,47,49,-26,60,-28,-127,-21,-27,-139,91,-21,60,-134,91,-25,-135,-139,91,-61,-139,-70,-71,-136,91,-24,137,-102,-103,162,-139,-31,-31,-60,-103,-50,-139,-139,-106,-88,-89,-139,-90,-79,-139,-78,-77,-139,-74,-76,-75,-72,-73,-139,-139,-139,-55,-139,162,-139,-139,-139,-93,-91,-92,137,91,-36,-40,-34,-32,-37,-128,-36,-33,]),'IF':([37,53,56,59,61,63,64,68,69,70,71,82,86,92,95,100,102,116,220,221,224,226,228,230,231,233,234,],[-26,-28,-21,-27,-139,93,-21,-134,93,-25,-135,93,-61,-70,-71,93,-24,-60,93,-36,-40,-34,-32,-37,-128,-36,-33,]),'AND':([104,105,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,156,159,168,175,176,177,178,179,192,196,198,201,202,210,212,213,214,219,222,223,229,],[-139,147,-139,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-84,-86,-49,-101,-108,-98,-83,-85,-137,-96,-100,-139,147,-59,-107,-97,-94,-58,-104,-101,-99,]),'MAP':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,53,56,58,59,61,63,64,68,69,70,71,72,82,86,92,95,100,102,116,220,221,224,226,228,230,231,233,234,],[-2,18,18,18,18,-9,18,18,-10,18,-26,-11,-8,18,-7,-12,-28,18,18,-27,18,18,18,-134,18,18,-135,-13,18,-61,-70,-71,18,-24,-60,18,-36,-40,-34,-32,-37,-128,-36,-33,]),'EQ':([104,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,168,175,176,177,192,196,198,201,210,212,213,214,219,222,223,229,],[-139,157,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-49,-101,-108,-98,-137,-96,-100,-139,-59,-107,-97,-94,-58,-104,-101,-99,]),'INT':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,53,56,58,59,61,64,70,72,],[-2,22,22,22,22,-9,22,22,-10,22,-26,-11,-8,22,-7,-12,-28,22,22,-27,22,22,22,-13,]),'SET_MATH_ADDSUB':([104,128,129,130,131,133,134,135,136,137,138,139,140,168,175,176,177,192,196,198,201,210,212,213,219,222,223,229,],[145,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-49,-101,-108,-98,-137,-96,-100,145,-59,-107,-97,-58,-104,-101,-99,]),'FLOAT':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,53,56,58,59,61,64,70,72,],[-2,21,21,21,21,-9,21,21,-10,21,-26,-11,-8,21,-7,-12,-28,21,21,-27,21,21,21,-13,]),'CTE_FLOAT':([73,88,103,106,109,112,113,114,121,122,124,125,132,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,174,185,189,190,195,197,199,200,],[-139,-139,138,-102,-103,-139,-31,-31,-103,-50,-139,-139,-106,-88,-89,-139,-90,-79,-139,-78,-77,-139,-74,-76,-75,-72,-73,-139,-139,-139,-55,-139,-139,-139,-139,-93,-91,-92,138,]),'CTE_BOOL':([73,88,103,106,109,112,113,114,121,122,124,125,132,142,143,144,145,147,148,150,152,153,154,155,157,158,160,163,166,167,169,174,185,189,190,195,197,199,200,],[-139,-139,139,-102,-103,-139,-31,-31,-103,-50,-139,-139,-106,-88,-89,-139,-90,-79,-139,-78,-77,-139,-74,-76,-75,-72,-73,-139,-139,-139,-55,-139,-139,-139,-139,-93,-91,-92,139,]),'LEQ':([104,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,168,175,176,177,192,196,198,201,210,212,213,214,219,222,223,229,],[-139,155,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-49,-101,-108,-98,-137,-96,-100,-139,-59,-107,-97,-94,-58,-104,-101,-99,]),'BOOL':([4,5,12,13,15,16,26,27,32,36,37,40,41,44,48,51,53,56,58,59,61,64,70,72,],[-2,23,23,23,23,-9,23,23,-10,23,-26,-11,-8,23,-7,-12,-28,23,23,-27,23,23,23,-13,]),'{':([24,39,43,54,205,211,217,227,232,],[-133,-132,56,61,-39,220,220,-35,220,]),'MAIN':([4,5,13,15,16,32,37,41,48,53,59,72,],[-2,24,24,24,-9,-10,-26,-8,-7,-28,-27,-13,]),'}':([37,53,56,59,61,62,63,64,68,69,70,71,79,82,84,86,92,95,97,99,100,101,102,115,116,127,220,221,224,225,226,228,230,231,233,234,],[-26,-28,-21,-27,-139,72,-139,-21,-134,-139,-25,-135,-20,-139,-23,-61,-70,-71,-19,126,-139,-130,-24,-22,-60,-129,-139,-36,-40,231,-34,-32,-37,-128,-36,-33,]),'OR':([104,105,107,128,129,130,131,133,134,135,136,137,138,139,140,141,146,156,159,168,175,176,177,178,179,192,196,198,201,202,210,212,213,214,219,222,223,229,],[-139,150,-139,-115,-109,-105,-116,-97,-114,-117,-110,-139,-111,-112,-113,-87,-95,-84,-86,-49,-101,-108,-98,-83,-85,-137,-96,-100,-139,150,-59,-107,-97,-94,-58,-104,-101,-99,]),'OP':([123,],[171,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'n_quad_muldiv':([133,213,],[175,223,]),'input1':([161,204,],[180,216,]),'n_add_one_to_counter':([169,],[189,]),'term2':([175,223,],[196,229,]),'vars':([61,70,],[68,102,]),'n_clear_scope':([24,],[39,]),'output1':([164,207,],[184,218,]),'map_definition':([5,12,13,15,26,27,36,44,56,58,61,63,64,69,70,82,100,220,],[7,7,7,7,7,7,7,7,7,7,7,75,7,75,7,75,75,75,]),'n_process_read':([110,181,],[161,204,]),'function_call':([63,69,82,100,103,200,220,],[76,76,76,76,128,128,76,]),'n_if_2':([227,],[232,]),'n_while_1':([77,],[111,]),'vars_aux':([61,],[69,]),'n_check_has_return':([32,],[48,]),'n_while_2':([173,205,],[193,217,]),'proc4':([63,82,],[79,115,]),'return':([63,69,82,100,220,],[85,85,85,85,85,]),'addsub':([104,201,],[144,144,]),'proc1':([12,26,],[28,28,]),'proc3':([56,64,],[62,97,]),'proc2':([30,57,],[46,66,]),'n_while_3':([224,],[230,]),'program1':([5,13,],[10,33,]),'program2':([5,13,15,],[11,11,34,]),'n_era_size':([63,69,82,100,103,200,220,],[88,88,88,88,88,88,88,]),'muldiv':([175,223,],[200,200,]),'exp2':([104,201,],[141,214,]),'n_main_quad2':([39,],[54,]),'exp0':([73,88,112,124,125,148,163,167,174,185,189,190,],[105,105,105,105,105,178,105,105,105,105,105,105,]),'proca1':([5,13,15,],[12,12,12,]),'n_pop_false_bottom':([212,],[222,]),'proca2':([6,],[26,]),'assignment2':([63,69,82,100,220,],[81,81,81,81,81,]),'program':([0,],[1,]),'n_output_quad':([112,185,],[164,207,]),'statement':([63,69,82,100,220,],[82,100,82,100,100,]),'n_quad_counter':([56,64,],[63,63,]),'var':([5,13,56,61,64,70,],[13,13,64,70,64,70,]),'input':([63,69,82,100,220,],[83,83,83,83,83,]),'main':([5,13,15,],[14,14,14,]),'proc':([5,13,15,],[15,15,15,]),'n_verify_argument':([88,189,],[120,120,]),'empty':([5,12,13,15,26,30,57,61,63,69,73,82,88,100,104,105,107,112,124,125,137,144,148,153,161,163,164,166,167,174,185,189,190,201,202,204,207,220,],[16,29,16,16,29,45,45,71,84,101,109,84,121,101,146,151,159,109,109,109,176,109,109,109,182,109,186,109,109,109,109,109,109,146,151,182,186,101,]),'condition1':([221,],[228,]),'term_not':([73,88,112,124,125,144,148,153,163,166,167,174,185,189,190,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'var1':([20,52,65,],[37,59,37,]),'statement2':([63,69,82,100,220,],[86,86,86,86,86,]),'statement1':([63,69,82,100,220,],[87,87,87,87,87,]),'container_operation':([63,69,82,100,103,200,220,],[89,89,89,89,135,135,89,]),'assignment':([63,69,82,100,220,],[90,90,90,90,90,]),'factor':([103,200,],[133,213,]),'logop':([105,202,],[148,148,]),'n_quad_assign':([113,114,],[166,167,]),'n_push_false_bottom':([132,],[174,]),'map_access':([63,69,82,100,103,200,220,],[80,80,80,80,131,131,80,]),'n_quad_logop':([178,],[202,]),'n_main_quad':([4,],[5,]),'expression2':([105,202,],[149,215,]),'n_if_3':([221,233,],[226,234,]),'condition':([63,69,82,100,220,],[92,92,92,92,92,]),'varcte':([103,200,],[130,130,]),'term':([73,88,112,124,125,144,148,153,163,166,167,174,185,189,190,],[104,104,104,104,104,177,104,104,104,104,104,104,104,104,104,]),'n_push_variable':([12,26,44,],[30,30,57,]),'set_definition':([5,12,13,15,26,27,36,44,56,58,61,64,70,],[19,19,19,19,19,19,19,19,19,19,19,19,19,]),'datatype':([5,12,13,15,26,27,36,44,56,58,61,64,70,],[20,31,20,35,31,42,50,31,65,67,65,65,65,]),'varcte1':([103,200,],[129,129,]),'relop':([107,],[153,]),'procA':([12,26,],[32,41,]),'function_call1':([88,],[118,]),'map_assignment':([63,69,82,100,220,],[94,94,94,94,94,]),'while':([63,69,82,100,220,],[95,95,95,95,95,]),'function_call2':([88,189,],[117,208,]),'exp':([73,88,112,124,125,148,153,163,166,167,174,185,189,190,],[107,107,107,107,107,107,179,107,187,107,107,107,107,107,]),'n_quad_addsub':([177,],[201,]),'output':([63,69,82,100,220,],[96,96,96,96,96,]),'exp02':([107,],[156,]),'n_quad_not':([175,223,],[198,198,]),'expression':([73,88,112,124,125,163,167,174,185,189,190,],[108,119,165,172,173,183,188,194,165,119,209,]),'block':([211,217,232,],[221,224,233,]),'statement_aux':([69,100,220,],[99,127,225,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID ; n_main_quad program1','program',5,'p_program','lexer.py',147),
  ('n_main_quad -> <empty>','n_main_quad',0,'p_n_main_quad','lexer.py',151),
  ('program1 -> var program1','program1',2,'p_program1','lexer.py',156),
  ('program1 -> program2','program1',1,'p_program1','lexer.py',157),
  ('program2 -> proc program2','program2',2,'p_program2','lexer.py',160),
  ('program2 -> main','program2',1,'p_program2','lexer.py',161),
  ('proc -> proca1 procA n_check_has_return','proc',3,'p_proc','lexer.py',165),
  ('proc -> VOID proca2 procA','proc',3,'p_proc','lexer.py',166),
  ('proc -> empty','proc',1,'p_proc','lexer.py',167),
  ('n_check_has_return -> <empty>','n_check_has_return',0,'p_n_check_has_return','lexer.py',173),
  ('proca2 -> ID (','proca2',2,'p_proca2','lexer.py',186),
  ('proca1 -> datatype ID (','proca1',3,'p_proca1','lexer.py',192),
  ('procA -> proc1 ) { proc3 }','procA',5,'p_procA','lexer.py',200),
  ('proc1 -> n_push_variable proc2','proc1',2,'p_proc1','lexer.py',206),
  ('proc1 -> empty','proc1',1,'p_proc1','lexer.py',207),
  ('proc2 -> , n_push_variable proc2','proc2',3,'p_proc2','lexer.py',210),
  ('proc2 -> empty','proc2',1,'p_proc2','lexer.py',211),
  ('n_push_variable -> datatype ID','n_push_variable',2,'p_n_push_variable','lexer.py',215),
  ('proc3 -> var proc3','proc3',2,'p_proc3','lexer.py',225),
  ('proc3 -> n_quad_counter proc4','proc3',2,'p_proc3','lexer.py',226),
  ('n_quad_counter -> <empty>','n_quad_counter',0,'p_n_quad_counter','lexer.py',230),
  ('proc4 -> statement proc4','proc4',2,'p_proc4','lexer.py',235),
  ('proc4 -> empty','proc4',1,'p_proc4','lexer.py',236),
  ('vars -> var vars','vars',2,'p_vars','lexer.py',239),
  ('vars -> var','vars',1,'p_vars','lexer.py',240),
  ('var -> datatype var1','var',2,'p_var','lexer.py',245),
  ('var1 -> ID , var1','var1',3,'p_var1','lexer.py',255),
  ('var1 -> ID ;','var1',2,'p_var1','lexer.py',256),
  ('assignment -> assignment2 ASSIGNATOR n_quad_assign expression','assignment',4,'p_assignment','lexer.py',264),
  ('assignment2 -> ID','assignment2',1,'p_assignment2','lexer.py',273),
  ('n_quad_assign -> <empty>','n_quad_assign',0,'p_n_quad_assign','lexer.py',284),
  ('condition -> IF ( expression n_while_2 ) block condition1','condition',7,'p_condition','lexer.py',301),
  ('condition1 -> ELSE n_if_2 block n_if_3','condition1',4,'p_condition1','lexer.py',305),
  ('condition1 -> n_if_3','condition1',1,'p_condition1','lexer.py',306),
  ('n_if_2 -> <empty>','n_if_2',0,'p_n_if_2','lexer.py',311),
  ('n_if_3 -> <empty>','n_if_3',0,'p_n_if_3','lexer.py',320),
  ('while -> WHILE n_while_1 ( expression ) n_while_2 block n_while_3','while',8,'p_while','lexer.py',326),
  ('n_while_1 -> <empty>','n_while_1',0,'p_n_while_1','lexer.py',330),
  ('n_while_2 -> <empty>','n_while_2',0,'p_n_while_2','lexer.py',335),
  ('n_while_3 -> <empty>','n_while_3',0,'p_n_while_3','lexer.py',340),
  ('input -> READ ( n_process_read input1 )','input',5,'p_input','lexer.py',356),
  ('input1 -> , n_process_read input1','input1',3,'p_input1','lexer.py',360),
  ('input1 -> empty','input1',1,'p_input1','lexer.py',361),
  ('n_process_read -> ID','n_process_read',1,'p_n_process_read','lexer.py',365),
  ('output -> PRINT ( n_output_quad output1 )','output',5,'p_output','lexer.py',375),
  ('output1 -> , n_output_quad output1','output1',3,'p_output1','lexer.py',379),
  ('output1 -> empty','output1',1,'p_output1','lexer.py',380),
  ('n_output_quad -> expression','n_output_quad',1,'p_n_output_quad','lexer.py',384),
  ('function_call -> n_era_size function_call1 )','function_call',3,'p_function_call','lexer.py',394),
  ('n_era_size -> ID (','n_era_size',2,'p_n_era_size','lexer.py',412),
  ('function_call1 -> empty','function_call1',1,'p_function_call1','lexer.py',421),
  ('function_call1 -> function_call2','function_call1',1,'p_function_call1','lexer.py',422),
  ('function_call2 -> n_verify_argument , n_add_one_to_counter function_call2','function_call2',4,'p_function_call2','lexer.py',426),
  ('function_call2 -> n_verify_argument','function_call2',1,'p_function_call2','lexer.py',427),
  ('n_add_one_to_counter -> <empty>','n_add_one_to_counter',0,'p_n_add_one_to_counter','lexer.py',433),
  ('n_verify_argument -> expression','n_verify_argument',1,'p_n_verify_argument','lexer.py',439),
  ('return -> RETURN expression','return',2,'p_return','lexer.py',454),
  ('container_operation -> ID . OP_ARGS ( expression )','container_operation',6,'p_container_operation_arg','lexer.py',469),
  ('container_operation -> ID . OP ( )','container_operation',5,'p_container_operation','lexer.py',491),
  ('statement -> statement1 ;','statement',2,'p_statement','lexer.py',513),
  ('statement -> statement2','statement',1,'p_statement','lexer.py',514),
  ('statement1 -> assignment','statement1',1,'p_statement1','lexer.py',518),
  ('statement1 -> input','statement1',1,'p_statement1','lexer.py',519),
  ('statement1 -> output','statement1',1,'p_statement1','lexer.py',520),
  ('statement1 -> container_operation','statement1',1,'p_statement1','lexer.py',521),
  ('statement1 -> map_definition','statement1',1,'p_statement1','lexer.py',522),
  ('statement1 -> return','statement1',1,'p_statement1','lexer.py',523),
  ('statement1 -> map_assignment','statement1',1,'p_statement1','lexer.py',524),
  ('statement1 -> function_call','statement1',1,'p_statement1','lexer.py',525),
  ('statement2 -> condition','statement2',1,'p_statement2','lexer.py',529),
  ('statement2 -> while','statement2',1,'p_statement2','lexer.py',530),
  ('relop -> <','relop',1,'p_relop','lexer.py',534),
  ('relop -> >','relop',1,'p_relop','lexer.py',535),
  ('relop -> NOT_EQ','relop',1,'p_relop','lexer.py',536),
  ('relop -> EQ','relop',1,'p_relop','lexer.py',537),
  ('relop -> LEQ','relop',1,'p_relop','lexer.py',538),
  ('relop -> GEQ','relop',1,'p_relop','lexer.py',539),
  ('logop -> OR','logop',1,'p_logop','lexer.py',544),
  ('logop -> AND','logop',1,'p_logop','lexer.py',545),
  ('expression -> exp0 expression2','expression',2,'p_expression','lexer.py',748),
  ('expression2 -> logop exp0 n_quad_logop expression2','expression2',4,'p_expression2','lexer.py',752),
  ('expression2 -> empty','expression2',1,'p_expression2','lexer.py',753),
  ('n_quad_logop -> <empty>','n_quad_logop',0,'p_n_quad_logop','lexer.py',757),
  ('exp0 -> exp exp02','exp0',2,'p_exp0','lexer.py',762),
  ('exp02 -> relop exp','exp02',2,'p_exp02','lexer.py',766),
  ('exp02 -> empty','exp02',1,'p_exp02','lexer.py',767),
  ('exp -> term exp2','exp',2,'p_exp','lexer.py',773),
  ('addsub -> +','addsub',1,'p_addsub','lexer.py',777),
  ('addsub -> -','addsub',1,'p_addsub','lexer.py',778),
  ('addsub -> SET_MATH_ADDSUB','addsub',1,'p_addsub','lexer.py',779),
  ('muldiv -> *','muldiv',1,'p_muldiv','lexer.py',784),
  ('muldiv -> /','muldiv',1,'p_muldiv','lexer.py',785),
  ('muldiv -> SET_MATH_MULDIV','muldiv',1,'p_muldiv','lexer.py',786),
  ('exp2 -> addsub term n_quad_addsub exp2','exp2',4,'p_exp2','lexer.py',791),
  ('exp2 -> empty','exp2',1,'p_exp2','lexer.py',792),
  ('term -> term_not factor n_quad_muldiv term2','term',4,'p_term','lexer.py',796),
  ('n_quad_muldiv -> <empty>','n_quad_muldiv',0,'p_n_quad_muldiv','lexer.py',800),
  ('n_quad_addsub -> <empty>','n_quad_addsub',0,'p_n_quad_addsub','lexer.py',805),
  ('term2 -> muldiv factor n_quad_muldiv term2','term2',4,'p_term2','lexer.py',810),
  ('term2 -> n_quad_not','term2',1,'p_term2','lexer.py',811),
  ('n_quad_not -> <empty>','n_quad_not',0,'p_n_quad_not','lexer.py',815),
  ('term_not -> !','term_not',1,'p_term_not','lexer.py',821),
  ('term_not -> empty','term_not',1,'p_term_not','lexer.py',822),
  ('factor -> ( n_push_false_bottom expression ) n_pop_false_bottom','factor',5,'p_factor','lexer.py',828),
  ('factor -> varcte','factor',1,'p_factor','lexer.py',829),
  ('n_push_false_bottom -> <empty>','n_push_false_bottom',0,'p_n_push_false_bottom','lexer.py',833),
  ('n_pop_false_bottom -> <empty>','n_pop_false_bottom',0,'p_n_pop_false_bottom','lexer.py',838),
  ('varcte -> ID empty','varcte',2,'p_varcte','lexer.py',843),
  ('varcte -> varcte1','varcte',1,'p_varcte','lexer.py',844),
  ('varcte1 -> CTE_INT','varcte1',1,'p_varcte1','lexer.py',862),
  ('varcte1 -> CTE_FLOAT','varcte1',1,'p_varcte1','lexer.py',863),
  ('varcte1 -> CTE_BOOL','varcte1',1,'p_varcte1','lexer.py',864),
  ('varcte1 -> CTE_STRING','varcte1',1,'p_varcte1','lexer.py',865),
  ('varcte1 -> CTE_CHAR','varcte1',1,'p_varcte1','lexer.py',866),
  ('varcte1 -> function_call','varcte1',1,'p_varcte1','lexer.py',867),
  ('varcte1 -> map_access','varcte1',1,'p_varcte1','lexer.py',868),
  ('varcte1 -> container_operation','varcte1',1,'p_varcte1','lexer.py',869),
  ('functype -> datatype','functype',1,'p_functype','lexer.py',879),
  ('functype -> VOID','functype',1,'p_functype','lexer.py',880),
  ('datatype -> INT','datatype',1,'p_datatype','lexer.py',884),
  ('datatype -> FLOAT','datatype',1,'p_datatype','lexer.py',885),
  ('datatype -> BOOL','datatype',1,'p_datatype','lexer.py',886),
  ('datatype -> STRING','datatype',1,'p_datatype','lexer.py',887),
  ('datatype -> CHAR','datatype',1,'p_datatype','lexer.py',888),
  ('datatype -> set_definition','datatype',1,'p_datatype','lexer.py',889),
  ('datatype -> map_definition','datatype',1,'p_datatype','lexer.py',890),
  ('set_definition -> SET < datatype >','set_definition',4,'p_set_definition','lexer.py',895),
  ('block -> { statement_aux }','block',3,'p_block','lexer.py',900),
  ('statement_aux -> statement statement_aux','statement_aux',2,'p_statement_aux','lexer.py',904),
  ('statement_aux -> empty','statement_aux',1,'p_statement_aux','lexer.py',905),
  ('main -> MAIN n_clear_scope n_main_quad2 { vars_aux statement_aux }','main',7,'p_main','lexer.py',909),
  ('n_main_quad2 -> <empty>','n_main_quad2',0,'p_n_main_quad2','lexer.py',915),
  ('n_clear_scope -> <empty>','n_clear_scope',0,'p_n_clear_scope','lexer.py',920),
  ('vars_aux -> vars','vars_aux',1,'p_vars_aux','lexer.py',929),
  ('vars_aux -> empty','vars_aux',1,'p_vars_aux','lexer.py',930),
  ('map_definition -> MAP < datatype , datatype >','map_definition',6,'p_map_definition','lexer.py',934),
  ('map_access -> ID [ expression ]','map_access',4,'p_map_access','lexer.py',940),
  ('map_assignment -> map_access ASSIGNATOR n_quad_assign exp','map_assignment',4,'p_map_assignment','lexer.py',964),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',968),
]
