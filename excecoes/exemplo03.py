import sys
try:
 intdividendo = int (input('Digite o dividendo:'))
 intDivisor = int (input('Digite o dividendo:'))
 fltResultado = intdividendo / intDivisor
except:
    print (f'ERRO:{sys.exc_info()}')
except ValueError:
    print('ERRO: Informe um valor que possa ser convertido em inteiro.')
except ZeroDivisionError:
    print(f'ERRO: Não existe divisão por ZERO.')
else:
    print(fltResultado)
