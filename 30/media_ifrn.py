# Calcular média da disciplina do IFRN
#
# 1) Solicitar ao usuário que informe duas notas (As notas são inteiras)
# 2) Calcular a média do IFRN
# 3) Exibir a média

etapa1 = int(input('Digite a nota da Etapa1:'))
etapa2 = int(input('Digite a nota da Etapa2:'))

media = (etapa1 * 2 + etapa2 *3)/5
print(f'Média ={media: .0f}')