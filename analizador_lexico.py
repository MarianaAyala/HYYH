import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = {
    'main': "MAIN",
    'var': 'VAR',
    'array': 'ARRAY',
    'int': 'INT',
    'dec': 'DEC',
    'funct': "FUNCT",
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'if': 'IF',
    'else': 'ELSE',
    'let': 'LET',
    'while': 'WHILE',
    'for': 'FOR',
    'enter': 'ENTER',
    'display': 'DISPLAY',
    'execute': 'EXECUTE',
    'do': 'DO',
    'break': 'BREAK'
}

tokens = [
    'MSG',
    'ID',
    'CTE',
    'FLOAT',
    'PUNTOCOMA',
    'SBIZQ',
    'SBDER',
    'IGUAL',
    'COMA',
    'PARDER',
    'PARIZQ',
    'CBIZQ',
    'CBDER',
    'IGUALIGUAL',
    'DIFERENTE',
    'MAYOR',
    'MENOR',
    'MAYORQUE',
    'MENORQUE',
    'PLUS',
    'MENOS',
    'MULT',
    'DIV'
]+ list(reservadas.values())

t_MSG = r'\".+\"'
t_PLUS = r'\+'
t_IGUAL = r'\='
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_PUNTOCOMA = r'\;'
t_SBIZQ = r'\['
t_SBDER = r'\]'
t_COMA = r'\,'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CBIZQ = r'\{'
t_CBDER = r'\}'
t_IGUALIGUAL = r'\=='
t_DIFERENTE = r'\!='
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MAYORQUE = r'\>='
t_MENORQUE = r'\<='


t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_]+[a-zA-Z0-9]*'
    if t.value.upper() in reservadas.values():
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_ignore_COMMENT(t):
    r'\#.+'
    pass

def t_FLOAT (t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE (t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("ILLEGAL CHARACTER %s" % t.value[0])
    t.lexer.sikip[1]


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()


