# 1. Numeros

# Int
idade = 20

# Float
altura = 1.7

# complex
# calculos com numeros complexos 
numero_complexo = 1 + 2j

# 2. Boolean
verdade = True
mentira = False 

# 3. Sequencias 
# str, list, tuple, set, dict

#str 
#conjunto de caracteres 
nome = "João da silva"
nome = 'Maria da silva'

# str de multiplas linhas
frase = """
Olá mundo
Parabéns amigo
"""

# interpolação de str (concatenação)
# f-strings
nome = 'Maria'
idade = 78
mensagem = f'(nome) é uma pessoa legal! Ela tem (idade) anos'

#Char 
# não existe 
# usar string de tamanho 1
letra = 'A'

# Como acessar os caracteres de uma string?
nome = 'Silvio Santos'
print(nome [2])

# Metodos de string 
print(nome.upper())
print (nome.lower())
print (nome.capitalize())

# list 
# lista de valores 
# permitir diferentes tipos de dados na mesma lista

habilidades = ['python', 'java', 'javascript']
print(habilidades[1]) #java

for habilidade in habilidades: 
    print("teste")
    print(habilidade)

#adiciona no final da lista
    habilidades.append('html') #'python', 'java', 'javascript', 'html'

    #adiciona em uma posição especifica
    habilidades.insert (1, "css") # 'python', 'css', 'java', 'javascript', 'html'

    #remover
    habilidades.remove ('css')

    #tuple 
    # 'lista' de valores 
    # não pode ser alterada 
    #sim, nao, talvez
    opcoes = ('sim', 'não', 'talvez')
    raca_rpg = ('humano', 'elfo', 'orc')


def estatistica_notas(notas):
    maior = max (notas)
    menor = min (notas)
    media = sum (notas)/ len(notas)
    return maior, menor, media

notas = [10.0, 3.5, 7.8]
estatistica = estatistica_notas(notas)
print (estatistica)

#desempacotar uma tupla
maior, menor, media = estatistica_notas(notas)
print (maior, menor, media)

#set
# conjunto de valores
# Não é indexado 
# não permite elementos duplicados

habilidades = {'java', 'python'}

habilidades.add {'js'}

print(habilidades)

# dict 
# palavra -> definição
# chave -> valor
# key -> value 

nome = 'silvio'
idade = 89
patrimonio = 2000000000
altura = 1.7

pessoa = {
    'nome': 'silvio',
    'idade': 89,
    'patrimonio': 2000000000
    'altura': 1.7}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['patrimonio'])
print(pessoa['altura'])

# none
# variaveis que serão inicializadas em tempo de execução
# retorno de função
# parametros de função

nulo = None
