
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programAND ASSIGNATOR BOOL CHAR CTE_BOOL CTE_CHAR CTE_FLOAT CTE_INT CTE_STRING ELSE EQ FLOAT GEQ ID IF INT LEQ MAIN MAP NOT_EQ OPERATION OR PRINT PROGRAM READ RETURN SET STRING VOID WHILEprogram : PROGRAM ID ';' program1program1 : program2 program3 mainprogram2 : vars\n                | emptyprogram3 : proc program3\n                | emptyvars : datatype vars1 ';' vars2vars1 : ID ',' vars1\n             | IDvars2 : vars\n             | emptyproc : functype ID '(' proc1 ')' '{' proc3 proc4 '}' proc1 : datatype ID proc2proc2 : ',' proc1\n             | emptyproc3 : vars\n             | emptyproc4 : statement proc4\n             | emptyassignment : ID ASSIGNATOR expressioncondition : IF '(' expression ')' block condition1condition1 : ELSE block\n                  | emptyinput : READ '(' ID input1 ')' input1 : ',' ID input1\n              | emptyoutput : PRINT '(' expression output1 ')' output1 : ',' expression output1\n               | emptyfunction_call : ID '(' function_call1 ')' function_call1 : function_call2\n                      | emptyfunction_call2 : expression ',' function_call2\n                      | emptyreturn : RETURN expressionset_operation : ID '.' OPERATION '(' set_operation1 ')' set_operation1 : expression\n                       | emptystatement : statement1 ';'\n                 | statement2 statement1 : assignment\n                  | input\n                  | output\n                  | set_operation\n                  | map_definition\n                  | return\n                  | map_assignment\n                  | map_operationstatement2 : condition\n                  | whilewhile : WHILE '(' expression ')' blockrelop : '<'\n             | '>'\n             | NOT_EQ\n             | EQ\n             | LEQ\n             | GEQlogop : OR\n          | ANDexpression : exp0 expression2expression2 : logop exp0 expression2\n                 | emptyexp0 : exp exp02exp02 : relop exp02\n           | emptyexp : term exp2addsub : '+'\n            | '-' muldiv : '*'\n            | '/' exp2 : addsub term exp2\n          | emptyterm : term_not factor term2term2 : muldiv factor term2\n           | emptyterm_not : '!'\n              | emptyfactor : '(' expression ')'\n            | factor2factor2 : factor3 varctefactor3 : addsub\n             | emptyvarcte : ID\n            | CTE_INT\n            | CTE_FLOAT\n            | CTE_BOOL\n            | CTE_STRING\n            | CTE_CHAR\n            | function_call\n            | map_access\n            | map_operation\n            | set_operation datatype : INT\n               | FLOAT\n               | BOOL\n               | STRING\n               | CHAR\n               | set_definition\n               | map_definitionset_definition : SET '<' datatype '>' functype : datatype\n               | VOIDblock : '{' statement_aux '}' statement_aux : statement statement_aux\n                   | emptymain : MAIN '{' vars_aux statement_aux '}' vars_aux : vars\n              | emptymap_definition : MAP '<' datatype ',' datatype '>' map_access : ID '(' exp ')' map_assignment : map_access ASSIGNATOR expmap_operation : ID '.' OPERATION '(' ')' empty : "
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,29,76,],[0,-1,-2,-106,]),'ID':([2,9,10,11,12,13,14,15,16,22,23,24,33,34,37,39,40,41,43,45,46,47,49,52,55,64,65,69,75,78,79,81,82,83,88,89,90,91,92,93,94,104,106,107,118,120,121,123,125,126,127,131,132,133,135,138,141,147,149,150,166,171,180,182,183,184,194,197,199,202,203,204,205,207,],[3,26,-93,-94,-95,-96,-97,-98,-99,32,-101,-102,-113,26,-113,-7,-10,-11,-100,66,-107,-108,74,66,-40,-49,-50,-113,-109,-39,-113,-113,101,-113,-113,-76,-77,-113,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,153,-81,-82,66,-16,-17,-113,173,-113,-113,-69,-70,66,-77,-113,-113,66,-51,-77,-21,-23,-113,-113,-22,-103,-77,]),';':([3,25,26,42,54,56,57,58,59,60,61,62,63,75,84,85,86,87,98,103,105,108,109,110,111,112,113,114,115,116,117,119,122,124,128,136,143,144,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,172,174,176,177,178,179,187,190,201,],[4,33,-9,-8,78,-41,-42,-43,-44,-45,-46,-47,-48,-109,-35,-113,-113,-113,-20,-60,-62,-63,-113,-65,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-111,-110,-113,-64,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-24,-27,-61,-71,-113,-78,-36,-74,-30,]),'VOID':([4,6,7,8,20,33,39,40,41,185,],[-113,24,-3,-4,24,-113,-7,-10,-11,-12,]),'INT':([4,6,7,8,20,27,28,33,37,38,39,40,41,44,94,96,185,],[10,10,-3,-4,10,10,10,10,10,10,-7,-10,-11,10,10,10,-12,]),'FLOAT':([4,6,7,8,20,27,28,33,37,38,39,40,41,44,94,96,185,],[11,11,-3,-4,11,11,11,11,11,11,-7,-10,-11,11,11,11,-12,]),'BOOL':([4,6,7,8,20,27,28,33,37,38,39,40,41,44,94,96,185,],[12,12,-3,-4,12,12,12,12,12,12,-7,-10,-11,12,12,12,-12,]),'STRING':([4,6,7,8,20,27,28,33,37,38,39,40,41,44,94,96,185,],[13,13,-3,-4,13,13,13,13,13,13,-7,-10,-11,13,13,13,-12,]),'CHAR':([4,6,7,8,20,27,28,33,37,38,39,40,41,44,94,96,185,],[14,14,-3,-4,14,14,14,14,14,14,-7,-10,-11,14,14,14,-12,]),'SET':([4,6,7,8,20,27,28,33,37,38,39,40,41,44,94,96,185,],[17,17,-3,-4,17,17,17,17,17,17,-7,-10,-11,17,17,17,-12,]),'MAP':([4,6,7,8,20,27,28,33,37,38,39,40,41,44,45,46,47,52,55,64,65,78,94,96,131,132,133,166,182,183,184,185,197,199,204,205,],[18,18,-3,-4,18,18,18,18,18,18,-7,-10,-11,18,18,-107,-108,18,-40,-49,-50,-39,18,18,18,-16,-17,18,-113,18,-51,-12,-21,-23,-22,-103,]),'MAIN':([4,6,7,8,19,20,21,31,33,39,40,41,185,],[-113,-113,-3,-4,30,-113,-6,-5,-113,-7,-10,-11,-12,]),'>':([10,11,12,13,14,15,16,35,43,50,75,86,87,109,111,112,113,114,115,116,117,119,122,124,136,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[-93,-94,-95,-96,-97,-98,-99,43,-100,75,-109,112,-113,112,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,112,-30,]),',':([10,11,12,13,14,15,16,26,36,43,74,75,85,86,87,101,102,103,105,108,109,110,111,112,113,114,115,116,117,119,122,124,136,143,144,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,173,175,176,177,178,179,187,190,192,195,201,],[-93,-94,-95,-96,-97,-98,-99,34,44,-100,96,-109,-113,-113,-113,138,141,-60,-62,-63,-113,-65,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,-113,-64,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,138,141,-61,-71,-113,-78,-36,-74,-113,202,-30,]),'<':([17,18,86,87,109,111,112,113,114,115,116,117,119,122,124,136,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[27,28,111,-113,111,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,111,-30,]),'{':([30,73,163,164,198,],[37,94,183,183,183,]),'(':([32,66,67,68,69,71,72,79,81,83,88,89,90,91,92,93,99,104,106,107,118,120,121,123,135,141,147,149,150,153,171,180,194,196,202,203,207,],[38,81,82,83,-113,92,93,-113,-113,-113,123,-76,-77,-113,-113,-113,135,-113,-58,-59,-113,-67,-68,-113,-113,-113,123,-69,-70,180,-77,-113,-77,203,-113,-113,-77,]),'READ':([33,37,39,40,41,45,46,47,52,55,64,65,78,94,131,132,133,166,182,183,184,197,199,204,205,],[-113,-113,-7,-10,-11,67,-107,-108,67,-40,-49,-50,-39,-113,67,-16,-17,67,-113,67,-51,-21,-23,-22,-103,]),'PRINT':([33,37,39,40,41,45,46,47,52,55,64,65,78,94,131,132,133,166,182,183,184,197,199,204,205,],[-113,-113,-7,-10,-11,68,-107,-108,68,-40,-49,-50,-39,-113,68,-16,-17,68,-113,68,-51,-21,-23,-22,-103,]),'RETURN':([33,37,39,40,41,45,46,47,52,55,64,65,78,94,131,132,133,166,182,183,184,197,199,204,205,],[-113,-113,-7,-10,-11,69,-107,-108,69,-40,-49,-50,-39,-113,69,-16,-17,69,-113,69,-51,-21,-23,-22,-103,]),'IF':([33,37,39,40,41,45,46,47,52,55,64,65,78,94,131,132,133,166,182,183,184,197,199,204,205,],[-113,-113,-7,-10,-11,71,-107,-108,71,-40,-49,-50,-39,-113,71,-16,-17,71,-113,71,-51,-21,-23,-22,-103,]),'WHILE':([33,37,39,40,41,45,46,47,52,55,64,65,78,94,131,132,133,166,182,183,184,197,199,204,205,],[-113,-113,-7,-10,-11,72,-107,-108,72,-40,-49,-50,-39,-113,72,-16,-17,72,-113,72,-51,-21,-23,-22,-103,]),'}':([33,37,39,40,41,45,46,47,51,52,53,55,64,65,77,78,94,131,132,133,165,166,167,182,183,184,186,197,199,200,204,205,],[-113,-113,-7,-10,-11,-113,-107,-108,76,-113,-105,-40,-49,-50,-104,-39,-113,-113,-16,-17,185,-113,-19,-113,-113,-51,-18,-21,-23,205,-22,-103,]),')':([48,74,85,86,87,95,97,100,101,102,103,105,108,109,110,111,112,113,114,115,116,117,119,122,124,129,130,134,135,136,137,139,140,142,143,144,145,146,148,151,152,153,154,155,156,157,158,159,160,161,162,168,169,170,171,173,175,176,177,178,179,180,187,188,189,190,191,192,193,194,201,202,203,206,207,],[73,-113,-113,-113,-113,-13,-15,136,-113,-113,-60,-62,-63,-113,-65,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,163,164,-14,169,-110,172,-26,174,-29,-113,-64,-113,-73,-75,179,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,187,-112,-37,-38,-113,-113,-61,-71,-113,-78,-113,-36,-25,-28,-74,201,136,-31,-32,-30,-113,169,-33,-34,]),'ASSIGNATOR':([66,70,136,],[79,91,-110,]),'.':([66,153,],[80,181,]),'!':([69,79,81,83,91,92,93,104,106,107,118,120,121,123,135,141,180,202,203,],[89,89,89,89,89,89,89,89,-58,-59,89,-67,-68,89,89,89,89,89,89,]),'+':([69,79,81,83,87,88,89,90,91,92,93,104,106,107,118,120,121,122,123,124,135,136,141,145,146,147,148,149,150,152,153,154,155,156,157,158,159,160,161,162,169,171,178,179,180,187,190,194,201,202,203,207,],[-113,-113,-113,-113,120,120,-76,-77,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,-113,-79,-113,-110,-113,120,-73,120,-75,-69,-70,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-77,-113,-78,-113,-36,-74,-77,-30,-113,-113,-77,]),'-':([69,79,81,83,87,88,89,90,91,92,93,104,106,107,118,120,121,122,123,124,135,136,141,145,146,147,148,149,150,152,153,154,155,156,157,158,159,160,161,162,169,171,178,179,180,187,190,194,201,202,203,207,],[-113,-113,-113,-113,121,121,-76,-77,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,-113,-79,-113,-110,-113,121,-73,121,-75,-69,-70,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-77,-113,-78,-113,-36,-74,-77,-30,-113,-113,-77,]),'CTE_INT':([69,79,81,83,88,89,90,91,92,93,104,106,107,118,120,121,123,125,126,127,135,141,147,149,150,171,180,194,202,203,207,],[-113,-113,-113,-113,-113,-76,-77,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,154,-81,-82,-113,-113,-113,-69,-70,-77,-113,-77,-113,-113,-77,]),'CTE_FLOAT':([69,79,81,83,88,89,90,91,92,93,104,106,107,118,120,121,123,125,126,127,135,141,147,149,150,171,180,194,202,203,207,],[-113,-113,-113,-113,-113,-76,-77,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,155,-81,-82,-113,-113,-113,-69,-70,-77,-113,-77,-113,-113,-77,]),'CTE_BOOL':([69,79,81,83,88,89,90,91,92,93,104,106,107,118,120,121,123,125,126,127,135,141,147,149,150,171,180,194,202,203,207,],[-113,-113,-113,-113,-113,-76,-77,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,156,-81,-82,-113,-113,-113,-69,-70,-77,-113,-77,-113,-113,-77,]),'CTE_STRING':([69,79,81,83,88,89,90,91,92,93,104,106,107,118,120,121,123,125,126,127,135,141,147,149,150,171,180,194,202,203,207,],[-113,-113,-113,-113,-113,-76,-77,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,157,-81,-82,-113,-113,-113,-69,-70,-77,-113,-77,-113,-113,-77,]),'CTE_CHAR':([69,79,81,83,88,89,90,91,92,93,104,106,107,118,120,121,123,125,126,127,135,141,147,149,150,171,180,194,202,203,207,],[-113,-113,-113,-113,-113,-76,-77,-113,-113,-113,-113,-58,-59,-113,-67,-68,-113,158,-81,-82,-113,-113,-113,-69,-70,-77,-113,-77,-113,-113,-77,]),'OPERATION':([80,181,],[99,196,]),'OR':([85,86,87,108,109,110,111,112,113,114,115,116,117,119,122,124,136,143,144,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[106,-113,-113,-63,-113,-65,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,106,-64,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,-113,-30,]),'AND':([85,86,87,108,109,110,111,112,113,114,115,116,117,119,122,124,136,143,144,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[107,-113,-113,-63,-113,-65,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,107,-64,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,-113,-30,]),'NOT_EQ':([86,87,109,111,112,113,114,115,116,117,119,122,124,136,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[113,-113,113,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,113,-30,]),'EQ':([86,87,109,111,112,113,114,115,116,117,119,122,124,136,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[114,-113,114,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,114,-30,]),'LEQ':([86,87,109,111,112,113,114,115,116,117,119,122,124,136,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[115,-113,115,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,115,-30,]),'GEQ':([86,87,109,111,112,113,114,115,116,117,119,122,124,136,145,146,148,152,153,154,155,156,157,158,159,160,161,162,169,177,178,179,187,190,192,201,],[116,-113,116,-52,-53,-54,-55,-56,-57,-66,-72,-113,-79,-110,-113,-73,-75,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,-71,-113,-78,-36,-74,116,-30,]),'*':([122,124,136,152,153,154,155,156,157,158,159,160,161,162,169,178,179,187,201,],[149,-79,-110,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,149,-78,-36,-30,]),'/':([122,124,136,152,153,154,155,156,157,158,159,160,161,162,169,178,179,187,201,],[150,-79,-110,-80,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-112,150,-78,-36,-30,]),'ELSE':([182,205,],[198,-103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program1':([4,],[5,]),'program2':([4,],[6,]),'vars':([4,33,37,94,],[7,40,46,132,]),'empty':([4,6,20,33,37,45,52,69,74,79,81,83,85,86,87,88,91,92,93,94,101,102,104,109,118,122,123,131,135,141,143,145,147,166,173,175,178,180,182,183,192,202,203,],[8,21,21,41,47,53,53,90,97,90,90,90,105,110,119,127,90,90,90,133,139,142,90,110,90,148,90,167,171,90,105,119,127,167,139,142,148,194,199,53,110,207,171,]),'datatype':([4,6,20,27,28,33,37,38,44,94,96,],[9,23,23,35,36,9,9,49,50,9,49,]),'set_definition':([4,6,20,27,28,33,37,38,44,94,96,],[15,15,15,15,15,15,15,15,15,15,15,]),'map_definition':([4,6,20,27,28,33,37,38,44,45,52,94,96,131,166,183,],[16,16,16,16,16,16,16,16,16,60,60,16,16,60,60,60,]),'program3':([6,20,],[19,31,]),'proc':([6,20,],[20,20,]),'functype':([6,20,],[22,22,]),'vars1':([9,34,],[25,42,]),'main':([19,],[29,]),'vars2':([33,],[39,]),'vars_aux':([37,],[45,]),'proc1':([38,96,],[48,134,]),'statement_aux':([45,52,183,],[51,77,200,]),'statement':([45,52,131,166,183,],[52,52,166,166,52,]),'statement1':([45,52,131,166,183,],[54,54,54,54,54,]),'statement2':([45,52,131,166,183,],[55,55,55,55,55,]),'assignment':([45,52,131,166,183,],[56,56,56,56,56,]),'input':([45,52,131,166,183,],[57,57,57,57,57,]),'output':([45,52,131,166,183,],[58,58,58,58,58,]),'set_operation':([45,52,125,131,166,183,],[59,59,162,59,59,59,]),'return':([45,52,131,166,183,],[61,61,61,61,61,]),'map_assignment':([45,52,131,166,183,],[62,62,62,62,62,]),'map_operation':([45,52,125,131,166,183,],[63,63,161,63,63,63,]),'condition':([45,52,131,166,183,],[64,64,64,64,64,]),'while':([45,52,131,166,183,],[65,65,65,65,65,]),'map_access':([45,52,125,131,166,183,],[70,70,160,70,70,70,]),'expression':([69,79,83,92,93,123,135,141,180,202,203,],[84,98,102,129,130,151,170,175,195,195,170,]),'exp0':([69,79,83,92,93,104,123,135,141,180,202,203,],[85,85,85,85,85,143,85,85,85,85,85,85,]),'exp':([69,79,81,83,91,92,93,104,123,135,141,180,202,203,],[86,86,100,86,128,86,86,86,86,86,86,192,86,86,]),'term':([69,79,81,83,91,92,93,104,118,123,135,141,180,202,203,],[87,87,87,87,87,87,87,87,145,87,87,87,87,87,87,]),'term_not':([69,79,81,83,91,92,93,104,118,123,135,141,180,202,203,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'proc2':([74,],[95,]),'expression2':([85,143,],[103,176,]),'logop':([85,143,],[104,104,]),'exp02':([86,109,192,],[108,144,108,]),'relop':([86,109,192,],[109,109,109,]),'exp2':([87,145,],[117,177,]),'addsub':([87,88,145,147,],[118,126,118,126,]),'factor':([88,147,],[122,178,]),'factor2':([88,147,],[124,124,]),'factor3':([88,147,],[125,125,]),'proc3':([94,],[131,]),'input1':([101,173,],[137,188,]),'output1':([102,175,],[140,189,]),'term2':([122,178,],[146,190,]),'muldiv':([122,178,],[147,147,]),'varcte':([125,],[152,]),'function_call':([125,],[159,]),'proc4':([131,166,],[165,186,]),'set_operation1':([135,203,],[168,168,]),'block':([163,164,198,],[182,184,204,]),'function_call1':([180,],[191,]),'function_call2':([180,202,],[193,206,]),'condition1':([182,],[197,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID ; program1','program',4,'p_program','lexer.py',93),
  ('program1 -> program2 program3 main','program1',3,'p_program1','lexer.py',96),
  ('program2 -> vars','program2',1,'p_program2','lexer.py',99),
  ('program2 -> empty','program2',1,'p_program2','lexer.py',100),
  ('program3 -> proc program3','program3',2,'p_program3','lexer.py',103),
  ('program3 -> empty','program3',1,'p_program3','lexer.py',104),
  ('vars -> datatype vars1 ; vars2','vars',4,'p_vars','lexer.py',107),
  ('vars1 -> ID , vars1','vars1',3,'p_vars1','lexer.py',110),
  ('vars1 -> ID','vars1',1,'p_vars1','lexer.py',111),
  ('vars2 -> vars','vars2',1,'p_vars2','lexer.py',114),
  ('vars2 -> empty','vars2',1,'p_vars2','lexer.py',115),
  ('proc -> functype ID ( proc1 ) { proc3 proc4 }','proc',9,'p_proc','lexer.py',118),
  ('proc1 -> datatype ID proc2','proc1',3,'p_proc1','lexer.py',121),
  ('proc2 -> , proc1','proc2',2,'p_proc2','lexer.py',124),
  ('proc2 -> empty','proc2',1,'p_proc2','lexer.py',125),
  ('proc3 -> vars','proc3',1,'p_proc3','lexer.py',128),
  ('proc3 -> empty','proc3',1,'p_proc3','lexer.py',129),
  ('proc4 -> statement proc4','proc4',2,'p_proc4','lexer.py',132),
  ('proc4 -> empty','proc4',1,'p_proc4','lexer.py',133),
  ('assignment -> ID ASSIGNATOR expression','assignment',3,'p_assignment','lexer.py',136),
  ('condition -> IF ( expression ) block condition1','condition',6,'p_condition','lexer.py',139),
  ('condition1 -> ELSE block','condition1',2,'p_condition1','lexer.py',142),
  ('condition1 -> empty','condition1',1,'p_condition1','lexer.py',143),
  ('input -> READ ( ID input1 )','input',5,'p_input','lexer.py',146),
  ('input1 -> , ID input1','input1',3,'p_input1','lexer.py',149),
  ('input1 -> empty','input1',1,'p_input1','lexer.py',150),
  ('output -> PRINT ( expression output1 )','output',5,'p_output','lexer.py',153),
  ('output1 -> , expression output1','output1',3,'p_output1','lexer.py',156),
  ('output1 -> empty','output1',1,'p_output1','lexer.py',157),
  ('function_call -> ID ( function_call1 )','function_call',4,'p_function_call','lexer.py',160),
  ('function_call1 -> function_call2','function_call1',1,'p_function_call1','lexer.py',163),
  ('function_call1 -> empty','function_call1',1,'p_function_call1','lexer.py',164),
  ('function_call2 -> expression , function_call2','function_call2',3,'p_function_call2','lexer.py',167),
  ('function_call2 -> empty','function_call2',1,'p_function_call2','lexer.py',168),
  ('return -> RETURN expression','return',2,'p_return','lexer.py',171),
  ('set_operation -> ID . OPERATION ( set_operation1 )','set_operation',6,'p_set_operation','lexer.py',174),
  ('set_operation1 -> expression','set_operation1',1,'p_set_operation1','lexer.py',177),
  ('set_operation1 -> empty','set_operation1',1,'p_set_operation1','lexer.py',178),
  ('statement -> statement1 ;','statement',2,'p_statement','lexer.py',181),
  ('statement -> statement2','statement',1,'p_statement','lexer.py',182),
  ('statement1 -> assignment','statement1',1,'p_statement1','lexer.py',185),
  ('statement1 -> input','statement1',1,'p_statement1','lexer.py',186),
  ('statement1 -> output','statement1',1,'p_statement1','lexer.py',187),
  ('statement1 -> set_operation','statement1',1,'p_statement1','lexer.py',188),
  ('statement1 -> map_definition','statement1',1,'p_statement1','lexer.py',189),
  ('statement1 -> return','statement1',1,'p_statement1','lexer.py',190),
  ('statement1 -> map_assignment','statement1',1,'p_statement1','lexer.py',191),
  ('statement1 -> map_operation','statement1',1,'p_statement1','lexer.py',192),
  ('statement2 -> condition','statement2',1,'p_statement2','lexer.py',195),
  ('statement2 -> while','statement2',1,'p_statement2','lexer.py',196),
  ('while -> WHILE ( expression ) block','while',5,'p_while','lexer.py',199),
  ('relop -> <','relop',1,'p_relop','lexer.py',202),
  ('relop -> >','relop',1,'p_relop','lexer.py',203),
  ('relop -> NOT_EQ','relop',1,'p_relop','lexer.py',204),
  ('relop -> EQ','relop',1,'p_relop','lexer.py',205),
  ('relop -> LEQ','relop',1,'p_relop','lexer.py',206),
  ('relop -> GEQ','relop',1,'p_relop','lexer.py',207),
  ('logop -> OR','logop',1,'p_logop','lexer.py',210),
  ('logop -> AND','logop',1,'p_logop','lexer.py',211),
  ('expression -> exp0 expression2','expression',2,'p_expression','lexer.py',216),
  ('expression2 -> logop exp0 expression2','expression2',3,'p_expression2','lexer.py',219),
  ('expression2 -> empty','expression2',1,'p_expression2','lexer.py',220),
  ('exp0 -> exp exp02','exp0',2,'p_exp0','lexer.py',223),
  ('exp02 -> relop exp02','exp02',2,'p_exp02','lexer.py',226),
  ('exp02 -> empty','exp02',1,'p_exp02','lexer.py',227),
  ('exp -> term exp2','exp',2,'p_exp','lexer.py',230),
  ('addsub -> +','addsub',1,'p_addsub','lexer.py',233),
  ('addsub -> -','addsub',1,'p_addsub','lexer.py',234),
  ('muldiv -> *','muldiv',1,'p_muldiv','lexer.py',237),
  ('muldiv -> /','muldiv',1,'p_muldiv','lexer.py',238),
  ('exp2 -> addsub term exp2','exp2',3,'p_exp2','lexer.py',241),
  ('exp2 -> empty','exp2',1,'p_exp2','lexer.py',242),
  ('term -> term_not factor term2','term',3,'p_term','lexer.py',245),
  ('term2 -> muldiv factor term2','term2',3,'p_term2','lexer.py',248),
  ('term2 -> empty','term2',1,'p_term2','lexer.py',249),
  ('term_not -> !','term_not',1,'p_term_not','lexer.py',252),
  ('term_not -> empty','term_not',1,'p_term_not','lexer.py',253),
  ('factor -> ( expression )','factor',3,'p_factor','lexer.py',256),
  ('factor -> factor2','factor',1,'p_factor','lexer.py',257),
  ('factor2 -> factor3 varcte','factor2',2,'p_factor2','lexer.py',260),
  ('factor3 -> addsub','factor3',1,'p_factor3','lexer.py',263),
  ('factor3 -> empty','factor3',1,'p_factor3','lexer.py',264),
  ('varcte -> ID','varcte',1,'p_varcte','lexer.py',267),
  ('varcte -> CTE_INT','varcte',1,'p_varcte','lexer.py',268),
  ('varcte -> CTE_FLOAT','varcte',1,'p_varcte','lexer.py',269),
  ('varcte -> CTE_BOOL','varcte',1,'p_varcte','lexer.py',270),
  ('varcte -> CTE_STRING','varcte',1,'p_varcte','lexer.py',271),
  ('varcte -> CTE_CHAR','varcte',1,'p_varcte','lexer.py',272),
  ('varcte -> function_call','varcte',1,'p_varcte','lexer.py',273),
  ('varcte -> map_access','varcte',1,'p_varcte','lexer.py',274),
  ('varcte -> map_operation','varcte',1,'p_varcte','lexer.py',275),
  ('varcte -> set_operation','varcte',1,'p_varcte','lexer.py',276),
  ('datatype -> INT','datatype',1,'p_datatype','lexer.py',279),
  ('datatype -> FLOAT','datatype',1,'p_datatype','lexer.py',280),
  ('datatype -> BOOL','datatype',1,'p_datatype','lexer.py',281),
  ('datatype -> STRING','datatype',1,'p_datatype','lexer.py',282),
  ('datatype -> CHAR','datatype',1,'p_datatype','lexer.py',283),
  ('datatype -> set_definition','datatype',1,'p_datatype','lexer.py',284),
  ('datatype -> map_definition','datatype',1,'p_datatype','lexer.py',285),
  ('set_definition -> SET < datatype >','set_definition',4,'p_set_definition','lexer.py',288),
  ('functype -> datatype','functype',1,'p_functype','lexer.py',291),
  ('functype -> VOID','functype',1,'p_functype','lexer.py',292),
  ('block -> { statement_aux }','block',3,'p_block','lexer.py',295),
  ('statement_aux -> statement statement_aux','statement_aux',2,'p_statement_aux','lexer.py',298),
  ('statement_aux -> empty','statement_aux',1,'p_statement_aux','lexer.py',299),
  ('main -> MAIN { vars_aux statement_aux }','main',5,'p_main','lexer.py',302),
  ('vars_aux -> vars','vars_aux',1,'p_vars_aux','lexer.py',305),
  ('vars_aux -> empty','vars_aux',1,'p_vars_aux','lexer.py',306),
  ('map_definition -> MAP < datatype , datatype >','map_definition',6,'p_map_definition','lexer.py',309),
  ('map_access -> ID ( exp )','map_access',4,'p_map_access','lexer.py',312),
  ('map_assignment -> map_access ASSIGNATOR exp','map_assignment',3,'p_map_assignment','lexer.py',315),
  ('map_operation -> ID . OPERATION ( )','map_operation',5,'p_map_operation','lexer.py',318),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',321),
]
