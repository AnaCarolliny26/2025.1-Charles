import sys


distância = int(input('Informe o valor da distância em km:'))
if distância <= 0:
    sys.exit ('Informe Distância Positiva')

V_ini = int (input('Informe a v_ini em km/h:'))
if V_ini <=0:
    sys.exit ('Informe Velocidade Positiva')

aceleração = int(input('Informe a aceleração em m/s ** 2:'))
if aceleração <=0:
    sys.exit ('Informe Aceleração Positiva')

delta = V_ini ** 2 - 4 * aceleração * distância
if delta <=0:
    sys.exit ('Não é possível calcular o tempo')

t = (-V_ini + delta ** 0.5) / (2 * aceleração)

hora = tempo // 3600

tempo = tempo % 3600

minuto = tempo // 60

segundo = tempo % 60

print (f'Tempo = {hora} : {minuto} : {segundo}')