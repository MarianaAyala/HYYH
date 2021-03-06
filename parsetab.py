
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY BREAK CBDER CBIZQ COMA CTE DEC DIFERENTE DISPLAY DIV DO ELSE ENTER EXECUTE FLOAT FOR FUNCT ID IF IGUAL IGUALIGUAL INT LET MAIN MAYOR MAYORQUE MENOR MENORQUE MENOS MSG MULT NOT OR PARDER PARIZQ PLUS PUNTOCOMA SBDER SBIZQ VAR WHILE\n    prog : v f MAIN CBIZQ st CBDER PUNTOCOMA\n            | v MAIN CBIZQ st CBDER PUNTOCOMA\n     v : v VAR tipo ID PUNTOCOMA\n            | v ARRAY tipo ID SBIZQ CTE SBDER PUNTOCOMA\n            | v ARRAY tipo ID SBIZQ CTE SBDER SBIZQ CTE SBDER PUNTOCOMA\n            | v ARRAY tipo ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER PUNTOCOMA\n            |\n    \n    tipo : INT\n            | DEC\n    \n    f : FUNCT ID CBIZQ st CBDER PUNTOCOMA f\n        |\n    \n    st : st LET variable IGUAL e PUNTOCOMA\n        | st ENTER SBIZQ variable SBDER PUNTOCOMA\n        | st DISPLAY SBIZQ MSG COMA variable SBDER PUNTOCOMA\n        | st DISPLAY SBIZQ MSG SBDER PUNTOCOMA\n        | st IF PARIZQ cond PARDER ifAux CBIZQ st CBDER PUNTOCOMA ifEndAux\n        | st IF PARIZQ cond PARDER ifAux CBIZQ st CBDER PUNTOCOMA ELSE ifAuxElse CBIZQ st CBDER PUNTOCOMA ifEndAux\n        | st auxIniWhile WHILE PARIZQ cond PARDER auxFauxWhile CBIZQ st CBDER PUNTOCOMA auxFinWhile\n        | st auxIniFor FOR PARIZQ cond auxFauxFor PUNTOCOMA e auxAssignFor PARDER CBIZQ st CBDER PUNTOCOMA auxFinFor\n        | st DO auxIniLoop CBIZQ st CBDER PUNTOCOMA auxFinLoop\n        | st LET variable IGUAL IF PARIZQ cond PARDER ifAux CBIZQ CTE PUNTOCOMA CBDER PUNTOCOMA ifEndAuxEsp\n        | st LET variable IGUAL IF PARIZQ cond PARDER ifAux CBIZQ CTE CBDER PUNTOCOMA ELSE ifAuxElse CBIZQ CTE CBDER PUNTOCOMA ifEndAux\n        | st BREAK auxFauxLoop PUNTOCOMA\n        |\n    ifAux : ifAuxElse : ifEndAux : ifEndAuxEsp : auxIniWhile : auxFauxWhile : auxFinWhile : auxIniFor : auxFauxFor : auxFinFor : auxAssignFor : auxIniLoop : auxFauxLoop : auxFinLoop : \n    variable : ID\n                | ID SBIZQ CTE SBDER\n                | ID SBIZQ CTE SBDER SBIZQ CTE SBDER\n                | ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER\n                | ID SBIZQ ID SBDER\n                | ID SBIZQ ID SBDER SBIZQ ID SBDER\n                | ID SBIZQ ID SBDER SBIZQ ID SBDER SBIZQ ID SBDER\n    \n    cond : oprel\n            | cond AND oprel\n            | cond OR oprel\n    \n    oprel :  operador IGUALIGUAL operador\n            | operador DIFERENTE operador\n            | operador MAYOR operador\n            | operador MENOR operador\n            | operador MAYORQUE operador\n            | operador MENORQUE operador\n            | PARIZQ oprel PARDER\n            | NOT PARIZQ oprel PARDER\n    \n    e : e PLUS t\n        | e MENOS t\n        | t\n    \n    t : t MULT m\n        | t DIV m\n        | m\n    \n    m : PARIZQ e PARDER\n        | operador\n    \n    operador : CTE\n               | FLOAT\n               | ID\n               | ID SBIZQ CTE SBDER\n               | ID SBIZQ CTE SBDER SBIZQ CTE SBDER\n               | ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER\n               | ID SBIZQ ID SBDER\n               | ID SBIZQ ID SBDER SBIZQ ID SBDER\n               | ID SBIZQ ID SBDER SBIZQ ID SBDER SBIZQ ID SBDER\n    '
    
_lr_action_items = {'MAIN':([0,2,3,30,64,92,93,151,179,],[-7,4,8,-3,-11,-4,-10,-5,-6,]),'VAR':([0,2,30,92,151,179,],[-7,5,-3,-4,-5,-6,]),'ARRAY':([0,2,30,92,151,179,],[-7,6,-3,-4,-5,-6,]),'FUNCT':([0,2,30,64,92,151,179,],[-7,7,-3,7,-4,-5,-6,]),'$end':([1,34,46,],[0,-2,-1,]),'CBIZQ':([4,8,14,28,42,77,107,119,136,140,152,168,174,184,196,200,],[9,15,19,-36,61,-25,132,-30,147,-25,161,178,-26,191,-26,203,]),'INT':([5,6,],[11,11,]),'DEC':([5,6,],[12,12,]),'ID':([7,10,11,12,13,22,37,39,47,48,51,59,60,67,74,78,79,80,81,82,83,84,85,86,87,95,96,97,99,100,129,137,145,162,175,],[14,17,-8,-9,18,36,36,58,58,71,58,58,58,58,36,58,58,58,58,58,58,58,58,58,117,58,58,58,58,58,141,58,156,171,185,]),'CBDER':([9,15,16,19,20,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,170,173,177,178,180,187,188,191,195,197,198,199,202,204,205,206,208,209,],[-24,-24,21,-24,33,45,-24,-23,121,-12,-13,-15,-24,-38,-14,155,-24,-20,167,-27,181,-16,-31,-24,189,-18,194,-24,-28,201,-34,-21,-19,-27,207,-17,-27,-22,]),'LET':([9,15,16,19,20,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,22,-24,22,22,-24,-23,22,-12,-13,-15,-24,-38,-14,22,-24,-20,22,-27,-16,-31,-24,-18,22,-24,-28,22,-34,-21,-19,-27,-17,-27,-22,]),'ENTER':([9,15,16,19,20,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,23,-24,23,23,-24,-23,23,-12,-13,-15,-24,-38,-14,23,-24,-20,23,-27,-16,-31,-24,-18,23,-24,-28,23,-34,-21,-19,-27,-17,-27,-22,]),'DISPLAY':([9,15,16,19,20,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,24,-24,24,24,-24,-23,24,-12,-13,-15,-24,-38,-14,24,-24,-20,24,-27,-16,-31,-24,-18,24,-24,-28,24,-34,-21,-19,-27,-17,-27,-22,]),'IF':([9,15,16,19,20,32,47,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,25,-24,25,25,66,-24,-23,25,-12,-13,-15,-24,-38,-14,25,-24,-20,25,-27,-16,-31,-24,-18,25,-24,-28,25,-34,-21,-19,-27,-17,-27,-22,]),'DO':([9,15,16,19,20,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,28,-24,28,28,-24,-23,28,-12,-13,-15,-24,-38,-14,28,-24,-20,28,-27,-16,-31,-24,-18,28,-24,-28,28,-34,-21,-19,-27,-17,-27,-22,]),'BREAK':([9,15,16,19,20,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,29,-24,29,29,-24,-23,29,-12,-13,-15,-24,-38,-14,29,-24,-20,29,-27,-16,-31,-24,-18,29,-24,-28,29,-34,-21,-19,-27,-17,-27,-22,]),'WHILE':([9,15,16,19,20,26,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,-29,-24,-29,40,-29,-24,-23,-29,-12,-13,-15,-24,-38,-14,-29,-24,-20,-29,-27,-16,-31,-24,-18,-29,-24,-28,-29,-34,-21,-19,-27,-17,-27,-22,]),'FOR':([9,15,16,19,20,27,32,61,62,90,94,103,105,132,138,143,144,147,149,158,164,173,177,178,187,188,191,195,197,198,199,202,204,206,208,209,],[-24,-24,-32,-24,-32,41,-32,-24,-23,-32,-12,-13,-15,-24,-38,-14,-32,-24,-20,-32,-27,-16,-31,-24,-18,-32,-24,-28,-32,-34,-21,-19,-27,-17,-27,-22,]),'PUNTOCOMA':([17,21,29,33,43,45,53,56,57,58,63,65,68,69,70,73,75,89,106,108,109,110,111,112,113,114,115,120,121,123,124,126,127,128,131,133,134,135,139,155,165,166,167,169,170,181,189,192,193,194,201,207,],[30,34,-37,46,62,64,-46,-65,-66,-67,92,94,-59,-62,-64,103,105,-33,-55,-47,-48,-49,-50,-51,-52,-53,-54,137,138,-57,-58,-63,-60,-61,143,-56,-71,-68,151,164,-72,-69,177,179,180,190,195,-73,-70,198,204,208,]),'SBIZQ':([18,23,24,36,58,63,101,102,134,135,139,153,154,165,166,],[31,37,38,48,87,91,129,130,145,146,150,162,163,175,176,]),'PARIZQ':([25,39,40,41,47,51,55,59,60,66,67,78,79,86,95,96,97,99,100,137,],[39,51,59,60,67,51,86,51,51,97,67,51,51,51,67,67,51,67,67,67,]),'CTE':([31,39,47,48,51,59,60,67,78,79,80,81,82,83,84,85,86,87,91,95,96,97,99,100,130,137,146,150,161,163,176,203,],[44,56,56,72,56,56,56,56,56,56,56,56,56,56,56,56,56,118,122,56,56,56,56,56,142,56,157,160,170,172,186,205,]),'IGUAL':([35,36,101,102,153,154,182,183,],[47,-39,-43,-40,-44,-41,-45,-42,]),'SBDER':([36,44,49,50,71,72,101,102,104,117,118,122,141,142,153,154,156,157,160,171,172,182,183,185,186,],[-39,63,73,75,101,102,-43,-40,131,134,135,139,153,154,-44,-41,165,166,169,182,183,-45,-42,192,193,]),'MSG':([38,],[50,]),'NOT':([39,51,59,60,78,79,86,97,],[55,55,55,55,55,55,55,55,]),'FLOAT':([39,47,51,59,60,67,78,79,80,81,82,83,84,85,86,95,96,97,99,100,137,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'COMA':([50,],[74,]),'PARDER':([52,53,56,57,58,68,69,70,76,88,98,106,108,109,110,111,112,113,114,115,116,123,124,125,126,127,128,133,134,135,148,159,165,166,192,193,],[77,-46,-65,-66,-67,-59,-62,-64,106,119,126,-55,-47,-48,-49,-50,-51,-52,-53,-54,133,-57,-58,140,-63,-60,-61,-56,-71,-68,-35,168,-72,-69,-73,-70,]),'AND':([52,53,56,57,58,88,89,106,108,109,110,111,112,113,114,115,125,133,134,135,165,166,192,193,],[78,-46,-65,-66,-67,78,78,-55,-47,-48,-49,-50,-51,-52,-53,-54,78,-56,-71,-68,-72,-69,-73,-70,]),'OR':([52,53,56,57,58,88,89,106,108,109,110,111,112,113,114,115,125,133,134,135,165,166,192,193,],[79,-46,-65,-66,-67,79,79,-55,-47,-48,-49,-50,-51,-52,-53,-54,79,-56,-71,-68,-72,-69,-73,-70,]),'IGUALIGUAL':([54,56,57,58,134,135,165,166,192,193,],[80,-65,-66,-67,-71,-68,-72,-69,-73,-70,]),'DIFERENTE':([54,56,57,58,134,135,165,166,192,193,],[81,-65,-66,-67,-71,-68,-72,-69,-73,-70,]),'MAYOR':([54,56,57,58,134,135,165,166,192,193,],[82,-65,-66,-67,-71,-68,-72,-69,-73,-70,]),'MENOR':([54,56,57,58,134,135,165,166,192,193,],[83,-65,-66,-67,-71,-68,-72,-69,-73,-70,]),'MAYORQUE':([54,56,57,58,134,135,165,166,192,193,],[84,-65,-66,-67,-71,-68,-72,-69,-73,-70,]),'MENORQUE':([54,56,57,58,134,135,165,166,192,193,],[85,-65,-66,-67,-71,-68,-72,-69,-73,-70,]),'MULT':([56,57,58,68,69,70,123,124,126,127,128,134,135,165,166,192,193,],[-65,-66,-67,99,-62,-64,99,99,-63,-60,-61,-71,-68,-72,-69,-73,-70,]),'DIV':([56,57,58,68,69,70,123,124,126,127,128,134,135,165,166,192,193,],[-65,-66,-67,100,-62,-64,100,100,-63,-60,-61,-71,-68,-72,-69,-73,-70,]),'PLUS':([56,57,58,65,68,69,70,98,123,124,126,127,128,134,135,148,165,166,192,193,],[-65,-66,-67,95,-59,-62,-64,95,-57,-58,-63,-60,-61,-71,-68,95,-72,-69,-73,-70,]),'MENOS':([56,57,58,65,68,69,70,98,123,124,126,127,128,134,135,148,165,166,192,193,],[-65,-66,-67,96,-59,-62,-64,96,-57,-58,-63,-60,-61,-71,-68,96,-72,-69,-73,-70,]),'ELSE':([164,190,],[174,196,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'v':([0,],[2,]),'f':([2,64,],[3,93,]),'tipo':([5,6,],[10,13,]),'st':([9,15,19,61,132,147,178,191,],[16,20,32,90,144,158,188,197,]),'auxIniWhile':([16,20,32,90,144,158,188,197,],[26,26,26,26,26,26,26,26,]),'auxIniFor':([16,20,32,90,144,158,188,197,],[27,27,27,27,27,27,27,27,]),'variable':([22,37,74,],[35,49,104,]),'auxIniLoop':([28,],[42,]),'auxFauxLoop':([29,],[43,]),'cond':([39,59,60,97,],[52,88,89,125,]),'oprel':([39,51,59,60,78,79,86,97,],[53,76,53,53,108,109,116,53,]),'operador':([39,47,51,59,60,67,78,79,80,81,82,83,84,85,86,95,96,97,99,100,137,],[54,70,54,54,54,70,54,54,110,111,112,113,114,115,54,70,70,54,70,70,70,]),'e':([47,67,137,],[65,98,148,]),'t':([47,67,95,96,137,],[68,68,123,124,68,]),'m':([47,67,95,96,99,100,137,],[69,69,69,69,127,128,69,]),'ifAux':([77,140,],[107,152,]),'auxFauxFor':([89,],[120,]),'auxFauxWhile':([119,],[136,]),'auxFinLoop':([138,],[149,]),'auxAssignFor':([148,],[159,]),'ifEndAux':([164,204,208,],[173,206,209,]),'ifAuxElse':([174,196,],[184,200,]),'auxFinWhile':([177,],[187,]),'ifEndAuxEsp':([195,],[199,]),'auxFinFor':([198,],[202,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> v f MAIN CBIZQ st CBDER PUNTOCOMA','prog',7,'p_prog','syntax.py',362),
  ('prog -> v MAIN CBIZQ st CBDER PUNTOCOMA','prog',6,'p_prog','syntax.py',363),
  ('v -> v VAR tipo ID PUNTOCOMA','v',5,'p_v','syntax.py',368),
  ('v -> v ARRAY tipo ID SBIZQ CTE SBDER PUNTOCOMA','v',8,'p_v','syntax.py',369),
  ('v -> v ARRAY tipo ID SBIZQ CTE SBDER SBIZQ CTE SBDER PUNTOCOMA','v',11,'p_v','syntax.py',370),
  ('v -> v ARRAY tipo ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER PUNTOCOMA','v',14,'p_v','syntax.py',371),
  ('v -> <empty>','v',0,'p_v','syntax.py',372),
  ('tipo -> INT','tipo',1,'p_tipo','syntax.py',439),
  ('tipo -> DEC','tipo',1,'p_tipo','syntax.py',440),
  ('f -> FUNCT ID CBIZQ st CBDER PUNTOCOMA f','f',7,'p_f','syntax.py',447),
  ('f -> <empty>','f',0,'p_f','syntax.py',448),
  ('st -> st LET variable IGUAL e PUNTOCOMA','st',6,'p_st','syntax.py',454),
  ('st -> st ENTER SBIZQ variable SBDER PUNTOCOMA','st',6,'p_st','syntax.py',455),
  ('st -> st DISPLAY SBIZQ MSG COMA variable SBDER PUNTOCOMA','st',8,'p_st','syntax.py',456),
  ('st -> st DISPLAY SBIZQ MSG SBDER PUNTOCOMA','st',6,'p_st','syntax.py',457),
  ('st -> st IF PARIZQ cond PARDER ifAux CBIZQ st CBDER PUNTOCOMA ifEndAux','st',11,'p_st','syntax.py',458),
  ('st -> st IF PARIZQ cond PARDER ifAux CBIZQ st CBDER PUNTOCOMA ELSE ifAuxElse CBIZQ st CBDER PUNTOCOMA ifEndAux','st',17,'p_st','syntax.py',459),
  ('st -> st auxIniWhile WHILE PARIZQ cond PARDER auxFauxWhile CBIZQ st CBDER PUNTOCOMA auxFinWhile','st',12,'p_st','syntax.py',460),
  ('st -> st auxIniFor FOR PARIZQ cond auxFauxFor PUNTOCOMA e auxAssignFor PARDER CBIZQ st CBDER PUNTOCOMA auxFinFor','st',15,'p_st','syntax.py',461),
  ('st -> st DO auxIniLoop CBIZQ st CBDER PUNTOCOMA auxFinLoop','st',8,'p_st','syntax.py',462),
  ('st -> st LET variable IGUAL IF PARIZQ cond PARDER ifAux CBIZQ CTE PUNTOCOMA CBDER PUNTOCOMA ifEndAuxEsp','st',15,'p_st','syntax.py',463),
  ('st -> st LET variable IGUAL IF PARIZQ cond PARDER ifAux CBIZQ CTE CBDER PUNTOCOMA ELSE ifAuxElse CBIZQ CTE CBDER PUNTOCOMA ifEndAux','st',20,'p_st','syntax.py',464),
  ('st -> st BREAK auxFauxLoop PUNTOCOMA','st',4,'p_st','syntax.py',465),
  ('st -> <empty>','st',0,'p_st','syntax.py',466),
  ('ifAux -> <empty>','ifAux',0,'p_ifAux','syntax.py',495),
  ('ifAuxElse -> <empty>','ifAuxElse',0,'p_ifAuxElse','syntax.py',503),
  ('ifEndAux -> <empty>','ifEndAux',0,'p_ifEndAux','syntax.py',513),
  ('ifEndAuxEsp -> <empty>','ifEndAuxEsp',0,'p_ifEndAuxEsp','syntax.py',520),
  ('auxIniWhile -> <empty>','auxIniWhile',0,'p_auxIniWhile','syntax.py',527),
  ('auxFauxWhile -> <empty>','auxFauxWhile',0,'p_auxFauxWhile','syntax.py',533),
  ('auxFinWhile -> <empty>','auxFinWhile',0,'p_auxFinWhile','syntax.py',541),
  ('auxIniFor -> <empty>','auxIniFor',0,'p_auxIniFor','syntax.py',550),
  ('auxFauxFor -> <empty>','auxFauxFor',0,'p_auxFauxFor','syntax.py',556),
  ('auxFinFor -> <empty>','auxFinFor',0,'p_auxFinFor','syntax.py',565),
  ('auxAssignFor -> <empty>','auxAssignFor',0,'p_auxAssignFor','syntax.py',574),
  ('auxIniLoop -> <empty>','auxIniLoop',0,'p_auxIniLoop','syntax.py',583),
  ('auxFauxLoop -> <empty>','auxFauxLoop',0,'p_auxFauxLoop','syntax.py',589),
  ('auxFinLoop -> <empty>','auxFinLoop',0,'p_auxFinLoop','syntax.py',596),
  ('variable -> ID','variable',1,'p_variable','syntax.py',607),
  ('variable -> ID SBIZQ CTE SBDER','variable',4,'p_variable','syntax.py',608),
  ('variable -> ID SBIZQ CTE SBDER SBIZQ CTE SBDER','variable',7,'p_variable','syntax.py',609),
  ('variable -> ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER','variable',10,'p_variable','syntax.py',610),
  ('variable -> ID SBIZQ ID SBDER','variable',4,'p_variable','syntax.py',611),
  ('variable -> ID SBIZQ ID SBDER SBIZQ ID SBDER','variable',7,'p_variable','syntax.py',612),
  ('variable -> ID SBIZQ ID SBDER SBIZQ ID SBDER SBIZQ ID SBDER','variable',10,'p_variable','syntax.py',613),
  ('cond -> oprel','cond',1,'p_cond','syntax.py',633),
  ('cond -> cond AND oprel','cond',3,'p_cond','syntax.py',634),
  ('cond -> cond OR oprel','cond',3,'p_cond','syntax.py',635),
  ('oprel -> operador IGUALIGUAL operador','oprel',3,'p_oprel','syntax.py',651),
  ('oprel -> operador DIFERENTE operador','oprel',3,'p_oprel','syntax.py',652),
  ('oprel -> operador MAYOR operador','oprel',3,'p_oprel','syntax.py',653),
  ('oprel -> operador MENOR operador','oprel',3,'p_oprel','syntax.py',654),
  ('oprel -> operador MAYORQUE operador','oprel',3,'p_oprel','syntax.py',655),
  ('oprel -> operador MENORQUE operador','oprel',3,'p_oprel','syntax.py',656),
  ('oprel -> PARIZQ oprel PARDER','oprel',3,'p_oprel','syntax.py',657),
  ('oprel -> NOT PARIZQ oprel PARDER','oprel',4,'p_oprel','syntax.py',658),
  ('e -> e PLUS t','e',3,'p_e','syntax.py',696),
  ('e -> e MENOS t','e',3,'p_e','syntax.py',697),
  ('e -> t','e',1,'p_e','syntax.py',698),
  ('t -> t MULT m','t',3,'p_t','syntax.py',716),
  ('t -> t DIV m','t',3,'p_t','syntax.py',717),
  ('t -> m','t',1,'p_t','syntax.py',718),
  ('m -> PARIZQ e PARDER','m',3,'p_m','syntax.py',736),
  ('m -> operador','m',1,'p_m','syntax.py',737),
  ('operador -> CTE','operador',1,'p_operador','syntax.py',748),
  ('operador -> FLOAT','operador',1,'p_operador','syntax.py',749),
  ('operador -> ID','operador',1,'p_operador','syntax.py',750),
  ('operador -> ID SBIZQ CTE SBDER','operador',4,'p_operador','syntax.py',751),
  ('operador -> ID SBIZQ CTE SBDER SBIZQ CTE SBDER','operador',7,'p_operador','syntax.py',752),
  ('operador -> ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER','operador',10,'p_operador','syntax.py',753),
  ('operador -> ID SBIZQ ID SBDER','operador',4,'p_operador','syntax.py',754),
  ('operador -> ID SBIZQ ID SBDER SBIZQ ID SBDER','operador',7,'p_operador','syntax.py',755),
  ('operador -> ID SBIZQ ID SBDER SBIZQ ID SBDER SBIZQ ID SBDER','operador',10,'p_operador','syntax.py',756),
]
