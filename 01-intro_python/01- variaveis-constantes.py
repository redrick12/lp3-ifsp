#identificadores 
#letra, numeros e _
# não pode ser palavra reservada: if, none, true, false
nome= "pedro"
Nome = "pedro"

#variáveis 
# tudo em minusculos
# separador _
# snake_case 
idade = 20
pessoa_fisica = "Marcio"
pessoa_juridica = "Paula LTDA"
imposto_renda = 2200.45

# E o tipo?
# Java
# String nome = "Pedro"
# int idade = 20
# No python temos inferencia do tipo
# O tipo será definido com base no valor definido (literal)
idade = 20 #int 
nome = "pedro"  #str

#Constantes 
# Não existe constantes no Python
# Convenção: nome em maiusculo 
PI= 3.14

# Comentario de unica linha

'''
Comentario de 
multiplas linhas
'''

#docstring (comentario de documentação)
#documentar classe, modulos, funções, ...
#docstring (comentario de documentação)
#documentar classe, modulos, funções, ...

def somar (numero1, numero2):
    '''
    Função que soma dois numeros
    :param numero1: primeiro numero
    :param numero2: segundo numero
    :return: a soma dos dois  numeros 
    '''
    return numero1 + numero2

somar