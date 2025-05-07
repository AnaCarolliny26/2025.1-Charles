# Faça um programa que solicite ao usuário os valores de v0, a e t.
# O programa deve calcular e exibir a distância percorrida pelo objeto

import sys


velocidade_inicial = int(input('Digite o valor de v0:'))
if velocidade_inicial <=0:
    sys.exit ('Informe Velocidade Positiva.')


aceleração = int(input('Digite o valor de a:'))
if aceleração <=0:
    sys.exit ('Informe Aceleração Positiva.')



tempo = int(input('Digite o valor de t:'))
if tempo <=0:
    sys.exit ('Informe o tempo positivo')


DS = velocidade_inicial * tempo + (( aceleração * tempo ** 2) / 2)

print(f'O valor de ΔS  é {DS} em m/s')








