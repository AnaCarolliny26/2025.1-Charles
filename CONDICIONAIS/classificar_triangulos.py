'''
Programa para classificar um triângulo quanto aos ângulos.

- O programa deverá solicitar 3 ângulos inteiros positivos;
- Para ser um triângulo, a soma dos ângulos deve ser igual a 180;

- Retângulo: Possui um ângulo interno reto (igual a 90).
- Obtusângulo: Possui um ângulo interno obtuso (maior que 90).
- Acutângulo: Possui todos os ângulos internos agudos (menores que 90).
'''

import sys 

# Informando o ângulo1
ângulo1 = int(input('Informe o valor do ângulo 1:'))
if ângulo1 < 0 or ângulo1 > 180:
    sys.exit('ERRO: valor do ângulo 1 Inválido. Informe valor entre 0 e 180')

# Informando o ângulo 2
ângulo2 = int(input('Informe o valor do ângulo 2:'))
if ângulo2 < 0 or ângulo2 > 180:
    sys.exit('ERRO: valor do ângulo 2 Inválido. Informe valor entre 0 e 180')

# Informando o ângulo 3
ângulo3 = int(input('Informe o valor do ângulo 3:'))
if ângulo3 < 0 or ângulo3 > 180:
    sys.exit('ERRO: valor do ângulo 3 Inválido. Informe valor entre 0 e 180')
