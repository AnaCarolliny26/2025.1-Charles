# As notas devem ser inteiras e entre 0  e 100 (inclusive).
# Caso a média seja igual ou superior a 60 o aluno estará aprovado; caso a média seja
# igual ou superior a 20 o aluno estará em prova final e os demais casos o aluno estará reprovado''

import sys

# Informando a nota da Etapa 1
etapa1 = int(input('Informe a nota da Etapa 1:'))
if etapa1 < 0 or etapa1 > 100:
    sys.exit ('ERRO: Nota etapa 2 Inválida. Informe nota entre 0 e 100.')

# Informando a nota da etapa 2
etapa2 = int(input('Informe a nota da etapa 2:'))
if etapa2 < 0 or etapa2  > 100:
    sys.exit ('ERRO: Nota etapa 2 Inválida. Informe nota entre 0 e 100.')

# Calculando a média
media = int(round((etapa1 * 2 + etapa2 * 3) / 5, 0) )
print(f'Média do aluno: {media}' )


# Verificando a situação do aluno
if media >= 60:
    print('Aluno aprovado.')
elif media >= 20:
    print('Aluno em prova final.')
else:
    print ('Aluno reprovado.')