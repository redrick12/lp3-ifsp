#exercicio01

numero_usuario = int 
adivinhar = 5 
print(' Tente adivinhar o numero estabelecido entre 0 a 100')
while numero_usuario!= adivinhar:
    numero_usuario = int (input('Entre com um numero:  '))
    if numero_usuario == adivinhar:
        print('você acertou o numero')
    if numero_usuario> 5 and numero_usuario<= 10:
        print('Quase!')
    elif numero_usuario<5 and numero_usuario>= 0:
        print('Está perto')
    elif numero_usuario> 10:
        print('Está longe')


#Ex02 
numero = int (input("Escolha o número a ser multiplicado "))
print(f'1x: {numero*1}')
print(f'2x: {numero*2}')
print(f'3x: {numero*3}')
print(f'4x: {numero*4}')
print(f'5x: {numero*5}')
print(f'6x: {numero*6}')
print(f'7x: {numero*7}')
print(f'8x: {numero*8}')
print(f'9x: {numero*9}')
print(f'10x: {numero*10}')




#Ex03
import re

def conta_letras(texto):
    vogais = 0
    consoantes = 0

    texto = re.sub('[^a-zA-Z]', '', texto)

    for letra in texto:
        if letra.lower() in 'aeiou':
            vogais += 1
        else:
            consoantes += 1

    return {'vogais': vogais, 'consoantes': consoantes}

frase = input('Digite uma frase: ')
resultado = conta_letras(frase)
print(f'Número de vogais: {resultado["vogais"]}')
print(f'Número de consoantes: {resultado["consoantes"]}')

#Ex04

candidatos = {"1": 0, "2": 0, "3": 0}
while True:
    voto = input(" Digite o número do candidato que deseja votar (1-Lucas, 2-Mateus, 3-Erick Golaço, 0-Sair): ")
    if voto == "0":
        break
    elif voto in candidatos:
        candidatos[voto] += 1
    else:
        print("Opção inválida. Tente novamente.")

for candidato, votos in candidatos.items():
    print(f"Candidato {candidato}: {votos} votos")

voto_max = max(candidatos.values())
for candidato, votos in candidatos.items():
    if votos == voto_max:
        print(f"O vencedor é o Candidato {candidato} com {votos} votos!")


#Ex05 
def verificar_palindromo (palavra):
    palavra = palavra.lower()
    if palavra == palavra [::-1]:
        return True
    else:
        return False
palavra = input ('Entre com uma palavra: ')
if verificar_palindromo(palavra):
        print("A palavra é um palíndromo.")
else:
        print("A palavra não é um palíndromo.")

#Ex06

def conversor_de_notas(nota):
    if nota < 0 or nota > 100:
        return 'Insira algo válido'
    elif nota <= 20:
        return 'A sua nota foi F'
    elif nota <= 40:
        return 'A sua nota foi D'
    elif nota <= 60:
        return 'A sua nota foi C'
    elif nota <= 80:
        return 'A sua nota foi B'
    else:
        return 'A sua nota foi A'

nota = int(input('Insira uma nota: '))
resultado = conversor_de_notas(nota)
print(resultado)

#ex07

def mostrar_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def jogar_forca():
    palavra = "python"
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra:")

    while tentativas > 0:
        mostrar_forca(palavra, letras_corretas)
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            if set(letras_corretas) == set(palavra):
                print("Parabéns! Você venceu!")
                print("A palavra era:", palavra)
                break
        else:
            tentativas -= 1
            print("Letra não encontrada. Você tem", tentativas, "tentativas restantes.")

    if tentativas == 0:
        print("Game over! A palavra era:", palavra)

if __name__ == "__main__":
    jogar_forca()

#ex08
def contar_palavras(frase):
    palavras = frase.lower().split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem
while True:
    texto = input("Digite uma frase (ou 'sair' para encerrar): ")
    if texto.lower() == "sair":
        break
    resultado = contar_palavras(texto)
    print("Contagem de palavras:")
    for palavra, quantidade in resultado.items():
        print(f"{palavra}: {quantidade}")
