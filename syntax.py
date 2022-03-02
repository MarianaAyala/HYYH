import ply.yacc as yacc
import math
import time

from analizador_lexico import tokens


tabla_Simbolos = {}
operandos = []
saltos = []
cuadruplos = {}
contador_cuadruplos = 0
contador_ciclos = 0
temporales = [x for x in range(1000, 0, -1)]
MATRIX_SPACE = []
array_control = {}
base_matrix = 0
PC = 0
array_per_cuadruplo = 0


def genera_cuadruplo(opcode, operando1, operando2 = None, resultado = None):
    global contador_cuadruplos
    cuadruplos[contador_cuadruplos] = {}
    cuadruplos[contador_cuadruplos]["OPCODE"] = opcode
    cuadruplos[contador_cuadruplos]["op1"] = operando1
    cuadruplos[contador_cuadruplos]["op2"] = operando2
    cuadruplos[contador_cuadruplos]["temp"] = resultado
    contador_cuadruplos += 1


def genera_cuadruplo_ciclos(opcode, operando1 = None, Ref = None):
    global contador_cuadruplos
    cuadruplos[contador_cuadruplos] = {}
    cuadruplos[contador_cuadruplos]["OPCODE"] = opcode
    cuadruplos[contador_cuadruplos]["DirBase"] = operando1
    cuadruplos[contador_cuadruplos]["Ref"] = Ref
    contador_cuadruplos += 1


def genera_cuadruplo_input(opcode, operando1 = None):
    global contador_cuadruplos
    cuadruplos[contador_cuadruplos] = {}
    cuadruplos[contador_cuadruplos]["OPCODE"] = opcode
    cuadruplos[contador_cuadruplos]["variable"] = operando1
    contador_cuadruplos += 1


def genera_cuadruplo_output(opcode, operando1 = None, operando2 = None):
    global contador_cuadruplos
    cuadruplos[contador_cuadruplos] = {}
    cuadruplos[contador_cuadruplos]["OPCODE"] = opcode
    cuadruplos[contador_cuadruplos]["string"] = operando1
    cuadruplos[contador_cuadruplos]["variable"] = operando2
    contador_cuadruplos += 1


def ajusta_saltos(direccion_cuadruplo, direccion_salto):
    global contador_cuadruplos
    cuadruplos[direccion_cuadruplo]["Ref"] = direccion_salto


def execution(numero_instruccion, tipo_instruccion):
    resultado = 0
    global PC
    #print("Cuadruplo en curso: ", cuadruplos[numero_instruccion])
    if tipo_instruccion != "GOTO_FALSO" and tipo_instruccion != "GOTO":
        if tipo_instruccion != "ASSIGN":
            if tipo_instruccion == "INPUT":
                variable_destino = cuadruplos[numero_instruccion]["variable"]
                print("Introduce el valor de la variable {0}".format(variable_destino))
                temporal = input()

                if tabla_Simbolos[variable_destino]['TYPE'] == 'INT':
                    temporal = int(float(temporal))
                    tabla_Simbolos[variable_destino]['VALUE'] = temporal
                elif tabla_Simbolos[variable_destino]['TYPE'] == 'DEC':
                    tabla_Simbolos[variable_destino]['VALUE'] = float(temporal)
            elif tipo_instruccion == "OUTPUT":
                msg = cuadruplos[numero_instruccion]["string"]
                msg = msg[:-1]
                msg = msg[1:]
                if(cuadruplos[numero_instruccion]["variable"] is None):
                    print(msg)
                else:
                    var = cuadruplos[numero_instruccion]["variable"]
                    valor_var = tabla_Simbolos[var]['VALUE']
                    print(msg, valor_var)

            else:
                operando1 = cuadruplos[numero_instruccion]["op1"]
                operando2 = cuadruplos[numero_instruccion]["op2"]

                if type(operando1) == type(2) or type(operando1) == type(3.45):
                    operando1 = operando1
                else:
                    if operando1 in tabla_Simbolos.keys():
                        operando1 = tabla_Simbolos[operando1]["VALUE"]
                    elif operando1[:1] == 'T':
                        aux_temp = operando1[1:]
                        operando1 = temporales[int(aux_temp)]

                if type(operando2) == type(2) or type(operando2) == type(3.45):
                    operando2 = operando2
                else:
                    if operando2 in tabla_Simbolos.keys():
                        operando2 = tabla_Simbolos[operando2]["VALUE"]
                    elif operando2[:1] == 'T':
                        aux_temp = operando2[1:]
                        operando2 = temporales[int(aux_temp)]

                #print("Operando 1 final: ", operando1)
                #print("Operando 2 final: ", operando2)

                if tipo_instruccion == "PLUS":
                    resultado = operando1 + operando2
                elif tipo_instruccion == "MINUS":
                    resultado = operando1 - operando2
                elif tipo_instruccion == "MULTIPLY":
                    resultado = operando1 * operando2
                elif tipo_instruccion == "DIV":
                    if operando1 % operando2 == 0:
                        resultado = operando1 // operando2
                    else:
                        resultado = operando1 / operando2
                elif tipo_instruccion == "IGUAL":
                    if operando1 == operando2:
                        resultado = True
                    else:
                        resultado = False
                elif tipo_instruccion == "DESIGUAL":
                    if operando1 != operando2:
                        resultado = True
                    else:
                        resultado = False
                elif tipo_instruccion == "MAYOR":
                    if operando1 > operando2:
                        resultado = True
                    else:
                        resultado = False
                elif tipo_instruccion == "MENOR":
                    if operando1 < operando2:
                        resultado = True
                    else:
                        resultado = False
                elif tipo_instruccion == "MAYOR_IGUAL":
                    if operando1 >= operando2:
                        resultado = True
                    else:
                        resultado = False
                elif tipo_instruccion == "MENOR_IGUAL":
                    if operando1 <= operando2:
                        resultado = True
                    else:
                        resultado = False
                elif tipo_instruccion == "AND":
                    resultado = operando1 and operando2
                elif tipo_instruccion == "OR":
                    resultado = operando1 or operando2
                elif tipo_instruccion == "NOT":
                    resultado = not operando1

                aux_temporal = cuadruplos[numero_instruccion]["temp"]
                temporales[int(aux_temporal[1:])] = resultado
                #print("Resultado ", resultado)
                #print(temporales[1])


        elif tipo_instruccion == "ASSIGN":

            aux_temporal = cuadruplos[numero_instruccion]["op1"]
            variable_destino = cuadruplos[numero_instruccion]["op2"]

            if tabla_Simbolos[variable_destino]['MATRIX'] == 0:

                if type(aux_temporal) == type(2) or type(aux_temporal) == type(3.45):
                    temporal = aux_temporal
                else:
                    if aux_temporal in tabla_Simbolos.keys():
                        if (tabla_Simbolos[aux_temporal]["MATRIX"] == 1):
                            index = 0
                            base = int(tabla_Simbolos[aux_temporal]["base"])
                            if (tabla_Simbolos[aux_temporal]["dim"] == 1):
                                filas_consulta_aux = array_control[PC]['FILAS']

                                if tabla_Simbolos.get(filas_consulta_aux) is None:
                                    filas_consulta  = int(array_control[PC]['FILAS'])
                                else:
                                    filas_consulta = int(tabla_Simbolos[filas_consulta_aux]['VALUE'])

                                index = filas_consulta + base

                            elif (tabla_Simbolos[aux_temporal]["dim"] == 2):
                                filas_consulta_aux = array_control[PC]['FILAS']
                                col_consulta_aux = array_control[PC]['COL']
                                filas_matrix = int(tabla_Simbolos[aux_temporal]["filas"])
                                col_matrix = int(tabla_Simbolos[aux_temporal]["col"])
                                base = int(tabla_Simbolos[aux_temporal]["base"])

                                if tabla_Simbolos.get(filas_consulta_aux) is None:
                                    filas_consulta  = int(array_control[PC]['FILAS'])
                                else:
                                    filas_consulta = int(tabla_Simbolos[filas_consulta_aux]['VALUE'])

                                if tabla_Simbolos.get(col_consulta_aux) is None:
                                    col_consulta  = int(array_control[PC]['COL'])
                                else:
                                    col_consulta = int(tabla_Simbolos[col_consulta_aux]['VALUE'])

                                index = (filas_consulta*col_matrix) + col_consulta + base

                            else:
                                filas_consulta_aux  = array_control[PC]['FILAS']
                                col_consulta_aux = array_control[PC]['COL']
                                prof_consulta_aux = array_control[PC]['PROF']
                                filas_matrix = int(tabla_Simbolos[aux_temporal]["filas"])
                                col_matrix = int(tabla_Simbolos[aux_temporal]["col"])
                                prof_matrix = int(tabla_Simbolos[aux_temporal]["prof"])
                                base = int(tabla_Simbolos[aux_temporal]["base"])

                                if tabla_Simbolos.get(filas_consulta_aux) is None:
                                    filas_consulta  = int(array_control[PC]['FILAS'])
                                else:
                                    filas_consulta = int(tabla_Simbolos[filas_consulta_aux]['VALUE'])

                                if tabla_Simbolos.get(col_consulta_aux) is None:
                                    col_consulta  = int(array_control[PC]['COL'])
                                else:
                                    col_consulta = int(tabla_Simbolos[col_consulta_aux]['VALUE'])

                                if tabla_Simbolos.get(prof_consulta_aux) is None:
                                    prof_consulta  = int(array_control[PC]['COL'])
                                else:
                                    prof_consulta = int(tabla_Simbolos[prof_consulta_aux]['VALUE'])

                                index = (filas_consulta*col_matrix*prof_matrix) +(col_consulta*prof_matrix)+prof_consulta+base

                            #print("hello index", index)
                            temporal = MATRIX_SPACE[index]
                            #print(variable_destino)

                        else:
                            temporal = tabla_Simbolos[aux_temporal]["VALUE"]

                    elif aux_temporal[:1] == 'T':
                        temporal = temporales[int(aux_temporal[1:])]

                if (type(temporal) is int) and (tabla_Simbolos[variable_destino]['TYPE'] == 'INT'):
                    tabla_Simbolos[variable_destino]['VALUE'] = temporal
                elif (type(temporal) is not int) and (tabla_Simbolos[variable_destino]['TYPE'] == 'DEC'):
                    tabla_Simbolos[variable_destino]['VALUE'] = temporal
                else:
                    print("* EXECUTION FAILED: NON MATCHING DATA TYPES *")
                    raise Exception()

            #PARTE DONDE EL OPERANDO 2 (VARIABLE DESTINO) ES UN ARREGLO
            # aux_temporal es el operando 1
            else:
                index = 0
                if (tabla_Simbolos[variable_destino]["dim"] == 1):
                    filas_consulta_aux = array_control[PC]['FILAS']
                    base = int(tabla_Simbolos[variable_destino]["base"])

                    if tabla_Simbolos.get(filas_consulta_aux) is None:
                        filas_consulta = int(array_control[PC]['FILAS'])
                    else:
                        filas_consulta = int(tabla_Simbolos[filas_consulta_aux]['VALUE'])

                    index = filas_consulta + base

                elif (tabla_Simbolos[variable_destino]["dim"] == 2):
                    filas_consulta_aux = array_control[PC]['FILAS']
                    col_consulta_aux = array_control[PC]['COL']
                    filas_matrix = int(tabla_Simbolos[variable_destino]["filas"])
                    col_matrix = int(tabla_Simbolos[variable_destino]["col"])
                    base = int(tabla_Simbolos[variable_destino]["base"])

                    if tabla_Simbolos.get(filas_consulta_aux) is None:
                        filas_consulta = int(array_control[PC]['FILAS'])
                    else:
                        filas_consulta = int(tabla_Simbolos[filas_consulta_aux]['VALUE'])

                    if tabla_Simbolos.get(col_consulta_aux) is None:
                        col_consulta = int(array_control[PC]['COL'])
                    else:
                        col_consulta = int(tabla_Simbolos[col_consulta_aux]['VALUE'])

                    base = int(tabla_Simbolos[variable_destino]["base"])
                    index = filas_consulta * col_matrix + col_consulta + base

                else:
                    filas_consulta_aux = array_control[PC]['FILAS']
                    col_consulta_aux = array_control[PC]['COL']
                    prof_consulta_aux = array_control[PC]['PROF']
                    filas_matrix = int(tabla_Simbolos[variable_destino]["filas"])
                    col_matrix = int(tabla_Simbolos[variable_destino]["col"])
                    prof_matrix = int(tabla_Simbolos[variable_destino]["prof"])
                    base = int(tabla_Simbolos[variable_destino]["base"])

                    if tabla_Simbolos.get(filas_consulta_aux) is None:
                        filas_consulta = int(array_control[PC]['FILAS'])
                    else:
                        filas_consulta = int(tabla_Simbolos[filas_consulta_aux]['VALUE'])

                    if tabla_Simbolos.get(col_consulta_aux) is None:
                        col_consulta = int(array_control[PC]['COL'])
                    else:
                        col_consulta = int(tabla_Simbolos[col_consulta_aux]['VALUE'])

                    if tabla_Simbolos.get(prof_consulta_aux) is None:
                        prof_consulta = int(array_control[PC]['COL'])
                    else:
                        prof_consulta = int(tabla_Simbolos[prof_consulta_aux]['VALUE'])

                    index = (filas_consulta * col_matrix * prof_matrix) + (col_consulta * prof_matrix) + prof_consulta + base

                #print("INDEX:", index)

                if type(aux_temporal) == type(2) or type(aux_temporal) == type(3.45):
                    temporal = aux_temporal
                else:
                    if aux_temporal in tabla_Simbolos.keys():
                        temporal = tabla_Simbolos[aux_temporal]["VALUE"]

                    elif aux_temporal[:1] == 'T':
                        temporal = temporales[int(aux_temporal[1:])]

                if (type(temporal) is int) and (tabla_Simbolos[variable_destino]['TYPE'] == 'INT'):
                    MATRIX_SPACE[index] = temporal
                elif (type(temporal) is not int) and (tabla_Simbolos[variable_destino]['TYPE'] == 'DEC'):
                    MATRIX_SPACE[index] = temporal
                else:
                    print("* EXECUTION FAILED: NON MATCHING DATA TYPES *")
                    raise Exception()

        PC += 1

    else:
        if (tipo_instruccion == "GOTO_FALSO" and cuadruplos[numero_instruccion]["DirBase"] != True):
            cond = cuadruplos[numero_instruccion]["DirBase"]
            edo_cond = temporales[int(cond[1:])]
            if edo_cond == False:
                PC = int(cuadruplos[numero_instruccion]["Ref"])
            else:
                PC += 1

        elif tipo_instruccion == "GOTO":
            PC = int(cuadruplos[numero_instruccion]["Ref"])

        else:
            PC += 1


    #print ("PC: ", PC)

    return PC



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
    global base_matrix
    if len(p) > 2:
        if p[2] == "VAR":
            if tabla_Simbolos.get(p[4]) is None:
                tabla_Simbolos[p[4]] = {}
                tabla_Simbolos[p[4]]['TYPE'] = p[3]
                tabla_Simbolos[p[4]]['MATRIX'] = 0
                tabla_Simbolos[p[4]]['VALUE'] = 0
            else:
                print("ERROR WITH ID {:1}: Variables can't be declared with the same name twice".format(p[4]))
                raise Exception
        elif p[2] =="ARRAY":
            if tabla_Simbolos.get(p[4]) is None:
                if len(p) > 12:
                    tabla_Simbolos[p[4]] = {}
                    tabla_Simbolos[p[4]]['TYPE'] = p[3]
                    tabla_Simbolos[p[4]]['MATRIX'] = 1
                    tabla_Simbolos[p[4]]['dim'] = 3
                    tabla_Simbolos[p[4]]['filas'] = p[6]
                    tabla_Simbolos[p[4]]['col'] = int(p[9])
                    tabla_Simbolos[p[4]]['prof'] = int(p[12])
                    size = int(p[6]) * int(p[9])*int(p[12])
                    tabla_Simbolos[p[4]]['size'] = size
                    tabla_Simbolos[p[4]]['base'] = base_matrix
                    base_matrix += tabla_Simbolos[p[4]]['size']
                    for x in range(size):
                        MATRIX_SPACE.append(0)

                elif len(p) > 9:
                        tabla_Simbolos[p[4]] = {}
                        tabla_Simbolos[p[4]]['TYPE'] = p[3]
                        tabla_Simbolos[p[4]]['MATRIX'] = 1
                        tabla_Simbolos[p[4]]['dim'] = 2
                        tabla_Simbolos[p[4]]['filas'] = p[6]
                        tabla_Simbolos[p[4]]['col'] = int(p[9])
                        tabla_Simbolos[p[4]]['prof'] = None
                        size = int(p[6])*int(p[9])
                        tabla_Simbolos[p[4]]['size'] = size
                        tabla_Simbolos[p[4]]['base'] = base_matrix
                        base_matrix += size
                        for x in range(size):
                            MATRIX_SPACE.append(0)

                elif len(p) > 3:
                        tabla_Simbolos[p[4]] = {}
                        tabla_Simbolos[p[4]]['TYPE'] = p[3]
                        tabla_Simbolos[p[4]]['MATRIX'] = 1
                        tabla_Simbolos[p[4]]['dim'] = 1
                        tabla_Simbolos[p[4]]['filas'] = p[6]
                        tabla_Simbolos[p[4]]['col'] = None
                        tabla_Simbolos[p[4]]['prof'] = None
                        size = int(p[6])
                        tabla_Simbolos[p[4]]['size'] = size
                        tabla_Simbolos[p[4]]['base'] = base_matrix
                        base_matrix += p[6]
                        for x in range(size):
                            MATRIX_SPACE.append(0)

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
        | st IF PARIZQ cond PARDER ifAux CBIZQ st CBDER PUNTOCOMA ifEndAux
        | st IF PARIZQ cond PARDER ifAux CBIZQ st CBDER PUNTOCOMA ELSE ifAuxElse CBIZQ st CBDER PUNTOCOMA ifEndAux
        | st auxIniWhile WHILE PARIZQ cond PARDER auxFauxWhile CBIZQ st CBDER PUNTOCOMA auxFinWhile
        | st auxIniFor FOR PARIZQ cond auxFauxFor PUNTOCOMA e auxAssignFor PARDER CBIZQ st CBDER PUNTOCOMA auxFinFor
        | st DO auxIniLoop CBIZQ st CBDER PUNTOCOMA auxFinLoop
        | st LET variable IGUAL IF PARIZQ cond PARDER ifAux CBIZQ CTE PUNTOCOMA CBDER PUNTOCOMA ifEndAuxEsp
        | st LET variable IGUAL IF PARIZQ cond PARDER ifAux CBIZQ CTE CBDER PUNTOCOMA ELSE ifAuxElse CBIZQ CTE CBDER PUNTOCOMA ifEndAux
        | st BREAK auxFauxLoop PUNTOCOMA
        |
    """
    global contador_cuadruplos
    if len(p) > 2:
        if p[2] == 'LET' and p[5]!='IF':
            oper1 = operandos.pop()
            oper2 = operandos.pop()
            genera_cuadruplo("ASSIGN", oper1, oper2)
        elif p[2] == 'LET' and p[5]=='IF':
            oper2 = operandos.pop()
            oper1 = p[11]
            genera_cuadruplo("ASSIGN", oper1, oper2)
        if p[2] == 'ENTER':
            var = operandos.pop()
            genera_cuadruplo_input("INPUT", var)
        if len(p) > 4:
            if p[2] == 'DISPLAY':
                msg = p[4]
                if p[5] == ',':
                    variable = operandos.pop()
                    genera_cuadruplo_output("OUTPUT", msg, variable)
                else:
                    genera_cuadruplo_output("OUTPUT", msg)



def p_ifAux(p):
    'ifAux : '
    global contador_cuadruplos
    resultado = operandos.pop()
    genera_cuadruplo_ciclos("GOTO_FALSO", resultado)
    saltos.append(contador_cuadruplos - 1)


def p_ifAuxElse(p):
    'ifAuxElse : '
    global contador_cuadruplos
    genera_cuadruplo_ciclos("GOTO")
    salto = saltos.pop()
    contador = contador_cuadruplos
    ajusta_saltos(salto, contador)
    saltos.append(contador_cuadruplos - 1)


def p_ifEndAux(p):
    'ifEndAux : '
    global contador_cuadruplos
    fin = saltos.pop()
    ajusta_saltos(fin, contador_cuadruplos)


def p_ifEndAuxEsp(p):
    'ifEndAuxEsp : '
    global contador_cuadruplos
    fin = saltos.pop()
    ajusta_saltos(fin, contador_cuadruplos+1)


def p_auxIniWhile(p):
    'auxIniWhile : '
    global contador_cuadruplos
    saltos.append(contador_cuadruplos)


def p_auxFauxWhile(p):
    'auxFauxWhile : '
    global contador_cuadruplos
    resultado = operandos.pop()
    genera_cuadruplo_ciclos("GOTO_FALSO", resultado)
    saltos.append(contador_cuadruplos - 1)


def p_auxFinWhile(p):
    'auxFinWhile : '
    global contador_cuadruplos
    f = saltos.pop()
    retorno = saltos.pop()
    genera_cuadruplo_ciclos("GOTO", None, retorno)
    ajusta_saltos(f, contador_cuadruplos)


def p_auxIniFor(p):
    'auxIniFor : '
    global contador_cuadruplos
    saltos.append(contador_cuadruplos)


def p_auxFauxFor(p):
    'auxFauxFor : '
    global contador_cuadruplos
    resultado = operandos.pop()
    #print(resultado)
    genera_cuadruplo_ciclos("GOTO_FALSO", resultado)
    saltos.append(contador_cuadruplos - 1)


def p_auxFinFor(p):
    'auxFinFor : '
    global contador_cuadruplos
    f = saltos.pop()
    retorno = saltos.pop()
    genera_cuadruplo_ciclos("GOTO", None, retorno)
    ajusta_saltos(f, contador_cuadruplos)


def p_auxAssignFor(p):
    'auxAssignFor : '
    global contador_cuadruplos
    op1 = cuadruplos[contador_cuadruplos - 1]["temp"]
    temp = cuadruplos[contador_cuadruplos - 1]["op1"]
    genera_cuadruplo("ASSIGN", op1, temp)



def p_auxIniLoop(p):
    'auxIniLoop : '
    global contador_cuadruplos
    saltos.append(contador_cuadruplos)


def p_auxFauxLoop(p):
    'auxFauxLoop : '
    global contador_cuadruplos
    genera_cuadruplo_ciclos("GOTO_FALSO", True)
    saltos.append(contador_cuadruplos)


def p_auxFinLoop(p):
    'auxFinLoop : '
    global contador_cuadruplos
    f = saltos.pop()
    retorno = saltos.pop()
    genera_cuadruplo_ciclos("GOTO", None, retorno)
    ajusta_saltos(f, contador_cuadruplos)



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
    p[0] = p[1]
    operandos.append(p[0])
    if (len(p) > 8):
        array_control[contador_cuadruplos] = {}
        array_control[contador_cuadruplos]['FILAS'] = p[3]
        array_control[contador_cuadruplos]['COL'] = p[6]
        array_control[contador_cuadruplos]['PROF'] = p[9]
    elif (len(p) > 5):
        array_control[contador_cuadruplos] = {}
        array_control[contador_cuadruplos]['FILAS'] = p[3]
        array_control[contador_cuadruplos]['COL'] = p[6]
    elif (len(p) > 2):
        array_control[contador_cuadruplos] = {}
        array_control[contador_cuadruplos]['FILAS'] = p[3]


def p_cond(p):
    """
    cond : oprel
            | cond AND oprel
            | cond OR oprel
    """
    if len(p) > 2:
        oper2 = operandos.pop()
        oper1 = operandos.pop()
        result = "T" + str(temporales.pop())
        if p[2] == 'AND':
            genera_cuadruplo("AND", oper1, oper2, result)
        elif p[2] == 'OR':
            genera_cuadruplo("OR", oper1, oper2, result)
        operandos.append(result)
        p[0] = p[3]


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
    if p[1] == '(':
        p[0] = p[2]
    elif p[1] == 'NOT':
        p[0] = p[3]
        oper1 = operandos.pop()
        result = "T" + str(temporales.pop())
        genera_cuadruplo("NOT", oper1, result)
        operandos.append(result)
    else:
        p[0] = p[1]
        oper2 = operandos.pop()
        oper1 = operandos.pop()
        if p[2] == '==':
            result = "T" + str(temporales.pop())
            genera_cuadruplo("IGUAL", oper1, oper2, result)
        elif p[2] == '!=':
            result = "T" + str(temporales.pop())
            genera_cuadruplo("DESIGUAL", oper1, oper2, result)
        elif p[2] == '>':
            result = "T" + str(temporales.pop())
            genera_cuadruplo("MAYOR", oper1, oper2, result)
        elif p[2] == '<':
            result = "T" + str(temporales.pop())
            genera_cuadruplo("MENOR", oper1, oper2, result)
        elif p[2] == '>=':
            result = "T" + str(temporales.pop())
            genera_cuadruplo("MAYOR_IGUAL", oper1, oper2, result)
        elif p[2] == '<=':
            result = "T" + str(temporales.pop())
            genera_cuadruplo("MENOR_IGUAL", oper1, oper2, result)
        operandos.append(result)



def p_e(p):
    """
    e : e PLUS t
        | e MENOS t
        | t
    """
    if len(p) > 2:
        oper2 = operandos.pop()
        oper1 = operandos.pop()
        result = "T" + str(temporales.pop())
        if p[2] == '+':
            genera_cuadruplo("PLUS", oper1, oper2, result)
        elif p[2] == '-':
            genera_cuadruplo("MINUS", oper1, oper2, result)
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
    if len(p) > 2:
        oper2 = operandos.pop()
        oper1 = operandos.pop()
        result = "T" + str(temporales.pop())
        if p[2] == '*':
            genera_cuadruplo("MULTIPLY", oper1, oper2, result)
        elif p[2] == '/':
            genera_cuadruplo("DIV", oper1, oper2, result)
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
               | ID SBIZQ CTE SBDER
               | ID SBIZQ CTE SBDER SBIZQ CTE SBDER
               | ID SBIZQ CTE SBDER SBIZQ CTE SBDER SBIZQ CTE SBDER
               | ID SBIZQ ID SBDER
               | ID SBIZQ ID SBDER SBIZQ ID SBDER
               | ID SBIZQ ID SBDER SBIZQ ID SBDER SBIZQ ID SBDER
    """
    p[0] = p[1]
    operandos.append(p[0])
    if (len(p) > 8):
        array_control[contador_cuadruplos] = {}
        array_control[contador_cuadruplos]['FILAS'] = p[3]
        array_control[contador_cuadruplos]['COL'] = p[6]
        array_control[contador_cuadruplos]['PROF'] = p[9]
    elif (len(p) > 5):
        array_control[contador_cuadruplos] = {}
        array_control[contador_cuadruplos]['FILAS'] = p[3]
        array_control[contador_cuadruplos]['COL'] = p[6]
    elif (len(p)>2):
        array_control[contador_cuadruplos] = {}
        array_control[contador_cuadruplos]['FILAS'] = p[3]


def p_error(token):
    if token is not None:
        print("Line %s, illegal token: %s" % (token.lineno, token.value))
    else:
        print('Unexpected end of input')
    raise SyntaxError("SYNTAX ERROR")


parser = yacc.yacc()
myfile = open("ciclos.txt")
code = myfile.read()
code_count = len(code)
myfile.close()
result = parser.parse(code)
print('\n')
print("Compilation complete! Errors: ", result)


print('\n')
print(tabla_Simbolos)
print(array_control)

#print('\n')
#variable_list = list(tabla_Simbolos)
#for i in range(len(tabla_Simbolos)):
#    current_ID = variable_list[i]
#    print("Table Index: {0}, ID: {1}, Tipo: {2}, Valor inicial: {3}".format(i, current_ID, tabla_Simbolos[current_ID]["TYPE"], tabla_Simbolos[current_ID]["VALUE"]))

print('\n')

for i in range(len(cuadruplos)):
    if (cuadruplos[i]["OPCODE"] == "GOTO_FALSO") or cuadruplos[i]["OPCODE"] == "GOTO":
        print("#{0}, Opcode: {1}, DirBase: {2}, Referencia: {3}".format(i, cuadruplos[i]["OPCODE"], cuadruplos[i]["DirBase"], cuadruplos[i]["Ref"]))
    elif ((cuadruplos[i]["OPCODE"] != "INPUT") and cuadruplos[i]["OPCODE"] != "OUTPUT"):
        print("#{0}, Opcode: {1}, Operando1: {2}, Operando2: {3}, Temporal: {4}".format(i, cuadruplos[i]["OPCODE"],  cuadruplos[i]["op1"], cuadruplos[i]["op2"], cuadruplos[i]["temp"]))
    else:
        if ((cuadruplos[i]["OPCODE"] == "INPUT")):
            print("#{0}, Opcode: {1}, Var: {2}".format(i, cuadruplos[i]["OPCODE"], cuadruplos[i]["variable"]))

print('\n')

while (PC != contador_cuadruplos) :
    PC = execution(PC, cuadruplos[PC]["OPCODE"])

print('\n')

print(tabla_Simbolos)
print(array_control)
print(MATRIX_SPACE)
