numero = int(input("Informe o multiplicador: "))

print (f"Tabuada do {numero}:")
print  (f"{numero} X 1 = {numero * 1}")
print  (f"{numero} X 2 = {numero * 2}")
print  (f"{numero} X 3 = {numero * 3}")
print  (f"{numero} X 4 = {numero * 4}")
print  (f"{numero} X 5 = {numero * 5}")
print  (f"{numero} X 6 = {numero * 6}")
print  (f"{numero} X 7 = {numero * 7}")
print  (f"{numero} X 8 = {numero * 8}")
print  (f"{numero} X 9 = {numero * 9}")
print  (f"{numero} X 10 = {numero * 10}")

# outra maneira de fazer
numero = 1
while numero <= 10:
    print  (f'{int(numero)} X {int(numero)} = {int(numero)} * {int(numero)}')
    numero += 1
