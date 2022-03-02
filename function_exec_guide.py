import ply.yacc as yacc
import time

from analizador_lexico import tokens


tabla_Simbolos = {}
operandos = []
cuadruplos = []
temporales = []
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

def genera_cuadruplo(opcode, operando1, operando2, resulatado):
    if (opcode) == "PLUS":
        resultado = operando1 + operando2
    elif opcode == "MINUS":
        resultado = operando1 - operando2
    elif opcode == "MULT":
        resultado = operando1 * operando2
    elif opcode == "DIV":
        if operando1 % operando2 == 0:
            resultado = operando1 // operando2
        else:
            resultado = operando1 / operando2
    elif opcode == "IGUAL":
        if operando1 == operando2:
            resultado = True
        else:
            resultado = False
    elif opcode == "DESIGUAL":
        if operando1 != operando2:
            resultado = True
        else:
            resultado = False
    elif opcode == "MAYOR":
        if operando1 > operando2:
            resultado = True
        else:
            resultado = False
    elif opcode == "MENOR":
        if operando1 < operando2:
            resultado = True
        else:
            resultado = False
    elif opcode == "MAYOR_IGUAL":
        if operando1 >= operando2:
            resultado = True
        else:
            resultado = False
    elif opcode == "MENOR_IGUAL":
        if operando1 <= operando2:
            resultado = True
        else:
            resultado = False
    elif opcode == "AND":
        resultado = operando1 and operando2
    elif opcode == "OR":
        resultado = operando1 or operando2
    elif opcode == "NOT":
        resultado = not operando1
    print ("Operacion: {0}, Resultado:{1}".format(opcode, resultado))
    return resultado



def p_prog(p):
    """
    prog : v f MAIN CBIZQ st CBDER PUNTOCOMA
            | v MAIN CBIZQ st CBDER PUNTOCOMA
    """


def p_v(p):
    """ v : v VAR tipo ID PUNTOCOMA
            | v ARRAY tipo ID SBIZQ CTE SBDER PUNTOCOMA
            | v ARRAY tipo ID SBIZQ CTE SBDER SBIZQ CTE SBDER PUNTOCOMA
            | v ARRAY tipo ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER PUNTOCOMA
            |
    """
    if len(p) > 2:
        if p[2] == "VAR":
            if tabla_Simbolos.get(p[4]) is None:
                tabla_Simbolos[p[4]] = {}
                tabla_Simbolos[p[4]]['TYPE'] = p[3]
                tabla_Simbolos[p[4]]['VALUE'] = 0
            else:
                print("ERROR WITH ID {:1}: Variables can't be declared with the same name twice".format(p[4]))
                raise Exception


def p_tipo(p):
    """
    tipo : INT
            | DEC
    """
    p[0] = p[1]


def p_f(p):
    """
    f : FUNCT ID CBIZQ st CBDER PUNTOCOMA f
        |
    """


def p_st(p):
    """
    st : st LET variable IGUAL e PUNTOCOMA
        | st ENTER SBIZQ variable SBDER PUNTOCOMA
        | st DISPLAY SBIZQ MSG COMA variable SBDER PUNTOCOMA
        | st DISPLAY SBIZQ MSG SBDER PUNTOCOMA
        | st DISPLAY SBIZQ variable SBDER PUNTOCOMA
        | st EXECUTE variable PUNTOCOMA
        | st IF PARIZQ cond PARDER CBIZQ st CBDER PUNTOCOMA
        | st IF PARIZQ cond PARDER CBIZQ st CBDER PUNTOCOMA ELSE CBIZQ st CBDER PUNTOCOMA
        | st LET variable IGUAL IF PARIZQ cond PARDER CBIZQ CTE CBDER PUNTOCOMA ELSE CBIZQ CTE CBDER PUNTOCOMA
        | st LET variable IGUAL IF PARIZQ cond PARDER CBIZQ CTE CBDER PUNTOCOMA
        | st WHILE PARIZQ cond PARDER CBIZQ st CBDER PUNTOCOMA
        | st FOR PARIZQ cond PUNTOCOMA e PARDER CBIZQ st CBDER PUNTOCOMA
        | st LOOP CBIZQ st CBDER PUNTOCOMA
        | st BREAK PUNTOCOMA
        |
    """
    if len(p) > 2:
        if p[2] == 'LET':
            oper1 = operandos.pop()
            oper2 = operandos.pop()
            cuadruplos.append(("ASSIGN", oper1, oper2))
            if (type(oper1) is int) and (tabla_Simbolos[oper2]['TYPE'] == 'INT'):
                tabla_Simbolos[oper2]['VALUE'] = oper1
            elif (type(oper1) is not int) and (tabla_Simbolos[oper2]['TYPE'] == 'DEC'):
                tabla_Simbolos[oper2]['VALUE'] = oper1
            else:
                print("* NON MATCHING DATA TYPES *")
                raise Exception()



def p_variable(p):
    """
    variable : ID
                | ID SBIZQ CTE SBDER
                | ID SBIZQ CTE SBDER SBIZQ CTE SBDER
                | ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER
                | ID SBIZQ ID SBDER
                | ID SBIZQ ID SBDER SBIZQ ID SBDER
                | ID SBIZQ ID SBDER SBIZQ ID SBDER SBIZQ ID SBDER
    """
    if len(p) == 2:
        p[0] = p[1]
        operandos.append(p[1])


def p_cond(p):
    """
    cond : oprel
            | cond AND oprel
            | cond OR oprel
    """
    global temp4
    if len(p)>2:
        if p[2] == 'AND' or p[2] == 'OR':
            oper2 = operandos.pop()
            oper1 = operandos.pop()
            if p[2] == 'AND':
                result = genera_cuadruplo("AND", oper1, oper2, temp4)
                cuadruplos.append(("AND", oper1, oper2, temp4))
            elif p[2] == 'OR':
                result = genera_cuadruplo("OR", oper1, oper2, temp4)
                cuadruplos.append(("OR", oper1, oper2, temp4))
            operandos.append(result)


def p_oprel(p):
    """
    oprel :  operador IGUALIGUAL operador
            | operador DIFERENTE operador
            | operador MAYOR operador
            | operador MENOR operador
            | operador MAYORQUE operador
            | operador MENORQUE operador
            | PARIZQ oprel PARDER
            | NOT PARIZQ oprel PARDER
    """
    global temp3
    if p[1] == '(':
        p[0] = p[2]
    elif p[1] == 'NOT':
        p[0] = p[3]
        oper1 = operandos.pop()
        result = genera_cuadruplo("NOT", oper1, 0,0)
        cuadruplos.append(("NOT", oper1, 0,0))
        operandos.append(result)
    else:
        p[0] = p[1]
        oper2 = operandos.pop()
        oper1 = operandos.pop()
        if p[2] == '==':
            result = genera_cuadruplo("IGUAL", oper1, oper2, temp3)
            cuadruplos.append(("IGUAL", oper1, oper2, temp3))
        elif p[2] == '!=':
            result = genera_cuadruplo("DESIGUAL", oper1, oper2, temp3)
            cuadruplos.append(("DESIGUAL", oper1, oper2, temp3))
        elif p[2] == '>':
            result = genera_cuadruplo("MAYOR", oper1, oper2, temp3)
            cuadruplos.append(("MAYOR", oper1, oper2, temp3))
        elif p[2] == '<':
            result = genera_cuadruplo("MENOR", oper1, oper2, temp3)
            cuadruplos.append(("MENOR", oper1, oper2, temp3))
        elif p[2] == '>=':
            result = genera_cuadruplo("MAYOR_IGUAL", oper1, oper2, temp3)
            cuadruplos.append(("MAYOR_IGUAL", oper1, oper2, temp3))
        elif p[2] == '<=':
            result = genera_cuadruplo("MENOR_IGUAL", oper1, oper2, temp3)
            cuadruplos.append(("MENOR_IGUAL", oper1, oper2, temp3))
        operandos.append(result)




def p_e(p):
    """
    e : e PLUS t
        | e MENOS t
        | t
    """
    global temp1
    if len(p) > 2:
        oper2 = operandos.pop()
        oper1 = operandos.pop()
        if p[2] == '+':
            result = genera_cuadruplo("PLUS", oper1, oper2, temp1)
            cuadruplos.append(("PLUS", oper1, oper2, temp1))

        elif p[2] == '-':
                result = genera_cuadruplo("MINUS", oper1, oper2, temp1)
                cuadruplos.append(("MINUS", oper1, oper2, temp1))
        operandos.append(result)
        p[0] = p[3]
    else:
        p[0] = p[1]


def p_t(p):
    """
    t : t MULT m
        | t DIV m
        | m
    """
    global temp2
    if len(p) > 2:
        oper2 = operandos.pop()
        oper1 = operandos.pop()
        if p[2] == '*':
            result = genera_cuadruplo("MULT", oper1, oper2, temp2)
            cuadruplos.append(("MULT", oper1, oper2, temp2))

        elif p[2] == '/':
            result = genera_cuadruplo("DIV", oper1, oper2, temp2)
            cuadruplos.append(("DIV", oper1, oper2, temp2))
        operandos.append(result)
        p[0] = p[3]
    else:
        p[0] = p[1]


def p_m(p):
    """
    m : PARIZQ e PARDER
        | operador
    """
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_operador(p):
    """
    operador : CTE
               | FLOAT
               | ID
    """
    p[0] = p[1]
    if p[0] in tabla_Simbolos.keys():
        operandos.append(tabla_Simbolos[p[0]]["VALUE"])
    else:
        operandos.append(p[0])


def p_error(token):
    if token is not None:
        print("Line %s, illegal token: %s" % (token.lineno, token.value))
    else:
        print('Unexpected end of input')
    raise SyntaxError("SYNTAX ERROR")


parser = yacc.yacc()
myfile = open("prueba3.txt")
code = myfile.read()
code_count = len(code)
myfile.close()
result = parser.parse(code)
print('\n')
print("Compilation complete! Errors: ", result)

print('\n')
variable_list = list(tabla_Simbolos)
for i in range(len(tabla_Simbolos)):
    current_ID = variable_list[i]
    print("Table Index: {0}, ID: {1}, Tipo: {2}".format(i, current_ID, tabla_Simbolos[current_ID]["TYPE"]))

print('\n')

for i in range(len(cuadruplos)):
    print ("Cuadruplo {0} = {1} ".format(i, cuadruplos[i]))

print('\n')

print (cuadruplos)