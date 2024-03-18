#exercicio1
numero = int (input('entre com um numero inteiro'))
sucessor = numero+ 1
antecessor = numero-1
print(f'antecessor = {antecessor}')
print(f'sucessor = {sucessor}')




#exercicio2
numero1 = int (input('entre com o primeiro numero: '))
numero2 = int (input('entre com o segundo numero:'))
numero3 =int (input('entre com o terceiro numero:'))
media = (numero1+ numero2+ numero3)/3
print(f'media= {media}') 


#exercicio3
valor_da_compra = float(input('entre com o valor da compra'))

if valor_da_compra>=0.1 and valor_da_compra<9.99:
    print(f'O valor final da compra foi de {valor_da_compra}')
elif valor_da_compra>=10 and valor_da_compra<=99.9:
    print(f'o valor final da compra foi de { valor_da_compra - (valor_da_compra*5)/100  }')
elif valor_da_compra>=100 and valor_da_compra<=499.9:
    print(f'o valor final da compra foi de { valor_da_compra - (valor_da_compra*10)/100  }')                   
elif valor_da_compra>=500:
    print(f'o valor final da compra foi de { valor_da_compra - (valor_da_compra*15)/100  }')
    
#exercicio4 
def verificador(identidade):
    if len(identidade) != 7:
        print('Inválido: o identificador deve ter 7 caracteres.')
        return False
    
    if identidade[0] != 'B' or identidade[1] != 'R' or identidade[6] != 'X':
        print('Inválido: o identificador deve começar com "BR" e terminar com "X".')
        return False
     #essa parte eu pedi ajuda
    for char in identidade[2:6]: 
        if not char.isdigit():
            print('Inválido: os caracteres 3 a 6 devem ser dígitos.')
            return False 
    print('Válido')
    return True
identidade = input('Entre com um identificador: ')
verificador(identidade)

#exercicio5

def verificador (identidade):
    if len(identidade) != 6:
        print ('invalido')
        return False
    if identidade != int:
        print('a identidade precisa ser um numero')
        return False
    print('valido')
    return True
identidade = input('entre com a identidade:')
verificador (identidade)

#exercicio6
 
def calculo_volume(comprimento, altura, largura):
    volume = (comprimento * altura * largura) / 1000
    return volume

comprimento = int(input('Entre com o comprimento em cm: '))
altura = int(input('Entre com a altura em cm: '))
largura = int(input('Entre com a largura em cm: '))

volume_calculado = calculo_volume(comprimento, altura, largura)

print(f'O volume é de {volume_calculado} metros cúbicos.')

def calculo_potencia (volume, temperatura_desejada, temperatura_ambiente):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia 
temperatura_desejada = int (input('entre com a temperatura desejada'))
temperatura_ambiente = int (input('entre com a temperatua ambiente'))
volume = calculo_volume (comprimento, altura, largura)
potencia = calculo_potencia(volume, temperatura_ambiente, temperatura_desejada)
print (f'a potencia foi de {potencia}')
print (f' A filtragem ideal é de {volume*2.5}')

#exercicio7

def calculo_de_imc (altura, peso):
    imc =  peso / altura * altura
    return imc
    if imc<18.5:
        print('baixo peso')
    elif imc>=18.5 and imc<=24.9:
        print('peso normal')
    elif imc>= 25 and imc<=29.9:
        print('Excesso de peso')
    elif imc>=30 and imc<=34.9:
        print('Obesidade de classe 1')
    elif imc>=35 and imc<=39.9:
        print('Obesidade de classe 2')
    elif imc>=40:
        print('Obesidade de classe 3')
        
def peso_ideal(altura, peso): 
    imc =  peso/altura **2
    peso_ideal = 24.9 * altura**2
    diferenca = peso - peso_ideal
    if diferenca > 0:
        print(f"Você precisa perder {abs(diferenca):.2f} kg para alcançar um IMC de 24.9.")
    elif diferenca < 0:
        print(f"Você precisa ganhar {abs(diferenca):.2f} kg para alcançar um IMC de 24.9.")
    else:
        print("Seu peso está dentro do normal.")
        return diferenca
altura = float (input('Entre com a sua altura:'))
peso = float (input('Entre com o seu peso'))
imc = calculo_de_imc(altura, peso)
print(f'O seu Indice de Massa Corporal é de {imc}')
peso_ideal = peso_ideal(altura, peso)