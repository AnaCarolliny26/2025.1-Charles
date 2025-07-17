import os, sys

# Obtendo o diretório onde o programa está salvo
strDir = os.path.dirname(__file__)

# Abrindo e lendo o arquivo
try:
   arqLeitura = open(f'{strDir}\\carta.txt', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   print(f'\nERRO: {erro}')

else:
   lstTimes = list ()
   while True:
       strLinha = arqLeitura.readline().strip() # Lendo a linha e armazenando na variável

       if not strLinha: break # Interrompe o laço quando não há conteúdo na linha (EOF)

       lstAux =  [int(i) if i.isdigit() else i for i in strLinha.split(';')]

       lstTimes.append(strLinha) # Adicionando linha lida na lista
       arqLeitura.close()

print(lstTimes)

for time in  lstTimes:
   time.insert (4, time [1]*3 + time[2])
   time.append (time[5] - time [6])
   



